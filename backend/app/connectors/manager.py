"""ConnectorManager — owns the shared HTTP client and runs federated search."""

from __future__ import annotations

import asyncio
import time

import httpx

from app.config import Settings
from app.connectors.base import BaseConnector, all_connector_classes
from app.models.entities import SearchResponse, SourceResult

# Import the connector package so every connector registers itself.
import app.connectors  # noqa: F401


class ConnectorManager:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = httpx.AsyncClient(
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent},
            follow_redirects=True,
        )
        self.connectors: dict[str, BaseConnector] = {
            cls.meta.id: cls(self.client, settings)
            for cls in all_connector_classes()
            if cls.meta.enabled
        }

    def get(self, source_id: str) -> BaseConnector | None:
        return self.connectors.get(source_id)

    def list_meta(self) -> list[dict]:
        return [c.meta.model_dump(mode="json") for c in self.connectors.values()]

    async def search(
        self,
        query: str,
        *,
        source_ids: list[str] | None = None,
        limit: int = 10,
    ) -> SearchResponse:
        targets = [
            c
            for cid, c in self.connectors.items()
            if (not source_ids or cid in source_ids) and c.available()
        ]
        started = time.perf_counter()
        results = await asyncio.gather(
            *(self._search_one(c, query, limit) for c in targets)
        )
        results.sort(key=lambda r: (r.error is not None, -(r.total or 0)))
        return SearchResponse(
            query=query,
            results=results,
            total_hits=sum(len(r.hits) for r in results),
            elapsed_ms=int((time.perf_counter() - started) * 1000),
        )

    async def _search_one(
        self, connector: BaseConnector, query: str, limit: int
    ) -> SourceResult:
        started = time.perf_counter()
        try:
            hits = await connector.search(query, limit=limit)
            return SourceResult(
                source_id=connector.meta.id,
                source_name=connector.meta.name,
                hits=hits,
                total=len(hits),
                elapsed_ms=int((time.perf_counter() - started) * 1000),
            )
        except Exception as exc:  # noqa: BLE001 — surface as a per-source error
            return SourceResult(
                source_id=connector.meta.id,
                source_name=connector.meta.name,
                error=f"{type(exc).__name__}: {exc}",
                elapsed_ms=int((time.perf_counter() - started) * 1000),
            )

    async def fulltext(self, entity_id: str) -> str | None:
        """Resolve a global entity id ("{source}:{record}") to its full text."""
        source_id, _, record_id = entity_id.partition(":")
        connector = self.connectors.get(source_id)
        if connector is None or not record_id:
            return None
        return await connector.fulltext(record_id)

    async def aclose(self) -> None:
        await self.client.aclose()

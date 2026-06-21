"""IngestPipeline — run connector searches and persist normalized results."""

from __future__ import annotations

import asyncio
from collections.abc import Callable, Iterable

from app.connectors.manager import ConnectorManager
from app.store.repository import Repository


class IngestPipeline:
    def __init__(self, manager: ConnectorManager, repo: Repository) -> None:
        self.manager = manager
        self.repo = repo

    async def ingest(
        self,
        source_id: str,
        queries: Iterable[str],
        *,
        limit: int = 10,
        fulltext_top: int = 0,
        log: Callable[[str], None] = print,
    ) -> int:
        connector = self.manager.get(source_id)
        if connector is None:
            log(f"  [{source_id}] unknown connector — skipped")
            return 0

        stored = 0
        for q in queries:
            try:
                hits = await connector.search(q, limit=limit)
            except Exception as exc:  # noqa: BLE001 — keep ingesting other queries
                log(f"  [{source_id}] '{q}' search failed: {type(exc).__name__}")
                continue

            entities = [h.entity for h in hits]

            # Pull full text for the first few hits (only sources that support it).
            for ent in entities[:fulltext_top]:
                if ent.full_text:
                    continue
                record_id = ent.provenance.source_record_id or ent.id.split(":", 1)[-1]
                try:
                    text = await connector.fulltext(record_id)
                    if text:
                        ent.full_text = text
                except Exception:  # noqa: BLE001
                    pass

            n = self.repo.upsert_many(entities)
            stored += n
            log(f"  [{source_id}] '{q}': +{n}")
            await asyncio.sleep(0.12)  # be polite to the source APIs

        return stored

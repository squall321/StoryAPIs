"""PoetryDB — full text of ~3k public-domain English poems. No auth.

Keyword search runs against poem *lines*, so hits include the matching verse.
https://poetrydb.org
"""

from __future__ import annotations

import asyncio

import httpx

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    License,
    Provenance,
    SearchHit,
    StoryEntity,
)

_BASE = "https://poetrydb.org"


@register
class PoetryDBConnector(BaseConnector):
    meta = ConnectorMeta(
        id="poetrydb",
        name="PoetryDB",
        description="Full text of classic public-domain English poetry.",
        homepage="https://poetrydb.org",
        regions=["global"],
        languages=["en"],
        entity_types=[EntityType.WORK],
        capabilities=[Capability.SEARCH, Capability.FULLTEXT],
        license=License(
            name="Public Domain",
            commercial_ok=True,
            attribution_required=False,
        ),
        notes="Search matches lines; full poem text returned in `full_text`.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        # /lines/<text> returns poems containing <text> in any line.
        # PoetryDB is intermittently flaky, so retry transient 5xx once.
        resp = await self.client.get(f"{_BASE}/lines/{query}")
        if resp.status_code >= 500:
            await asyncio.sleep(0.6)
            resp = await self.client.get(f"{_BASE}/lines/{query}")
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        try:
            data = resp.json()
        except (ValueError, httpx.DecodingError):
            return []
        # PoetryDB returns {"status":404,"reason":"Not found"} when nothing matches.
        if isinstance(data, dict):
            return []
        return [self._to_hit(poem, query) for poem in data[:limit]]

    def _to_hit(self, poem: dict, query: str) -> SearchHit:
        lines = poem.get("lines", []) or []
        author = poem.get("author", "Unknown")
        title = poem.get("title", "(untitled)")
        snippet = next((ln for ln in lines if query.lower() in ln.lower()), None)
        entity = StoryEntity(
            id=self.make_id(f"{author}::{title}".replace(" ", "_")),
            type=EntityType.WORK,
            title=title,
            aliases=[author],
            summary=f"by {author}",
            full_text="\n".join(lines),
            languages=["en"],
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=f"{author}::{title}",
                source_url=self.meta.homepage,
                license=self.meta.license,
                language="en",
            ),
            extra={"author": author, "linecount": poem.get("linecount")},
        )
        return SearchHit(entity=entity, snippet=snippet)

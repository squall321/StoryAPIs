"""Wikipedia full-text search across multiple language editions.

Queries each configured language edition's MediaWiki ``list=search`` endpoint
concurrently and merges the results. No auth. The shared httpx client already
sends a polite User-Agent.
"""

from __future__ import annotations

import asyncio
import html
import re

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    License,
    Provenance,
    SearchHit,
    StoryEntity,
)

_TAG = re.compile(r"<[^>]+>")


def clean(s: str) -> str:
    return html.unescape(_TAG.sub("", s or "")).strip()


@register
class WikipediaConnector(BaseConnector):
    LANGS = ("en", "ko")

    meta = ConnectorMeta(
        id="wikipedia",
        name="Wikipedia",
        description="Wikipedia full-text search across language editions (default EN + KO).",
        homepage="https://www.wikipedia.org",
        regions=["global"],
        languages=["en", "ko", "ja", "zh", "fr", "de", "es"],
        entity_types=[EntityType.OTHER, EntityType.CONCEPT],
        capabilities=[Capability.SEARCH],
        license=License(
            name="CC BY-SA 4.0",
            url="https://creativecommons.org/licenses/by-sa/4.0/",
            commercial_ok=True,
            attribution_required=True,
        ),
        notes="The shared httpx client already sends a polite User-Agent.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        per = max(1, limit // len(self.LANGS) + (1 if limit % len(self.LANGS) else 0))
        results = await asyncio.gather(
            *(self._search_lang(query, lang, per) for lang in self.LANGS),
            return_exceptions=True,
        )
        merged: list[SearchHit] = []
        for result in results:
            if isinstance(result, Exception):
                continue
            merged.extend(result)
        return merged[:limit]

    async def _search_lang(self, query: str, lang: str, per: int) -> list[SearchHit]:
        resp = await self.client.get(
            f"https://{lang}.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": per,
                "srprop": "snippet",
            },
        )
        resp.raise_for_status()
        items = (resp.json() or {}).get("query", {}).get("search", [])
        return [self._to_hit(it, lang) for it in items]

    def _to_hit(self, item: dict, lang: str) -> SearchHit:
        snippet = clean(item.get("snippet", ""))
        return SearchHit(
            entity=StoryEntity(
                id=self.make_id(f"{lang}:{item['pageid']}"),
                type=EntityType.OTHER,
                title=item["title"],
                summary=snippet,
                languages=[lang],
                tags=[],
                provenance=Provenance(
                    source_id=self.meta.id,
                    source_name=self.meta.name,
                    source_record_id=f"{lang}:{item['pageid']}",
                    source_url=f"https://{lang}.wikipedia.org/?curid={item['pageid']}",
                    license=self.meta.license,
                    language=lang,
                ),
            ),
            snippet=snippet,
        )

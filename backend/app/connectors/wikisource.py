"""Wikisource — primary-source full texts via MediaWiki (Korean + English).

This is the practical path to 조선왕조실록 and other primary sources: the
Annals of the Joseon Dynasty (and its sub-volumes) live on ko.wikisource with
clean full-text extracts. Unlike encyclopedia summaries, this returns the actual
source text — exactly what a writer wants as raw material.
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


def _clean(s: str | None) -> str:
    return html.unescape(_TAG.sub("", s or "")).strip()


@register
class WikisourceConnector(BaseConnector):
    LANGS = ("ko", "en")

    meta = ConnectorMeta(
        id="wikisource",
        name="Wikisource",
        description="Primary-source full texts (incl. 조선왕조실록) via Wikisource.",
        homepage="https://wikisource.org",
        regions=["global", "korea"],
        languages=["ko", "en"],
        entity_types=[EntityType.WORK],
        capabilities=[Capability.SEARCH, Capability.FULLTEXT],
        license=License(
            name="Public Domain / CC BY-SA",
            url="https://creativecommons.org/licenses/by-sa/4.0/",
            commercial_ok=True,
            attribution_required=True,
        ),
        notes="Source texts are usually public domain; the wiki transcription is CC BY-SA.",
    )

    def _api(self, lang: str) -> str:
        return f"https://{lang}.wikisource.org/w/api.php"

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        per = max(1, -(-limit // len(self.LANGS)))  # ceil division
        groups = await asyncio.gather(
            *(self._search_lang(query, lang, per) for lang in self.LANGS),
            return_exceptions=True,
        )
        merged: list[SearchHit] = []
        for g in groups:
            if isinstance(g, list):
                merged.extend(g)
        return merged[:limit]

    async def _search_lang(self, query: str, lang: str, limit: int) -> list[SearchHit]:
        resp = await self.client.get(
            self._api(lang),
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": limit,
                "srprop": "snippet",
            },
        )
        resp.raise_for_status()
        items = resp.json().get("query", {}).get("search", []) or []
        return [self._to_hit(it, lang) for it in items]

    def _to_hit(self, item: dict, lang: str) -> SearchHit:
        pageid = item["pageid"]
        snippet = _clean(item.get("snippet"))
        return SearchHit(
            entity=StoryEntity(
                id=self.make_id(f"{lang}:{pageid}"),
                type=EntityType.WORK,
                title=item.get("title", "(untitled)"),
                summary=snippet or None,
                languages=[lang],
                provenance=Provenance(
                    source_id=self.meta.id,
                    source_name=self.meta.name,
                    source_record_id=f"{lang}:{pageid}",
                    source_url=f"https://{lang}.wikisource.org/?curid={pageid}",
                    license=self.meta.license,
                    language=lang,
                ),
                extra={"pageid": pageid, "lang": lang},
            ),
            snippet=snippet or None,
        )

    async def fulltext(self, record_id: str) -> str | None:
        lang, _, pageid = record_id.partition(":")
        if not pageid:
            return None
        resp = await self.client.get(
            self._api(lang),
            params={
                "action": "query",
                "prop": "extracts",
                "explaintext": 1,
                "exsectionformat": "plain",
                "pageids": pageid,
                "format": "json",
            },
        )
        resp.raise_for_status()
        pages = resp.json().get("query", {}).get("pages", {}) or {}
        page = pages.get(str(pageid)) or {}
        return page.get("extract") or None

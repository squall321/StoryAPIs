"""SuttaCentral — early Buddhist texts (Pali Canon & parallels) + dictionaries.

Instant search returns mixed hits (suttas, dictionary entries) with an HTML
highlight snippet. Translations (esp. Bhikkhu Sujato's) are largely CC0.
https://suttacentral.net/
"""

from __future__ import annotations

import re

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    License,
    Provenance,
    SearchHit,
    StoryEntity,
)

_BASE = "https://suttacentral.net"
_TAG = re.compile(r"<[^>]+>")


def _clean(s: str | None, limit: int = 400) -> str:
    text = _TAG.sub("", s or "").strip()
    return text[:limit] + ("…" if len(text) > limit else "")


@register
class SuttaCentralConnector(BaseConnector):
    meta = ConnectorMeta(
        id="suttacentral",
        name="SuttaCentral",
        description="Early Buddhist texts: Pali Canon, parallels, Jataka, dictionaries.",
        homepage="https://suttacentral.net",
        regions=["south-asia", "global"],
        languages=["en", "pli"],
        entity_types=[EntityType.WORK],
        capabilities=[Capability.SEARCH],
        license=License(
            name="CC0 / CC-BY (per text)",
            url="https://suttacentral.net/licensing",
            commercial_ok=True,
            attribution_required=True,
        ),
        notes="Sujato's translations are CC0; other texts vary.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(
            f"{_BASE}/api/search/instant",
            params={"query": query, "language": "en"},
        )
        resp.raise_for_status()
        hits = resp.json().get("hits", []) or []
        out: list[SearchHit] = []
        for h in hits[:limit]:
            url = h.get("url", "") or ""
            heading = h.get("heading", {}) or {}
            title = heading.get("title") or url.strip("/").replace("/", " ") or query
            content = (h.get("highlight", {}) or {}).get("content") or []
            snippet = _clean(content[0]) if content else None
            category = h.get("category")
            out.append(
                SearchHit(
                    entity=StoryEntity(
                        id=self.make_id(url or title),
                        type=EntityType.WORK,
                        title=title,
                        summary=snippet,
                        languages=["en"],
                        tags=[t for t in [category, heading.get("division")] if t],
                        provenance=Provenance(
                            source_id=self.meta.id,
                            source_name=self.meta.name,
                            source_record_id=url or title,
                            source_url=f"{_BASE}{url}" if url.startswith("/") else _BASE,
                            license=self.meta.license,
                            language="en",
                        ),
                        extra={"category": category},
                    ),
                    snippet=snippet,
                )
            )
        return out

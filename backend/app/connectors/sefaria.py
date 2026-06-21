"""Sefaria — Jewish texts (Tanakh, Talmud, Midrash, Zohar, commentaries).

Search via the Elasticsearch-backed ``/api/search-wrapper``; full text via
``/api/texts/{ref}``. Per-text licenses vary (PD / CC0 / CC-BY).
https://developers.sefaria.org/
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

_BASE = "https://www.sefaria.org"
_TAG = re.compile(r"<[^>]+>")


def _strip(s: str | None) -> str:
    return _TAG.sub("", s or "").strip()


def _ref_to_url(ref: str) -> str:
    return ref.replace(" ", "_").replace(":", ".")


@register
class SefariaConnector(BaseConnector):
    meta = ConnectorMeta(
        id="sefaria",
        name="Sefaria",
        description="Jewish canon: Tanakh, Talmud, Midrash, Zohar, commentaries.",
        homepage="https://www.sefaria.org",
        regions=["middle-east", "global"],
        languages=["en", "he"],
        entity_types=[EntityType.WORK],
        capabilities=[Capability.SEARCH, Capability.FULLTEXT],
        license=License(name="Per-text (PD / CC0 / CC-BY)", attribution_required=True),
        notes="License varies per text/version — check the source page before reuse.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.post(
            f"{_BASE}/api/search-wrapper",
            json={"query": query, "type": "text", "size": limit},
        )
        resp.raise_for_status()
        hits = (resp.json().get("hits", {}) or {}).get("hits", []) or []
        out: list[SearchHit] = []
        for h in hits[:limit]:
            doc_id = h.get("_id", "")
            ref = doc_id.rsplit(" (", 1)[0] if doc_id else "(unknown)"
            exact = (h.get("highlight", {}) or {}).get("exact") or []
            snippet = _strip(exact[0]) if exact else None
            out.append(
                SearchHit(
                    entity=StoryEntity(
                        id=self.make_id(ref),
                        type=EntityType.WORK,
                        title=ref,
                        summary=snippet,
                        languages=["en"],
                        provenance=Provenance(
                            source_id=self.meta.id,
                            source_name=self.meta.name,
                            source_record_id=ref,
                            source_url=f"{_BASE}/{_ref_to_url(ref)}",
                            license=self.meta.license,
                            language="en",
                        ),
                        extra={"score": h.get("_score")},
                    ),
                    snippet=snippet,
                )
            )
        return out

    async def fulltext(self, record_id: str) -> str | None:
        resp = await self.client.get(f"{_BASE}/api/texts/{_ref_to_url(record_id)}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        data = resp.json()
        segments = _flatten(data.get("text"))
        if not segments:
            segments = _flatten(data.get("he"))
        text = "\n".join(_strip(s) for s in segments if s)
        return text or None


def _flatten(value: object) -> list[str]:
    """Sefaria's text can be a string, a list, or nested lists."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(_flatten(item))
        return out
    return [str(value)]

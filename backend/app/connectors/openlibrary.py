"""Open Library — book metadata for ~40M editions (CC0 data). No auth.

A discovery layer (metadata, not full text): titles, authors, subjects, dates,
covers — good for finding source works to then pull from a full-text connector.
https://openlibrary.org/developers/api
"""

from __future__ import annotations

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    License,
    MediaRef,
    Provenance,
    SearchHit,
    StoryEntity,
    TimeRef,
)

_BASE = "https://openlibrary.org"


@register
class OpenLibraryConnector(BaseConnector):
    meta = ConnectorMeta(
        id="openlibrary",
        name="Open Library",
        description="Book metadata & subjects for ~40M editions (CC0 data).",
        homepage="https://openlibrary.org",
        regions=["global"],
        languages=["en", "multi"],
        entity_types=[EntityType.WORK, EntityType.PERSON],
        capabilities=[Capability.SEARCH, Capability.FETCH],
        license=License(
            name="CC0 1.0 (data)",
            url="https://openlibrary.org/developers/licensing",
            commercial_ok=True,
            attribution_required=False,
        ),
        notes="Metadata only; pair with Gutendex/Internet Archive for full text.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(
            f"{_BASE}/search.json",
            params={
                "q": query,
                "limit": limit,
                "fields": "key,title,author_name,first_publish_year,"
                "cover_i,subject,language,ia",
            },
        )
        resp.raise_for_status()
        docs = resp.json().get("docs", [])
        return [SearchHit(entity=self._to_entity(d)) for d in docs[:limit]]

    def _to_entity(self, doc: dict) -> StoryEntity:
        key = doc.get("key", "").lstrip("/")
        authors = doc.get("author_name", []) or []
        cover_id = doc.get("cover_i")
        cover = (
            f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else None
        )
        year = doc.get("first_publish_year")
        return StoryEntity(
            id=self.make_id(key.replace("works/", "")),
            type=EntityType.WORK,
            title=doc.get("title", "(untitled)"),
            aliases=authors,
            summary=("by " + ", ".join(authors)) if authors else None,
            languages=doc.get("language", []) or [],
            tags=(doc.get("subject", []) or [])[:12],
            time=TimeRef(label=str(year), start_year=year, end_year=year) if year else None,
            media=[MediaRef(type="image", url=cover)] if cover else [],
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=key,
                source_url=f"{_BASE}/{key}" if key else _BASE,
                license=self.meta.license,
            ),
            extra={"internet_archive_ids": doc.get("ia", [])},
        )

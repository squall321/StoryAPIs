"""Project Gutenberg via the Gutendex API (https://gutendex.com).

~75,000 public-domain books with direct full-text download links. No auth.
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

_BASE = "https://gutendex.com"


@register
class GutendexConnector(BaseConnector):
    meta = ConnectorMeta(
        id="gutendex",
        name="Project Gutenberg",
        description="~75k public-domain books with full text (Gutendex API).",
        homepage="https://gutendex.com",
        regions=["global"],
        languages=["en", "fr", "de", "es", "it", "pt", "nl", "fi", "zh"],
        entity_types=[EntityType.WORK, EntityType.PERSON],
        capabilities=[Capability.SEARCH, Capability.FETCH, Capability.FULLTEXT],
        license=License(
            name="Public Domain (US)",
            url="https://www.gutenberg.org/policy/permission.html",
            commercial_ok=True,
            attribution_required=False,
        ),
        notes="Strip the Gutenberg license header/trademark before reuse.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(f"{_BASE}/books", params={"search": query})
        resp.raise_for_status()
        data = resp.json()
        return [
            SearchHit(entity=self._to_entity(book))
            for book in data.get("results", [])[:limit]
        ]

    async def fetch(self, record_id: str) -> StoryEntity | None:
        resp = await self.client.get(f"{_BASE}/books/{record_id}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return self._to_entity(resp.json())

    def _to_entity(self, book: dict) -> StoryEntity:
        authors = book.get("authors", [])
        author_names = [a.get("name", "") for a in authors if a.get("name")]
        formats = book.get("formats", {}) or {}

        # Prefer a plain-text format for the full-text link.
        text_url = next(
            (
                url
                for mime, url in formats.items()
                if mime.startswith("text/plain") and "zip" not in url
            ),
            None,
        )
        cover = formats.get("image/jpeg")

        time = None
        birth = authors[0].get("birth_year") if authors else None
        death = authors[0].get("death_year") if authors else None
        if birth or death:
            time = TimeRef(label=f"author {birth or '?'}–{death or '?'}",
                           start_year=birth, end_year=death)

        return StoryEntity(
            id=self.make_id(book["id"]),
            type=EntityType.WORK,
            title=book.get("title", "(untitled)"),
            aliases=author_names,
            summary=("by " + ", ".join(author_names)) if author_names else None,
            languages=book.get("languages", []),
            tags=(book.get("subjects", []) or [])[:12] + (book.get("bookshelves", []) or []),
            time=time,
            media=[MediaRef(type="image", url=cover)] if cover else [],
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=str(book["id"]),
                source_url=f"https://www.gutenberg.org/ebooks/{book['id']}",
                license=self.meta.license,
                language=(book.get("languages") or [None])[0],
            ),
            extra={
                "download_count": book.get("download_count"),
                "fulltext_url": text_url,
                "formats": formats,
            },
        )

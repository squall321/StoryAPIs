"""Art Institute of Chicago — open access API.

No key. Open-access artworks released under CC0. Great for paintings, prints,
and artifacts spanning world cultures and history.
https://api.artic.edu/docs/
"""

from __future__ import annotations

import httpx

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    GeoRef,
    License,
    MediaRef,
    Provenance,
    SearchHit,
    StoryEntity,
    TimeRef,
)

_BASE = "https://api.artic.edu/api/v1"
_FIELDS = (
    "id,title,artist_display,date_display,date_start,date_end,image_id,"
    "classification_title,place_of_origin,term_titles,medium_display,"
    "is_public_domain"
)
_DEFAULT_IIIF = "https://www.artic.edu/iiif/2"


@register
class ArticConnector(BaseConnector):
    meta = ConnectorMeta(
        id="artic",
        name="Art Institute of Chicago",
        description="Art Institute of Chicago open access artworks (CC0).",
        homepage="https://api.artic.edu/docs/",
        regions=["global"],
        languages=["en"],
        entity_types=[EntityType.ARTIFACT, EntityType.WORK],
        capabilities=[Capability.SEARCH, Capability.FETCH],
        license=License(
            name="CC0 1.0",
            url="https://creativecommons.org/publicdomain/zero/1.0/",
            commercial_ok=True,
            attribution_required=False,
        ),
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(
            f"{_BASE}/artworks/search",
            params={"q": query, "limit": limit, "fields": _FIELDS},
        )
        resp.raise_for_status()
        data = resp.json() or {}
        iiif_url = (data.get("config") or {}).get("iiif_url", _DEFAULT_IIIF)
        return [
            SearchHit(entity=self._to_entity(item, iiif_url))
            for item in (data.get("data") or [])[:limit]
        ]

    async def fetch(self, record_id: str) -> StoryEntity | None:
        try:
            resp = await self.client.get(
                f"{_BASE}/artworks/{record_id}", params={"fields": _FIELDS}
            )
            resp.raise_for_status()
        except httpx.HTTPError:
            return None
        data = resp.json() or {}
        iiif_url = (data.get("config") or {}).get("iiif_url", _DEFAULT_IIIF)
        item = data.get("data")
        if not item:
            return None
        return self._to_entity(item, iiif_url)

    def _to_entity(self, item: dict, iiif_url: str = _DEFAULT_IIIF) -> StoryEntity:
        image_id = item.get("image_id")
        img = f"{iiif_url}/{image_id}/full/600,/0/default.jpg" if image_id else None
        is_public_domain = item.get("is_public_domain", False)

        artist_display = item.get("artist_display")
        date_display = item.get("date_display")
        place_of_origin = item.get("place_of_origin")
        classification_title = item.get("classification_title")
        term_titles = item.get("term_titles") or []

        summary = " · ".join(
            x for x in (artist_display, date_display) if x
        ) or None

        tags = [
            t
            for t in (term_titles[:10] + [classification_title, place_of_origin])
            if t
        ]

        media = (
            [
                MediaRef(
                    type="image",
                    url=img,
                    thumbnail_url=img,
                    license=self.meta.license if is_public_domain else None,
                )
            ]
            if img
            else []
        )

        places = (
            [GeoRef(label=place_of_origin, country=place_of_origin)]
            if place_of_origin
            else []
        )

        return StoryEntity(
            id=self.make_id(item["id"]),
            type=EntityType.ARTIFACT,
            title=item.get("title") or "(untitled)",
            summary=summary,
            description=item.get("medium_display") or None,
            tags=tags,
            time=TimeRef(
                label=date_display or None,
                start_year=item.get("date_start"),
                end_year=item.get("date_end"),
            ),
            places=places,
            media=media,
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=str(item["id"]),
                source_url=f"https://www.artic.edu/artworks/{item['id']}",
                license=self.meta.license
                if is_public_domain
                else License(name="Art Institute (rights vary)"),
            ),
            extra={
                "artist_display": artist_display,
                "classification": classification_title,
                "is_public_domain": is_public_domain,
            },
        )

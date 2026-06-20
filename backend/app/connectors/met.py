"""The Metropolitan Museum of Art — Open Access API.

No key. ~470k objects; many CC0 images. Great for artifacts, costume, arms &
armor, and visual motifs across world cultures and history.
https://metmuseum.github.io/
"""

from __future__ import annotations

import asyncio

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

_BASE = "https://collectionapi.metmuseum.org/public/collection/v1"


@register
class MetMuseumConnector(BaseConnector):
    meta = ConnectorMeta(
        id="met",
        name="The Met Museum",
        description="Metropolitan Museum of Art open-access objects (CC0).",
        homepage="https://metmuseum.github.io/",
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
        notes="Search returns object IDs; objects are fetched individually.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(
            f"{_BASE}/search", params={"q": query, "hasImages": "true"}
        )
        resp.raise_for_status()
        ids = (resp.json() or {}).get("objectIDs") or []
        ids = ids[:limit]
        objects = await asyncio.gather(
            *(self._fetch_object(i) for i in ids), return_exceptions=True
        )
        hits: list[SearchHit] = []
        for obj in objects:
            if isinstance(obj, StoryEntity):
                hits.append(SearchHit(entity=obj))
        return hits

    async def fetch(self, record_id: str) -> StoryEntity | None:
        return await self._fetch_object(int(record_id))

    async def _fetch_object(self, object_id: int) -> StoryEntity | None:
        try:
            resp = await self.client.get(f"{_BASE}/objects/{object_id}")
            resp.raise_for_status()
        except httpx.HTTPError:
            return None
        return self._to_entity(resp.json())

    def _to_entity(self, obj: dict) -> StoryEntity:
        image = obj.get("primaryImage") or obj.get("primaryImageSmall")
        thumb = obj.get("primaryImageSmall")
        is_cc0 = obj.get("isPublicDomain", False)
        media = (
            [MediaRef(type="image", url=image, thumbnail_url=thumb,
                      license=self.meta.license if is_cc0 else None)]
            if image
            else []
        )
        places = []
        if obj.get("country") or obj.get("city"):
            places = [GeoRef(label=obj.get("city") or obj.get("country"),
                             country=obj.get("country") or None)]

        tags = [
            t for t in (
                obj.get("classification"),
                obj.get("culture"),
                obj.get("period"),
                obj.get("department"),
                *[tag.get("term") for tag in (obj.get("tags") or [])],
            ) if t
        ]

        return StoryEntity(
            id=self.make_id(obj["objectID"]),
            type=EntityType.ARTIFACT,
            title=obj.get("title") or "(untitled object)",
            summary=", ".join(
                p for p in (obj.get("artistDisplayName"), obj.get("objectDate")) if p
            ) or None,
            description=obj.get("medium") or None,
            tags=tags[:12],
            time=TimeRef(
                label=obj.get("objectDate") or None,
                start_year=obj.get("objectBeginDate"),
                end_year=obj.get("objectEndDate"),
            ),
            places=places,
            media=media,
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=str(obj["objectID"]),
                source_url=obj.get("objectURL"),
                license=self.meta.license if is_cc0 else License(name="Met (rights vary)"),
            ),
            extra={
                "artist": obj.get("artistDisplayName"),
                "culture": obj.get("culture"),
                "classification": obj.get("classification"),
                "is_public_domain": is_cc0,
            },
        )

"""Cleveland Museum of Art — Open Access API.

No key. Thousands of open-access artworks released under CC0. Good for
artifacts, paintings, and artworks across world cultures.
https://openaccess-api.clevelandart.org/
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

_BASE = "https://openaccess-api.clevelandart.org/api"


@register
class ClevelandConnector(BaseConnector):
    meta = ConnectorMeta(
        id="cleveland",
        name="Cleveland Museum of Art",
        description="Cleveland Museum of Art open access (CC0).",
        homepage="https://openaccess-api.clevelandart.org/",
        regions=["global"],
        languages=["en"],
        entity_types=[EntityType.ARTIFACT, EntityType.WORK],
        capabilities=[Capability.SEARCH],
        license=License(
            name="CC0 1.0",
            url="https://creativecommons.org/publicdomain/zero/1.0/",
            commercial_ok=True,
            attribution_required=False,
        ),
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(
            f"{_BASE}/artworks/", params={"q": query, "limit": limit}
        )
        resp.raise_for_status()
        data = resp.json() or {}
        return [
            SearchHit(entity=self._to_entity(item))
            for item in (data.get("data") or [])[:limit]
        ]

    def _to_entity(self, item: dict) -> StoryEntity:
        images = item.get("images") or {}
        img = (images.get("web") or {}).get("url")

        culture = item.get("culture") or []
        technique = item.get("technique")
        type_ = item.get("type")
        creation_date = item.get("creation_date")
        share_license_status = item.get("share_license_status")
        is_cc0 = share_license_status == "CC0"

        summary = item.get("tombstone") or item.get("did_you_know") or None

        tags = [t for t in (culture + [technique, type_]) if t]

        media = (
            [
                MediaRef(
                    type="image",
                    url=img,
                    thumbnail_url=img,
                    license=self.meta.license if is_cc0 else None,
                )
            ]
            if img
            else []
        )

        return StoryEntity(
            id=self.make_id(item["id"]),
            type=EntityType.ARTIFACT,
            title=item.get("title") or "(untitled)",
            summary=summary,
            description=item.get("description") or None,
            tags=tags,
            time=TimeRef(
                label=creation_date or None,
                start_year=item.get("creation_date_earliest"),
                end_year=item.get("creation_date_latest"),
            ),
            media=media,
            provenance=Provenance(
                source_id=self.meta.id,
                source_name=self.meta.name,
                source_record_id=str(item["id"]),
                source_url=item.get("url"),
                license=self.meta.license
                if is_cc0
                else License(name=f"Cleveland ({share_license_status})"),
            ),
            extra={
                "culture": culture,
                "technique": technique,
                "share_license_status": share_license_status,
            },
        )

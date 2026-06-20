"""Wikidata — the cross-domain knowledge graph (CC0).

Uses ``wbsearchentities`` for fast keyword lookup of people, places, deities,
events, works, creatures... the federation spine for everything else.
https://www.wikidata.org/w/api.php
"""

from __future__ import annotations

from app.connectors.base import BaseConnector, Capability, ConnectorMeta, register
from app.models.entities import (
    EntityType,
    License,
    Provenance,
    SearchHit,
    StoryEntity,
)

_API = "https://www.wikidata.org/w/api.php"


@register
class WikidataConnector(BaseConnector):
    meta = ConnectorMeta(
        id="wikidata",
        name="Wikidata",
        description="Cross-domain structured knowledge graph (CC0).",
        homepage="https://www.wikidata.org",
        regions=["global"],
        languages=["en", "ko", "ja", "zh", "fr", "de", "es", "ar", "ru"],
        entity_types=[
            EntityType.PERSON,
            EntityType.PLACE,
            EntityType.EVENT,
            EntityType.DEITY,
            EntityType.CREATURE,
            EntityType.WORK,
            EntityType.CONCEPT,
        ],
        capabilities=[Capability.SEARCH, Capability.FETCH],
        license=License(
            name="CC0 1.0",
            url="https://creativecommons.org/publicdomain/zero/1.0/",
            commercial_ok=True,
            attribution_required=False,
        ),
        notes="wbsearchentities gives label+description; claims fetched on demand.",
    )

    async def search(
        self, query: str, *, limit: int = 10, language: str = "en"
    ) -> list[SearchHit]:
        resp = await self.client.get(
            _API,
            params={
                "action": "wbsearchentities",
                "search": query,
                "language": language,
                "uselang": language,
                "format": "json",
                "limit": min(limit, 50),
                "type": "item",
            },
        )
        resp.raise_for_status()
        data = resp.json()
        hits: list[SearchHit] = []
        for item in data.get("search", []):
            hits.append(
                SearchHit(
                    entity=StoryEntity(
                        id=self.make_id(item["id"]),
                        type=EntityType.OTHER,
                        title=item.get("label") or item["id"],
                        aliases=[a for a in [item.get("match", {}).get("text")] if a],
                        summary=item.get("description"),
                        languages=[language],
                        provenance=Provenance(
                            source_id=self.meta.id,
                            source_name=self.meta.name,
                            source_record_id=item["id"],
                            source_url=item.get("concepturi")
                            or f"https://www.wikidata.org/wiki/{item['id']}",
                            license=self.meta.license,
                            language=language,
                        ),
                        extra={"qid": item["id"]},
                    ),
                    snippet=item.get("description"),
                )
            )
        return hits

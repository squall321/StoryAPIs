"""Qur'an via the alquran.cloud API (https://alquran.cloud/api).

Verse search with an English translation (Muhammad Asad). No auth. Useful for
scripture works, motifs, and cross-cultural narrative references.
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

_BASE = "https://api.alquran.cloud/v1"


@register
class AlquranConnector(BaseConnector):
    meta = ConnectorMeta(
        id="alquran",
        name="Quran (alquran.cloud)",
        description="Qur'an verses with English translation (Muhammad Asad).",
        homepage="https://alquran.cloud/api",
        regions=["global", "middle-east"],
        languages=["ar", "en"],
        entity_types=[EntityType.WORK],
        capabilities=[Capability.SEARCH, Capability.FULLTEXT],
        license=License(
            name="Arabic PD; Asad translation terms vary",
            commercial_ok=None,
            attribution_required=None,
        ),
        notes="Verify Asad translation license before commercial reuse.",
    )

    async def search(self, query: str, *, limit: int = 10) -> list[SearchHit]:
        resp = await self.client.get(f"{_BASE}/search/{query}/all/en.asad")
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        payload = resp.json() or {}
        data = payload.get("data")
        if not isinstance(data, dict) or not data.get("count") or "matches" not in data:
            return []
        hits: list[SearchHit] = []
        for match in (data.get("matches") or [])[:limit]:
            hits.append(self._to_hit(match))
        return hits

    def _to_hit(self, match: dict) -> SearchHit:
        surah = match.get("surah") or {}
        text = match.get("text")
        return SearchHit(
            entity=StoryEntity(
                id=self.make_id(match["number"]),
                type=EntityType.WORK,
                title=(
                    f"Qur'an — {surah.get('englishName')} "
                    f"{surah.get('number')}:{match.get('numberInSurah')}"
                ),
                summary=(
                    f"Surah {surah.get('englishName')} "
                    f"({surah.get('englishNameTranslation')}) · "
                    f"{surah.get('revelationType')}"
                ),
                full_text=text,
                languages=["en"],
                tags=[
                    t
                    for t in (surah.get("englishName"), surah.get("revelationType"))
                    if t
                ],
                provenance=Provenance(
                    source_id=self.meta.id,
                    source_name=self.meta.name,
                    source_record_id=str(match["number"]),
                    source_url=(
                        f"https://quran.com/{surah.get('number')}/"
                        f"{match.get('numberInSurah')}"
                    ),
                    license=self.meta.license,
                    language="en",
                ),
            ),
            snippet=text,
        )

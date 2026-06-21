"""Deep crawler — enumerate every subpage under a Wikisource prefix and store it.

Used to pull 조선왕조실록 *in full*: the Annals are split into hundreds of
sub-pages (per king, per volume/year) nested under "조선왕조실록/". The live
search connector only sees a page at a time; this walks the whole tree.
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable

from app.connectors.manager import ConnectorManager
from app.models.entities import (
    EntityType,
    License,
    Provenance,
    StoryEntity,
)
from app.store.repository import Repository

_LICENSE = License(
    name="Public Domain / CC BY-SA",
    url="https://creativecommons.org/licenses/by-sa/4.0/",
    commercial_ok=True,
    attribution_required=True,
)


def _entity(lang: str, pageid: int, title: str, full_text: str | None) -> StoryEntity:
    return StoryEntity(
        id=f"wikisource:{lang}:{pageid}",
        type=EntityType.WORK,
        title=title,
        full_text=full_text,
        languages=[lang],
        provenance=Provenance(
            source_id="wikisource",
            source_name="Wikisource",
            source_record_id=f"{lang}:{pageid}",
            source_url=f"https://{lang}.wikisource.org/?curid={pageid}",
            license=_LICENSE,
            language=lang,
        ),
        extra={"pageid": pageid, "lang": lang, "crawled": True},
    )


async def crawl_wikisource(
    manager: ConnectorManager,
    repo: Repository,
    *,
    lang: str = "ko",
    prefix: str = "조선왕조실록",
    cap: int = 2500,
    log: Callable[[str], None] = print,
) -> int:
    client = manager.client
    connector = manager.get("wikisource")
    if connector is None:
        log("wikisource connector unavailable")
        return 0
    api = f"https://{lang}.wikisource.org/w/api.php"

    # 1. Enumerate every page titled "{prefix}/..." in the main namespace.
    pages: list[tuple[int, str]] = []
    apcontinue: str | None = None
    while len(pages) < cap:
        params = {
            "action": "query",
            "list": "allpages",
            "apprefix": f"{prefix}/",
            "apnamespace": 0,
            "aplimit": 500,
            "format": "json",
        }
        if apcontinue:
            params["apcontinue"] = apcontinue
        resp = await client.get(api, params=params)
        resp.raise_for_status()
        data = resp.json()
        for p in data.get("query", {}).get("allpages", []):
            pages.append((p["pageid"], p["title"]))
        apcontinue = data.get("continue", {}).get("apcontinue")
        if not apcontinue:
            break
    pages = pages[:cap]
    log(f"  found {len(pages)} subpages under '{prefix}/'")

    # 2. Fetch full text for each and store in batches.
    stored = 0
    batch: list[StoryEntity] = []
    for i, (pageid, title) in enumerate(pages, 1):
        try:
            text = await connector.fulltext(f"{lang}:{pageid}")
        except Exception:  # noqa: BLE001
            text = None
        batch.append(_entity(lang, pageid, title, text))
        if len(batch) >= 25:
            stored += repo.upsert_many(batch)
            batch = []
            log(f"  stored {stored}/{len(pages)}")
        await asyncio.sleep(0.05)
    if batch:
        stored += repo.upsert_many(batch)
    log(f"  crawl done: {stored} pages stored")
    return stored

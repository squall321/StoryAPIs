"""Aozora Bunko (青空文庫) ingest — Japan's public-domain literature library.

~19,000 works (夏目漱石, 芥川龍之介, 太宰治, 宮沢賢治, …). There is no clean
search API, so we pull the official index CSV, filter to public-domain works by
an author allowlist, then fetch + clean each work's full text into the library.
"""

from __future__ import annotations

import asyncio
import csv
import io
import re
import zipfile
from collections.abc import Callable

from app.connectors.manager import ConnectorManager
from app.models.entities import EntityType, License, Provenance, StoryEntity
from app.store.repository import Repository

INDEX_URL = "https://www.aozora.gr.jp/index_pages/list_person_all_extended_utf8.zip"
_BASE = "https://www.aozora.gr.jp"

_RUBY = re.compile(r"《[^》]*》")  # ruby readings: 漢字《かな》
_RUBY_MARK = re.compile(r"｜")  # ruby start marker
_ANNOT = re.compile(r"［＃[^］]*］")  # editorial annotations
_SEP = re.compile(r"^-{10,}$", re.M)  # legend block separators
_LICENSE = License(name="Public Domain (Japan)", commercial_ok=True, attribution_required=False)

# Famous public-domain authors (surname as it appears in the index 姓 column).
DEFAULT_AUTHORS = [
    "夏目", "芥川", "太宰", "宮沢", "森", "樋口", "泉", "中島",
    "梶井", "国木田", "新美", "坂口", "小泉", "堀", "宮本", "中原",
    "石川", "有島", "岡本", "豊島",
]


def _clean(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = _SEP.split(text)
    body = parts[2] if len(parts) >= 3 else text  # drop title/author + legend
    body = re.split(r"^底本：", body, flags=re.M)[0]  # drop the colophon footer
    body = _ANNOT.sub("", body)
    body = _RUBY.sub("", body)
    body = _RUBY_MARK.sub("", body)
    return body.strip()


async def _fetch_work(client, row: list[str]) -> StoryEntity | None:
    work_id, title = row[0], row[1]
    author = (row[15] + row[16]).strip()
    url = row[45]
    if not url:
        return None
    if not url.startswith("http"):
        url = _BASE + url
    enc = (row[47] or "").upper()
    try:
        data = (await client.get(url)).content
        if url.endswith(".zip"):
            zf = zipfile.ZipFile(io.BytesIO(data))
            txt_name = next(n for n in zf.namelist() if n.lower().endswith(".txt"))
            raw = zf.read(txt_name)
        else:
            raw = data
        codec = "utf-8" if "UTF-8" in enc else "shift_jis"
        body = _clean(raw.decode(codec, errors="replace"))
    except Exception:  # noqa: BLE001
        return None
    if not body:
        return None
    return StoryEntity(
        id=f"aozora:{work_id}",
        type=EntityType.WORK,
        title=title,
        aliases=[author],
        summary=f"{author} 作",
        full_text=body,
        languages=["ja"],
        provenance=Provenance(
            source_id="aozora",
            source_name="Aozora Bunko",
            source_record_id=work_id,
            source_url=row[13] or url,
            license=_LICENSE,
            language="ja",
        ),
        extra={"author": author, "author_roman": f"{row[21]} {row[22]}".strip()},
    )


async def ingest_aozora(
    manager: ConnectorManager,
    repo: Repository,
    *,
    authors: list[str] | None = None,
    cap: int = 400,
    log: Callable[[str], None] = print,
) -> int:
    authors = authors or DEFAULT_AUTHORS
    client = manager.client

    log("downloading Aozora index ...")
    resp = await client.get(INDEX_URL)
    resp.raise_for_status()
    zf = zipfile.ZipFile(io.BytesIO(resp.content))
    csv_text = zf.read(zf.namelist()[0]).decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(csv_text)))[1:]

    picked: list[list[str]] = []
    for r in rows:
        if len(r) < 51:
            continue
        if r[10] != "なし":  # 作品著作権フラグ: keep only public-domain works
            continue
        if r[15] not in authors:
            continue
        if not r[45]:
            continue
        picked.append(r)
        if len(picked) >= cap:
            break
    log(f"selected {len(picked)} public-domain works (of {len(rows)} total)")

    stored = 0
    batch: list[StoryEntity] = []
    for i, r in enumerate(picked, 1):
        ent = await _fetch_work(client, r)
        if ent:
            batch.append(ent)
        if len(batch) >= 20:
            stored += repo.upsert_many(batch)
            batch = []
            log(f"  stored {stored}/{len(picked)}")
        await asyncio.sleep(0.05)
    if batch:
        stored += repo.upsert_many(batch)
    log(f"  aozora done: {stored} works stored")
    return stored

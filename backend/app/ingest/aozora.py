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
from collections import defaultdict
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
    "夏目", "芥川", "太宰", "宮沢", "中島", "梶井", "坂口", "樋口",
    "泉", "小泉", "堀", "有島", "国木田", "新美", "森", "中原",
]

# Masterpieces guaranteed in regardless of the per-author cap.
FAMOUS_TITLES = {
    "走れメロス", "羅生門", "吾輩は猫である", "坊っちゃん", "こころ",
    "山月記", "注文の多い料理店", "銀河鉄道の夜", "檸檬", "地獄変",
    "河童", "人間失格", "斜陽", "蜘蛛の糸", "セロ弾きのゴーシュ",
    "風の又三郎", "よだかの星", "舞姫", "高瀬舟", "たけくらべ",
    "夢十夜", "三四郎", "それから", "門", "杜子春", "トロッコ",
    "ヴィヨンの妻", "津軽", "casket",
}


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
    per_author: int = 45,
    cap: int = 1600,
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

    def ok(r: list[str]) -> bool:
        return len(r) >= 51 and r[10] == "なし" and bool(r[45])

    picked: list[list[str]] = []
    seen: set[str] = set()

    # 1. guaranteed masterpieces (any allowed author)
    for r in rows:
        if ok(r) and r[1] in FAMOUS_TITLES and r[0] not in seen:
            picked.append(r)
            seen.add(r[0])

    # 2. balanced per-author fill so no single author dominates
    by_author: dict[str, list[list[str]]] = defaultdict(list)
    for r in rows:
        if ok(r) and r[15] in authors:
            by_author[r[15]].append(r)
    for surname in authors:
        n = 0
        for r in by_author[surname]:
            if r[0] in seen:
                continue
            picked.append(r)
            seen.add(r[0])
            n += 1
            if n >= per_author:
                break
    picked = picked[:cap]
    log(f"selected {len(picked)} public-domain works from {len(by_author)} authors")

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

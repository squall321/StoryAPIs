"""Crawl 조선왕조실록 (or any Wikisource prefix) in full into the library.

    cd backend
    .venv/Scripts/python.exe scripts/crawl.py                 # 조선왕조실록, cap 2500
    .venv/Scripts/python.exe scripts/crawl.py 삼국사기 1000   # other prefix + cap
"""

from __future__ import annotations

import asyncio
import sys
import time

from app.config import get_settings
from app.connectors.manager import ConnectorManager
from app.ingest.crawl import crawl_wikisource
from app.store.repository import Repository


async def main() -> int:
    prefix = sys.argv[1] if len(sys.argv) > 1 else "조선왕조실록"
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 2500

    settings = get_settings()
    manager = ConnectorManager(settings)
    repo = Repository(settings.library_db_path)

    print(f"crawling '{prefix}/' (cap {cap}) ...")
    started = time.perf_counter()
    try:
        n = await crawl_wikisource(manager, repo, prefix=prefix, cap=cap)
    finally:
        await manager.aclose()

    stats = repo.stats()
    print(f"\nDONE — crawled {n} pages in {time.perf_counter() - started:.0f}s")
    print(f"  library total : {stats['total']} (fulltext {stats['with_fulltext']})")
    print(f"  by source     : {stats['by_source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))

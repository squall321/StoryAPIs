"""Crawl Korean historical sources (사료) from Wikisource into the library.

    cd backend
    .venv/Scripts/python.exe scripts/crawl.py                 # default 사료 list
    .venv/Scripts/python.exe scripts/crawl.py 삼국사기 고려사   # specific prefixes
"""

from __future__ import annotations

import asyncio
import sys
import time

from app.config import get_settings
from app.connectors.manager import ConnectorManager
from app.ingest.crawl import crawl_wikisource
from app.store.repository import Repository

# Korean primary histories / classics available on ko.wikisource.
DEFAULT_PREFIXES = [
    "삼국사기", "삼국유사", "고려사", "고려사절요",
    "동국통감", "해동역사", "연려실기술", "난중일기", "징비록",
    "목민심서", "열하일기", "동의보감", "택리지", "동사강목",
]


async def main() -> int:
    prefixes = sys.argv[1:] or DEFAULT_PREFIXES
    cap = 2500

    settings = get_settings()
    manager = ConnectorManager(settings)
    repo = Repository(settings.library_db_path)

    print(f"crawling {len(prefixes)} sources (cap {cap} each) ...")
    started = time.perf_counter()
    total = 0
    try:
        for prefix in prefixes:
            print(f"== {prefix} ==")
            total += await crawl_wikisource(manager, repo, prefix=prefix, cap=cap)
    finally:
        await manager.aclose()

    stats = repo.stats()
    print(f"\nDONE — crawled {total} pages in {time.perf_counter() - started:.0f}s")
    print(f"  library total : {stats['total']} (fulltext {stats['with_fulltext']})")
    print(f"  wikisource    : {stats['by_source'].get('wikisource')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))

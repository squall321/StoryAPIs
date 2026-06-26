"""Ingest Aozora Bunko (青空文庫) Japanese literature into the library.

    cd backend
    .venv/Scripts/python.exe scripts/aozora.py            # default authors, cap 400
    .venv/Scripts/python.exe scripts/aozora.py 夏目 芥川   # specific surnames
"""

from __future__ import annotations

import asyncio
import sys
import time

from app.config import get_settings
from app.connectors.manager import ConnectorManager
from app.ingest.aozora import ingest_aozora
from app.store.repository import Repository


async def main() -> int:
    authors = sys.argv[1:] or None

    settings = get_settings()
    manager = ConnectorManager(settings)
    repo = Repository(settings.library_db_path)

    started = time.perf_counter()
    try:
        n = await ingest_aozora(manager, repo, authors=authors, cap=400)
    finally:
        await manager.aclose()

    stats = repo.stats()
    print(f"\nDONE — {n} Aozora works in {time.perf_counter() - started:.0f}s")
    print(f"  library total : {stats['total']} (fulltext {stats['with_fulltext']})")
    print(f"  aozora        : {stats['by_source'].get('aozora')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))

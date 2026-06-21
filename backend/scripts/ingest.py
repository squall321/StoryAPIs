"""Run the ingestion plan: collect data from live sources into the local library.

    cd backend
    .venv/Scripts/python.exe scripts/ingest.py
"""

from __future__ import annotations

import asyncio
import sys
import time

from app.config import get_settings
from app.connectors.manager import ConnectorManager
from app.ingest.pipeline import IngestPipeline
from app.ingest.plan import PLAN
from app.store.repository import Repository


def _scale(plan: list, factor: int) -> list:
    """`--deep`: roughly double breadth and pull more full text per query."""
    scaled = []
    for source_id, queries, opts in plan:
        o = dict(opts)
        o["limit"] = min(o.get("limit", 10) * factor, 50)
        if "fulltext_top" in o:
            o["fulltext_top"] = o["fulltext_top"] + 3
        scaled.append((source_id, queries, o))
    return scaled


async def main() -> int:
    deep = "--deep" in sys.argv
    plan = _scale(PLAN, 2) if deep else PLAN
    print(f"ingest mode: {'DEEP' if deep else 'standard'}")

    settings = get_settings()
    manager = ConnectorManager(settings)
    repo = Repository(settings.library_db_path)
    pipe = IngestPipeline(manager, repo)

    started = time.perf_counter()
    total = 0
    try:
        for source_id, queries, opts in plan:
            print(f"== {source_id} ({len(queries)} queries) ==")
            total += await pipe.ingest(source_id, queries, **opts)
    finally:
        await manager.aclose()

    elapsed = time.perf_counter() - started
    stats = repo.stats()
    print(f"\nDONE — wrote {total} records in {elapsed:.0f}s into {repo.path}")
    print(f"  unique stored : {stats['total']}")
    print(f"  with fulltext : {stats['with_fulltext']}")
    print(f"  by source     : {stats['by_source']}")
    print(f"  by type       : {stats['by_type']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))

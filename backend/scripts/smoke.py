"""Live smoke test: hit every connector against the real APIs and report.

    cd backend
    .venv/Scripts/python.exe scripts/smoke.py "joseon" "dragon"
"""

from __future__ import annotations

import asyncio
import sys

from app.config import get_settings
from app.connectors.manager import ConnectorManager


async def main(queries: list[str]) -> int:
    manager = ConnectorManager(get_settings())
    print(f"Registered connectors: {sorted(manager.connectors)}\n")
    failures = 0
    try:
        for q in queries:
            print(f"=== search: {q!r} ===")
            resp = await manager.search(q, limit=3)
            for r in resp.results:
                if r.error:
                    print(f"  [FAIL] {r.source_id:12} {r.error}")
                    failures += 1
                else:
                    sample = r.hits[0].entity.title if r.hits else "(no hits)"
                    print(
                        f"  [ ok ] {r.source_id:12} {r.total:>2} hits "
                        f"in {r.elapsed_ms:>4}ms  e.g. {sample[:60]}"
                    )
            print()
    finally:
        await manager.aclose()
    print(f"DONE — {failures} connector error(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    qs = sys.argv[1:] or ["dragon", "조선"]
    raise SystemExit(asyncio.run(main(qs)))

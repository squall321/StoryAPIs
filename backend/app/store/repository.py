"""SQLite repository for collected (ingested) StoryEntity records.

The live connectors are a gateway; this is the warehouse. Ingested records are
normalized to StoryEntity and stored here so the corpus can be browsed, counted,
and fed to the story composer without re-hitting external APIs.
"""

from __future__ import annotations

import sqlite3
import threading
from pathlib import Path

from app.models.entities import StoryEntity

_SCHEMA = """
CREATE TABLE IF NOT EXISTS entities (
  id           TEXT PRIMARY KEY,
  source_id    TEXT NOT NULL,
  type         TEXT,
  title        TEXT,
  summary      TEXT,
  language     TEXT,
  source_url   TEXT,
  license      TEXT,
  has_fulltext INTEGER DEFAULT 0,
  retrieved_at TEXT,
  data         TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_entities_source ON entities(source_id);
CREATE INDEX IF NOT EXISTS idx_entities_type   ON entities(type);
CREATE INDEX IF NOT EXISTS idx_entities_title  ON entities(title);
"""

_UPSERT = """
INSERT INTO entities
  (id, source_id, type, title, summary, language, source_url, license,
   has_fulltext, retrieved_at, data)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
  source_id=excluded.source_id, type=excluded.type, title=excluded.title,
  summary=excluded.summary, language=excluded.language,
  source_url=excluded.source_url, license=excluded.license,
  has_fulltext=excluded.has_fulltext, retrieved_at=excluded.retrieved_at,
  data=excluded.data
"""


class Repository:
    def __init__(self, path: str) -> None:
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        with self._conn() as c:
            c.executescript(_SCHEMA)

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _row(self, e: StoryEntity) -> tuple:
        return (
            e.id,
            e.provenance.source_id,
            e.type.value,
            e.title,
            e.summary,
            e.languages[0] if e.languages else None,
            e.provenance.source_url,
            e.provenance.license.name,
            1 if e.full_text else 0,
            e.provenance.retrieved_at.isoformat(),
            e.model_dump_json(),
        )

    def upsert_many(self, entities: list[StoryEntity]) -> int:
        rows = [self._row(e) for e in entities]
        if not rows:
            return 0
        with self._lock, self._conn() as c:
            c.executemany(_UPSERT, rows)
        return len(rows)

    def search(
        self,
        q: str | None = None,
        source_id: str | None = None,
        type_: str | None = None,
        limit: int = 50,
    ) -> list[StoryEntity]:
        clauses: list[str] = []
        params: list[object] = []
        if q:
            like = f"%{q}%"
            clauses.append("(title LIKE ? OR summary LIKE ?)")
            params += [like, like]
        if source_id:
            clauses.append("source_id = ?")
            params.append(source_id)
        if type_:
            clauses.append("type = ?")
            params.append(type_)
        where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
        params.append(limit)
        with self._conn() as c:
            rows = c.execute(
                f"SELECT data FROM entities{where} LIMIT ?", params
            ).fetchall()
        return [StoryEntity.model_validate_json(r["data"]) for r in rows]

    def get(self, entity_id: str) -> StoryEntity | None:
        with self._conn() as c:
            row = c.execute(
                "SELECT data FROM entities WHERE id = ?", (entity_id,)
            ).fetchone()
        return StoryEntity.model_validate_json(row["data"]) if row else None

    def stats(self) -> dict:
        with self._conn() as c:
            total = c.execute("SELECT COUNT(*) n FROM entities").fetchone()["n"]
            ft = c.execute(
                "SELECT COUNT(*) n FROM entities WHERE has_fulltext = 1"
            ).fetchone()["n"]
            by_source = {
                r["source_id"]: r["n"]
                for r in c.execute(
                    "SELECT source_id, COUNT(*) n FROM entities "
                    "GROUP BY source_id ORDER BY n DESC"
                )
            }
            by_type = {
                r["type"]: r["n"]
                for r in c.execute(
                    "SELECT type, COUNT(*) n FROM entities "
                    "GROUP BY type ORDER BY n DESC"
                )
            }
        return {
            "total": total,
            "with_fulltext": ft,
            "by_source": by_source,
            "by_type": by_type,
        }

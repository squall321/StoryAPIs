"""SQLite repository for collected (ingested) StoryEntity records.

The live connectors are a gateway; this is the warehouse. Records are normalized
to StoryEntity and stored here so the corpus can be browsed, full-text searched
(incl. CJK via an FTS5 trigram index), and fed to the story composer.
"""

from __future__ import annotations

import sqlite3
import threading
from pathlib import Path

from app.models.entities import StoryEntity

_SCHEMA_BASE = """
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

# Trigram tokenizer → substring matching that works for CJK (Korean/Chinese/…)
# and Latin alike, and searches the full text, not just metadata.
_FTS_CREATE = (
    "CREATE VIRTUAL TABLE IF NOT EXISTS entities_fts USING fts5("
    "id UNINDEXED, title, summary, full_text, tokenize='trigram')"
)

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
        self.fts_enabled = False
        with self._conn() as c:
            c.execute("PRAGMA journal_mode=WAL")  # readers don't block the writer
            c.executescript(_SCHEMA_BASE)
            try:
                c.execute(_FTS_CREATE)
                self.fts_enabled = True
            except sqlite3.OperationalError:
                self.fts_enabled = False  # trigram unavailable → LIKE only
        if self.fts_enabled:
            self._maybe_backfill_fts()

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path, timeout=10)
        conn.row_factory = sqlite3.Row
        return conn

    # --- writes ---------------------------------------------------------
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
        if not entities:
            return 0
        rows = [self._row(e) for e in entities]
        with self._lock, self._conn() as c:
            c.executemany(_UPSERT, rows)
            if self.fts_enabled:
                ids = [(e.id,) for e in entities]
                fts = [
                    (e.id, e.title or "", e.summary or "", e.full_text or "")
                    for e in entities
                ]
                c.executemany("DELETE FROM entities_fts WHERE id = ?", ids)
                c.executemany(
                    "INSERT INTO entities_fts(id, title, summary, full_text) "
                    "VALUES (?, ?, ?, ?)",
                    fts,
                )
        return len(rows)

    def _maybe_backfill_fts(self) -> None:
        with self._conn() as c:
            n_e = c.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
            n_f = c.execute("SELECT COUNT(*) FROM entities_fts").fetchone()[0]
        if n_e and not n_f:
            self.rebuild_fts()

    def rebuild_fts(self) -> int:
        if not self.fts_enabled:
            return 0
        with self._lock, self._conn() as c:
            c.execute("DELETE FROM entities_fts")
            batch = []
            for r in c.execute("SELECT data FROM entities"):
                e = StoryEntity.model_validate_json(r["data"])
                batch.append((e.id, e.title or "", e.summary or "", e.full_text or ""))
            c.executemany(
                "INSERT INTO entities_fts(id, title, summary, full_text) "
                "VALUES (?, ?, ?, ?)",
                batch,
            )
        return len(batch)

    # --- reads ----------------------------------------------------------
    def search(
        self,
        q: str | None = None,
        source_id: str | None = None,
        type_: str | None = None,
        limit: int = 50,
    ) -> list[StoryEntity]:
        qs = (q or "").strip()
        # FTS trigram needs >=3 chars; shorter queries use LIKE (also CJK-safe).
        if self.fts_enabled and len(qs) >= 3:
            try:
                return self._fts_search(qs, source_id, type_, limit)
            except sqlite3.OperationalError:
                pass
        return self._like_search(qs, source_id, type_, limit)

    def _fts_search(
        self, qs: str, source_id: str | None, type_: str | None, limit: int
    ) -> list[StoryEntity]:
        match = '"' + qs.replace('"', '""') + '"'  # phrase = substring under trigram
        clauses = ["entities_fts MATCH ?"]
        params: list[object] = [match]
        if source_id:
            clauses.append("e.source_id = ?")
            params.append(source_id)
        if type_:
            clauses.append("e.type = ?")
            params.append(type_)
        params.append(limit)
        sql = (
            "SELECT e.data FROM entities_fts "
            "JOIN entities e ON e.id = entities_fts.id "
            f"WHERE {' AND '.join(clauses)} ORDER BY rank LIMIT ?"
        )
        with self._conn() as c:
            rows = c.execute(sql, params).fetchall()
        return [StoryEntity.model_validate_json(r["data"]) for r in rows]

    def _like_search(
        self, qs: str, source_id: str | None, type_: str | None, limit: int
    ) -> list[StoryEntity]:
        clauses: list[str] = []
        params: list[object] = []
        if qs:
            like = f"%{qs}%"
            # `data` holds the serialized entity (incl. full_text), so this also
            # matches inside the body — correct for any-length CJK queries.
            clauses.append("(title LIKE ? OR summary LIKE ? OR data LIKE ?)")
            params += [like, like, like]
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

    def get_many(self, ids: list[str]) -> list[StoryEntity]:
        if not ids:
            return []
        placeholders = ",".join("?" for _ in ids)
        with self._conn() as c:
            rows = c.execute(
                f"SELECT data FROM entities WHERE id IN ({placeholders})", ids
            ).fetchall()
        return [StoryEntity.model_validate_json(r["data"]) for r in rows]

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
            "fts": self.fts_enabled,
        }

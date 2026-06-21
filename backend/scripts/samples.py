"""Dump a few real records (with excerpts) from the library to judge quality.

Writes UTF-8 so non-Latin text renders correctly when read back.
"""

from __future__ import annotations

from pathlib import Path

from app.config import get_settings
from app.store.repository import Repository

OUT = Path(__file__).resolve().parents[1] / "samples_preview.txt"

# (label, source_id, query|None) — None = any record from that source.
PICKS = [
    ("조선왕조실록 (실록 본문)", "wikisource", "세종실록"),
    ("삼국사기", "wikisource", "삼국사기"),
    ("열하일기", "wikisource", "열하일기"),
    ("동의보감", "wikisource", "동의보감"),
    ("Gutenberg 전문", "gutendex", None),
    ("Quran (영역)", "alquran", None),
    ("Sefaria (유대 경전)", "sefaria", None),
    ("The Met (유물 메타데이터)", "met", None),
    ("Wikidata (지식그래프)", "wikidata", "dragon"),
]


def _pick(repo: Repository, source: str, query: str | None):
    items = repo.search(query, source_id=source, limit=40)
    # prefer an item that actually carries full text
    return next((e for e in items if e.full_text), items[0] if items else None)


def main() -> int:
    repo = Repository(get_settings().library_db_path)
    blocks: list[str] = []
    for label, source, query in PICKS:
        e = _pick(repo, source, query)
        if e is None:
            blocks.append(f"## {label}\n(해당 소스에서 레코드 없음)\n")
            continue
        body = e.full_text or e.description or e.summary or "(본문/요약 없음)"
        excerpt = body[:700].strip()
        ellipsis = "…" if len(body) > 700 else ""
        blocks.append(
            f"## {label}\n"
            f"- 제목: {e.title}\n"
            f"- 타입: {e.type.value} | 소스: {e.provenance.source_name}\n"
            f"- 출처: {e.provenance.source_url}\n"
            f"- 전문보유: {bool(e.full_text)} | 전문 길이: {len(e.full_text or '')}자\n"
            f"- 라이선스: {e.provenance.license.name}\n"
            f"--- 발췌 ---\n{excerpt}{ellipsis}\n"
        )
    OUT.write_text("\n".join(blocks), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

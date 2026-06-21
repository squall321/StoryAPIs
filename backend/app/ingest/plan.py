"""Default ingestion plan — seed queries per source for a broad first harvest.

Tuned to gather a meaningful, multilingual corpus quickly: 조선왕조실록 and other
Korean primary sources with full text, plus mythology/folklore/literature/artifacts
across the world. Edit freely; `scripts/ingest.py` runs this.
"""

from __future__ import annotations

# Cross-cultural motif seeds (good recall across most sources).
MOTIFS_EN = [
    "dragon", "ghost", "hero", "king", "queen", "love", "war", "god",
    "monster", "sword", "witch", "fox", "tiger", "moon", "sea", "fire",
    "serpent", "phoenix", "demon", "flood",
]
MOTIFS_KO = [
    "용", "유령", "영웅", "왕", "사랑", "전쟁", "신", "요괴",
    "호랑이", "구미호", "도깨비", "바다", "달", "칼", "귀신",
]

# Joseon Dynasty Annals (조선왕조실록) + Korean primary histories on Wikisource.
SILLOK = [
    "조선왕조실록", "태조실록", "정종실록", "태종실록", "세종실록",
    "문종실록", "단종실록", "세조실록", "예종실록", "성종실록",
    "연산군일기", "중종실록", "인종실록", "명종실록", "선조실록",
    "광해군일기", "인조실록", "효종실록", "현종실록", "숙종실록",
    "경종실록", "영조실록", "정조실록", "순조실록", "헌종실록",
    "철종실록", "고종실록", "순종실록",
    "고려사", "삼국사기", "삼국유사", "동국통감",
]

# (source_id, queries, options)
PLAN: list[tuple[str, list[str], dict]] = [
    ("wikisource", SILLOK, {"limit": 6, "fulltext_top": 2}),
    (
        "gutendex",
        ["dragon", "myth", "fairy tale", "legend", "King Arthur", "Norse",
         "Greek mythology", "folklore", "Gilgamesh", "Beowulf"],
        {"limit": 12, "fulltext_top": 1},
    ),
    ("wikidata", MOTIFS_EN + MOTIFS_KO, {"limit": 20}),
    ("wikipedia", MOTIFS_EN + ["조선", "신화", "설화", "민담"], {"limit": 10}),
    (
        "met",
        ["dragon", "samurai", "buddha", "crown", "sword", "mask",
         "phoenix", "demon", "tiger", "deity"],
        {"limit": 15},
    ),
    ("artic", ["dragon", "myth", "god", "mask", "tiger", "phoenix", "buddha"],
     {"limit": 12}),
    ("cleveland", ["dragon", "buddha", "myth", "mask", "tiger", "deity"],
     {"limit": 12}),
    (
        "sefaria",
        ["angel", "king", "flood", "creation", "serpent", "prophet", "demon"],
        {"limit": 8, "fulltext_top": 2},
    ),
    ("suttacentral", ["compassion", "mind", "karma", "desire", "rebirth"],
     {"limit": 8}),
    ("alquran", ["light", "mercy", "garden", "mountain", "sea", "fire"],
     {"limit": 10}),
    (
        "openlibrary",
        ["mythology", "folklore", "legend", "fairy tales", "epic poetry",
         "world mythology"],
        {"limit": 15},
    ),
    ("poetrydb", ["love", "death", "sea", "moon", "war", "night", "dream"],
     {"limit": 12}),
]

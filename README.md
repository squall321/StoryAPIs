# 📚 StoryAPIs

> 세계의 역사·신화·문학을 한데 모으는 **이야기의 원천(知識寶庫)** 플랫폼.
>
> 조선왕조실록에서 길가메시 서사시, 그리스 신화, 메트로폴리탄 미술관 유물까지 —
> 흩어진 세계의 지식 데이터베이스를 하나의 통합 모델로 검색·추출하고,
> 그 자료를 바탕으로 새로운 이야기를 짓는 데 활용한다.

---

## 무엇을 하는 프로젝트인가

소설·비문학·시나리오 등 모든 창작의 바탕이 되는 **원천 데이터**는 이미 전 세계에
방대하게 구축되어 있다 — 다만 수백 개의 사이트·API·아카이브에 흩어져 있고, 형식도
라이선스도 제각각이다. StoryAPIs는 이것들을:

1. **조사한다** — 접근 가능한 세계의 지식 DB/API를 체계적으로 카탈로그화 (`docs/research/`)
2. **연결한다** — 각 소스를 *커넥터(Connector)* 로 감싸 하나의 통합 모델로 정규화
3. **검색·추출한다** — 여러 소스를 동시에(federated) 검색하고 자료를 가져온다
4. **창작에 쓴다** — 모은 자료를 수집함에 담아 Claude가 새 이야기 초안을 짓는다 *(구현됨)*

## 현재 동작하는 것 (v0.2)

**12개 소스**에 대한 통합 연합 검색 + 전문(全文) 리더 + **수집함→집필(Claude 컴포저)**:

| 소스 | 내용 | 라이선스 |
|------|------|----------|
| **Project Gutenberg** (Gutendex) | ~75,000권 퍼블릭 도메인 도서 전문(全文) | Public Domain |
| **Wikisource** | **조선왕조실록** 등 1차 사료 전문 (ko/en) | PD / CC BY-SA |
| **The Met / Art Institute / Cleveland** | 미술·유물 (이미지 포함) | CC0 |
| **Wikidata** | 인물·장소·사건·신·괴물·작품 — 범분야 지식그래프 | CC0 |
| **Wikipedia** | 다국어(한국어 포함) 전문 검색 | CC BY-SA |
| **Sefaria / SuttaCentral / Quran** | 유대·불교·이슬람 경전 원전 | per-text |
| **Open Library / PoetryDB** | 도서 메타데이터 · 고전 영시 전문 | CC0 / PD |

검색해서 카드를 **수집함에 담고** → **집필** 탭에서 브리프를 적으면
`POST /api/compose`가 Opus 4.8로 출처를 인용한 새 이야기 초안을 생성한다
(작문은 `STORYAPIS_ANTHROPIC_API_KEY` 필요).

**실제 데이터 수집(인제스트)** — 라이브 게이트웨이를 넘어 로컬 SQLite에 정규화 저장:

```bash
cd backend && .venv/Scripts/python.exe scripts/ingest.py   # seed 플랜으로 대량 수집
# → 조선왕조실록 + 신화/문학/유물 1,498건 수집 (data/library.db, gitignore됨)
curl "http://localhost:8000/api/library/stats"
curl "http://localhost:8000/api/library/search?q=실록&source=wikisource"
```

```bash
$ curl "http://localhost:8000/api/search?q=gilgamesh&limit=3"
# → met / openlibrary / wikidata / gutendex 에서 정규화된 결과를 한 번에
```

## 아키텍처

```
┌────────────────────┐     /api/search?q=...      ┌──────────────────────────┐
│  Frontend          │ ─────────────────────────▶ │  FastAPI backend         │
│  React + TS + Vite │ ◀───── SearchResponse ───── │                          │
└────────────────────┘                             │   ConnectorManager       │
                                                   │   ├─ gutendex            │
   통합 모델(StoryEntity)로 정규화된               │   ├─ met        (async,  │
   카드 UI · 소스 필터 · 라이선스 배지             │   ├─ wikidata    병렬)   │
                                                   │   ├─ openlibrary         │
                                                   │   └─ poetrydb            │
                                                   └──────────────────────────┘
```

- **통합 모델** — 모든 소스는 [`StoryEntity`](backend/app/models/entities.py)
  (id·type·title·summary·time·places·media·relations·provenance) 하나로 정규화된다.
- **커넥터 프레임워크** — [`BaseConnector`](backend/app/connectors/base.py) 를 상속하고
  `@register` 하면 끝. 매니저가 비동기로 모든 소스를 병렬 검색하고, 한 소스가 실패해도
  나머지 결과는 그대로 반환한다(소스별 오류 격리).

자세한 설계는 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), 전체 로드맵은
[docs/ROADMAP.md](docs/ROADMAP.md), 조사된 데이터 소스 카탈로그는
[docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) 참고.

## 빠른 시작

### 백엔드 (FastAPI)

```bash
cd backend
python -m venv .venv
.venv/Scripts/activate        # Windows  (mac/linux: source .venv/bin/activate)
pip install -r requirements.txt
uvicorn app.main:app --reload # http://localhost:8000/docs
```

키 없이도 위 5개 소스는 바로 동작한다. 선택적 키는 `.env.example` 참고(`.env`로 복사).

라이브 스모크 테스트:

```bash
cd backend
.venv/Scripts/python.exe scripts/smoke.py "dragon" "조선"
```

### 프론트엔드 (React + Vite)

```bash
cd frontend
npm install
npm run dev                   # http://localhost:5173  (/api 는 :8000 으로 프록시)
```

## 기술 스택

- **백엔드** — Python 3.13 · FastAPI · httpx(비동기) · Pydantic v2
- **프론트엔드** — React 19 · TypeScript · Vite
- **창작 보조** *(로드맵)* — Anthropic Claude (`claude-opus-4-8`)

## 프로젝트 구조

```
StoryAPIs/
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI 앱
│   │   ├── config.py              # 설정 (STORYAPIS_* 환경변수)
│   │   ├── models/entities.py     # 통합 모델 (StoryEntity 등)
│   │   ├── connectors/            # 소스별 커넥터 + base + manager
│   │   └── api/routes/            # /health /sources /search
│   └── scripts/smoke.py           # 라이브 검증 스크립트
├── frontend/                      # React + TS + Vite 검색 UI
└── docs/
    ├── ARCHITECTURE.md
    ├── ROADMAP.md
    ├── DATA_SOURCES.md            # 조사 카탈로그 통합 인덱스
    └── research/                  # 영역별 상세 조사 (6개 파일)
```

## 라이선스 · 윤리 주의

소스마다 라이선스가 다르다(CC0 / CC-BY / Public Domain / NC·ND / 스크래핑 한정).
각 `StoryEntity.provenance.license` 에 출처와 권리를 항상 보존하며, 상업적 재사용
가능 여부는 소스별로 반드시 확인해야 한다. 또한 일부 원주민·토착 전승 자료는 저작권과
별개로 **공동체의 문화적 이용 규약(ICIP)** 을 따른다 — 자세한 플래그는
[docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) 참고.

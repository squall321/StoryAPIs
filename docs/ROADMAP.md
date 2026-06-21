# 로드맵 — 방대한 계획

"세계의 모든 이야기 원천을 모아 새 이야기에 쓰는" 목표를 단계로 나눈 것. 각 단계는
이전 단계 위에서 실제로 동작하는 산출물을 남긴다(빅뱅 금지, 점진적 확장).

범례: ✅ 완료 · 🚧 진행/부분 · ⬜ 예정

---

## Phase 0 — 기반 (✅ v0.1, 현재)

- ✅ 세계 데이터 소스 조사·카탈로그화 (6개 영역, `docs/research/`)
- ✅ 모노레포 + 통합 데이터 모델(`StoryEntity`) + 커넥터 프레임워크
- ✅ 무인증 커넥터 5종(Gutenberg, Met, Wikidata, Open Library, PoetryDB) — 라이브 검증
- ✅ 연합 검색 API(`/api/search`) + 소스 카탈로그 API
- ✅ React+TS 검색 UI (소스 필터·카드·라이선스 배지)

## Phase 1 — 소스 확장 (🚧 대부분 완료, 5→12 커넥터)

목표: "외국 DB 대폭 보강" 지시 반영 — 커넥터를 무인증 깨끗한 라이선스부터 폭넓게.

- ✅ **미술관(CC0)**: Art Institute of Chicago, Cleveland Museum
- ✅ **종교·신화 원전**: Sefaria(유대 경전), SuttaCentral(불교), alquran.cloud(꾸란)
- ✅ **Wikipedia 다국어 검색**(EN+KO 병합) — 한국어 콘텐츠 확보
- ✅ **한국 핵심**: 조선왕조실록 → ko/en **Wikisource** MediaWiki API로 1차 사료 전문 제공
  (sillok.history.go.kr은 JS/AJAX라 공개 API 없음 → Wikisource 경유)
- ⬜ **지식그래프 심화**: Wikidata `wbgetentities` relations, DBpedia
- ⬜ **고전·신화 원전 추가**: Perseus(TEI), ctext.org(山海經), GRETIL(산스크리트)
- ⬜ **지리/작명/세계관**: GeoNames, World Historical Gazetteer, Wiktionary 어원, GBIF
- ⬜ 키 필요한 소스용 설정 키 배선(Europeana, Trove, Smithsonian…)

## Phase 2 — 영속화 & 색인 (🚧 SQLite로 동작, 실측 3,088건 수집)

실시간 호출만으로는 느리고 일부 소스는 덤프형이다. 정규화 저장 + 검색 가속.

- ✅ **로컬 라이브러리(SQLite + WAL)** — `StoryEntity` 영속화(`backend/app/store/repository.py`)
- ✅ **인제스트 파이프라인 + seed 플랜**(`app/ingest/`, `scripts/ingest.py --deep`)
  + **조선왕조실록 전권 크롤러**(`app/ingest/crawl.py`, `scripts/crawl.py`)
  — **실측 3,088건 수집**(전문 463건; 조선왕조실록 284개 하위 페이지 전문 포함)
- ✅ **CJK 전문검색** — FTS5 trigram(한글/한문 부분·본문 검색) + 짧은 쿼리 LIKE 폴백
- ✅ **라이브러리 조회 API**: `GET /api/library/stats`, `GET /api/library/search`
- ⬜ Postgres 이관(프로덕션) — 현재는 SQLite FTS5로 CJK 검색 충족
- ⬜ 응답 캐시 레이어, 덤프형 소스 대량 인제스트(Aozora/CBETA/Perseus 전권)

## Phase 3 — 의미 검색 & 엔티티 해소 (⬜)

- ⬜ 임베딩 색인(pgvector/Qdrant) — "비슷한 모티프/인물/사건" 의미 검색
- ⬜ 엔티티 해소: 소스 간 동일 인물/장소 병합(Wikidata QID를 허브로)
- ⬜ 관계 그래프 탐색 UI(인물↔사건↔장소 네트워크)

## Phase 4 — 창작 워크스페이스 & 스토리 컴포저 (🚧 MVP 동작)

프로젝트의 최종 목적 — 모은 자료로 **새 이야기 짓기**.

- ✅ 수집함: 검색/상세에서 "담기" → localStorage 컬렉션
- ✅ `/api/compose`: 수집한 `StoryEntity` 묶음 + 브리프를 Claude(`claude-opus-4-8`)에
  전달 → 새 이야기 초안 생성, **출처 인용 보존** (키 없으면 503)
- ✅ 집필 뷰: 브리프·옵션(분량/언어/장르/톤) + 초안 리더 + 인용 출처 패널
- ⬜ 모티프 추출: 폭/원전에서 ATU 유형·Thompson 모티프 자동 태깅
- ⬜ 컴포저 스트리밍, 메모/태깅, 초안 버전 관리, 컬렉션 서버 영속화

## Phase 5 — 운영 & 공개 (⬜)

- ⬜ 배포(백엔드 컨테이너 + 프론트 정적 호스팅), 환경별 설정
- ⬜ 사용자 계정·저장된 컬렉션·작업물
- ⬜ 레이트리밋·관측성(로깅/메트릭), 라이선스 준수 자동 점검
- ⬜ 단위/통합 테스트(녹화 응답), CI

---

## 지금 바로 다음에 할 일 (Phase 1 착수 후보)

1. Art Institute of Chicago + Cleveland 커넥터(무인증 CC0) — 카탈로그 다양성 즉시 +.
2. Sefaria / SuttaCentral / alquran.cloud — 종교·신화 **원전 전문** 확보(창작 모티프 핵심).
3. Wikidata 엔티티 상세(`fetch`)로 relations 채워 그래프 토대 마련.
4. 조선왕조실록 접근 경로 확정(API vs 덤프) — 사용자 1순위 관심 소스.

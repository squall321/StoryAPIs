# 아키텍처

StoryAPIs는 "흩어진 세계 지식 → 통합 모델 → 검색/추출 → 창작 활용"의 4단계 파이프라인이다.
현재(v0.1)는 1~3단계의 실시간(live) 경로가 구현되어 있고, 4단계와 영속화(저장/색인)는
로드맵 단계다.

## 1. 핵심 원칙

- **단일 통합 모델** — 어떤 소스든 결과는 하나의 `StoryEntity`로 정규화된다. 프론트엔드,
  검색, 추후 RAG/창작기는 출처가 조선왕조실록이든 Wikidata든 동일하게 다룬다.
- **출처 보존(provenance-first)** — 모든 레코드는 출처·원본 URL·**라이선스**를 항상 들고
  다닌다. 창작 재사용 가능 여부 판단의 근거이자, 추후 인용/각주의 토대다.
- **소스별 격리** — 한 소스가 느리거나 죽어도 연합 검색 전체가 죽지 않는다. 각 커넥터는
  비동기로 병렬 실행되고 실패는 그 소스의 `error` 필드로만 표면화된다.
- **플러그인형 커넥터** — 소스 추가 = `BaseConnector` 상속 + `@register`. 코어 수정 불필요.

## 2. 통합 데이터 모델 (`backend/app/models/entities.py`)

```
StoryEntity
├── id            "{source_id}:{record_id}"  (전역 유일)
├── type          EntityType  (person/place/event/period/work/deity/
│                              creature/artifact/organization/concept/motif/other)
├── title, aliases[], summary, description
├── full_text     필요 시에만(전문 작품) 채움
├── languages[], tags[]
├── time          TimeRef   (label, start_year, end_year — 음수 = BCE)
├── places[]      GeoRef    (label, lat, lon, country)
├── media[]       MediaRef  (image/iiif/audio, url, license)
├── relations[]   Relation  (predicate, target — 지식그래프 엣지)
├── provenance    Provenance(source, url, **License**, language, retrieved_at)
└── extra         소스 고유 원자료(full-text url, qid, 다운로드 포맷 등)
```

이 형태는 의도적으로 "느슨한 지식 노드 + 엣지"다. 인물·장소·사건·신·괴물·작품·유물을
모두 한 타입으로 표현하되, `type`과 `relations`로 그래프를 구성할 수 있다.

## 3. 커넥터 프레임워크 (`backend/app/connectors/`)

```
BaseConnector (ABC)
├── meta: ConnectorMeta   # id, name, 설명, 지역/언어, capabilities, license, auth 필요여부
├── search(query, limit) -> [SearchHit]      # 필수
├── fetch(record_id)     -> StoryEntity|None # 선택 (상세/전문)
├── health()             -> bool
└── available()          -> bool             # 키 유무 등 실행 가능 여부

@register  →  전역 레지스트리
ConnectorManager
├── 공유 httpx.AsyncClient (User-Agent, timeout, redirect)
├── search(): asyncio.gather 로 대상 커넥터 병렬 실행 → SearchResponse
└── _search_one(): 소스별 try/except + 소요시간 측정
```

**현재 커넥터**: `gutendex`, `met`, `wikidata`, `openlibrary`, `poetrydb` (모두 무인증).

### 새 커넥터 추가 절차
1. `app/connectors/<source>.py` 에 `BaseConnector` 상속 클래스 작성, `meta` 정의.
2. `search()` 에서 외부 API 호출 → `StoryEntity`로 매핑.
3. 클래스에 `@register` 데코레이터.
4. `app/connectors/__init__.py` 의 import 목록에 모듈 추가(등록 트리거).
5. `scripts/smoke.py` 로 라이브 검증.

## 4. API 레이어 (`backend/app/api/`)

| 엔드포인트 | 설명 |
|-----------|------|
| `GET /api/health` | 상태 + 등록된 커넥터 수 |
| `GET /api/sources` | 소스 카탈로그(메타데이터 전체) |
| `GET /api/sources/{id}/health` | 개별 소스 헬스체크 |
| `GET /api/search?q=&sources=&limit=` | 연합 검색 |
| `GET /api/sources/{id}/items/{record_id}` | 단건 상세/전문 fetch |

FastAPI `lifespan`에서 `ConnectorManager`를 생성해 `app.state`에 보관(앱 수명과 동일한
단일 httpx 클라이언트 재사용). CORS는 Vite dev 오리진 허용.

## 5. 프론트엔드 (`frontend/`)

React + TS + Vite. `/api/*`는 Vite dev 프록시로 백엔드(:8000)에 연결.
검색 → 소스별 블록 → `StoryEntity` 카드(타입 배지·시대·이미지·태그·라이선스·원문 링크).
백엔드 모델은 `src/types.ts`에 1:1로 미러링.

## 6. 로드맵 단계의 설계 (아직 미구현)

```
[live connectors]          ← 현재 v0.1
      │  ingest
      ▼
[정규화 저장소]   Postgres + 전문검색(pg_trgm/tsvector) 또는 OpenSearch
      │  embed
      ▼
[벡터 색인]       pgvector / Qdrant  — 의미 검색 & RAG
      │  retrieve
      ▼
[스토리 컴포저]   Claude (claude-opus-4-8) — 모은 자료를 컨텍스트로 초안 생성
      │
      ▼
[창작 워크스페이스]  사용자가 자료를 수집·태깅·재구성해 새 이야기로
```

- **수집/캐시**: 검색은 실시간이지만, 무거운 소스(덤프형: Wikidata/Aozora/CBETA 등)는
  배치로 내려받아 로컬 정규화 저장이 효율적. `data/cache/`, `data/dumps/`(gitignore).
- **검색 진화**: 키워드 연합 → 통합 색인 → 임베딩 의미검색 → 엔티티 해소(같은 인물/장소
  소스 간 병합, Wikidata QID를 허브로).
- **창작기**: 선택한 `StoryEntity` 묶음을 구조화 컨텍스트로 Claude에 전달, 출처 각주를
  보존한 채 모티프·세계관·플롯 초안을 제안. (`/api/compose` 예정)

## 7. 횡단 관심사

- **레이트리밋/예의** — 공용 API엔 식별 가능한 User-Agent 전송, 덤프 제공 소스는 웹
  프런트 스크래핑 대신 덤프 우선.
- **라이선스 게이팅** — `License.commercial_ok`로 상업 재사용 필터링. NC/ND·스크래핑
  한정·토착 전승(ICIP) 소스는 카탈로그에서 플래그.
- **테스트** — 라이브 스모크(`scripts/smoke.py`) + (예정) 녹화 응답 기반 단위테스트.

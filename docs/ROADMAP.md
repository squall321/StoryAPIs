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

## Phase 1 — 소스 확장 (🚧 다음)

목표: "외국 DB 대폭 보강" 지시 반영 — 커넥터를 무인증 깨끗한 라이선스부터 폭넓게.

- ⬜ **무인증 CC0/PD 우선**: Art Institute of Chicago, Cleveland Museum, Smithsonian(키),
  Sefaria(유대 경전), SuttaCentral(불교 경전), alquran.cloud(꾸란), bible-api(성경)
- ⬜ **지식그래프 심화**: Wikidata `wbgetentities`로 claims·relations 채우기(엔티티 그래프),
  Wikipedia 요약(REST summary), DBpedia
- ⬜ **한국 핵심**: 조선왕조실록(국사편찬위/NIKH), 한국고전종합DB(ITKC Open API),
  공공데이터포털(국가유산청 등) — KOGL 라이선스 확인
- ⬜ **고전·신화 원전**: Perseus(그리스·로마 TEI), ctext.org(한문 고전·山海經), GRETIL(산스크리트)
- ⬜ **지리/작명/세계관**: GeoNames, World Historical Gazetteer, Wiktionary 어원, GBIF
- ⬜ 키 필요한 소스용 `available()`/설정 키 배선(Europeana, Trove, Smithsonian…)

## Phase 2 — 영속화 & 색인 (⬜)

실시간 호출만으로는 느리고 일부 소스는 덤프형이다. 정규화 저장 + 검색 가속.

- ⬜ Postgres 스키마(`StoryEntity` 영속화) + Alembic 마이그레이션
- ⬜ 배치 인제스트 파이프라인(덤프 소스: Wikidata/Aozora/CBETA/Perseus → 로컬 정규화)
- ⬜ 전문검색: Postgres `tsvector`/`pg_trgm` (다국어 고려) 또는 OpenSearch
- ⬜ 응답 캐시 레이어(소스별 TTL) — 무거운 외부 호출 절감

## Phase 3 — 의미 검색 & 엔티티 해소 (⬜)

- ⬜ 임베딩 색인(pgvector/Qdrant) — "비슷한 모티프/인물/사건" 의미 검색
- ⬜ 엔티티 해소: 소스 간 동일 인물/장소 병합(Wikidata QID를 허브로)
- ⬜ 관계 그래프 탐색 UI(인물↔사건↔장소 네트워크)

## Phase 4 — 창작 워크스페이스 & 스토리 컴포저 (⬜)

프로젝트의 최종 목적 — 모은 자료로 **새 이야기 짓기**.

- ⬜ 컬렉션/보드: 검색 결과를 워크스페이스에 수집·태깅·메모
- ⬜ `/api/compose`: 선택한 `StoryEntity` 묶음을 구조화 컨텍스트로 Claude(`claude-opus-4-8`)에
  전달 → 세계관/캐릭터/플롯 초안 생성, **출처 각주 보존**
- ⬜ 모티프 추출: 폭/원전에서 ATU 유형·Thompson 모티프 자동 태깅
- ⬜ 집필 에디터(초안 + 인용 사이드패널)

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

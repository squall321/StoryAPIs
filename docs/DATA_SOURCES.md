# 데이터 소스 카탈로그 (통합 인덱스)

세계의 접근 가능한 지식 DB/API를 6개 영역으로 조사한 결과의 인덱스다. 영역별 상세
(엔드포인트·접근방식·포맷·인증·레이트리밋·라이선스·창작가치)는 `research/` 의 각 파일에 있다.

> ⚠️ **검증 상태**: 이 환경의 서브에이전트는 네트워크가 차단되어, 상세 카탈로그는 학습
> 지식(2026-01 기준)으로 작성되었고 "라이브 미검증"으로 표시되어 있다. 실제 구현된
> 커넥터는 메인에서 **라이브로 검증**되었다(아래 표). 신규 소스 도입 시 엔드포인트·
> 라이선스를 반드시 재확인할 것.

## 영역별 상세 문서

| # | 영역 | 파일 | 대표 소스 |
|---|------|------|-----------|
| 01 | 한국·동아시아 | [research/01-korea-east-asia.md](research/01-korea-east-asia.md) | 조선왕조실록, 한국고전종합DB, ctext.org, 青空文庫, Japan Search |
| 02 | 서구·글로벌 지식그래프·GLAM | [research/02-western-knowledge-graphs.md](research/02-western-knowledge-graphs.md) | Wikidata, Met, Rijksmuseum, Europeana, 각국 국립도서관 (47+ 상세) |
| 03 | 세계 신화·민담·종교 | [research/03-mythology-folklore-religion.md](research/03-mythology-folklore-religion.md) | Sefaria, SuttaCentral, Perseus, GRETIL, ctext, sacred-texts (25개 전통) |
| 04 | 퍼블릭 도메인 문학(전문) | [research/04-public-domain-literature.md](research/04-public-domain-literature.md) | Project Gutenberg, Standard Ebooks, Wikisource, PoetryDB, Gallica |
| 05 | 전문·세계관 구축 지식 | [research/05-specialized-worldbuilding.md](research/05-specialized-worldbuilding.md) | GeoNames, Natural Earth, NASA, GBIF, 어원/작명, CLDF 언어학 |
| 06 | 세계 지역별 심화 | [research/06-world-regions-expanded.md](research/06-world-regions-expanded.md) | OpenITI, CBDB, Ganjoor, Qatar Digital Library, Trove (72개 소스) |

## 구현 커넥터 현황

| 커넥터 | 소스 | 접근 | 인증 | 라이선스 | 상태 |
|--------|------|------|------|----------|------|
| `gutendex` | Project Gutenberg | REST JSON + 전문 다운로드 | 불필요 | Public Domain | ✅ 라이브 |
| `met` | The Met Museum | REST JSON | 불필요 | CC0 | ✅ 라이브 |
| `wikidata` | Wikidata | REST(wbsearchentities) | 불필요 | CC0 | ✅ 라이브 |
| `openlibrary` | Open Library | REST JSON | 불필요 | CC0(data) | ✅ 라이브 |
| `poetrydb` | PoetryDB | REST JSON | 불필요 | Public Domain | ✅ 라이브 |

## 도입 우선순위 (라이선스·접근 난이도 기준)

### Tier 1 — 무인증 · CC0/PD · 깨끗한 REST (즉시 도입)
Art Institute of Chicago, Cleveland Museum, Smithsonian(키), **Sefaria**, **SuttaCentral**,
**alquran.cloud**, **bible-api.com**, Wikipedia REST summary, MusicBrainz, Natural Earth(덤프)

### Tier 2 — 무인증/소액 키 · 일부 share-alike · 약간의 가공 필요
Wikidata(claims/SPARQL), DBpedia, **Perseus**(TEI), **ctext.org**(무료 키), **GRETIL**,
GeoNames(무료 username), World Historical Gazetteer, Wiktionary/Kaikki 어원, GBIF, NASA(키)

### Tier 3 — 한국 핵심 · 공공 API/덤프 (KOGL 확인 필요)
**조선왕조실록**(국사편찬위/NIKH), **한국고전종합DB**(ITKC Open API), 공공데이터포털
(국가유산청 등), Japan Search(SPARQL), Aozora Bunko(덤프)

### ⚠️ 주의 — 라이선스/윤리 플래그
- **NC(비상업)**: CBETA, ETCSL, World History Encyclopedia, BabelNet, Folger, British Museum 메타
- **ND/독점/스크래핑 한정**: Stanford Encyclopedia, 현대 Britannica, sacred-texts(마크업), mftd.org
- **토착 전승(ICIP)**: Aboriginal Australian, Native American, Yoruba/Ifá, Polynesian 신성 구전
  — 퍼블릭 도메인 여부와 별개로 **공동체 이용 규약**을 따른다.
- **현대 2차 저작물 ©**: D'Aulaire, Edith Hamilton, Campbell, Propp, 현대 번역본(Popol Vuh 등)
  은 데이터로 재사용 불가 — 원전(PD)을 사용할 것.

각 소스의 정확한 권리·엔드포인트는 해당 `research/0x-*.md` 의 항목별 라이선스 줄을 참고.

# Korean & East Asian Historical / Classical / Literary Data Sources

> **Focus domain:** Korean and East Asian historical, classical, and literary data sources for a "story source material" platform.
>
> **Compiled:** 2026-06-20

---

## ⚠️ IMPORTANT VERIFICATION NOTICE

**Live network verification could NOT be performed for this document.** In the environment where this catalog was compiled, all outbound-network tools — `WebSearch`, `WebFetch`, `Bash`/`curl`, `PowerShell`/`Invoke-WebRequest`, and even delegated sub-agents — were **denied by sandbox permissions**. A connectivity probe to `https://ctext.org/tools/api` via a sub-agent returned `NETWORK ACCESS DENIED`.

Consequently, every entry below is reconstructed from **prior knowledge of these well-documented sources** and is **NOT confirmed against the live 2026 state** of each site. Treat all of the following as **provisional / to-be-verified**:

- Exact endpoint paths and base URLs.
- Whether an API key is required *today* and how to obtain it.
- Current rate limits.
- Current license terms (these change; Korean public-data licenses in particular are revised periodically).
- Whether a service still exists / has been migrated (e.g., 국가유산청 rebrand of 문화재청; AKS portal restructurings).

**Re-run this research with network access enabled** before relying on any endpoint for production. Each entry carries a `VERIFY` line listing the specific facts to re-confirm. Items known to be **scrape-only** or **restrictively licensed** are flagged with 🚩.

---

## Quick comparison table

| # | Source | Country | Access method | Format | API key? | License (provisional) | Flag |
|---|--------|---------|---------------|--------|----------|------------------------|------|
| 1 | 조선왕조실록 Annals of Joseon (sillok.history.go.kr) | KR | Web DB; bulk via NIKH | XML/HTML/text | Likely no | KOGL-attribution (verify) | — |
| 2 | 한국사데이터베이스 (db.history.go.kr) | KR | Web DB; some Open API | XML/HTML | Some | KOGL (verify) | partial 🚩 scrape |
| 3 | 승정원일기 Seungjeongwon Ilgi (sjw.history.go.kr) | KR | Web DB | HTML/text | No | KOGL (verify) | 🚩 scrape-heavy |
| 4 | 한국고전종합DB (db.itkc.or.kr / ITKC) | KR | Web DB + Open API + bulk | XML/JSON/TEI | Some | Open w/ attribution (verify) | — |
| 5 | 한국민족문화대백과사전 EncyKorea (encykorea.aks.ac.kr) | KR | Web; Linked Data; partial API | HTML/RDF/JSON-LD | Some | CC BY-NC-ND-ish (verify) | 🚩 NC/ND likely |
| 6 | 공공데이터포털 data.go.kr (history/culture APIs) | KR | REST Open API | JSON/XML | **Yes** | KOGL Type 1 (verify) | — |
| 7 | 국립중앙도서관 NL Korea APIs (nl.go.kr) | KR | REST/SRU/LOD | XML/JSON/RDF | **Yes** | KOGL / mixed | — |
| 8 | 국가유산청 / 국가유산포털 (heritage.go.kr) | KR | REST Open API | XML/JSON | Some | KOGL (verify) | — |
| 9 | 한국향토문화전자대전 (grandculture.net) | KR | Web; some LOD | HTML/RDF | Verify | KOGL/CC (verify) | 🚩 scrape-likely |
| 10 | Chinese Text Project ctext.org | CN/intl | REST API + web | JSON | **Yes (free)** | CC BY-SA (varies by text) | — |
| 11 | Academia Sinica resources (Scripta Sinica etc.) | TW | Web DB; some API | HTML/XML | Verify | Mixed/restrictive | 🚩 scrape-likely |
| 12 | 青空文庫 Aozora Bunko (aozora.gr.jp) | JP | Bulk download (GitHub) | TXT/XHTML | No | Public domain / CC | — |
| 13 | NDL National Diet Library APIs (ndl.go.jp) | JP | SRU/OpenSearch/OAI-PMH/REST | XML/JSON/RDF | Mostly no | Mixed (PD + rights) | — |
| 14 | Japan Search (jpsearch.go.jp) | JP | REST + SPARQL | JSON/RDF | Some | Per-provider | partial 🚩 |
| 15 | NDL Digital Collections / 国立国会図書館デジタル | JP | IIIF + API | IIIF JSON | No | Per-item rights | partial 🚩 |

---

# KOREA

## 1. 조선왕조실록 — Annals of the Joseon Dynasty (Veritable Records)

- **Official name:** 조선왕조실록 / The Annals of the Joseon Dynasty (Joseon Wangjo Sillok). UNESCO Memory of the World.
- **URL:** https://sillok.history.go.kr (run by 국사편찬위원회 / National Institute of Korean History, NIKH).
- **Coverage / scope:** Day-by-day court chronicle of the Joseon dynasty, **1392–1863** (the main 25 reigns; the *Gojong*/*Sunjong* sillok are included but treated as later compilations). Original **Classical Chinese (한문)** plus full modern **Korean translation**; many entries cross-referenced.
- **Access method:** Primarily a **web database** with stable per-article URLs (article ID scheme like `kefoma_…`). Bulk/derived datasets have historically been distributable through NIKH; the translated corpus is also widely mirrored. No prominent self-serve REST API on the sillok site itself.
- **Data format:** HTML for reading; underlying records are structured (XML-style article records). Plain-text/translation exports exist in third-party corpora.
- **Auth / API key:** None for web reading.
- **Rate limits:** Not formally published — heavy automated crawling is discouraged; treat as scrape-with-courtesy.
- **License (provisional):** Korea Open Government License (**KOGL**) attribution-style for the public content, but **VERIFY** — translation copyright and reuse terms have nuances.
- **Value for fiction:** ⭐ Top-tier. Court intrigue, royal succession crises, omens/astronomical portents, natural disasters, criminal cases, diplomatic incidents, factional politics — an almost inexhaustible well of period-accurate plot seeds, dialogue registers, and named historical figures.
- **VERIFY:** Existence/format of any official API or bulk download; exact KOGL type; whether translated text reuse needs separate permission.

## 2. 국사편찬위원회 한국사데이터베이스 (Korean History DB)

- **Official name:** 한국사데이터베이스 (Korean History Database), NIKH.
- **URL:** https://db.history.go.kr
- **Coverage:** Umbrella portal aggregating dozens of corpora: 삼국사기, 삼국유사, 고려사, 비변사등록, 일제강점기 자료, 신문 자료, 古문서, etc. Spans **ancient Korea through the modern colonial period**.
- **Access method:** Web DB; **some collections expose Open API / structured endpoints**, but coverage is uneven across sub-DBs. Many sub-collections are **read-only web** (🚩 scrape-only).
- **Data format:** HTML; XML for some structured records.
- **Auth / API key:** Some Open APIs require registration; many do not.
- **Rate limits:** Not formally published.
- **License (provisional):** KOGL — **VERIFY** per sub-collection.
- **Value for fiction:** Single richest gateway to Korean primary sources across all eras — myth (삼국유사), dynastic history (고려사, 삼국사기), institutional records, and modern-era newspapers for colonial-period stories.
- **VERIFY:** Which sub-DBs have a real API vs. scrape-only; current Open API catalog.

## 3. 승정원일기 — Seungjeongwon Ilgi (Records of the Royal Secretariat)

- **Official name:** 승정원일기 / Diaries of the Royal Secretariat. UNESCO Memory of the World.
- **URL:** https://sjw.history.go.kr (NIKH).
- **Coverage:** Extraordinarily detailed daily administrative log of the royal secretariat, **1623–1910** (earlier volumes lost to fire). One of the largest single historical records in the world.
- **Access method:** Web DB; translation project ongoing. **Largely scrape-only** for bulk text. 🚩
- **Data format:** HTML/text; original 한문 with partial modern translation.
- **Auth:** None for reading.
- **License:** KOGL-style — **VERIFY**.
- **Value for fiction:** Granular daily-life-of-court detail — weather, who entered the palace, what was said in audiences — ideal for texture and realism in palace/period drama. Density makes it better as a *flavor source* than a plot index.
- **VERIFY:** Translation coverage %, any export/API.

## 4. 한국고전종합DB — ITKC (Institute for the Translation of Korean Classics)

- **Official name:** 한국고전종합DB (DB of Korean Classics), 한국고전번역원 (ITKC / Institute for the Translation of Korean Classics).
- **URL:** https://db.itkc.or.kr ; org site https://www.itkc.or.kr
- **Coverage:** Massive corpus of classical Korean literature & scholarship: 문집총간 (collected literary works of scholars), 조선왕조실록 translations, 승정원일기 translations, 일성록, 한국문집, classical poetry/prose. Mostly **Goryeo–Joseon** literati writing.
- **Access method:** Web DB **plus a published Open API** and downloadable datasets; ITKC has actively promoted open/linked data and TEI-encoded texts.
- **Data format:** HTML; **XML/TEI** for structured classical texts; JSON via API where available.
- **Auth / API key:** Registration likely for API/bulk — **VERIFY**.
- **Rate limits:** Not formally published.
- **License (provisional):** Open with attribution for many translations — **VERIFY** (some texts have translator copyright).
- **Value for fiction:** ⭐ Best source for the *literary voice* of premodern Korea — poems, essays, letters, anecdotes (필기/야담 style), scholar biographies. Great for authentic dialogue, allusions, and characterization of yangban/scholar figures.
- **VERIFY:** Current API base URL, key process, TEI download availability.

## 5. 한국민족문화대백과사전 — Encyclopedia of Korean Culture (EncyKorea)

- **Official name:** 한국민족문화대백과사전 (Encyclopedia of Korean Culture), 한국학중앙연구원 (Academy of Korean Studies, AKS).
- **URL:** https://encykorea.aks.ac.kr
- **Coverage:** Comprehensive encyclopedia of Korean history, folklore, religion, geography, biography, material culture, customs — all eras.
- **Access method:** Web; AKS has produced **Linked Open Data / RDF** versions and some API surfaces, but the main consumer site is web. Partial 🚩.
- **Data format:** HTML; RDF / JSON-LD for the LOD edition.
- **Auth:** Verify.
- **License (provisional):** Likely **CC BY-NC-ND** or similar restrictive variant (NC/ND common for AKS) — 🚩 **VERIFY**; commercial story-product reuse may be restricted.
- **Value for fiction:** ⭐ Best *lookup/worldbuilding* reference — folk beliefs, rituals, mythical creatures (도깨비, 구미호 lore), regional customs, historical figures. Excellent for grounding invented stories in real cultural detail.
- **VERIFY:** Exact license (NC? ND?), whether LOD endpoint/API is public and stable.

## 6. 공공데이터포털 — data.go.kr (history & culture APIs)

- **Official name:** 공공데이터포털 / Public Data Portal (operated by 행정안전부 / NIA).
- **URL:** https://www.data.go.kr
- **Coverage:** National open-data clearinghouse. Relevant datasets/APIs include cultural heritage, museum collections (e.g., 국립중앙박물관 e뮤지엄), folk culture, place-name histories, tourism-culture data.
- **Access method:** **REST Open API** (per-dataset endpoints) + file downloads (CSV/JSON/XML).
- **Data format:** JSON / XML / CSV.
- **Auth / API key:** **Yes — mandatory.** Free registration; per-API service key (활용신청). Some APIs auto-approve, some need approval.
- **Rate limits:** Per-API daily call quotas (commonly ~1,000–10,000/day on the free tier; raise on request).
- **License (provisional):** Mostly **KOGL Type 1** (free use incl. commercial with attribution) — **VERIFY per dataset**.
- **Value for fiction:** Structured, license-clear data — museum artifact metadata, heritage site info, folk-culture datasets — good for *factual scaffolding* and props/setting detail with commercially-usable licensing.
- **VERIFY:** Which specific history/culture APIs are live in 2026; per-API license and quota.

## 7. 국립중앙도서관 — National Library of Korea APIs

- **Official name:** 국립중앙도서관 (National Library of Korea, NLK).
- **URL:** https://www.nl.go.kr ; open data hub and 국가서지 LOD.
- **Coverage:** National bibliography, digitized old books (古書), Korean Old and Rare Collection, periodicals, 한국고전적종합목록.
- **Access method:** REST/OpenAPI, **SRU**, and **Linked Open Data (국가서지 LOD)**; bulk MARC/RDF downloads for some sets.
- **Data format:** XML / JSON / RDF / MARC.
- **Auth / API key:** **Yes** for the Open APIs (free registration).
- **License:** Mixed — bibliographic metadata generally open (KOGL); digitized full text subject to per-item rights.
- **Value for fiction:** Discovery layer for rare/old Korean books and their metadata; pathway to digitized premodern texts and illustrations.
- **VERIFY:** Current API catalog, key process, which full texts are openly downloadable.

## 8. 국가유산청 / 국가유산포털 (formerly 문화재청 / Cultural Heritage Administration)

- **Official name:** 국가유산청 (Korea Heritage Service — **renamed from 문화재청 in 2024**) / 국가유산포털.
- **URL:** https://www.khs.go.kr ; portal https://www.heritage.go.kr (legacy 문화재청 URLs may redirect).
- **Coverage:** National designated heritage — buildings, artifacts, intangible heritage, historic sites, traditional crafts and performing arts; rich descriptive + image data.
- **Access method:** **REST Open API** (heritage info API), also surfaced via data.go.kr.
- **Data format:** XML / JSON.
- **Auth:** Some APIs key-free, some via data.go.kr key — **VERIFY**.
- **License:** KOGL-style — **VERIFY**; images may have separate terms. 🚩 check image reuse.
- **Value for fiction:** Authentic settings and props — palaces, temples, artifacts, intangible traditions (rituals, crafts, folk performance) for period-accurate scene-building.
- **VERIFY:** Post-rebrand URLs/endpoints (the 2024 rename means older docs/links may be stale), image license.

## 9. 한국향토문화전자대전 — Encyclopedia of Korean Local Culture

- **Official name:** 한국향토문화전자대전 (Encyclopedia of Korean Local Culture / "Grand Culture"), AKS.
- **URL:** https://www.grandculture.net
- **Coverage:** Region-by-region (시·군 단위) local history, legends, folklore, place names, local figures, customs across all of Korea.
- **Access method:** Web; some AKS LOD overlap. Likely **scrape-only** for bulk. 🚩
- **Data format:** HTML; possibly RDF via AKS LOD.
- **License:** KOGL/CC mix — **VERIFY** (AKS content often NC).
- **Value for fiction:** ⭐ Goldmine of *local legends and regional motifs* — village foundation myths, ghost stories, local heroes — perfect for grounding stories in a specific Korean place with authentic folklore.
- **VERIFY:** Any API/LOD access; license for commercial reuse.

---

# CHINA / TAIWAN

## 10. Chinese Text Project — 中國哲學書電子化計劃 (ctext.org)

- **Official name:** Chinese Text Project (CTP) / 中國哲學書電子化計劃.
- **URL:** https://ctext.org ; API docs historically at https://ctext.org/tools/api
- **Coverage:** The largest open digital library of **pre-modern Chinese texts** — pre-Qin & Han classics (諸子百家, 十三經), histories (二十四史 portions), and a vast OCR'd wiki of post-Han works. Classical Chinese throughout; many texts with English translations (esp. Legge).
- **Access method:** **Documented REST/JSON API** (`gettext`, `gettextinfo`, `searchtexts`, dictionary lookups, etc.) plus full web reading and a public crowd-sourced library.
- **Data format:** **JSON** (API); plain text; some downloadable.
- **Auth / API key:** **Free API key** (register for an `urn`/API key); anonymous low-volume access historically allowed.
- **Rate limits:** Yes — anonymous/low tier is limited; registered keys get higher quotas. **VERIFY current limits.**
- **License (provisional):** Mixed — many core texts **CC BY-SA**; the API and metadata have their own terms. Verify per text before commercial reuse.
- **Value for fiction:** ⭐ Top-tier for Chinese/East-Asian classical motifs — Confucian/Daoist philosophy, *Shanhaijing* (山海經) mythical creatures and geography, dynastic histories, strategy texts (孫子兵法), poetry. Endless allusions, creatures, and parable structures.
- **VERIFY:** Current endpoint list, key registration flow, rate-limit tiers, per-text license.

## 11. Academia Sinica digital resources (Scripta Sinica / 漢籍電子文獻)

- **Official name:** Academia Sinica (中央研究院) — 漢籍電子文獻資料庫 (Scripta Sinica) and related history/language DBs.
- **URL:** https://hanchi.ihp.sinica.edu.tw (Scripta Sinica) and various Academia Sinica project sites.
- **Coverage:** Authoritative, scholar-curated full text of the **dynastic histories (二十四史/二十五史)**, classics, and many premodern Chinese works; also linguistics corpora.
- **Access method:** Web DB; **largely scrape-only / login-gated** for full functionality. Some sister projects expose data. 🚩
- **Data format:** HTML; limited structured export.
- **Auth:** Some content requires institutional access/registration.
- **License (provisional):** **Restrictive** — academic-use terms; commercial reuse generally **not** permitted without permission. 🚩
- **Value for fiction:** Most *authoritative* text of the standard histories (better punctuation/editing than crowd-sourced sources) — valuable for accuracy, but licensing makes it a *reference*, not a redistributable source.
- **VERIFY:** Current access model, any API, exact terms.

---

# JAPAN

## 12. 青空文庫 — Aozora Bunko

- **Official name:** 青空文庫 (Aozora Bunko), volunteer digital library.
- **URL:** https://www.aozora.gr.jp ; bulk data mirrored on GitHub (`aozorabunko/aozorabunko`).
- **Coverage:** **Public-domain Japanese literature** — Meiji/Taishō/early-Shōwa fiction, poetry, essays (Natsume Sōseki, Akutagawa, Dazai, Miyazawa Kenji, etc.), plus older classics. Works whose copyright has expired (+ some CC-licensed).
- **Access method:** **Full bulk download** (entire repo via GitHub), per-work download, and a community CSV index of all titles.
- **Data format:** Ruby-annotated **plain text (Shift-JIS / UTF-8)** and **XHTML**; index as CSV.
- **Auth / API key:** **None.**
- **Rate limits:** None for the GitHub bulk repo (use the repo, not aggressive site crawling).
- **License:** **Public domain** for expired-copyright works (plus a few CC works clearly marked). The single cleanest license situation in this catalog.
- **Value for fiction:** ⭐ Directly reusable full literary texts — ideal for style modeling, retellings, intertextual reference, and training/example material with clean rights.
- **VERIFY:** Confirm GitHub mirror is current; per-work license flag in the index.

## 13. 国立国会図書館 — National Diet Library (NDL) APIs

- **Official name:** 国立国会図書館 / National Diet Library (NDL), Japan.
- **URL:** https://www.ndl.go.jp ; NDL Search APIs; NDL Digital Collections.
- **Coverage:** National bibliography, digitized books incl. **pre-modern and Meiji-era** materials, periodicals, NDL Digital Collections (millions of items, many full-view public-domain).
- **Access method:** **SRU, OpenSearch, OAI-PMH, and REST** for NDL Search; **IIIF** for Digital Collections images.
- **Data format:** XML (DC, DCNDL, MODS), JSON, RDF; IIIF JSON for images.
- **Auth / API key:** Mostly **no key** for search/metadata APIs.
- **Rate limits:** Reasonable-use; published guidance for SRU/OAI.
- **License:** Metadata broadly open; **full-text/image rights vary per item** (public-domain vs. in-copyright vs. "available within Japan only"). 🚩 per-item.
- **Value for fiction:** Access to scanned premodern Japanese books, illustrations (e.g., woodblock-print pages), and Meiji-era texts — strong for visual/setting reference and rare-source discovery.
- **VERIFY:** Current API endpoints (NDL rebranded "NDL Search" in recent years), per-item rights flags.

## 14. Japan Search (ジャパンサーチ)

- **Official name:** Japan Search / ジャパンサーチ (national aggregation platform, run by NDL).
- **URL:** https://jpsearch.go.jp
- **Coverage:** Cross-domain aggregator of Japan's cultural heritage metadata — museums, libraries, archives, art, history — from 100+ provider databases.
- **Access method:** **REST API** and a **SPARQL endpoint** over its RDF knowledge graph.
- **Data format:** JSON / RDF (Schema.org-aligned).
- **Auth / API key:** Some API access requires registration — **VERIFY**.
- **Rate limits:** Verify.
- **License:** **Per-provider** — Japan Search exposes the rights statement of each source; mixed (some CC0, some restricted). Partial 🚩.
- **Value for fiction:** ⭐ Best *single SPARQL/REST entry point* for Japanese cultural motifs across institutions — link artifacts, art, folklore, and historical records in one query.
- **VERIFY:** API/SPARQL endpoint URLs, key requirement, rights-filtering for commercial reuse.

## 15. NDL Digital Collections / IIIF (国立国会図書館デジタルコレクション)

- **Official name:** 国立国会図書館デジタルコレクション (NDL Digital Collections).
- **URL:** https://dl.ndl.go.jp
- **Coverage:** Digitized books, manuscripts, maps, ukiyo-e and illustrated works; large public-domain segment.
- **Access method:** Web + **IIIF Image/Presentation API** (deep-zoom, programmatic image access); OAI-PMH harvesting.
- **Data format:** IIIF JSON manifests; image tiles (JPEG).
- **Auth:** None for public-domain items.
- **License:** **Per-item** — clearly flagged public-domain items are freely reusable; others restricted. 🚩 per-item.
- **Value for fiction:** Visual source material — historical illustrations, maps, and print art for mood/reference and (for PD items) direct reuse.
- **VERIFY:** IIIF manifest URL pattern, current rights flags.

---

## Cross-cutting notes & recommendations

- **Cleanest licensing for direct text reuse:** ① **Aozora Bunko** (public domain, bulk via GitHub), ② **ctext.org** (CC BY-SA on many texts, free API), ③ **data.go.kr** datasets under **KOGL Type 1** (commercial-OK with attribution). Prioritize these for anything that ships inside a product.
- **Richest *story-motif* sources:** 조선왕조실록 (plots), 한국고전종합DB (literary voice), 한국민족문화대백과사전 + 향토문화전자대전 (folklore/creatures), ctext.org 山海經 (mythical beasts), Aozora Bunko (reusable literary text).
- **🚩 Watch out for:**
  - **AKS content (EncyKorea, 향토문화전자대전):** frequently **NC/ND** — fine as a *reference*, risky for redistribution. Verify before embedding.
  - **Academia Sinica / Scripta Sinica:** academic-use, login-gated, **not** for commercial redistribution.
  - **승정원일기 & much of db.history.go.kr:** effectively **scrape-only**; no clean bulk/API for large parts — build a courteous crawler with caching, respect robots.txt.
  - **국가유산청 (ex-문화재청):** **2024 rebrand** means many older URLs/endpoint docs are stale — re-verify all endpoints.
  - **Per-item rights** dominate Japanese digital-collection material (NDL, Japan Search) — always read the per-record rights statement before reuse.
- **Korea Open Government License (KOGL) cheat-sheet:** *Type 1* = free use incl. commercial, attribution required; *Type 2* = adds no-commercial; *Type 3* = adds no-derivatives; *Type 4* = no-commercial + no-derivatives. Always check the **type number** on each Korean dataset.

---

## ❗ Action item before production use

This catalog was assembled **without live network verification** (sandbox denied all web/network tools). Before integrating any source:

1. Re-run with `WebFetch`/`WebSearch` enabled and confirm each `VERIFY` line.
2. Pull and read the **current** terms-of-use / license page for every source.
3. For Korean public data, record the exact **KOGL type number**.
4. For Japanese aggregators, confirm **per-item rights** handling.
5. Confirm post-rename URLs for **국가유산청** and any restructured AKS portals.

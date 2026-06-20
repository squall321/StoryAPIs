# Western & Global Knowledge Graphs, Encyclopedias & GLAM APIs

> **Focus domain:** Western + GLOBAL structured knowledge graphs, encyclopedias, and GLAM (Galleries / Libraries / Archives / Museums) APIs worldwide, for a "story source material" platform.
>
> **Foreign / international sources are deliberately EXPANDED** — breadth and country/institution coverage are prioritized.
>
> **Compiled:** 2026-06-20

---

## ⚠️ UNVERIFIED — compiled from training knowledge; endpoints/licenses to be live-verified

**Live network verification could NOT be performed for this document.** In the environment where this catalog was compiled, all outbound-network tools (`WebSearch`, `WebFetch`, `curl`, `Invoke-WebRequest`, and delegated sub-agents) were **denied by sandbox permissions**.

Every entry below is reconstructed from **prior knowledge (training cutoff Jan 2026)** and is **NOT confirmed against the live state** of each service. Treat all endpoint paths, API-key requirements, rate limits, and especially **license terms** as **provisional / to-be-verified**. The main thread has network access and will live-verify endpoints later — the goal here is **breadth + accurate structural detail**.

Specific things that drift and MUST be re-confirmed:
- Exact base URLs and endpoint paths (services migrate, e.g. Wikimedia REST `/api/rest_v1/` → `/w/rest.php/` and the newer `api.wikimedia.org`).
- Whether an API key / registration is required *today*.
- Current rate limits (Wikimedia is tightening anonymous limits over 2024–2025).
- License terms (these change; per-item rights in aggregators vary wildly).

Items that are **NC / ND / restrictive / scrape-only** are flagged with 🚩.

**License shorthand:** CC0 = public-domain dedication (most permissive) · CC-BY = attribution · CC-BY-SA = attribution + share-alike · ODC-BY = Open Data Commons attribution · ODbL = Open Database License (share-alike) · NC = non-commercial 🚩 · ND = no-derivatives 🚩 · PD = public domain.

---

## Quick-reference table — sorted by ease of use / openness (most open first)

| # | Source | Country/Org | Access method | Format | API key? | License (provisional) | Flag |
|---|--------|-------------|---------------|--------|----------|------------------------|------|
| 1 | The Met Collection API | US | REST | JSON | **No** | CC0 (open-access objects) | — |
| 2 | Art Institute of Chicago API | US | REST + IIIF | JSON | No | CC0 (public-domain art) | — |
| 3 | Smithsonian Open Access | US | REST | JSON | Yes (free) | CC0 | — |
| 4 | Cleveland Museum of Art API | US | REST + IIIF | JSON | No | CC0 (open-access) | — |
| 5 | Rijksmuseum API | NL | REST + OAI-PMH + IIIF | JSON/XML | Yes (free) | CC0 / PD (images vary) | — |
| 6 | Wikidata | Wikimedia | SPARQL + REST + dumps | JSON/RDF/TTL | No (key helps) | CC0 | — |
| 7 | Wikimedia Commons | Wikimedia | Action/REST API + dumps | JSON | No | per-file (mostly CC/PD) | partial 🚩 |
| 8 | Wikipedia / MediaWiki | Wikimedia | REST + Action + dumps | JSON/HTML/XML | No | CC-BY-SA (text) | — |
| 9 | DBpedia | DBpedia/Leipzig | SPARQL + dumps + LD | RDF/JSON-LD | No | CC-BY-SA | — |
| 10 | GeoNames | intl (CH-hosted) | REST | JSON/XML/RDF | Yes (free) | CC-BY | — |
| 11 | Harvard Art Museums API | US | REST + IIIF | JSON | Yes (free) | per-item rights (PD many) | partial 🚩 |
| 12 | Library of Congress (loc.gov JSON, LCCN, id.loc.gov) | US | REST/JSON + LD + SRU + IIIF | JSON/MARCXML/RDF | No | mostly PD / no known restriction | — |
| 13 | Europeana API | EU | REST + SPARQL + OAI | JSON-LD/RDF | Yes (free) | metadata CC0; media per-item | partial 🚩 |
| 14 | DPLA API | US | REST | JSON | Yes (free) | metadata CC0; media per-item | partial 🚩 |
| 15 | Trove API | AU | REST | JSON/XML | Yes (free) | metadata mixed; per-item | partial 🚩 |
| 16 | DigitalNZ API | NZ | REST | JSON | Yes (free) | per-item rights | partial 🚩 |
| 17 | Gallica / BnF | FR | IIIF + SRU + OAI-PMH + SPARQL (data.bnf.fr) | IIIF/MARCXML/RDF | No | mostly PD / Gallica licence | partial 🚩 |
| 18 | Deutsche Digitale Bibliothek API | DE | REST + IIIF | JSON | Yes (free) | per-item rights | partial 🚩 |
| 19 | Getty Vocabularies (AAT/ULAN/TGN) | US | SPARQL + LD + bulk + reconcile | RDF/JSON/CSV | No | **ODC-BY** (attribution) | — |
| 20 | VIAF | OCLC | REST + bulk + LD | JSON/RDF/XML | No | ODC-BY / CC0-ish (verify) | — |
| 21 | ConceptNet | MIT/intl | REST + dumps | JSON-LD | No | CC-BY-SA (parts NC) | partial 🚩 |
| 22 | ISNI | intl | SRU + REST + bulk | XML/RDF | partial | ODC-BY-ish (verify) | — |
| 23 | YAGO | Max Planck | dumps + SPARQL | RDF/TTL | No | CC-BY (varies) | — |
| 24 | Pleiades (ancient places) | US/intl | bulk + REST | JSON/CSV/RDF | No | CC-BY | — |
| 25 | Perseus Digital Library | US | bulk (GitHub) + Hopper | TEI-XML | No | CC-BY-SA / CC-BY-NC | partial 🚩 |
| 26 | Victoria & Albert Museum API | UK | REST + IIIF | JSON | No | per-item (metadata open) | partial 🚩 |
| 27 | Cooper Hewitt API | US | REST | JSON | Yes (free) | CC0 metadata | — |
| 28 | Brooklyn Museum API | US | REST | JSON | Yes (free) | per-item (CC-BY many) | partial 🚩 |
| 29 | Walters Art Museum API | US | REST | JSON | Yes (free) | CC0 metadata; images vary | partial 🚩 |
| 30 | Japan Search | JP | REST + SPARQL | JSON/RDF | partial | per-provider | partial 🚩 |
| 31 | National Diet Library (NDL) | JP | SRU/OpenSearch/OAI-PMH/IIIF | XML/JSON/RDF | mostly no | per-item rights | partial 🚩 |
| 32 | British Library | UK | SRU + OAI-PMH + IIIF + SPARQL(BNB) | MARCXML/RDF/IIIF | partial | mixed / CC0 (BNB LD) | partial 🚩 |
| 33 | KB National Library NL | NL | SRU + OAI-PMH + Jsru | XML/MARC | partial | mixed | partial 🚩 |
| 34 | Biblioteca Nacional de España (BNE) | ES | SRU + OAI-PMH + LD (datos.bne.es) | MARCXML/RDF | No | CC0 (datos.bne.es LD) | — |
| 35 | Stanford Encyclopedia of Philosophy | US | web + limited | HTML | No | per-article copyright 🚩 | 🚩 ND-like |
| 36 | World History Encyclopedia | UK/intl | web + partial API | HTML/JSON | partial | CC-BY-NC-SA 🚩 | 🚩 NC |
| 37 | 1911 Encyclopaedia Britannica | PD | bulk (Wikisource/Gutenberg) | text/wiki | No | PD | — |
| 38 | Encyclopaedia Britannica (modern) | US | no open API | — | — | proprietary 🚩 | 🚩 closed |
| 39 | BabelNet | intl (Sapienza) | REST + RDF + indices | JSON/RDF | Yes (free tier) | CC-BY-NC-SA 🚩 | 🚩 NC |
| 40 | Pelagios / Recogito / Peripleo | intl | LD + annotations | RDF/JSON-LD | No | CC-BY (varies) | — |
| 41 | Papyri.info | US/intl | bulk (GitHub) + APIs | EpiDoc TEI-XML | No | CC-BY | — |
| 42 | Open Greek and Latin / Scaife | intl | bulk (GitHub) + CTS API | TEI-XML | No | CC-BY-SA | — |
| 43 | OpenStreetMap / Nominatim / Overpass | intl | REST + bulk | JSON/XML/PBF | No (key for some) | ODbL | — |

---

# CATEGORY A — Core Knowledge Graphs & Linked Data

## 1. Wikidata
- **Official name:** Wikidata (Wikimedia Foundation).
- **URLs:**
  - SPARQL endpoint: `https://query.wikidata.org/sparql` (Wikidata Query Service / WDQS).
  - REST: `https://www.wikidata.org/w/rest.php/wikibase/v1/` (Wikibase REST API) and `https://www.wikidata.org/w/api.php` (MediaWiki Action API, `wbgetentities` etc.).
  - Entity data: `https://www.wikidata.org/wiki/Special:EntityData/Q42.json` (also `.ttl`, `.rdf`, `.nt`).
  - Linked Data Fragments: `https://query.wikidata.org/bigdata/ldf`.
  - Dumps: `https://dumps.wikimedia.org/wikidatawiki/entities/` (JSON, TTL, NT — multi-GB, latest-all.json.gz/.bz2).
- **Coverage:** ~110M+ items — people, places, organizations, works, taxa, events, concepts — multilingual labels, cross-linked to virtually every external authority (VIAF, GND, Getty, GeoNames, IMDb, etc.). The central hub of the linked-data web.
- **Access method:** SPARQL (primary for structured queries), REST/Action API, per-entity JSON/RDF, bulk dumps, LDF.
- **Data format:** JSON, RDF/Turtle/N-Triples, JSON-LD.
- **Auth / API key:** None required. Anonymous use is rate-limited; an account + OAuth or a `User-Agent` with contact info is strongly recommended. WDQS has query-timeout (60s) and concurrency limits; consider the dumps or the new **WDQS Graph Split** / Query Service Updater for heavy use.
- **Rate limits:** WDQS ~ one-minute query timeout, per-IP concurrency caps; API ~ generous but enforce `maxlag`; heavy scraping → use dumps.
- **License:** **CC0** (all data). Most permissive possible.
- **Value for fiction:** ⭐ The master index — resolve any historical figure, place, or work and pivot to every connected fact (birth/death, relations, events, coordinates, images). Ideal backbone for an entity graph.
- **VERIFY:** Current Wikibase REST path; WDQS limits post graph-split; dump filenames.

## 2. Wikipedia / MediaWiki (all language editions)
- **Official name:** Wikipedia, via the MediaWiki APIs.
- **URLs:**
  - Action API: `https://en.wikipedia.org/w/api.php` (swap language code).
  - REST v1: `https://en.wikipedia.org/api/rest_v1/` (page/summary, HTML, related, media).
  - Wikimedia REST (cross-project): `https://api.wikimedia.org/core/v1/wikipedia/en/...`.
  - Dumps: `https://dumps.wikimedia.org/` (pages-articles.xml.bz2 per wiki).
- **Coverage:** 300+ language editions; the English edition alone ~6.8M articles. Biographies, history, mythology, geography, science, culture.
- **Access method:** REST + Action API + full XML dumps (best for bulk/NLP).
- **Data format:** JSON, HTML, wikitext, XML (dumps).
- **Auth / API key:** None required; `api.wikimedia.org` supports optional access tokens that raise rate limits. Always send a descriptive `User-Agent`.
- **Rate limits:** Anonymous REST historically ~200 req/s aggregate but **per-IP limits are being tightened** (2024–2025); Action API expects serial, `maxlag`-aware access. For corpus work use dumps.
- **License:** Text **CC-BY-SA 4.0** (+ GFDL legacy); embedded media per-file.
- **Value for fiction:** Narrative prose summaries, plot/biography context, mythology, and the "infobox" structured facts; the multilingual editions give culture-specific detail not in English.
- **VERIFY:** Current REST base paths; new token-based rate tiers.

## 3. DBpedia
- **Official name:** DBpedia (Leipzig University / DBpedia Association).
- **URLs:**
  - SPARQL: `https://dbpedia.org/sparql`.
  - Resource LD: `https://dbpedia.org/resource/{Name}` (content-negotiable RDF/JSON-LD).
  - Dumps: `https://databus.dbpedia.org/` (DBpedia Databus) and historical `downloads.dbpedia.org`.
  - Language chapters: `http://{lang}.dbpedia.org/sparql` (de, fr, es, ja, etc.); **DBpedia Live** for near-real-time.
- **Coverage:** Structured extraction from Wikipedia infoboxes/categories across many language chapters; ~ billions of triples. Strong ontology typing.
- **Access method:** SPARQL (Virtuoso), Linked Data deref, bulk dumps.
- **Data format:** RDF (Turtle, N-Triples), JSON-LD.
- **Auth / API key:** None.
- **Rate limits:** Public SPARQL has result-row and timeout limits (Virtuoso defaults ~10k rows); be polite or self-host a dump.
- **License:** **CC-BY-SA** (follows Wikipedia).
- **Value for fiction:** Cleaner-typed structured facts than raw wikitext; good for ontology-driven queries ("all 19th-century French composers born in Paris").
- **VERIFY:** Which language chapters' SPARQL endpoints are live; Databus collection paths.

## 4. YAGO
- **Official name:** YAGO (Yet Another Great Ontology) — Max Planck Institute for Informatics / Télécom Paris.
- **URLs:** `https://yago-knowledge.org/` (downloads); SPARQL endpoint historically hosted (often via the project's own Virtuoso, availability intermittent).
- **Coverage:** YAGO 4 / 4.5 derived from Wikidata + schema.org taxonomy + Wikipedia, with strong logical consistency and clean types; tens of millions of entities, billions of facts. Temporal/spatial dimensions.
- **Access method:** Bulk dumps (TTL) primarily; SPARQL when the hosted endpoint is up.
- **Data format:** RDF / Turtle, conforming to schema.org + a constrained taxonomy.
- **Auth / API key:** None.
- **Rate limits:** N/A for dumps.
- **License:** **CC-BY** (with some source-dependent terms; verify per release).
- **Value for fiction:** A logically clean type system over Wikidata — useful for reliable category reasoning (genres, professions, place hierarchies) when Wikidata's looser modeling is noisy.
- **VERIFY:** Current public SPARQL availability; exact YAGO version + license file.

## 5. ConceptNet
- **Official name:** ConceptNet (originated at MIT Media Lab; maintained by Robyn Speer / Luminoso lineage).
- **URLs:** REST API `http://api.conceptnet.io/c/en/{term}` (JSON-LD); web `https://conceptnet.io/`; dumps on the site / GitHub (`conceptnet5`).
- **Coverage:** A multilingual **commonsense** knowledge graph — relations like `IsA`, `UsedFor`, `CapableOf`, `AtLocation`, `Causes`, `MotivatedByGoal` between everyday concepts; ~34M edges across many languages.
- **Access method:** REST (per-term lookups, relatedness), bulk dumps; ConceptNet Numberbatch embeddings separately.
- **Data format:** JSON-LD; CSV/edge dumps.
- **Auth / API key:** None.
- **Rate limits:** Politeness limit (~roughly 1 req/s on the public API); self-host the dump for volume.
- **License:** **CC-BY-SA 4.0** for the core; some incorporated sources are NC or otherwise restricted 🚩 (e.g. certain dictionaries) — check the per-source breakdown.
- **Value for fiction:** Brainstorming/plot-logic engine — "what is a sword used for," "what emotions cause revenge," "what is found in a castle" — great for generative association and world-logic rather than facts.
- **VERIFY:** Which sub-sources carry NC restrictions; current API host (http vs https).

## 6. BabelNet 🚩
- **Official name:** BabelNet (Sapienza University of Rome, Babelscape).
- **URLs:** `https://babelnet.org/`; REST `https://babelnet.io/v9/...`; RDF/SPARQL via the BabelNet Live / linguistic linked data; downloadable indices (large).
- **Coverage:** A massive multilingual encyclopedic dictionary + semantic network merging WordNet, Wikipedia, Wiktionary, Wikidata, OmegaWiki, etc.; ~20M "Babel synsets," 500+ languages. Combines lexical + encyclopedic senses.
- **Access method:** REST API (key-gated, daily quota), downloadable indices (license-gated), SPARQL.
- **Data format:** JSON (REST), RDF/Lemon (linked data).
- **Auth / API key:** **API key required** (free academic tier with a daily "Babelcoin" quota; commercial use needs a paid license).
- **Rate limits:** Free tier limited to a few thousand requests/day.
- **License:** **CC-BY-NC-SA 4.0** 🚩 (non-commercial). Commercial use requires a Babelscape license.
- **Value for fiction:** Best-in-class for multilingual sense disambiguation and cross-language synonyms/translations of concepts — useful if building cross-lingual story tooling, but NC blocks commercial product use.
- **VERIFY:** Current API version path (v9?), free-tier quota, commercial terms.

## 7. Getty Vocabularies — AAT, ULAN, TGN (+ CONA, IA)
- **Official name:** Getty Vocabularies (Art & Architecture Thesaurus = AAT; Union List of Artist Names = ULAN; Thesaurus of Geographic Names = TGN; Cultural Objects Name Authority = CONA; Iconography Authority = IA).
- **URLs:** SPARQL `https://vocab.getty.edu/sparql`; LD deref `https://vocab.getty.edu/aat/{id}` / `/ulan/{id}` / `/tgn/{id}`; bulk downloads (REL/N-Triples/RDF) under `vocab.getty.edu/dataset/...`; OpenRefine reconciliation service available.
- **Coverage:** AAT — art/architecture/material/style terminology; ULAN — artists & makers (names, nationalities, dates, roles); TGN — historical & modern place names with hierarchy/coordinates. Hundreds of thousands to millions of terms.
- **Access method:** SPARQL, Linked Open Data deref, bulk dumps, reconciliation API.
- **Data format:** RDF (SKOS), JSON, CSV, N-Triples.
- **Auth / API key:** None.
- **Rate limits:** Reasonable-use on SPARQL; bulk for heavy work.
- **License:** **ODC-BY 1.0** — open, **attribution required** (cite the Getty). Not CC0.
- **Value for fiction:** Authoritative controlled vocabulary for art objects, materials, styles, artist identities, and especially **historical place names** (TGN) — great for period-accurate terminology and disambiguating people/places.
- **VERIFY:** Exact dataset download paths; current attribution wording.

## 8. VIAF (Virtual International Authority File)
- **Official name:** VIAF (OCLC, aggregating national-library name authorities).
- **URLs:** `https://viaf.org/viaf/{id}/` with `.json`, `.rdf.xml`, `.marcxml`; search API `https://viaf.org/viaf/search?query=...`; AutoSuggest `https://viaf.org/viaf/AutoSuggest?query=...`; bulk data dumps on `viaf.org/viaf/data/`.
- **Coverage:** Cross-walks personal/corporate/geographic name authorities from ~50+ national libraries (LC, BnF, DNB, NDL, etc.) into clustered identities; tens of millions of records.
- **Access method:** REST per-record, search API, AutoSuggest, bulk dumps, SRU.
- **Data format:** JSON, RDF/XML, MARC21 XML.
- **Auth / API key:** None.
- **Rate limits:** Politeness expected; bulk dumps for volume.
- **License:** Historically **ODC-BY** / open with attribution (OCLC terms have shifted — **VERIFY**, OCLC has been changing data-reuse policy).
- **Value for fiction:** Disambiguate and unify historical persons across languages/catalogs; bridge to every national library's holdings for a given author.
- **VERIFY:** Current OCLC reuse terms (these are in flux); bulk dump availability.

## 9. ISNI (International Standard Name Identifier)
- **Official name:** ISNI (ISO 27729; ISNI International Agency).
- **URLs:** `https://isni.org/`; SRU search `https://isni.oclc.org/sru/...`; per-record `https://isni.org/isni/{id}` (HTML + linked data); bulk for members.
- **Coverage:** ~12M+ identities (persons + organizations) — authors, performers, publishers — with links to VIAF, Wikidata, ORCID.
- **Access method:** SRU (search/retrieve), web deref, member bulk feeds.
- **Data format:** XML (MARCXML-ish / ISNI XML), RDF.
- **Auth / API key:** Public SRU search generally open; assignment/bulk needs membership.
- **Rate limits:** Reasonable-use.
- **License:** Open public-data with attribution-style terms (verify; not formally CC).
- **Value for fiction:** Stable cross-domain author/creator IDs to deduplicate people across sources.
- **VERIFY:** Current SRU host/path; public reuse license.

## 10. GeoNames
- **Official name:** GeoNames geographical database.
- **URLs:** REST `http://api.geonames.org/searchJSON?...&username=YOU`; many endpoints (`getJSON`, `findNearbyJSON`, `countryInfoJSON`, `hierarchyJSON`, `timezoneJSON`); full dumps `https://download.geonames.org/export/dump/`.
- **Coverage:** ~12M place names worldwide — countries, admin divisions, populated places, features — with coordinates, population, alternate names (many languages), feature codes, elevation, timezones.
- **Access method:** REST (username-gated), bulk TXT dumps (allCountries.zip, etc.).
- **Data format:** JSON, XML, RDF; tab-delimited dumps.
- **Auth / API key:** **Free username required** (register, then enable web services); free tier has daily credit limits; commercial/high-volume → premium endpoints.
- **Rate limits:** Free account ~20k–30k credits/day (varies by endpoint cost); hourly cap too.
- **License:** **CC-BY 4.0** (attribution).
- **Value for fiction:** Geocode and enrich any setting — coordinates, nearby places, country/region context, historic alternate names — ideal for building plausible geography.
- **VERIFY:** Current daily credit limits; free-tier endpoint set.

## 11. OpenStreetMap / Nominatim / Overpass (bonus geo KG)
- **Official name:** OpenStreetMap; Nominatim (geocoding); Overpass API (querying).
- **URLs:** Nominatim `https://nominatim.openstreetmap.org/search?...`; Overpass `https://overpass-api.de/api/interpreter`; planet/extracts `https://planet.openstreetmap.org/`, regional via Geofabrik.
- **Coverage:** Global crowdsourced map data — streets, buildings, POIs, natural features, boundaries; far richer present-day spatial detail than GeoNames.
- **Access method:** REST geocoding (Nominatim), Overpass QL queries, bulk PBF/XML extracts.
- **Data format:** JSON, XML, PBF.
- **Auth / API key:** None for the public instances, but strict usage policy (1 req/s Nominatim, descriptive UA, no bulk on public servers — self-host for volume).
- **Rate limits:** Nominatim 1 req/s absolute; Overpass fair-use with timeouts.
- **License:** **ODbL** (Open Database License — share-alike for derived databases).
- **Value for fiction:** Real street layouts, building footprints, and POIs to ground a scene in a real city; ODbL share-alike matters if you redistribute derived data.
- **VERIFY:** Public-instance usage policy specifics.

---

# CATEGORY B — Encyclopedias & Reference Works

## 12. Encyclopaedia Britannica (modern) 🚩
- **Official name:** Encyclopaedia Britannica, Inc.
- **URLs:** `https://www.britannica.com/` (consumer); no public open API. There have historically been B2B/syndication products and a legacy developer API that is **not openly available**.
- **Coverage:** Curated encyclopedia + Merriam-Webster ties; high editorial reliability.
- **Access method:** Web only (scrape 🚩 against ToS); commercial licensing for content syndication.
- **Data format:** HTML.
- **Auth / API key:** No open key; commercial license required.
- **License:** **Proprietary / all rights reserved** 🚩. Do not scrape or redistribute.
- **Value for fiction:** Authoritative quick facts — but use only via licensing; for open use prefer Wikipedia/1911 Britannica.
- **VERIFY:** Whether any B2B API/syndication tier currently exists.

## 13. 1911 Encyclopaedia Britannica (Public Domain)
- **Official name:** Encyclopaedia Britannica, 11th Edition (1910–1911).
- **URLs:** Wikisource `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica` (access via MediaWiki API); Project Gutenberg volumes; `studylight`/`theodora.com` mirrors (varying quality).
- **Coverage:** ~40,000 articles — a complete, scholarly early-20th-century encyclopedia. Strong on history, geography, biography, classics, mythology (with period biases).
- **Access method:** Via Wikisource MediaWiki API; bulk text from Gutenberg/Internet Archive.
- **Data format:** Wikitext/HTML (Wikisource), plain text (Gutenberg).
- **Auth / API key:** None.
- **Rate limits:** Wikimedia API limits apply.
- **License:** **Public Domain** (US/most countries).
- **Value for fiction:** Freely reusable encyclopedic prose for historical/period settings; the dated worldview itself is useful for writing period-authentic narration.
- **VERIFY:** Completeness of Wikisource transcription per volume.

## 14. Stanford Encyclopedia of Philosophy (SEP) 🚩
- **Official name:** Stanford Encyclopedia of Philosophy (Metaphysics Research Lab, Stanford).
- **URLs:** `https://plato.stanford.edu/`; entries at `/entries/{topic}/`; downloadable PDFs per article; no general REST API (an internal SEP "InPhO" linkage exists).
- **Coverage:** ~1,800 peer-reviewed long-form articles on philosophy, ethics, logic, philosophy of mind/science, major thinkers.
- **Access method:** Web; structured cross-references via the companion **InPhO** (Indiana Philosophy Ontology) which does offer data/SPARQL-ish access.
- **Data format:** HTML/PDF (SEP); RDF/JSON (InPhO).
- **Auth / API key:** None for reading.
- **License:** **Copyrighted by SEP/authors** 🚩 — free to read, but **not openly licensed** for redistribution/derivatives (no CC). Treat as ND-like.
- **Value for fiction:** Deep, reliable conceptual grounding for philosophical themes, ethical dilemmas, and thinker biographies — use as reference/inspiration, not as redistributable text.
- **VERIFY:** Current InPhO data access; any text-reuse permissions.

## 15. World History Encyclopedia (formerly Ancient History Encyclopedia) 🚩
- **Official name:** World History Encyclopedia (WHE).
- **URLs:** `https://www.worldhistory.org/`; a partner/REST API has existed (`https://www.worldhistory.org/api/` style) for licensed partners; structured content available.
- **Coverage:** Thousands of articles, definitions, timelines, maps, and images across ancient–modern world history; strong on antiquity, mythology, and civilizations.
- **Access method:** Web; partner API (gated).
- **Data format:** HTML; JSON (partner API).
- **Auth / API key:** API access historically partner-gated.
- **License:** **CC-BY-NC-SA** 🚩 for much of the content (non-commercial + share-alike). Images vary; some third-party rights.
- **Value for fiction:** Excellent accessible articles on civilizations, gods, battles, daily life — great research reading; NC blocks commercial redistribution of the text.
- **VERIFY:** Current API availability/terms; per-article license.

## 16. Other open reference worth cataloging
- **Wiktionary** — `https://en.wiktionary.org/w/api.php`; CC-BY-SA; definitions, etymologies, translations across languages (use for period vocabulary, name meanings). Bulk via dumps; **DBnary** provides RDF extractions (CC-BY-SA / CC-BY-NC depending on edition 🚩).
- **Wikiquote** — MediaWiki API; CC-BY-SA; sourced quotations (dialogue inspiration, epigraphs).
- **Wikisource** — MediaWiki API + IIIF; mostly PD source texts (historical documents, classic literature).
- **Encyclopedia.com / Infoplease** 🚩 — aggregators, proprietary, no open API.
- **Catholic Encyclopedia (1913)** — PD, via New Advent / Wikisource (medieval/religious history detail).
- **Jewish Encyclopedia (1906)** — PD, `jewishencyclopedia.com` + Wikisource (Jewish history, mythology, biblical figures).
- **Encyclopædia Iranica** 🚩 — `iranicaonline.org`; scholarly, copyrighted (Persian/Iranian history & culture) — read-only.
- **VERIFY:** DBnary per-language license; Iranica reuse terms.

---

# CATEGORY C — Cultural-Heritage Aggregators (multi-country)

## 17. Europeana API
- **Official name:** Europeana (Europeana Foundation, EU).
- **URLs:** Search/Record API `https://api.europeana.eu/record/v2/search.json?wskey=...`; Entity API; IIIF `https://iiif.europeana.eu/`; SPARQL (historical) `http://sparql.europeana.eu/`; OAI-PMH; annotations API.
- **Coverage:** ~50M+ digitized objects aggregated from **3,000+ institutions across all EU member states** — artworks, books, photos, manuscripts, audio, 3D. Pan-European in 30+ languages.
- **Access method:** REST (Search/Record/Entity), IIIF, OAI-PMH, SPARQL (LD).
- **Data format:** JSON-LD, RDF (Europeana Data Model / EDM), IIIF.
- **Auth / API key:** **Free API key (wskey) required.**
- **Rate limits:** Generous free tier (historically ~10k req/day, negotiable).
- **License:** **Metadata is CC0**; media carries **per-item rights** (rightsstatements.org values — many PD/CC, some In-Copyright 🚩). Always check `edm:rights`.
- **Value for fiction:** ⭐ The single broadest European visual/textual heritage index — period images, manuscripts, maps, portraits across dozens of countries in one query. Filter by `REUSABILITY=open`.
- **VERIFY:** SPARQL endpoint still live?; current rate quota; key signup flow.

## 18. DPLA (Digital Public Library of America)
- **Official name:** Digital Public Library of America.
- **URLs:** REST `https://api.dp.la/v2/items?api_key=...`; bulk data exports (S3 / annual dumps).
- **Coverage:** ~50M+ items aggregated from US libraries, archives, museums (hubs like NYPL, HathiTrust, Smithsonian, state digital libraries). Photos, texts, maps, ephemera, oral histories.
- **Access method:** REST, bulk JSON dumps.
- **Data format:** JSON (MAPS / DPLA MAP model), some JSON-LD.
- **Auth / API key:** **Free API key required** (request via email/endpoint).
- **Rate limits:** Reasonable-use; bulk for volume.
- **License:** **Metadata CC0**; media per-item rights (check `rights` / `edmRights`) 🚩 some In-Copyright.
- **Value for fiction:** Deep Americana — historical photos, newspapers, regional archives — for US-set period stories; complements Europeana's European focus.
- **VERIFY:** Current bulk-export location; key request process.

## 19. Trove (Australia)
- **Official name:** Trove (National Library of Australia).
- **URLs:** API v3 `https://api.trove.nla.gov.au/v3/...` (replaced v2); requires key.
- **Coverage:** Massive Australian aggregation — **digitized newspapers (a standout, OCR full text), books, photos, maps, music, archived websites, diaries**; hundreds of millions of records.
- **Access method:** REST.
- **Data format:** JSON, XML.
- **Auth / API key:** **Free API key required** (register a Trove account).
- **Rate limits:** Reasonable-use; non-commercial vs commercial key tiers.
- **License:** Metadata terms mixed; **digitized newspapers** are largely out-of-copyright; per-item rights vary 🚩.
- **Value for fiction:** ⭐ The historical-newspaper full text is gold for period dialogue, events, advertisements, and local color (esp. 19th–20th c. Australia/colonial).
- **VERIFY:** v3 endpoint paths; commercial-use terms; key tiers.

## 20. DigitalNZ (New Zealand)
- **Official name:** DigitalNZ (operated by the National Library of New Zealand / DigitalNZ team).
- **URLs:** REST `https://api.digitalnz.org/v3/records.json?api_key=...`.
- **Coverage:** ~30M+ items aggregated from NZ libraries, museums, galleries, archives — photos, newspapers, artworks, audio, Māori cultural materials (with appropriate cultural protocols).
- **Access method:** REST.
- **Data format:** JSON.
- **Auth / API key:** **Free API key required.**
- **Rate limits:** Reasonable-use.
- **License:** Per-item rights (mixed; many open, some restricted) 🚩; respect Māori data-sovereignty notices.
- **Value for fiction:** NZ/Pacific historical imagery and texts; Māori cultural context (handle with care/respect).
- **VERIFY:** Current API version; cultural-use guidance.

## 21. Japan Search (ジャパンサーチ)
- **Official name:** Japan Search (Japan's national cultural-heritage aggregation portal).
- **URLs:** `https://jpsearch.go.jp/`; REST API and **SPARQL** endpoint for the integrated linked data.
- **Coverage:** Cross-institution aggregation — NDL, museums, archives, universities — covering books, artworks, cultural properties, photographs across Japan.
- **Access method:** REST + SPARQL (RDF linked data).
- **Data format:** JSON, RDF.
- **Auth / API key:** Some endpoints open; check per-database.
- **License:** **Per-provider** (mixed) 🚩 — many CC, some restricted.
- **Value for fiction:** Unified gateway to Japanese cultural heritage with structured linked data for cross-referencing.
- **VERIFY:** API/SPARQL endpoint URLs; provider license matrix. (Also covered in 01-korea-east-asia.md.)

## 22. Other aggregators worth knowing
- **Digital Collections aggregators (national):**
  - **Kulturpool** (Austria) — `kulturpool.at`, aggregates Austrian GLAM, feeds Europeana.
  - **Cultura Italia / CulturaItalia** (Italy) 🚩 — OAI-PMH/Linked Open Data, feeds Europeana.
  - **Hispana** (Spain) — `hispana.mcu.es`, OAI-PMH aggregator, feeds Europeana.
  - **Swissbib / swisscovery / memoriav** (Switzerland) — library/media aggregation.
  - **Finna.fi** (Finland) — `api.finna.fi`, REST, aggregates Finnish libraries/museums/archives (very open, good API).
  - **Kulturarvsdata / SOCH (K-samsök)** (Sweden) — `kulturarvsdata.se`, REST/RDF, Swedish heritage.
  - **DigitaltMuseum** (Norway/Sweden) — `digitaltmuseum.org`, API, museum objects.
  - **CER.es / red digital** (Spain museums).
  - **Deutsche Digitale Bibliothek** (Germany — see Cat. D).
  - **Trove / DigitalNZ / Japan Search** (above).
  - **PARTHENOS / CLARIN / DARIAH** — European research infrastructures (linguistic/heritage data).
- **Internet Archive** — `https://archive.org/`; Advanced Search + Metadata API (`archive.org/metadata/{id}`), Scholar, Wayback CDX API; huge PD book/audio/film/software corpus; mixed rights but vast PD core. **Excellent, key-less, well-documented.**
- **HathiTrust** 🚩 — `hathitrust.org`; Bibliographic API + Data API (member-gated for full text); huge digitized book corpus, much in-copyright restricted.
- **VERIFY:** Finna/SOCH endpoint paths; which aggregators expose open APIs vs OAI-only.

---

# CATEGORY D — National Libraries (APIs / SRU / OAI-PMH / IIIF / SPARQL)

## 23. Library of Congress (USA)
- **Official name:** Library of Congress (LoC).
- **URLs:**
  - loc.gov JSON API: append `?fo=json` to most `loc.gov` URLs (e.g. `https://www.loc.gov/collections/?fo=json`, `/search/?q=...&fo=json`).
  - LC Linked Data Service: `https://id.loc.gov/` (LCSH, LC Name Authority File LCNAF, MARC relators, vocabularies) — content-negotiable RDF.
  - SRU/Z39.50: `http://lx2.loc.gov:210/LCDB`.
  - Chronicling America (historic newspapers): `https://chroniclingamerica.loc.gov/` — JSON + OpenSearch + bulk OCR.
  - IIIF for digitized items; bulk datasets via `data.labs.loc.gov` / LC Labs.
- **Coverage:** Largest library in the world — books, manuscripts, maps, photos (e.g. FSA/OWI), recordings, historic US newspapers, subject/name authorities.
- **Access method:** REST/JSON, Linked Data, SRU, IIIF, OAI-PMH (some collections), bulk.
- **Data format:** JSON, MARCXML, MODS, RDF, IIIF.
- **Auth / API key:** None (rate-limited; descriptive UA recommended).
- **Rate limits:** loc.gov JSON API enforces burst limits (e.g. ~ tens of req/min before throttling; "newspapers" and "search" endpoints have specific caps).
- **License:** Most LoC-created metadata/images have **no known copyright restriction / PD**; some collections restricted 🚩 — check rights per item.
- **Value for fiction:** ⭐ Authorities (LCSH/LCNAF) for controlled subjects/names; Chronicling America OCR newspapers for period American voice; vast PD photo archive for visual reference.
- **VERIFY:** Current loc.gov JSON rate limits; id.loc.gov vocab list.

## 24. British Library (UK)
- **Official name:** The British Library (BL).
- **URLs:**
  - SRU/Z39.50 catalogue: `http://sru.bl.uk/` (Explore / Primo-based search has shifted; verify).
  - British National Bibliography (BNB) Linked Data: `https://bnb.data.bl.uk/` + SPARQL endpoint.
  - IIIF for digitized manuscripts (`https://api.bl.uk/...` / Digitised Manuscripts viewer).
  - Data portal / `data.bl.uk` and shared datasets (some on `bl.iro.bl.uk`, GitHub).
  - **Note:** BL suffered a major cyberattack (Oct 2023); several services were degraded/rebuilt through 2024–2025 🚩 — **verify current availability.**
- **Coverage:** UK national library — books, the BNB, medieval/illuminated manuscripts, maps, sound archive, philatelic, newspapers.
- **Access method:** SRU, OAI-PMH, IIIF, SPARQL (BNB LD), bulk datasets.
- **Data format:** MARCXML, RDF/Turtle, IIIF, CSV.
- **Auth / API key:** Mostly none; some registration.
- **License:** **BNB Linked Data is CC0**; digitized images often PD or BL terms; per-item 🚩.
- **Value for fiction:** Illuminated-manuscript IIIF imagery, the BNB for British bibliographic data, historic UK newspapers.
- **VERIFY:** Post-cyberattack service status; current SRU/SPARQL endpoints.

## 25. BnF / Gallica (France)
- **Official name:** Bibliothèque nationale de France (BnF); Gallica (its digital library); data.bnf.fr (linked data).
- **URLs:**
  - Gallica IIIF: `https://gallica.bnf.fr/iiif/ark:/12148/{ark}/manifest.json`; Gallica API/SRU `https://gallica.bnf.fr/SRU?...`; Gallica `Document` & `Pagination` APIs; OAI-PMH `https://gallica.bnf.fr/services/OAIRecord`.
  - BnF catalogue SRU: `http://catalogue.bnf.fr/api/SRU`.
  - data.bnf.fr: `https://data.bnf.fr/` — Linked Data + **SPARQL** (`https://data.bnf.fr/sparql`), RDF dumps.
- **Coverage:** Millions of digitized items — books, the Bibliothèque bleue, manuscripts, maps, the **Bibliothèque nationale's newspaper collection (Retronews / Gallica press)**, images, music. data.bnf.fr links authors/works/subjects.
- **Access method:** IIIF, SRU, OAI-PMH, SPARQL/LD, document APIs.
- **Data format:** IIIF, MARCXML/UNIMARC, RDF, JSON.
- **Auth / API key:** None for Gallica/data.bnf.fr public APIs.
- **License:** **data.bnf.fr is open** (largely CC-BY / Etalab Open Licence); Gallica items mostly **public domain** but carry a **Gallica reuse notice** (free for non-commercial; commercial reuse of PD images may incur conditions) 🚩 — verify.
- **Value for fiction:** ⭐ Enormous French/European PD imagery and texts; data.bnf.fr SPARQL for French authors/works; historic French press for period detail.
- **VERIFY:** Gallica commercial-reuse terms; SRU parameter set.

## 26. Deutsche Nationalbibliothek (DNB) + Deutsche Digitale Bibliothek (DDB) (Germany)
- **Official name:** Deutsche Nationalbibliothek (DNB) and Deutsche Digitale Bibliothek (DDB).
- **URLs:**
  - DNB SRU: `https://services.dnb.de/sru/dnb` (also `/authorities` for GND).
  - **GND** (Gemeinsame Normdatei / Integrated Authority File) Linked Data: `https://d-nb.info/gnd/{id}` (content-negotiable RDF); GND now also via **lobid-gnd** `https://lobid.org/gnd/...` (excellent JSON-LD API + reconciliation).
  - DNB OAI-PMH; bulk RDF dumps of GND.
  - DDB API: `https://api.deutsche-digitale-bibliothek.de/` (REST, key required); IIIF; search across German GLAM.
- **Coverage:** DNB — German national bibliography + GND authorities (persons, organizations, subjects, places, works — millions, widely reused across Europe). DDB — ~40M+ objects from German libraries/archives/museums.
- **Access method:** SRU, OAI-PMH, Linked Data (GND/lobid), REST (DDB), IIIF.
- **Data format:** MARCXML/MARC21, RDF/Turtle, JSON-LD, IIIF.
- **Auth / API key:** DNB SRU/LD open; **DDB API requires a free key.**
- **License:** **GND data is CC0**; lobid is open; DDB media per-item rights 🚩.
- **Value for fiction:** GND is a top-tier authority for German/European persons & works (links to Wikidata/VIAF); DDB for German heritage imagery/texts.
- **VERIFY:** DDB key signup; lobid endpoint stability.

## 27. KB — Koninklijke Bibliotheek (National Library of the Netherlands)
- **Official name:** Koninklijke Bibliotheek (KB), Nederland.
- **URLs:** SRU `http://jsru.kb.nl/sru/...` and `http://services.kb.nl/`; OAI-PMH; **Delpher** (digitized Dutch newspapers/books/magazines) `https://www.delpher.nl/` with APIs; Data services / `dataservices.kb.nl`.
- **Coverage:** Dutch national bibliography, **Delpher** historic newspapers & books (huge OCR corpus, 17th–20th c.), the GGC union catalog, manuscripts.
- **Access method:** SRU, OAI-PMH, REST data services, IIIF.
- **Data format:** MARCXML, Dublin Core, JSON, IIIF.
- **Auth / API key:** Some services need a (free) key/registration.
- **License:** Mixed; much PD newspaper content; per-item 🚩.
- **Value for fiction:** Delpher's centuries of Dutch press = period events, ads, voice for Netherlands/colonial settings.
- **VERIFY:** Current Delpher API access policy (has had restrictions); SRU hosts.

## 28. Biblioteca Nacional de España (BNE) (Spain)
- **Official name:** Biblioteca Nacional de España.
- **URLs:** SRU/Z39.50; OAI-PMH; **datos.bne.org / datos.bne.es** — Linked Open Data + SPARQL + RDF dumps (built on the BNE's "linked data" project); Biblioteca Digital Hispánica (BDH) IIIF.
- **Coverage:** Spanish national bibliography, authors/works linked data, digitized rare books & manuscripts (BDH), Cervantes-era materials.
- **Access method:** SRU, OAI-PMH, SPARQL/LD, IIIF.
- **Data format:** MARCXML, RDF, IIIF.
- **Auth / API key:** LD/SPARQL open; catalogue SRU open.
- **License:** **datos.bne LD released as CC0**; BDH digitized PD items generally free reuse; per-item 🚩.
- **Value for fiction:** Spanish Golden Age & colonial-Spanish source materials; structured author/work data with CC0 linked data.
- **VERIFY:** Current datos.bne domain (.org vs .es); SPARQL endpoint.

## 29. National Diet Library (NDL) (Japan)
- **Official name:** 国立国会図書館 / National Diet Library.
- **URLs:** NDL Search SRU/OpenSearch/OpenURL; OAI-PMH; **NDL Digital Collections IIIF**; **Web NDL Authorities** (`https://id.ndl.go.jp/auth/`) Linked Data; NDL Ngram / full-text datasets.
- **Coverage:** Japan's national bibliography, digitized books (much PD pre-1968), the NDL authorities, historic materials.
- **Access method:** SRU/OpenSearch, OAI-PMH, IIIF, Linked Data.
- **Data format:** DC-NDL XML, MARC, RDF, IIIF.
- **Auth / API key:** Mostly none.
- **License:** Per-item rights (much PD; some restricted) 🚩.
- **Value for fiction:** Japanese historical texts/images; authorities link to VIAF/Wikidata. (Also in 01-korea-east-asia.md.)
- **VERIFY:** Current SRU/IIIF endpoints.

## 30. More national / major libraries (breadth expansion)
Grouped quick entries — all to be verified; most expose **SRU and/or OAI-PMH and/or IIIF**, many with linked-data authorities:

**Europe**
- **British Library** (UK) — above (#24).
- **National Library of Scotland** — `data.nls.uk` (open data, maps), IIIF.
- **National Library of Wales / Llyfrgell Genedlaethol Cymru** — IIIF, open data, Welsh newspapers (`papuraunewydd`/Welsh Newspapers Online).
- **Trinity College Dublin Digital Collections** (Book of Kells IIIF) — Ireland.
- **National Library of Ireland** — catalogue, photos (Flickr Commons).
- **ONB — Österreichische Nationalbibliothek** (Austria) — ANNO historic newspapers (`anno.onb.ac.at`), IIIF, APIs; **AustriaN Newspapers Online** is a strong OCR press corpus.
- **Swiss National Library / e-newspaperarchives.ch / e-rara / e-codices** (Switzerland) — e-codices IIIF manuscripts (excellent), e-rara rare books.
- **KBR — Royal Library of Belgium** (Belgium) — Belgica, IIIF.
- **National Library of Norway (Nasjonalbiblioteket)** — `api.nb.no` (very rich API, large digitized corpus, books/newspapers), IIIF; strong open access.
- **National Library of Sweden (Kungliga biblioteket, KB)** — `libris.kb.se` (LIBRIS union catalog, SPARQL/LD), Swedish newspapers.
- **National Library of Finland** — `finna.fi` API (#22), Fennica bibliography, Digi historic newspapers.
- **National Library of Denmark / Det Kgl. Bibliotek** — Mediestream newspapers, IIIF, APIs.
- **National Library of Portugal (BNP)** — catalogue, BND digital library.
- **National Library of Poland (Polona)** — `polona.pl` huge digitized collection, API/IIIF.
- **National Library of the Czech Republic / Kramerius** — Kramerius API (shared across Czech libraries), IIIF.
- **Russian State Library / National Library of Russia** 🚩 — access variable; geopolitical/legal caveats.
- **Europeana Newspapers / The European Library legacy** — aggregated historic press.
- **Vatican Library (BAV) — DigiVatLib** — `digi.vatlib.it`, **IIIF** manuscripts (superb for medieval/Renaissance), metadata open-ish 🚩 image reuse terms.

**Americas**
- **Library of Congress** (US) — above (#23).
- **HathiTrust** (US) 🚩 — #22.
- **Internet Archive** (US/global) — #22.
- **Library and Archives Canada (BAC-LAC)** — catalogue, Canadiana, OAI.
- **Biblioteca Nacional de México / Mexicana** — `mexicana.cultura.gob.mx` aggregator, API.
- **Biblioteca Nacional Digital Brasil / Hemeroteca Digital** — Brazilian historic newspapers (`hemerotecadigital.bn.gov.br`).
- **Biblioteca Nacional de Chile / Memoria Chilena / BND** — `bibliotecanacionaldigital.gob.cl`.
- **Biblioteca Nacional Argentina** — digital catalog.

**Asia / MENA / Africa / Oceania**
- **National Diet Library** (Japan) — #29.
- **National Library of Korea (국립중앙도서관)** — REST/SRU/LOD (see 01-korea-east-asia.md).
- **National Library of China (中国国家图书馆) / CADAL / CTEXT** 🚩 — access variable.
- **National Library Board Singapore** — `eservice.nlb.gov.sg` OpenWeb / NLB Labs APIs (good), historic newspapers (NewspaperSG).
- **Qatar Digital Library** — `qdl.qa` (British Library partnership) IIIF, Gulf/Arabic historical archives, **open** (much PD/CC).
- **National Library of Israel (NLI)** — `https://www.nli.org.il/` open APIs + IIIF + linked data (`Ktiv` manuscripts); strong open program.
- **National Library of Australia / Trove** — #19.
- **National Library of New Zealand / DigitalNZ** — #20.
- **HathiTrust, World Digital Library (legacy, now folded into LoC)** — global digitized treasures.
- **VERIFY (all of #30):** Endpoint URLs, API-key needs, and per-item license — these vary widely; National Library of Norway (`api.nb.no`), Finland (`finna.fi`), Poland (Polona), Qatar Digital Library, and NLI are the most API-friendly.

---

# CATEGORY E — Museum & Art APIs

## 31. The Metropolitan Museum of Art (The Met) — Open Access API
- **Official name:** The Metropolitan Museum of Art Collection API.
- **URLs:** `https://collectionapi.metmuseum.org/public/collection/v1/objects`, `/objects/{id}`, `/search?q=...`, `/departments`.
- **Coverage:** ~470k+ objects across all departments/cultures; ~400k+ images. Global art history.
- **Access method:** REST.
- **Data format:** JSON (+ image URLs).
- **Auth / API key:** **None.**
- **Rate limits:** ~80 requests/second suggested cap (be polite).
- **License:** Open-access objects' images & data are **CC0**; non-open objects metadata-only 🚩.
- **Value for fiction:** ⭐ Best beginner art API — pull period-accurate objects, costume, weapons, artifacts with CC0 images for reference/mood.
- **VERIFY:** Current rate guidance.

## 32. Art Institute of Chicago API
- **Official name:** Art Institute of Chicago (AIC) Public API.
- **URLs:** `https://api.artic.edu/api/v1/artworks`, `/artworks/search`; IIIF image server `https://www.artic.edu/iiif/2/{id}/full/...`.
- **Coverage:** ~120k+ artworks; rich metadata; strong IIIF imagery.
- **Access method:** REST + IIIF + Elasticsearch-backed search; data dumps on GitHub.
- **Data format:** JSON, JSON-LD, IIIF.
- **Auth / API key:** None (descriptive UA / `AIC-User-Agent` requested).
- **License:** Public-domain artworks' images **CC0**; metadata CC0; some images restricted 🚩.
- **Value for fiction:** Excellent IIIF zoomable images of major artworks; clean modern API.
- **VERIFY:** UA header requirement.

## 33. Smithsonian Open Access
- **Official name:** Smithsonian Institution Open Access (via data.gov / api.si.edu).
- **URLs:** `https://api.si.edu/openaccess/api/v1.0/search?q=...&api_key=...`; bulk on GitHub/AWS Open Data.
- **Coverage:** ~5M+ records across 19 museums + research centers + zoo — art, history, science, natural history, air & space; ~4.5M+ CC0 media.
- **Access method:** REST (api.si.edu via data.gov), bulk.
- **Data format:** JSON.
- **Auth / API key:** **Free api.data.gov key required.**
- **Rate limits:** data.gov default (~1,000 req/hr per key, raisable).
- **License:** **CC0** for the Open Access subset; non-OA items metadata-only 🚩.
- **Value for fiction:** ⭐ Enormous cross-domain CC0 imagery — natural history, Americana, aviation, ethnographic objects.
- **VERIFY:** Current rate tier; bulk location.

## 34. Cleveland Museum of Art (CMA) Open Access API
- **Official name:** Cleveland Museum of Art Open Access API.
- **URLs:** `https://openaccess-api.clevelandart.org/api/artworks/`, `?q=...`; IIIF; data on GitHub (CSV/JSON).
- **Coverage:** ~60k+ artworks, ~30k+ open-access CC0 images.
- **Access method:** REST + IIIF + bulk.
- **Data format:** JSON, CSV, IIIF.
- **Auth / API key:** None.
- **License:** Open-access works **CC0**; others restricted 🚩.
- **Value for fiction:** Clean CC0 art with IIIF; well-documented.
- **VERIFY:** Endpoint base.

## 35. Rijksmuseum API (Netherlands)
- **Official name:** Rijksmuseum API.
- **URLs:** `https://www.rijksmuseum.nl/api/{lang}/collection?key=...`; OAI-PMH `https://www.rijksmuseum.nl/api/oai/...`; IIIF.
- **Coverage:** ~1M+ objects; ~700k+ images (Rembrandt, Vermeer, Dutch Golden Age, Asian art, history).
- **Access method:** REST + OAI-PMH + IIIF.
- **Data format:** JSON, XML (OAI), IIIF.
- **Auth / API key:** **Free API key** (request via Rijksstudio account).
- **Rate limits:** ~10k req/day (varies).
- **License:** Public-domain works' high-res images **CC0 / PD** (Rijksstudio); newer/in-copyright works restricted 🚩.
- **Value for fiction:** ⭐ Dutch Golden Age and global art in stunning high-res; superb for visual mood/reference.
- **VERIFY:** Key signup; current rate cap.

## 36. Harvard Art Museums API
- **Official name:** Harvard Art Museums API.
- **URLs:** `https://api.harvardartmuseums.org/object?apikey=...` (also `/person`, `/exhibition`, `/gallery`); IIIF.
- **Coverage:** ~250k+ objects (Fogg, Busch-Reisinger, Sackler) — Western, Asian, ancient art; rich color/technique metadata.
- **Access method:** REST + IIIF.
- **Data format:** JSON, IIIF.
- **Auth / API key:** **Free API key required.**
- **Rate limits:** Reasonable-use.
- **License:** **Per-item rights** 🚩 (many PD with open images; some restricted) — check `imagepermissionlevel`/copyright fields.
- **Value for fiction:** Deep, research-grade metadata (provenance, technique, color); good for object study.
- **VERIFY:** Image-reuse fields.

## 37. Victoria & Albert Museum (V&A) API (UK)
- **Official name:** Victoria and Albert Museum Collections API.
- **URLs:** `https://api.vam.ac.uk/v2/objects/search?...`, `/object/{id}`; IIIF.
- **Coverage:** ~1.2M+ records — decorative arts, design, fashion/costume, ceramics, furniture, theatre, photographs. ⭐ for material culture.
- **Access method:** REST + IIIF.
- **Data format:** JSON, IIIF.
- **Auth / API key:** None (rate-limited).
- **License:** Metadata open; images per-item (many free for non-commercial; some restricted) 🚩.
- **Value for fiction:** ⭐ Unmatched for **costume, fashion, design, everyday objects** across eras/cultures — ideal for material-culture accuracy.
- **VERIFY:** Image license fields.

## 38. Cooper Hewitt, Smithsonian Design Museum API
- **Official name:** Cooper Hewitt Collection API.
- **URLs:** `https://api.collection.cooperhewitt.org/rest/` (method-style, e.g. `cooperhewitt.objects.getInfo`).
- **Coverage:** ~200k+ design objects (textiles, wallpaper, product design, drawings).
- **Access method:** REST (Flickr-style method API).
- **Data format:** JSON.
- **Auth / API key:** **Free token/key required.**
- **License:** Metadata **CC0**; images per-item 🚩.
- **Value for fiction:** Design/pattern/textile reference; pioneering open-collection metadata.
- **VERIFY:** API host still live.

## 39. Walters Art Museum API (Baltimore)
- **Official name:** The Walters Art Museum API.
- **URLs:** `http://api.thewalters.org/v1/objects?apikey=...`.
- **Coverage:** ~36k+ objects — ancient, medieval, Islamic, Renaissance art, illuminated manuscripts.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth / API key:** **Free API key required.**
- **License:** Metadata **CC0**; many images CC-BY-SA/PD; per-item 🚩.
- **Value for fiction:** Strong medieval/ancient/Islamic holdings for premodern settings.
- **VERIFY:** http vs https; key signup.

## 40. Brooklyn Museum API
- **Official name:** Brooklyn Museum Collection API.
- **URLs:** `https://www.brooklynmuseum.org/api/v2/...` (objects, collections); key required.
- **Coverage:** ~150k+ objects — Egyptian, American, African, feminist art (Dinner Party), decorative arts.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth / API key:** **Free API key required.**
- **License:** Per-item; many images **CC-BY** or PD 🚩 (check).
- **Value for fiction:** Strong Egyptology and Americana.
- **VERIFY:** Current v2 paths; key process.

## 41. More museum/art APIs (breadth expansion)
- **Getty Museum** — `data.getty.edu` / Getty's collection Linked Art JSON-LD; many images **open content** (CC0/PD); plus the Getty Vocabularies (#7) and Getty Provenance/Photo Study.
- **National Gallery of Art (Washington, NGA)** — open-data on GitHub (CSV/images), many **CC0** images; API limited (bulk data).
- **MoMA** 🚩 — collection **data on GitHub** (CC0 metadata) but **no live API and images restricted**.
- **Whitney, Tate** 🚩 — Tate released collection metadata on GitHub (CC-BY-NC-ND-ish for some / images restricted); read carefully.
- **Europeana art** (#17) — pan-European artworks.
- **Paris Musées (Open Content)** — `parismusees` open data portal; ~100k+ **CC0** images from Paris city museums (Carnavalet, etc.).
- **Finnish National Gallery (FNG) API** — `https://www.kansallisgalleria.fi/` API, open data.
- **Statens Museum for Kunst (SMK, Denmark)** — `https://api.smk.dk/` excellent open API, many **CC0** high-res images. ⭐
- **Nationalmuseum Sweden** — open data, many PD images.
- **Rijksmuseum / Mauritshuis** (NL) — Mauritshuis has open content too.
- **Auckland Museum** (NZ) — API/Linked Data.
- **Te Papa (Museum of NZ)** — `https://data.tepapa.govt.nz/` collections API (key), many open images.
- **Powerhouse / Museums Victoria / Australian Museum** (AU) — Museums Victoria has an open **collections API** (`collections.museumsvictoria.com.au/api`), CC-BY/CC0 records. ⭐
- **National Palace Museum (Taipei)** 🚩 — open-data portal, some CC; verify.
- **British Museum** — collection **Semantic Web / SPARQL** endpoint historically (`collection.britishmuseum.org/sparql`) + web collection online + IIIF; metadata CC-BY-NC-SA in places 🚩; huge global antiquities coverage. ⭐ but check NC.
- **Science Museum Group (UK)** — `https://collection.sciencemuseumgroup.org.uk/` open API (CC-BY-NC-SA metadata 🚩).
- **Wellcome Collection (UK)** — `https://api.wellcomecollection.org/catalogue/v2/...` excellent API + IIIF; much **CC0/CC-BY** (medical/history of science imagery). ⭐
- **Yale Center for British Art / Yale University Art Gallery / LUX** — Yale's **LUX** (`lux.collections.yale.edu`) cross-collection Linked Art; many **open access** images. ⭐
- **VERIFY (all of #41):** Per-museum image license (CC0 vs NC vs restricted) and API-key needs. **Highlights for openness:** SMK (Denmark), Wellcome, Paris Musées, Te Papa, Museums Victoria, Yale LUX, NGA, Finnish National Gallery.

---

# CATEGORY F — Classics & Ancient World

## 42. Perseus Digital Library
- **Official name:** Perseus Digital Library (Tufts University).
- **URLs:** Perseus Hopper `http://www.perseus.tufts.edu/hopper/`; CTS/CITE APIs (Scaife/CapiTainS); **bulk TEI-XML on GitHub** (`PerseusDL/canonical-greekLit`, `canonical-latinLit`).
- **Coverage:** Greek & Latin classical texts (with morphological analysis, parallel translations), plus art/archaeology and reference works (LSJ lexicon, Smith's dictionaries).
- **Access method:** Web (Hopper), CTS API, bulk TEI-XML repos.
- **Data format:** TEI-XML; some JSON via APIs.
- **Auth / API key:** None.
- **License:** Mostly **CC-BY-SA**; some texts **CC-BY-NC-SA** 🚩 — per-text (check the repo's license).
- **Value for fiction:** ⭐ Source texts + translations of Homer, Virgil, Herodotus, etc.; lexica for authentic terminology; foundation for mythological/antique fiction.
- **VERIFY:** Per-text NC flags.

## 43. Open Greek and Latin / Scaife Viewer (OGL)
- **Official name:** Open Greek and Latin (DH @ Leipzig/Harvard/Tufts); Scaife Viewer.
- **URLs:** Scaife `https://scaife.perseus.org/`; CTS API; GitHub repos (`OpenGreekAndLatin/...`, `PerseusDL/...`).
- **Coverage:** Aims at the full corpus of ancient Greek & Latin (and translations); First1KGreek project; canonical text services (CTS URNs).
- **Access method:** CTS API, bulk TEI-XML (GitHub).
- **Data format:** TEI-XML.
- **Auth / API key:** None.
- **License:** Mostly **CC-BY-SA** (per-text).
- **Value for fiction:** Broadest open ancient-text corpus with stable citation URNs.
- **VERIFY:** Repo licenses per work.

## 44. Pleiades (ancient places gazetteer)
- **Official name:** Pleiades (NYU ISAW et al.).
- **URLs:** `https://pleiades.stoa.org/`; JSON per place `…/places/{id}/json`; bulk dumps (CSV/JSON/RDF/KML) `pleiades.stoa.org/downloads`.
- **Coverage:** ~40k+ ancient places (Greek/Roman world + beyond) with coordinates, names over time, time periods, links.
- **Access method:** REST/JSON, bulk, RDF.
- **Data format:** JSON, CSV, RDF, KML.
- **Auth / API key:** None.
- **License:** **CC-BY** 3.0.
- **Value for fiction:** ⭐ The gazetteer for the ancient Mediterranean — map your antiquity settings to real attested places, with historical name variants.
- **VERIFY:** Download paths.

## 45. Pelagios / Recogito / Peripleo
- **Official name:** Pelagios Network (linked ancient/historical geodata); Recogito (annotation); Peripleo (search/map).
- **URLs:** `https://pelagios.org/`; Recogito `https://recogito.pelagios.org/`; gazetteer interconnections (Pleiades, iDAI, etc.).
- **Coverage:** Federated network linking texts, maps, and places across the ancient & medieval world via shared gazetteer URIs.
- **Access method:** Linked Data / annotations; various member APIs.
- **Data format:** RDF, JSON-LD (Web Annotation), GeoJSON.
- **Auth / API key:** Varies by component.
- **License:** **CC-BY** (varies by dataset).
- **Value for fiction:** Connect places across sources/maps; discover where ancient texts mention a location.
- **VERIFY:** Which Peripleo/Recogito APIs are live.

## 46. Papyri.info
- **Official name:** Papyri.info (Duke/Heidelberg et al.; integrates DDbDP, HGV, APIS, Trismegistos links).
- **URLs:** `https://papyri.info/`; data on GitHub (`papyri.info` / `idp.data`); APIs/search.
- **Coverage:** Documentary papyri — Greek/Latin/Egyptian everyday documents (contracts, letters, receipts) with EpiDoc TEI editions.
- **Access method:** Bulk GitHub (EpiDoc TEI-XML), search APIs.
- **Data format:** EpiDoc TEI-XML.
- **Auth / API key:** None.
- **License:** **CC-BY** (texts).
- **Value for fiction:** ⭐ Real everyday-life documents from Greco-Roman Egypt — letters, complaints, contracts — gold for grounded daily-life detail and authentic voice.
- **VERIFY:** API endpoints vs bulk-only.

## 47. More ancient/epigraphy resources (breadth)
- **Trismegistos** — `https://www.trismegistos.org/` metadata hub for ancient texts/people/places (Egypt & wider); APIs partly gated 🚩.
- **Epigraphic Database (EDH / EDR / EDCS — Clauss-Slaby)** — Roman inscriptions; EDCS searchable, EDH had open data (CC-BY) + bulk.
- **PHI Greek Inscriptions** (`epigraphy.packhum.org`) 🚩 — searchable, reuse terms restrictive.
- **iDAI (German Archaeological Institute)** — iDAI.gazetteer, iDAI.objects/Arachne (object DB), Linked Open Data, IIIF; CC licenses.
- **Coins:** **Nomisma.org** (Linked Open Data for numismatics, CC-BY) + **OCRE/CRRO** (Roman coinage) — great for material/economic detail.
- **Pleiades + Pelagios + Recogito** (above) for geography.
- **ToposText** — `topostext.org` places + ancient texts linked (CC-BY-ish).
- **DARE (Digital Atlas of the Roman Empire)** / **Pelagios maps**.
- **Open Context** — `opencontext.org` archaeology data publishing, APIs, CC-BY/CC0.
- **The Digital Loeb / Logeion** (lexica search) — Logeion is free reference (aggregates LSJ, Lewis & Short).
- **VERIFY:** License + API status per resource; Trismegistos/PHI are the most restricted 🚩.

---

# CATEGORY G — Cross-cutting / honorable mentions

- **OCLC WorldCat Search API** 🚩 — huge union catalog, but **key + (increasingly) paid/member-gated**; reuse terms restrictive.
- **CrossRef / OpenAlex / Semantic Scholar** — scholarly metadata (OpenAlex is **CC0**, excellent free API `api.openalex.org`); useful for citing real research within stories, author networks.
- **Open Library (Internet Archive)** — `https://openlibrary.org/` REST + bulk dumps; **CC0** bibliographic data; book covers; links to readable/borrowable texts. ⭐ open.
- **Project Gutenberg / Gutendex** — `https://gutendex.com/` JSON API over Gutenberg; PD full texts (overlaps with the public-domain-literature catalog #04).
- **Standard Ebooks** — PD/CC0 polished ebook editions; bulk via GitHub/OPDS.
- **MusicBrainz** — `https://musicbrainz.org/ws/2/` REST; **CC0 core data** (+ CC-BY-NC supplementary 🚩); music/artist relationships, useful for period soundtracks/culture.
- **TheGraph of GLAM via Wikidata** — most institutions above have a Wikidata property linking their IDs, so Wikidata can act as a federation hub across all of them.
- **rightsstatements.org / Creative Commons API** — to programmatically interpret the rights values returned by Europeana/DPLA/etc.
- **GBIF / iNaturalist / Catalogue of Life** — biodiversity (species, distributions); GBIF is **CC-BY/CC0**, great for flora/fauna realism in settings.
- **Geonames + OSM + Pleiades + TGN** together = a layered gazetteer stack (modern + ancient place names).

---

## Federation strategy note (for the platform)
1. **Wikidata is the spine.** Resolve any entity to a Q-ID, then fan out to VIAF, GND, Getty (ULAN/AAT/TGN), GeoNames, and museum IDs via Wikidata's external-ID properties — all CC0 to traverse.
2. **For images/objects:** prefer **CC0-first** APIs (Met, AIC, Smithsonian, Cleveland, Rijksmuseum PD, SMK, Paris Musées, Wellcome, NGA) to stay clean for commercial use; treat Europeana/DPLA/Trove as **per-item** (filter to open).
3. **For text:** Wikipedia (CC-BY-SA), PD encyclopedias (1911 Britannica, 1913 Catholic, 1906 Jewish), Perseus/OGL/Papyri (CC-BY/SA) for antiquity; avoid SEP/Britannica-modern/BabelNet/World History Encyclopedia for *redistribution* (read-only / NC) 🚩.
4. **Attribution-required but open:** Getty (ODC-BY), GeoNames (CC-BY), Pleiades (CC-BY) — build attribution into the data model from day one.

---

## Global VERIFY checklist (top priorities for the networked pass)
- Wikimedia REST base paths + new anonymous/token rate tiers (changing 2024–2025).
- VIAF + ISNI current reuse licenses (OCLC policy in flux 🚩).
- Europeana SPARQL still live? current `wskey` quota.
- British Library post-cyberattack service availability (2023 incident) 🚩.
- Per-museum image licenses: confirm CC0 vs NC vs restricted for Harvard, V&A, British Museum (NC?), Science Museum Group (NC 🚩), Brooklyn, Walters.
- Trove v3 commercial-use terms; Delpher (KB) API access policy.
- Getty download dataset paths + exact ODC-BY attribution string.
- Per-text NC flags in Perseus / OGL repos.
- BabelNet free-tier quota + confirm CC-BY-NC-SA 🚩.
- National-library API specifics for the breadth list (#30) — esp. Norway `api.nb.no`, Finland `finna.fi`, Poland Polona, Qatar Digital Library, NLI Israel, SMK Denmark.

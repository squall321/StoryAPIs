# Specialized Structured Knowledge for World-Building — Source Catalog

**Focus domain:** Specialized structured knowledge useful for world-building — events, people, places, things, sciences.

**Compiled:** 2026-06-20

---

## ⚠️ Verification status

> **IMPORTANT — read before relying on this document.** This catalog was compiled from established, well-documented knowledge of these sources (knowledge cutoff January 2026). In this run, **all network-capable tools (WebSearch, WebFetch, Bash/curl, PowerShell/Invoke-WebRequest) were denied**, so endpoints, rate limits, and licensing terms below **could not be live-verified for today's date (2026-06-20)**. Treat every entry as **"expected available, unverified"**.
>
> Each entry carries a confidence tag:
> - **[Stable]** — long-lived, institutionally maintained; very likely unchanged.
> - **[Verify]** — known to drift (pricing, hosting, paywalls, repo renames, uptime). Confirm before integrating.
>
> Before building on any of these, re-run a verification pass with network access enabled and confirm: (1) endpoint returns 2xx, (2) current rate limits, (3) current license, (4) whether a paid tier is now required.

---

## How to use this catalog

A "story source material" platform typically wants three layers:

1. **Hub knowledge graphs** (Wikidata, DBpedia, Wikipedia/MediaWiki, Wikimedia Commons) — one query surface for "give me all X related to Y" across every domain. Start here.
2. **Domain authorities** (GeoNames, GBIF, NASA, museum APIs, WALS, etc.) — deeper, cleaner, domain-specific data.
3. **Bulk dumps** — for a production platform, mirror the big sources (Wikidata, DBpedia, GeoNames, Natural Earth) into your own store so you are not beholden to public-endpoint rate limits.

Licensing watch-outs for a **commercial** platform: CC BY-SA imposes share-alike; CC BY-NC (e.g. BabelNet open data, many iNaturalist photos) blocks commercial use without a separate license; ODbL (OSM) has share-alike for derived databases. CC0 (Wikidata, Natural Earth, US-gov public domain) is the friendliest.

---

# 1. HUB KNOWLEDGE BASES (cross-domain backbone)

## Wikidata — Query Service (WDQS) [Stable]
- **URL / endpoint:** UI `https://query.wikidata.org/` · SPARQL `https://query.wikidata.org/sparql`
- **Covers:** ~115M+ structured items linking people, places, events, taxa, works, fictional entities, cross-referenced to nearly every other authority file (VIAF, GeoNames, Getty, etc.).
- **Access method:** SPARQL (GET/POST); federated SPARQL supported.
- **Data format:** JSON (`application/sparql-results+json`), XML, CSV, TSV; RDF for `CONSTRUCT`.
- **Auth:** No key. Descriptive `User-Agent` with contact required by policy.
- **Rate limits:** **60-second query timeout** per query; per-IP concurrency throttling (historically ~5 parallel / ~30/min on the shared endpoint). Scholarly-articles subgraph split to a separate endpoint.
- **License:** **CC0 1.0** (public domain).
- **Worldbuilding value:** The single best backbone for "all battles in a region," "all monarchs of a dynasty," "all deities tied to the sea."

## Wikidata — Entity Data / wbgetentities REST & Action API [Stable]
- **URL / endpoint:** Action `https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q42&format=json` · Linked Data `https://www.wikidata.org/wiki/Special:EntityData/Q42.json` (also `.rdf`, `.ttl`, `.nt`) · REST `https://www.wikidata.org/w/rest.php/wikibase/v1/`
- **Covers:** Full single-entity retrieval (labels, descriptions, statements, sitelinks) without writing SPARQL.
- **Access method:** REST.
- **Data format:** JSON; RDF/Turtle/N-Triples via EntityData.
- **Auth:** No for reads; OAuth for writes.
- **Rate limits:** Standard MediaWiki API limits; descriptive `User-Agent` required; EntityData URLs are CDN-cached (ideal for bulk single-item hydration).
- **License:** CC0 1.0.
- **Worldbuilding value:** Fast, cache-friendly way to hydrate one entity at a time inside an app.

## Wikidata — Bulk Dumps [Stable]
- **URL / endpoint:** `https://dumps.wikimedia.org/wikidatawiki/entities/` (`latest-all.json.gz`, `latest-all.ttl.gz`, `latest-all.nt.gz`)
- **Covers:** The entire knowledge base.
- **Access method:** Bulk download (HTTPS); mirrors available.
- **Data format:** JSON, Turtle, N-Triples (gzip/bzip2). Full JSON dump is tens of GB compressed.
- **Auth:** No.
- **Rate limits:** None beyond courtesy.
- **License:** CC0 1.0.
- **Worldbuilding value:** Load into your own triplestore/index so you are not bound by WDQS limits.

## Wikipedia / MediaWiki — REST & Action API [Stable]
- **URL / endpoint:** Summary (legacy) `https://en.wikipedia.org/api/rest_v1/page/summary/{title}` · Core REST `https://api.wikimedia.org/core/v1/wikipedia/en/page/{title}` · Action `https://en.wikipedia.org/w/api.php`
- **Covers:** Article text/HTML, summaries (extracts), media lists, links, search — all language editions.
- **Access method:** REST + Action (GET/POST).
- **Data format:** JSON (primary), HTML, XML (Action legacy).
- **Auth:** Anonymous allowed; free Wikimedia API portal account + OAuth raises limits.
- **Rate limits:** Anonymous via `api.wikimedia.org` historically ~**500 req/hour**; authenticated ~**5,000 req/hour**. Legacy `rest_v1`/Action allow higher volume with a good `User-Agent`.
- **License:** Text **CC BY-SA 4.0** (some GFDL); attribution required.
- **Worldbuilding value:** Instant prose summaries/full articles on any real-world topic to seed lore.

## Wikimedia "On this day" / Featured Feed API [Stable]
- **URL / endpoint:** `https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/{MM}/{DD}` · `/featured/{YYYY}/{MM}/{DD}`
- **Covers:** Historical events, births, deaths, holidays per calendar date; daily featured article/image/news.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No (account/token raises limits).
- **Rate limits:** Same tiers as the REST API above.
- **License:** CC BY-SA (text) / per-file media.
- **Worldbuilding value:** Generate "what happened on this day" timelines and in-world calendars/festivals.

## Wikimedia Enterprise API [Verify]
- **URL / endpoint:** `https://enterprise.wikimedia.com/` · API base `https://api.enterprise.wikimedia.com/`
- **Covers:** Commercial-grade high-volume structured snapshots + real-time change streams of all Wikimedia content ("Structured Contents" with parsed infoboxes/sections).
- **Access method:** REST + bulk snapshots + streaming.
- **Data format:** JSON / NDJSON.
- **Auth:** **Yes** — account + API key/OAuth. Paid tiers; a free trial / free account tier with a monthly quota exists for evaluation.
- **Rate limits:** Contract-defined; free tier capped.
- **License:** Underlying content CC BY-SA / CC0; commercial service agreement governs delivery/SLA.
- **Worldbuilding value:** If your platform scales, the supported way to ingest all Wikipedia/Wikidata without scraping.

## DBpedia — SPARQL Endpoint [Stable]
- **URL / endpoint:** `https://dbpedia.org/sparql` (Virtuoso) · faceted UI `https://dbpedia.org/fct/`
- **Covers:** Structured knowledge extracted from Wikipedia infoboxes/abstracts, richly typed via the DBpedia Ontology; multilingual.
- **Access method:** SPARQL (GET/POST).
- **Data format:** JSON, XML, CSV, RDF/Turtle, HTML.
- **Auth:** No.
- **Rate limits:** Virtuoso anonymous limits — typically **~10,000-row result cap**, **~120s** max query exec, per-IP connection throttling.
- **License:** **CC BY-SA 4.0** + GFDL.
- **Worldbuilding value:** Cleanly typed ontology (`dbo:Castle`, `dbo:MythologicalFigure`) makes category-driven queries easy.

## DBpedia — Spotlight (entity linking) [Verify]
- **URL / endpoint:** Public demo historically `https://api.dbpedia-spotlight.org/en/annotate` (+ `/disambiguate`); self-hosted Docker recommended.
- **Covers:** Named-entity recognition + linking of free text to DBpedia/Wikipedia resources.
- **Access method:** REST.
- **Data format:** JSON, XML.
- **Auth:** No.
- **Rate limits:** Public instance is best-effort and often unstable — **self-host for production**.
- **License:** Apache 2.0 (software); data CC BY-SA.
- **Worldbuilding value:** Auto-tag user-written lore and link it to real-world reference entities.

## DBpedia — Dumps / Databus [Stable]
- **URL / endpoint:** `https://databus.dbpedia.org/` · `https://www.dbpedia.org/resources/`
- **Covers:** Full RDF dumps (mappings, infobox properties, abstracts, links).
- **Access method:** Bulk download.
- **Data format:** RDF/Turtle, N-Triples (compressed).
- **Auth:** No (Databus account optional for publishing).
- **License:** CC BY-SA.
- **Worldbuilding value:** Self-host a typed knowledge graph for offline, rate-limit-free querying.

## Wikimedia Commons — Media API [Stable]
- **URL / endpoint:** `https://commons.wikimedia.org/w/api.php` · structured data `https://api.wikimedia.org/core/v1/commons/` · file metadata module `action=query&prop=imageinfo`
- **Covers:** ~100M+ freely licensed images, audio, video, maps; Structured Data on Commons; category trees.
- **Access method:** REST + Action API.
- **Data format:** JSON; media in native formats (JPG/PNG/SVG/OGG/WEBM).
- **Auth:** No for reads; account/OAuth raises limits.
- **Rate limits:** Standard MediaWiki limits; `User-Agent` required. Use `imageinfo` + `iiurlwidth` for thumbnails.
- **License:** Mixed but **all free** — CC0/CC BY/CC BY-SA/public domain; **per-file attribution required** (machine-readable).
- **Worldbuilding value:** Massive royalty-free image bank for moodboards, reference art, maps, heraldry.

## YAGO [Verify]
- **URL / endpoint:** `https://yago-knowledge.org/sparql` · downloads at the same site.
- **Covers:** Wikidata + schema.org-derived knowledge graph with a clean, consistent taxonomy.
- **Access method:** SPARQL + bulk download.
- **Data format:** RDF/Turtle, N-Triples; SPARQL JSON/XML.
- **Auth:** No.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** A cleaner-typed alternative to DBpedia for category-driven queries.

## ConceptNet 5 [Stable]
- **URL / endpoint:** `https://api.conceptnet.io/` (e.g. `/c/en/dragon`)
- **Covers:** ~34M+ commonsense semantic relations (IsA, UsedFor, AtLocation, HasProperty) across many languages.
- **Access method:** REST (also full DB dump + Postgres build).
- **Data format:** JSON-LD.
- **Auth:** No.
- **Rate limits:** Public API ~**1 req/sec** (~3,600/hr) — self-host for volume.
- **License:** **CC BY-SA 4.0** (some components CC BY).
- **Worldbuilding value:** Generate plausible associations — what a "blacksmith" uses, where a "swamp" is found — to flesh out world logic.

## WordNet (Princeton / Open English WordNet) [Stable]
- **URL / endpoint:** `https://wordnet.princeton.edu/download` · Open English WordNet `https://en-word.net/`. No canonical official REST API; use local libs (NLTK, `wn`).
- **Covers:** English lexical DB: synsets, hypernym/hyponym hierarchies, meronyms, antonyms, glosses.
- **Access method:** Bulk download / local library.
- **Data format:** WNDB flat files; Open English WordNet ships RDF & XML/LMF.
- **Auth:** No.
- **License:** Princeton WordNet license (permissive, BSD-like); **Open English WordNet CC BY 4.0**.
- **Worldbuilding value:** Controlled vocabularies, synonym expansion, "kinds of creature/plant" trees.

## BabelNet [Verify — commercial license caveat]
- **URL / endpoint:** `https://babelnet.org/` · HTTP API `https://babelnet.io/v9/` · SPARQL + RDF + Java API.
- **Covers:** Large multilingual encyclopedic dictionary + semantic network merging WordNet, Wikipedia, Wikidata, Wiktionary (500+ languages).
- **Access method:** REST, SPARQL, Java API, bulk indices.
- **Data format:** JSON; RDF/Turtle.
- **Auth:** **Yes** — free registration gives an API key with a daily quota (historically ~1,000 "Babelcoins"/day, ~1 coin/request).
- **Rate limits:** Daily Babelcoin budget; resets daily.
- **License:** **CC BY-NC-SA 4.0** (non-commercial) for open data — **commercial use needs a separate license**.
- **Worldbuilding value:** Best multilingual concept layer — but watch the NC license for a paid product.

## Getty Vocabularies — AAT / ULAN / TGN (Linked Open Data) [Stable]
- **URL / endpoint:** SPARQL `https://vocab.getty.edu/sparql` · resolvable URIs `https://vocab.getty.edu/aat/{id}`, `/ulan/{id}`, `/tgn/{id}` · bulk downloads at `http://vocab.getty.edu/`
- **Covers:** Controlled vocabularies for art/architecture concepts & styles (AAT), artists/makers (ULAN), and **historical & current place names incl. obsolete ones** (TGN).
- **Access method:** SPARQL + resolvable Linked Data + bulk download.
- **Data format:** RDF, JSON-LD, Turtle, N-Triples; SPARQL JSON/XML/CSV.
- **Auth:** No.
- **License:** **ODC-BY 1.0** (attribution; commercial OK).
- **Worldbuilding value:** Period-correct terminology for objects, art styles, materials, and historical place names.

## Library of Congress Linked Data Service (id.loc.gov) [Stable]
- **URL / endpoint:** `https://id.loc.gov/`
- **Covers:** LCSH subject headings, name authorities, genre/form terms, MARC code lists.
- **Access method:** Resolvable Linked Data + bulk download; content negotiation.
- **Data format:** RDF/XML, Turtle, JSON-LD, N-Triples.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** A strong general subject taxonomy for organizing in-world topics.

## Schema.org [Stable]
- **URL / endpoint:** `https://schema.org/` · vocab `https://schema.org/version/latest/schemaorg-current-https.jsonld` (also `.ttl`, `.nt`, `.rdf`, `.csv`)
- **Covers:** Shared vocabulary/type system (CreativeWork, Person, Place, Event…). A modeling standard, not a data source.
- **Access method:** Bulk download; used as a JSON-LD `@context`.
- **Data format:** JSON-LD, Turtle, RDF/XML, N-Triples, CSV.
- **Auth:** No.
- **License:** Vocabulary **CC BY-SA 4.0**.
- **Worldbuilding value:** The schema to model **your own** world-building data so it interoperates with Wikidata/DBpedia.

---

# 2. HISTORICAL EVENTS & TIMELINES

## Wikidata events (via SPARQL) [Stable]
- **URL / endpoint:** `https://query.wikidata.org/sparql` (query items with `point in time` P585 / `start time` P580 / `end time` P582, or class `occurrence`/`event`).
- **Covers:** Battles, treaties, disasters, coronations, discoveries — anything modeled as an event, with dates, locations, participants.
- **Access method:** SPARQL.
- **Data format:** JSON/CSV/XML/TSV.
- **Auth:** No.
- **Rate limits:** 60s query timeout.
- **License:** CC0 1.0.
- **Worldbuilding value:** Build queryable historical timelines filtered by place, era, or theme.

## EventKG [Verify]
- **URL / endpoint:** `http://eventkg.l3s.uni-hannover.de/` · SPARQL + RDF dumps.
- **Covers:** A multilingual event-centric knowledge graph (~1M+ events, ~3M+ relations) integrating Wikidata, DBpedia, YAGO, Wikipedia, and Wikipedia "current events."
- **Access method:** SPARQL + bulk RDF download.
- **Data format:** RDF/Turtle/N-Triples.
- **Auth:** No.
- **License:** CC BY 4.0 (per dataset components).
- **Worldbuilding value:** Pre-built event graph with temporal/relational structure — saves building timelines from scratch. *(Academic project; verify uptime.)*

## Wikimedia "On this day" feed (see Hub section) [Stable]
- Cross-listed; `https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/{MM}/{DD}`. JSON, CC BY-SA. Quickest path to date-keyed historical events.

## byabbe.se "On This Day" API [Verify]
- **URL / endpoint:** `https://byabbe.se/on-this-day/{month}/{day}/events.json` (also `/births.json`, `/deaths.json`).
- **Covers:** Wikipedia-sourced historical events/births/deaths per calendar date.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No.
- **Rate limits:** None published (courtesy use).
- **License:** Data derived from Wikipedia (CC BY-SA).
- **Worldbuilding value:** A dead-simple, no-key endpoint for "this day in history" widgets. *(Third-party hobby project — verify it is still hosted.)*

## Histropedia [Verify]
- **URL / endpoint:** `https://www.histropedia.com/` — a visual timeline product built on Wikidata.
- **Covers:** Interactive visual timelines of historical figures and events.
- **Access method:** Web app; **no documented public API** — it is a consumer of Wikidata, not a data API. For data, query Wikidata directly.
- **Data format:** N/A (web UI).
- **Auth:** N/A.
- **License:** Underlying data from Wikidata (CC0).
- **Worldbuilding value:** Inspiration/visualization reference; pull the underlying facts from Wikidata instead.

## Chronas [Verify]
- **URL / endpoint:** `https://chronas.org/` · API historically `https://chronas.org/en/app/datalayer/...`
- **Covers:** Interactive historical world map + linked data (political entities, rulers, battles, cultures over time, 2000 BCE→present).
- **Access method:** Web app with a backing API; open-source on GitHub.
- **Data format:** JSON / GeoJSON.
- **Auth:** No (for public data).
- **License:** Open-source (code); data from Wikipedia/Wikidata (CC BY-SA / CC0).
- **Worldbuilding value:** Excellent for visualizing shifting borders/empires over time — a great mental model for fictional geopolitics. *(Verify current hosting/API.)*

---

# 3. GEOGRAPHY, PLACES & MAPS

## GeoNames API [Stable]
- **URL / endpoint:** `http://api.geonames.org/` (e.g. `/searchJSON`, `/findNearbyJSON`, `/countryInfoJSON`).
- **Covers:** ~12M+ place names worldwide — cities, features, admin divisions, populations, elevations, timezones, alternate/historical names.
- **Access method:** REST; also full bulk download at `https://download.geonames.org/export/dump/`.
- **Data format:** JSON, XML, RDF; bulk as tab-delimited text.
- **Auth:** **Free account/username required** (passed as `&username=`).
- **Rate limits:** Credit-based per username — historically **~20,000 credits/day** and ~1,000/hour (different calls cost different credits). Bulk dump for heavy use.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** Real toponymy + feature data to ground invented geographies, or mine for naming patterns.

## OpenStreetMap — Overpass API [Stable]
- **URL / endpoint:** `https://overpass-api.de/api/interpreter` (public instance; others mirror it).
- **Covers:** Query the full OSM database — roads, buildings, natural features, POIs, boundaries — by tag/area.
- **Access method:** REST with Overpass QL queries.
- **Data format:** JSON, XML, CSV (via `out` options).
- **Auth:** No.
- **Rate limits:** Public instance is shared; fair-use with timeouts; heavy users should self-host or use a paid mirror.
- **License:** **ODbL 1.0** (share-alike for derived databases — relevant for commercial use).
- **Worldbuilding value:** Extract real street/feature layouts to model realistic settlements or seed map generators.

## OpenStreetMap — Nominatim (geocoding) [Stable]
- **URL / endpoint:** `https://nominatim.openstreetmap.org/search` · `/reverse`
- **Covers:** Forward/reverse geocoding (place name ↔ coordinates) over OSM data.
- **Access method:** REST.
- **Data format:** JSON, JSONv2, XML, GeoJSON.
- **Auth:** No.
- **Rate limits:** **Max 1 request/second** on the public instance; bulk geocoding prohibited (self-host for volume); `User-Agent`/referer required.
- **License:** ODbL.
- **Worldbuilding value:** Resolve real places to coordinates for map-anchored stories.

## Natural Earth [Stable]
- **URL / endpoint:** `https://www.naturalearthdata.com/downloads/`
- **Covers:** Curated public-domain vector + raster map data at 1:10m / 1:50m / 1:110m — countries, states, coastlines, rivers, lakes, roads, populated places, physical labels.
- **Access method:** Bulk download.
- **Data format:** Shapefile, GeoPackage, GeoJSON (via mirrors), raster (TIFF).
- **Auth:** No.
- **Rate limits:** N/A.
- **License:** **Public domain** (no attribution required).
- **Worldbuilding value:** The friendliest base-map dataset for rendering fictional-but-plausible world maps.

## Pleiades (ancient world gazetteer) [Stable]
- **URL / endpoint:** `https://pleiades.stoa.org/` · per-place JSON at `{place-url}/json` · bulk dumps available.
- **Covers:** ~40,000+ ancient (Greek/Roman + broader antiquity) places, names, locations, time periods.
- **Access method:** REST (per-resource JSON), bulk download; resolvable URIs.
- **Data format:** JSON, CSV, KML, RDF/Turtle.
- **Auth:** No.
- **Rate limits:** Courtesy.
- **License:** **CC BY 3.0**.
- **Worldbuilding value:** Authentic ancient place names and locations for classical/antiquity-flavored settings.

## World Historical Gazetteer (WHG) [Verify]
- **URL / endpoint:** `https://whgazetteer.org/` · API `https://whgazetteer.org/api/`
- **Covers:** Historical place names linked across time/space, with temporal attestations; reconciliation service.
- **Access method:** REST API; bulk via the site.
- **Data format:** JSON / GeoJSON (Linked Places format).
- **Auth:** Account needed for some upload/reconciliation features; read access open.
- **Rate limits:** Courtesy.
- **License:** CC BY 4.0 (per-dataset varies).
- **Worldbuilding value:** Tracks how place names changed over history — perfect for evolving fictional toponymy.

## Who's On First (gazetteer) [Stable]
- **URL / endpoint:** `https://whosonfirst.org/` · data on GitHub / via the Geocode Earth / spatial.io tooling.
- **Covers:** ~26M+ places with stable IDs, hierarchies, alternate names, geometries, and historical/ceased flags.
- **Access method:** Bulk download (GeoJSON per record); SQLite bundles.
- **Data format:** GeoJSON, SQLite.
- **Auth:** No.
- **License:** **CC0** (data) — note some geometry provenance has separate terms.
- **Worldbuilding value:** A clean, ID-stable gazetteer to model an in-world place hierarchy.

## GADM (administrative boundaries) [Stable]
- **URL / endpoint:** `https://gadm.org/download_country.html`
- **Covers:** Detailed administrative-area boundaries (country → sub-national levels) for every country.
- **Access method:** Bulk download.
- **Data format:** GeoPackage, Shapefile, GeoJSON, R formats.
- **Auth:** No.
- **License:** **Free for academic/non-commercial use; commercial use requires permission.** (Watch this for a paid platform.)
- **Worldbuilding value:** Real administrative geometry to model provinces/regions; **check license before commercial use.**

## REST Countries [Verify]
- **URL / endpoint:** `https://restcountries.com/v3.1/all` (and `/name/{n}`, `/region/{r}`).
- **Covers:** Country metadata — names, capitals, regions, populations, currencies, languages, flags (SVG/PNG), borders, lat/long.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No.
- **Rate limits:** None published (community-hosted — verify uptime/host).
- **License:** Mozilla Public License (project); data is factual/public.
- **Worldbuilding value:** Quick "real-country template" data when designing fictional nations and their attributes.

---

# 4. PEOPLE & BIOGRAPHY

## Wikidata people (via SPARQL) [Stable]
- **URL / endpoint:** `https://query.wikidata.org/sparql` (`?p wdt:P31 wd:Q5` for humans, with occupation/dates/places).
- **Covers:** Millions of real people with birth/death dates, places, occupations, relations, and cross-links to VIAF/DBpedia/etc.
- **Access method:** SPARQL.
- **Data format:** JSON/CSV/XML.
- **Auth:** No.
- **License:** CC0 1.0.
- **Worldbuilding value:** Mine biographical patterns (titles, life events, family structures) for plausible character backstories.

## VIAF — Virtual International Authority File [Stable]
- **URL / endpoint:** `https://viaf.org/` · per-record `https://viaf.org/viaf/{id}/` (append `/justlinks.json`, `/viaf.json`) · AutoSuggest `https://viaf.org/viaf/AutoSuggest?query=`
- **Covers:** Consolidated authority records for persons/orgs across the world's national libraries — name variants, dates, identifiers.
- **Access method:** REST; bulk data dumps.
- **Data format:** JSON, XML/MARC, RDF.
- **Auth:** No.
- **Rate limits:** Courtesy.
- **License:** ODC-BY-style / open (OCLC terms).
- **Worldbuilding value:** Canonical name-variant data for real historical figures — great for reconciling/standardizing names.

## DBpedia persons [Stable]
- **URL / endpoint:** `https://dbpedia.org/sparql` (type `dbo:Person`).
- **Covers:** People extracted from Wikipedia with typed properties (birthDate, birthPlace, occupation).
- **Access method:** SPARQL.
- **Data format:** JSON/XML/RDF.
- **Auth:** No.
- **License:** CC BY-SA 4.0.
- **Worldbuilding value:** Typed person data for structured biographical queries.

## WikiTree API [Verify]
- **URL / endpoint:** `https://api.wikitree.com/api.php`
- **Covers:** Community single-family-tree genealogy — profiles, relationships, ancestry/descendancy.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No for public profiles; login token for private/watchlist data.
- **Rate limits:** Fair-use; documented usage guidelines.
- **License:** Profile data shared under CC BY-SA; respect privacy of living people.
- **Worldbuilding value:** Study real family-tree structures and naming inheritance to build believable lineages and houses.

## FamilySearch API [Verify — approval required]
- **URL / endpoint:** `https://www.familysearch.org/developers/` · API base `https://api.familysearch.org/`
- **Covers:** Vast genealogical records, family trees, historical vital records.
- **Access method:** REST (GEDCOM X model), OAuth2.
- **Data format:** JSON (GEDCOM X), XML.
- **Auth:** **Yes** — developer registration + OAuth; **app review/approval required.**
- **Rate limits:** Per-app throttling.
- **License:** Restrictive partner terms; not open data.
- **Worldbuilding value:** Deep genealogical structure reference — but heavy access barriers; use for modeling patterns, not bulk pull.

## Open Library — Authors [Stable]
- **URL / endpoint:** `https://openlibrary.org/authors/{id}.json` · search `https://openlibrary.org/search/authors.json?q=`
- **Covers:** Author records — names, dates, works, bios.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No.
- **License:** **CC0** (data).
- **Worldbuilding value:** Author personas/bibliographies to populate in-world libraries and writer characters.

## Find A Grave [Verify — scraping caveat]
- **URL / endpoint:** `https://www.findagrave.com/` — **no official public API**; access is by scraping (against ToS) or partner agreements.
- **Covers:** ~200M+ memorial records — names, dates, burial locations, epitaphs.
- **Access method:** Web scraping only (discouraged); some data mirrored to Wikidata/Wikitree.
- **Auth:** N/A.
- **License:** Proprietary (Ancestry-owned); **do not scrape for a product.**
- **Worldbuilding value:** Epitaph/naming inspiration — but no clean legal data path. Prefer Wikidata for death/burial facts.

---

# 5. NAMING & ETYMOLOGY

## Behind the Name [Verify — API status]
- **URL / endpoint:** `https://www.behindthename.com/` · API historically `https://www.behindthename.com/api/` (`lookup.json`, `random.json`).
- **Covers:** Given-name meanings, origins, etymologies, usage by culture; also a surname sister-site (surnames.behindthename.com).
- **Access method:** REST API (key-gated) **historically existed** — **verify it is still offered**; otherwise the site is the reference.
- **Data format:** JSON/XML.
- **Auth:** **API key required** (free key historically available on request).
- **Rate limits:** Historically modest daily caps per key.
- **License:** Proprietary content; API terms restrict redistribution. **Confirm current terms before integrating.**
- **Worldbuilding value:** The classic resource for authentic name meanings/origins to ground character naming.

## US SSA Baby Names dataset [Stable]
- **URL / endpoint:** `https://www.ssa.gov/oact/babynames/limits.html` (national + state files).
- **Covers:** US given-name frequencies by year and sex, 1880→present.
- **Access method:** Bulk download.
- **Data format:** Zipped fixed/CSV text.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Real popularity-over-time curves to pick era-appropriate names or model naming fashions.

## US Census surname data [Stable]
- **URL / endpoint:** `https://www.census.gov/topics/population/genealogy/data/2010_surnames.html` (also 2000, 1990).
- **Covers:** Frequency and demographic breakdown of US surnames (~160k+ names above threshold).
- **Access method:** Bulk download.
- **Data format:** CSV/XLSX.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Real surname frequency tables for plausible family-name distributions.

## Forebears.io [Verify]
- **URL / endpoint:** `https://forebears.io/` — surname/forename frequency & distribution by country.
- **Covers:** Global surname/forename incidence and geographic distribution.
- **Access method:** Web UI; **API is commercial/contact-based** (no open public API).
- **Data format:** N/A (UI) / licensed data.
- **Auth:** Commercial license.
- **License:** Proprietary.
- **Worldbuilding value:** Best for global surname-geography research — but not free/open for integration.

## Wiktionary / Wiktextract (Kaikki.org) [Stable]
- **URL / endpoint:** `https://kaikki.org/dictionary/` (Wiktextract data) · Wiktionary API `https://en.wiktionary.org/w/api.php`
- **Covers:** Machine-readable extraction of Wiktionary — definitions, **etymologies**, pronunciations (IPA), translations, inflections, for hundreds of languages.
- **Access method:** Bulk download (JSONL) from Kaikki; live API via MediaWiki.
- **Data format:** JSON / JSONL; wikitext/HTML via API.
- **Auth:** No.
- **Rate limits:** Standard MediaWiki limits (live); none for bulk.
- **License:** **CC BY-SA 4.0** (+ GFDL).
- **Worldbuilding value:** The richest open source of real etymologies and phonology — ideal for building etymologically-plausible conlang/place/character names.

## Wikidata Lexemes [Stable]
- **URL / endpoint:** `https://query.wikidata.org/sparql` (lexeme namespace) · `https://www.wikidata.org/wiki/Lexeme:L1`
- **Covers:** Structured lexemes — forms, senses, grammatical features, language links, etymological relations.
- **Access method:** SPARQL + Entity Data.
- **Data format:** JSON/RDF.
- **Auth:** No.
- **License:** CC0 1.0.
- **Worldbuilding value:** CC0 structured word data — the cleanest-licensed lexical source for derivation logic.

## Online Etymology Dictionary (etymonline) [Verify — no API]
- **URL / endpoint:** `https://www.etymonline.com/`
- **Covers:** Etymologies/word histories for English vocabulary.
- **Access method:** Web UI only — **no official public API**; scraping is against ToS.
- **Data format:** N/A.
- **Auth:** N/A.
- **License:** Proprietary.
- **Worldbuilding value:** Excellent human reference for word origins; for programmatic etymology use Wiktextract instead.

---

# 6. MATERIAL CULTURE (weapons, armor, costume, food, currency, heraldry, ships)

> **Strategy:** Museum open-access APIs are the gold mine here — rich object metadata + high-res imagery, mostly CC0 or open. Combine with Wikidata categories for cross-museum coverage.

## The Metropolitan Museum of Art — Open Access API [Stable]
- **URL / endpoint:** `https://collectionapi.metmuseum.org/public/collection/v1/objects` · `/objects/{id}` · `/search?q=`
- **Covers:** ~470k+ objects incl. **Arms and Armor** and **Costume Institute** departments — full metadata + images; large share are CC0.
- **Access method:** REST.
- **Data format:** JSON; images via URLs.
- **Auth:** No key.
- **Rate limits:** ~**80 requests/second** suggested ceiling (be courteous).
- **License:** Metadata CC0; many images CC0 / public domain (per-object "isPublicDomain" flag).
- **Worldbuilding value:** Authentic weapons, armor, and historical costume with imagery — directly reusable reference for material culture.

## Rijksmuseum API [Verify — key]
- **URL / endpoint:** `https://www.rijksmuseum.nl/api/en/collection` (key as `?key=`).
- **Covers:** ~700k+ objects (Dutch/European art, arms, decorative arts, ship models, costume) with very high-res imagery.
- **Access method:** REST (and OAI-PMH harvest).
- **Data format:** JSON, XML.
- **Auth:** **Free API key** (register via Rijksstudio).
- **Rate limits:** ~10,000 requests/day historically.
- **License:** Public-domain images CC0; metadata open.
- **Worldbuilding value:** Superb high-res reference for historical objects, ships, and dress.

## Victoria & Albert Museum (V&A) API [Stable]
- **URL / endpoint:** `https://api.vam.ac.uk/v2/objects/search` · `/object/{id}`
- **Covers:** ~1.2M+ records — **fashion/costume**, textiles, metalwork, arms, decorative arts, design.
- **Access method:** REST.
- **Data format:** JSON; IIIF image URLs.
- **Auth:** No key.
- **Rate limits:** Courtesy/fair-use.
- **License:** Metadata CC BY (open); image rights vary per object.
- **Worldbuilding value:** Premier source for fashion/costume history and decorative material culture.

## Smithsonian Open Access API [Verify — key]
- **URL / endpoint:** `https://api.si.edu/openaccess/api/v1.0/search` (key via api.data.gov).
- **Covers:** ~5M+ items across 19 museums (incl. military history, costume, transport) — ~4M+ CC0 images.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** **Free api.data.gov key.**
- **Rate limits:** ~1,000 req/hour (api.data.gov default).
- **License:** **CC0** for designated open-access content.
- **Worldbuilding value:** Huge CC0 cross-domain object + image trove for any material-culture need.

## Europeana API [Verify — key]
- **URL / endpoint:** `https://api.europeana.eu/record/v2/search.json` (key as `&wskey=`).
- **Covers:** ~50M+ cultural-heritage items from thousands of European institutions — arms, costume, manuscripts, maps, ships.
- **Access method:** REST.
- **Data format:** JSON, JSON-LD.
- **Auth:** **Free API key.**
- **Rate limits:** ~10,000 req/day historically.
- **License:** Metadata CC0; per-item rights flagged (many open).
- **Worldbuilding value:** The broadest aggregator of European material culture imagery/metadata.

## Harvard Art Museums API [Verify — key]
- **URL / endpoint:** `https://api.harvardartmuseums.org/object` (key as `?apikey=`).
- **Covers:** ~250k+ objects with rich metadata (colors, classifications, periods, cultures).
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** **Free API key.**
- **Rate limits:** ~2,500 req/day historically.
- **License:** Metadata open (CC0-ish); image rights vary.
- **Worldbuilding value:** Unusually rich structured metadata (color palettes, materials) for object reference.

## Cleveland Museum of Art — Open Access API [Stable]
- **URL / endpoint:** `https://openaccess-api.clevelandart.org/api/artworks/`
- **Covers:** ~60k+ objects; ~30k+ CC0 images.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No key.
- **License:** **CC0** for open-access works.
- **Worldbuilding value:** No-key, CC0 object/image source — easiest museum API to integrate.

## Art Institute of Chicago API [Stable]
- **URL / endpoint:** `https://api.artic.edu/api/v1/artworks`
- **Covers:** ~120k+ objects with IIIF imagery and structured metadata.
- **Access method:** REST.
- **Data format:** JSON; IIIF images.
- **Auth:** No key.
- **License:** CC0 metadata; many public-domain images.
- **Worldbuilding value:** Clean, modern, no-key API for art/object reference.

## Nomisma.org (numismatics Linked Data) [Stable]
- **URL / endpoint:** `https://nomisma.org/` · SPARQL `https://nomisma.org/query`
- **Covers:** Linked-data vocabulary + datasets for ancient/historical coinage — mints, denominations, rulers, materials, hoards.
- **Access method:** SPARQL + resolvable URIs + RDF dumps.
- **Data format:** RDF/Turtle, JSON-LD; SPARQL JSON/XML.
- **Auth:** No.
- **License:** CC BY (varies by contributing dataset).
- **Worldbuilding value:** Authentic coinage/currency concepts (denominations, mints, metals) for in-world economies.

## American Numismatic Society — OCRE / collection [Stable]
- **URL / endpoint:** `http://numismatics.org/ocre/` (Online Coins of the Roman Empire) and related (CRRO, PELLA); collection API at `http://numismatics.org/search/apis`.
- **Covers:** Detailed catalogs of Roman/Greek coinage tied to Nomisma vocabulary, with imagery.
- **Access method:** REST/SPARQL; data export.
- **Data format:** JSON, RDF, CSV.
- **Auth:** No.
- **License:** CC BY (open).
- **Worldbuilding value:** Concrete coin types, legends, and imagery to design believable currency.

## flagcdn / FlagsAPI (flag images) [Verify]
- **URL / endpoint:** `https://flagcdn.com/{code}.svg` (and sized PNGs) · alt `https://flagsapi.com/`
- **Covers:** National (and some subnational) flag images by ISO code.
- **Access method:** REST (image URLs).
- **Data format:** SVG, PNG.
- **Auth:** No.
- **Rate limits:** Courtesy (CDN).
- **License:** Public-domain flag designs; service terms permissive.
- **Worldbuilding value:** Instant flag imagery; study designs to inform fictional vexillology.

## REST Countries — flags (see Geography) [Verify]
- Cross-listed; `https://restcountries.com/v3.1/all` returns flag SVG/PNG URLs + country metadata. JSON, no key.

## Wikimedia Commons — heraldry/flags categories [Stable]
- **URL / endpoint:** `https://commons.wikimedia.org/w/api.php` (query categories like "Coats of arms", "Flags by country").
- **Covers:** Tens of thousands of coats of arms, flags, blazons, seals — mostly SVG, freely licensed.
- **Access method:** REST/Action API.
- **Data format:** JSON metadata; SVG/PNG media.
- **Auth:** No.
- **License:** Free (CC0/CC BY/CC BY-SA/PD per file).
- **Worldbuilding value:** Vast free heraldry/vexillology image bank to study and adapt for fictional houses/nations.

## TheMealDB [Verify]
- **URL / endpoint:** `https://www.themealdb.com/api/json/v1/1/search.php?s=`
- **Covers:** Recipes by name/category/area/ingredient with images; cuisine tagging.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** Test key `1`; supporter key for premium endpoints.
- **Rate limits:** Courtesy.
- **License:** Free for educational/non-commercial; check terms for commercial.
- **Worldbuilding value:** Cuisine/ingredient patterns by region to design culturally-grounded fictional food.

---

# 7. SCIENCE (for grounding sci-fi & fantasy)

## NASA Open APIs (api.nasa.gov) [Stable]
- **URL / endpoint:** `https://api.nasa.gov` — APOD `/planetary/apod`, NeoWs `/neo/rest/v1/feed`, Mars Photos `/mars-photos/api/v1/rovers/{rover}/photos`, EPIC, NASA Image Library.
- **Covers:** Astronomy Picture of the Day, near-Earth asteroids, Mars rover imagery, Earth imagery.
- **Access method:** REST.
- **Data format:** JSON; image URLs.
- **Auth:** **API key** (free `DEMO_KEY` for testing).
- **Rate limits:** `DEMO_KEY` ~30/hour, 50/day per IP; registered key ~**1,000 req/hour**.
- **License:** NASA content generally public domain (some embedded third-party media excepted).
- **Worldbuilding value:** Real asteroid orbits, daily cosmic imagery, authentic Mars surface photos to ground sci-fi.

## NASA Exoplanet Archive (TAP) [Stable]
- **URL / endpoint:** `https://exoplanetarchive.ipac.caltech.edu/TAP/sync` (ADQL). (Legacy `nph-nstedAPI` deprecated → TAP.)
- **Covers:** Confirmed/candidate exoplanets + host-star parameters (mass, radius, temperature, distance).
- **Access method:** TAP/ADQL (sync + async).
- **Data format:** VOTable, CSV, JSON, TSV.
- **Auth:** No.
- **Rate limits:** None published; fair-use; async for big queries.
- **License:** Public; citation requested.
- **Worldbuilding value:** Real catalog of habitable-zone planets and their stars for plausible alien worlds.

## SIMBAD Astronomical Database [Stable]
- **URL / endpoint:** `https://simbad.cds.unistra.fr/simbad/` · TAP `/simbad/sim-tap`
- **Covers:** Identifiers, coordinates, bibliography for millions of stars/objects beyond the solar system.
- **Access method:** TAP/ADQL, scriptable query, VO services.
- **Data format:** VOTable, ASCII, JSON.
- **Auth:** No.
- **Rate limits:** Fair-use; throttling on heavy scripted hits.
- **License:** **CC BY 4.0** (CDS); citation required.
- **Worldbuilding value:** Authentic named stars + catalog IDs for naming and placing fictional systems.

## ESA Gaia Archive [Stable]
- **URL / endpoint:** `https://gea.esac.esa.int/archive/` · TAP `https://gea.esac.esa.int/tap-server/tap`
- **Covers:** Astrometry, parallax/distance, photometry for ~2 billion stars (DR3; DR4 expected this era).
- **Access method:** TAP/ADQL (sync + async), bulk download.
- **Data format:** VOTable, CSV, FITS.
- **Auth:** Anonymous allowed; free account for large async jobs.
- **Rate limits:** Anonymous job/row caps; higher when logged in.
- **License:** Open; ESA/Gaia citation.
- **Worldbuilding value:** Precise 3D stellar positions/distances to build a realistic galactic neighborhood.

## HYG / ATHYG Stellar Database [Verify — repo renamed]
- **URL / endpoint:** GitHub `https://github.com/astronexus/HYG-Database` (note: reorganized toward an **ATHYG** dataset — verify current repo name).
- **Covers:** ~120k nearby/bright stars with XYZ coords, magnitude, spectral type, common names (merges Hipparcos, Yale BSC, Gliese).
- **Access method:** Bulk download (Git/CSV).
- **Data format:** CSV.
- **Auth:** No.
- **License:** **CC BY-SA 2.5/4.0** (per repo).
- **Worldbuilding value:** Ready-made 3D star map with real names — ideal for plotting interstellar travel.

## Open Exoplanet Catalogue [Verify — staleness]
- **URL / endpoint:** `https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue` · `https://www.openexoplanetcatalogue.com`
- **Covers:** Community catalog of exoplanets/host systems in structured XML (binary stars + planets).
- **Access method:** Bulk download (Git).
- **Data format:** XML (one file per system).
- **Auth:** No.
- **License:** MIT / open.
- **Worldbuilding value:** Hierarchical system data for designing exotic systems. *(Update cadence has slowed — may be stale.)*

## JPL Horizons & SSD/CNEOS APIs [Stable]
- **URL / endpoint:** Horizons `https://ssd.jpl.nasa.gov/api/horizons.api` · SBDB `https://ssd-api.jpl.nasa.gov/sbdb.api` · close-approach `/cad.api` · fireball `/fireball.api`
- **Covers:** High-precision ephemerides (planets, moons, asteroids, comets, spacecraft); small-body orbits/physical params; Earth close approaches; observed fireballs.
- **Access method:** REST.
- **Data format:** JSON, text.
- **Auth:** No key.
- **Rate limits:** Fair-use.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Compute real positions of solar-system bodies at any date for hard-SF accuracy; impact/close-approach data for disaster plots.

## GBIF — Global Biodiversity Information Facility [Stable]
- **URL / endpoint:** `https://api.gbif.org/v1/` (`/occurrence/search`, `/species`).
- **Covers:** ~2B+ species occurrence records, taxonomic backbone, distributions.
- **Access method:** REST; bulk via async download API.
- **Data format:** JSON (API); Darwin Core Archive / CSV (downloads).
- **Auth:** None for search; free account to request bulk downloads.
- **Rate limits:** No hard published limit; fair-use; downloads queued.
- **License:** Records CC0/CC BY/CC BY-NC per dataset; cite the download DOI.
- **Worldbuilding value:** Where any real species actually lives — build biome-accurate ecosystems.

## Encyclopedia of Life (EOL) [Verify — uptime]
- **URL / endpoint:** `https://eol.org/api` (`/api/pages/1.0`, `/api/search/1.0`); TraitBank.
- **Covers:** Species pages, descriptions, media, and structured traits (TraitBank).
- **Access method:** REST; TraitBank query.
- **Data format:** JSON, XML.
- **Auth:** No key for basic API; token for some endpoints.
- **Rate limits:** Fair-use.
- **License:** Aggregated content under varied CC licenses; attribution per source.
- **Worldbuilding value:** Rich trait + imagery per organism to flesh out alien-analog biology. *(Historic funding/uptime fluctuations — verify.)*

## Catalogue of Life (ChecklistBank) [Stable]
- **URL / endpoint:** `https://api.checklistbank.org/` · site `https://www.catalogueoflife.org`
- **Covers:** Authoritative consolidated checklist of the world's known species names/taxonomy.
- **Access method:** REST; bulk download.
- **Data format:** JSON; Darwin Core / ColDP archives.
- **Auth:** No key for read.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** Canonical taxonomy/naming scaffold for inventing plausible new species names.

## iNaturalist API [Stable]
- **URL / endpoint:** `https://api.inaturalist.org/v1/` (`/observations`, `/taxa`).
- **Covers:** Crowd-sourced wildlife observations with photos, geolocation, taxonomy.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** None for read; OAuth for write.
- **Rate limits:** ~100 req/min; be gentle (≤~10k/day).
- **License:** Observations vary (many **CC BY-NC**); photos per uploader. (NC caveat for commercial use.)
- **Worldbuilding value:** Real photos + locations of organisms for vivid, place-accurate flora/fauna.

## ITIS — Integrated Taxonomic Information System [Stable]
- **URL / endpoint:** `https://www.itis.gov/ITISWebService/jsonservice/`
- **Covers:** Standardized taxonomy with TSN identifiers (esp. North American biota).
- **Access method:** REST/SOAP; bulk DB download.
- **Data format:** JSON, XML; SQLite/MySQL dumps.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Stable taxonomic IDs/hierarchy for consistent in-world species cataloging.

## NCBI Taxonomy (E-utilities) [Stable]
- **URL / endpoint:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` (`esearch`/`efetch`, `db=taxonomy`).
- **Covers:** Taxonomic tree for organisms with sequence data; TaxIDs, lineages.
- **Access method:** REST (E-utilities).
- **Data format:** XML, JSON.
- **Auth:** Optional API key (raises limit).
- **Rate limits:** 3 req/sec without key; 10 req/sec with key.
- **License:** Public domain.
- **Worldbuilding value:** Authoritative lineage data to root invented organisms in real phylogeny.

## WoRMS — World Register of Marine Species [Stable]
- **URL / endpoint:** `https://www.marinespecies.org/rest/`
- **Covers:** Marine taxonomy — accepted names, classification, distributions.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No.
- **License:** **CC BY**.
- **Worldbuilding value:** Marine/aquatic species authority for ocean world-building.

## PubChem PUG REST [Stable]
- **URL / endpoint:** `https://pubchem.ncbi.nlm.nih.gov/rest/pug/`
- **Covers:** >100M chemical compounds — structures, properties, names, safety/hazard data.
- **Access method:** REST.
- **Data format:** JSON, XML, CSV, SDF, PNG.
- **Auth:** No.
- **Rate limits:** ~5 req/sec, ≤400 req/min, dynamic throttling.
- **License:** Mostly public domain/free; some sources have terms.
- **Worldbuilding value:** Real compound properties/toxicity to invent plausible drugs, poisons, materials.

## Periodic Table JSON (Bowserinator) [Stable]
- **URL / endpoint:** `https://github.com/Bowserinator/Periodic-Table-JSON`
- **Covers:** All elements with physical/chemical properties, electron config, discovery info.
- **Access method:** Bulk download / raw GitHub fetch.
- **Data format:** JSON.
- **Auth:** No.
- **License:** **CC BY-SA 4.0**.
- **Worldbuilding value:** Drop-in element data for chemistry-accurate materials/tech.

## NIST CODATA Fundamental Physical Constants [Stable]
- **URL / endpoint:** `https://physics.nist.gov/cuu/Constants/`
- **Covers:** Authoritative physical constants (c, G, h…) with uncertainties.
- **Access method:** Bulk download (ASCII/JSON); web pages.
- **Data format:** ASCII, JSON, HTML.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Canonical constants for hard-SF physics/engineering plausibility.

## USGS Earthquake Catalog (FDSN) [Stable]
- **URL / endpoint:** `https://earthquake.usgs.gov/fdsnws/event/1/query` · feeds `/earthquakes/feed/v1.0/`
- **Covers:** Global earthquakes — magnitude, location, depth, time; near-real-time feeds.
- **Access method:** REST; static GeoJSON feeds.
- **Data format:** GeoJSON, QuakeML, CSV, KML, text.
- **Auth:** No.
- **Rate limits:** Fair-use; window large queries.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Real seismic patterns to drive disaster scenarios and tectonic world-building.

## Mindat.org API (OpenMindat) [Verify — terms]
- **URL / endpoint:** `https://api.mindat.org/` · site `https://www.mindat.org`
- **Covers:** Comprehensive mineralogy — species, properties, localities, geology.
- **Access method:** REST (token-based).
- **Data format:** JSON.
- **Auth:** **API token** (free registration).
- **Rate limits:** Per-account fair-use throttling.
- **License:** Data terms per Mindat (non-commercial/attribution constraints — **check current terms**).
- **Worldbuilding value:** Real minerals + where they form for believable geology, mining, resource lore.

## USGS Mineral Resources (MRDS / mrdata) [Stable]
- **URL / endpoint:** `https://mrdata.usgs.gov/`
- **Covers:** Mineral deposit/occurrence locations, commodities, geology, geochemistry.
- **Access method:** REST/WMS/WFS; bulk download.
- **Data format:** JSON, CSV, Shapefile, GeoJSON, WMS.
- **Auth:** No.
- **License:** Public domain (US Gov).
- **Worldbuilding value:** Real deposit maps to ground resource economics and frontier mining plots.

## Open-Meteo [Verify]
- **URL / endpoint:** `https://open-meteo.com/`
- **Covers:** Weather/climate (forecast + historical reanalysis) globally.
- **Access method:** REST.
- **Data format:** JSON.
- **Auth:** No key (free tier).
- **Rate limits:** Generous free tier; commercial tiers for volume.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** Realistic climate/weather patterns by latitude/terrain for plausible world climates.

---

# 8. LAW/GOVERNANCE, MILITARY, ECONOMICS HISTORY

## Constitute Project [Verify — API]
- **URL / endpoint:** `https://www.constituteproject.org/` · API/data historically at `/service/` and bulk RDF/CSV.
- **Covers:** The world's constitutions, tagged by ~300+ topics (rights, institutions, powers), comparable across countries/time.
- **Access method:** Web UI + data export; an API has existed historically — **verify current availability.**
- **Data format:** JSON, CSV, RDF, PDF.
- **Auth:** Historically open.
- **License:** Open for non-commercial/research; check terms.
- **Worldbuilding value:** Real constitutional structures/clauses to design believable in-world governments and laws.

## V-Dem (Varieties of Democracy) [Stable]
- **URL / endpoint:** `https://www.v-dem.net/data/the-v-dem-dataset/`
- **Covers:** Hundreds of indicators of democracy/governance for ~200 polities, 1789→present.
- **Access method:** Bulk download (+ R package).
- **Data format:** CSV, R, Stata, SPSS.
- **Auth:** Free registration for download.
- **License:** Free for research; attribution.
- **Worldbuilding value:** Quantitative governance profiles to model regime types and political change over time.

## Correlates of War (COW) [Stable]
- **URL / endpoint:** `https://correlatesofwar.org/data-sets/`
- **Covers:** Inter-state/intra-state wars, militarized disputes, alliances, national capabilities, 1816→present.
- **Access method:** Bulk download.
- **Data format:** CSV.
- **Auth:** No.
- **License:** Free for academic use; attribution.
- **Worldbuilding value:** Structured war/conflict/alliance data to model fictional geopolitics and military history.

## UCDP — Uppsala Conflict Data Program [Stable]
- **URL / endpoint:** `https://ucdp.uu.se/` · API `https://ucdpapi.pcr.uu.se/api/`
- **Covers:** Organized violence/armed conflicts worldwide, 1946→present, with actors, locations, fatalities.
- **Access method:** REST API + bulk download.
- **Data format:** JSON, CSV, Excel.
- **Auth:** No.
- **Rate limits:** Fair-use.
- **License:** CC BY 4.0.
- **Worldbuilding value:** Granular conflict-event data to ground war narratives and conflict patterns.

## ACLED — Armed Conflict Location & Event Data [Verify — access model]
- **URL / endpoint:** `https://acleddata.com/` · API `https://api.acleddata.com/`
- **Covers:** Real-time-ish political violence/protest events globally, geolocated, dated, typed.
- **Access method:** REST API.
- **Data format:** JSON, CSV.
- **Auth:** **Registration + API key required; access model has tightened** (free for non-commercial with limits; commercial paid). **Verify current terms.**
- **Rate limits:** Per-key.
- **License:** Attribution; restrictions on redistribution/commercial use.
- **Worldbuilding value:** Fine-grained modern conflict-event patterns — but check access tier before use.

## Wikidata battles (via SPARQL) [Stable]
- **URL / endpoint:** `https://query.wikidata.org/sparql` (`wd:Q178561` battle and subclasses).
- **Covers:** Battles/sieges/wars with dates, locations, belligerents, commanders, outcomes.
- **Access method:** SPARQL.
- **Data format:** JSON/CSV.
- **Auth:** No.
- **License:** CC0 1.0.
- **Worldbuilding value:** CC0 structured battle data with belligerents/commanders for military-history scaffolding.

## Maddison Project Database [Stable]
- **URL / endpoint:** `https://www.rug.nl/ggdc/historicaldevelopment/maddison/`
- **Covers:** Long-run historical GDP and population estimates by country, year 1→present.
- **Access method:** Bulk download.
- **Data format:** Excel, Stata, CSV.
- **Auth:** No.
- **License:** Open for research; attribution.
- **Worldbuilding value:** Long-run economic trajectories to ground the wealth/development of fictional nations across eras.

## Our World in Data [Stable]
- **URL / endpoint:** `https://ourworldindata.org/` · Chart/data CSV exports; `https://github.com/owid/owid-datasets`; catalog API emerging.
- **Covers:** Thousands of curated long-run datasets (economy, demography, health, war, energy, food).
- **Access method:** Bulk CSV download; GitHub; some programmatic catalog access.
- **Data format:** CSV, JSON.
- **Auth:** No.
- **License:** **CC BY 4.0** (OWID-produced data; source data per provider).
- **Worldbuilding value:** One-stop curated long-run trends to anchor a world's demographics, economy, and crises.

## World Bank Open Data API [Stable]
- **URL / endpoint:** `https://api.worldbank.org/v2/`
- **Covers:** ~1,400+ development indicators (GDP, population, trade, etc.) by country, 1960→present.
- **Access method:** REST.
- **Data format:** JSON, XML.
- **Auth:** No.
- **Rate limits:** Fair-use.
- **License:** **CC BY 4.0** for most indicators.
- **Worldbuilding value:** Real-country economic/demographic templates for modeling fictional nations' stats.

## International Institute of Social History — historical prices/wages [Verify]
- **URL / endpoint:** `https://iisg.amsterdam/en/data/datasets` (HPW datasets; Allen wage/price series).
- **Covers:** Historical prices, wages, and living standards across centuries/regions.
- **Access method:** Bulk download.
- **Data format:** Excel/CSV.
- **Auth:** No.
- **License:** Open for research; attribution.
- **Worldbuilding value:** Real historical wage/price levels to make in-world economies and "what a loaf costs" feel authentic.

---

# 9. LANGUAGES, LINGUISTICS & CONLANG

## WALS — World Atlas of Language Structures Online [Stable]
- **URL / endpoint:** `https://wals.info/` · data on GitHub (CLDF) `https://github.com/cldf-datasets/wals`
- **Covers:** ~2,600+ languages described across ~190 structural features (phonology, morphology, syntax, word order).
- **Access method:** Web UI + bulk download (CLDF).
- **Data format:** CSV (CLDF), RDF.
- **Auth:** No.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** A menu of real typological features to design internally-consistent conlang grammar.

## Glottolog [Stable]
- **URL / endpoint:** `https://glottolog.org/` · GitHub CLDF `https://github.com/glottolog/glottolog`
- **Covers:** Comprehensive catalog of world languages/dialects/families with genealogical classification, geocoordinates, references.
- **Access method:** Web UI + bulk download (CLDF); resolvable glottocodes.
- **Data format:** CSV (CLDF), JSON.
- **Auth:** No.
- **License:** **CC BY 4.0**.
- **Worldbuilding value:** Language-family trees and geography to design plausible fictional language families.

## PHOIBLE [Stable]
- **URL / endpoint:** `https://phoible.org/` · GitHub `https://github.com/phoible/dev`
- **Covers:** Phoneme inventories for ~2,000+ languages (~3,000+ inventories).
- **Access method:** Web UI + bulk download.
- **Data format:** CSV, TSV.
- **Auth:** No.
- **License:** **CC BY-SA 3.0**.
- **Worldbuilding value:** Real phoneme inventories to give a conlang an authentic, learnable sound system.

## Universal Dependencies [Stable]
- **URL / endpoint:** `https://universaldependencies.org/` · GitHub treebanks.
- **Covers:** Annotated treebanks (morphology + syntax) for ~150+ languages.
- **Access method:** Bulk download (Git).
- **Data format:** CoNLL-U (text).
- **Auth:** No.
- **License:** Mostly CC BY-SA / CC BY (per treebank).
- **Worldbuilding value:** Real grammatical-dependency patterns to inform conlang syntax.

## Lingua Libre [Stable]
- **URL / endpoint:** `https://lingualibre.org/` (Wikimedia) · API via MediaWiki/Wikibase; media on Commons.
- **Covers:** Crowd-sourced audio recordings of words/phrases across many languages.
- **Access method:** REST/Action API; bulk via Commons.
- **Data format:** JSON metadata; OGG/WAV audio.
- **Auth:** No.
- **License:** **CC BY-SA / CC0** (free).
- **Worldbuilding value:** Real pronunciation audio to model phonetics for a conlang's sound.

## Ethnologue [Verify — paywalled]
- **URL / endpoint:** `https://www.ethnologue.com/`
- **Covers:** Catalog of ~7,000+ living languages — speakers, locations, vitality, classification.
- **Access method:** Web UI; **mostly paywalled / subscription**; no open API.
- **Data format:** N/A (subscription data).
- **Auth:** Subscription.
- **License:** Proprietary.
- **Worldbuilding value:** Authoritative speaker/vitality data — but **prefer Glottolog/WALS** for open access.

## Swadesh lists (via Wiktionary) [Stable]
- **URL / endpoint:** `https://en.wiktionary.org/wiki/Appendix:Swadesh_lists` (per-language appendices).
- **Covers:** Core basic-vocabulary lists (~100–207 concepts) across many languages.
- **Access method:** MediaWiki API / scrape of appendix pages; bulk lexical data via Wiktextract.
- **Data format:** Wikitext/HTML; JSON via Wiktextract.
- **Auth:** No.
- **License:** CC BY-SA.
- **Worldbuilding value:** A ready concept list to systematically build a conlang's core vocabulary.

## CLDF / CLLD datasets ecosystem [Stable]
- **URL / endpoint:** `https://clld.org/` and `https://cldf.clld.org/` (hosts WALS, Glottolog, PHOIBLE, Lexibank, Grambank, etc.).
- **Covers:** A family of standardized cross-linguistic datasets incl. **Grambank** (grammatical features) and **Lexibank** (comparative wordlists).
- **Access method:** Bulk download (CLDF); web UIs.
- **Data format:** CSV (CLDF), RDF.
- **Auth:** No.
- **License:** Mostly CC BY / CC BY-SA.
- **Worldbuilding value:** One ecosystem covering grammar, phonology, and vocabulary — the conlanger's open-data toolkit.

---

# Top 8–10 most valuable sources (quick reference)

| Source | Domain | Access | License |
|---|---|---|---|
| **Wikidata (WDQS + dumps)** | Everything (events, people, places, things) | SPARQL + bulk | CC0 |
| **Wikimedia Commons API** | Imagery for all material culture | REST/Action | Free (CC0/CC BY/PD per file) |
| **The Met Open Access API** | Weapons, armor, costume | REST (no key) | CC0 metadata + many CC0 images |
| **GeoNames** | Places/toponymy | REST + bulk (free username) | CC BY 4.0 |
| **OpenStreetMap (Overpass/Nominatim)** | Maps/features/geocoding | REST | ODbL (share-alike) |
| **Natural Earth** | Base-map vector/raster | Bulk download | Public domain |
| **NASA APIs + Exoplanet Archive** | Astronomy/space (sci-fi) | REST / TAP | Public domain / open |
| **GBIF** | Biodiversity/species distribution | REST + bulk | CC0/CC BY (per dataset) |
| **Wiktextract / Kaikki.org** | Etymology, phonology, naming | Bulk JSONL + API | CC BY-SA |
| **WALS + Glottolog + PHOIBLE (CLDF)** | Conlang/linguistics | Bulk CLDF | CC BY / CC BY-SA |

**Recommended starting stack:** Wikidata (hub) + Wikimedia Commons (imagery) + GeoNames/Natural Earth (geography) + a couple of museum APIs (Met, Cleveland — both no-key, CC0) + NASA + GBIF + the CLDF linguistics set. This covers events, people, places, things, and sciences with predominantly CC0/CC-BY licensing.

---

## Next step: live verification (required before integration)

This catalog needs a verification pass with network access enabled. Priority items to confirm (most likely to have drifted):
1. **Behind the Name API** — confirm the API still exists and its current terms.
2. **ACLED** — confirm current access tier/pricing (has tightened over time).
3. **Constitute Project API** — confirm endpoint still served.
4. **REST Countries** — confirm hosting/uptime and rate limits.
5. **HYG → ATHYG** — confirm the current GitHub repo name/structure.
6. **Open Exoplanet Catalogue & EOL** — confirm freshness/uptime.
7. **GADM & Mindat** — re-read commercial-use terms before any paid-product use.
8. **DBpedia Spotlight public instance** & **Wikidata Linked Data Fragments** — confirm still hosted (self-host otherwise).

# World Regions Expanded — Historical, Archival & Cultural Data Sources

> **UNVERIFIED — compiled from training knowledge (cutoff Jan 2026); to be live-verified.**
>
> Focus: deep regional coverage **outside** Korea / Western Europe / US. Endpoints, rate limits, and licenses
> below are from memory and **must be re-checked live**. Many "API" claims for cultural-heritage portals are
> actually IIIF image APIs, OAI-PMH metadata feeds, or SPARQL endpoints rather than clean JSON REST.
>
> Legend: 🚩 = restrictive, scrape-only, login-walled, or otherwise hard to use programmatically.
> Access codes: **REST** JSON/XML HTTP API · **SPARQL** RDF query · **OAI-PMH** metadata harvest ·
> **IIIF** image/manifest API (Presentation/Image) · **bulk** downloadable dumps · **scrape** HTML only ·
> **Z39.50/SRU** library protocols · **Git** repo of plaintext.

---

## Quick-reference table (grouped by region)

### South Asia / India

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 1 | GRETIL (Göttingen Sanskrit etexts) | bulk / scrape | TEI-XML, plaintext, HTML | none | Mixed/free for research | Raw Sanskrit epics, Vedas, kāvya, śāstra for myth/plot mining |
| 2 | SARIT (Search & Retrieval of Indic Texts) | bulk / Git / scrape | TEI-XML | none | CC-BY / mixed | Critically-encoded Sanskrit philosophical & literary corpus |
| 3 | Digital Corpus of Sanskrit (DCS) | REST-ish / bulk | JSON / SQL dump | none | CC-BY-SA | Morphologically tagged Sanskrit — name/word etymology |
| 4 | Indian Culture Portal (indianculture.gov.in) | scrape 🚩 | HTML / PDF / IIIF? | none | Gov't / GODL-India | Manuscripts, folktales, festivals, textiles, cuisine — texture |
| 5 | Digital Library of India / IIIT-archive 🚩 | scrape / archive.org mirror | DjVu / PDF / TXT | none | Mixed (defunct primary) | Scanned vernacular & Sanskrit books (now via archive.org) |
| 6 | Murty Classical Library of India (Harvard) 🚩 | scrape | HTML / print | none | © Harvard UP | Curated translations (Pali/Sanskrit/Persian/Urdu/Tamil) — reference only |
| 7 | Archive.org "Indian texts" collections | REST | JSON / many | none/key | Public domain / CC | Mass scanned Indic books, gazetteers, colonial ethnography |
| 8 | Tamil Virtual Academy / Project Madurai | bulk / scrape | Unicode TXT / HTML | none | Free (PM: free use) | Tamil Sangam classics, Thirukkural, devotional corpus |
| 9 | Telugu / TDIL & vernacular corpora 🚩 | bulk / scrape | TXT / corpus | none | Gov't mixed | Telugu literary + lexical data for Dravidian worldbuilding |
| 10 | Panini / Sanskrit Heritage (INRIA Heritage) | REST/CGI | HTML / JSON-ish | none | Free academic | Sanskrit morphology, declension, readers — naming engine |
| 11 | Pandanus / Vedic Concordance & DH tools | bulk | DB / TXT | none | Academic | Cross-text concordances for motif tracing |

### Middle East / Islamic world

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 12 | OpenITI (Open Islamicate Texts Initiative) | Git / bulk | mARkdown / plaintext | none | CC-BY-NC-SA (mixed) | Largest machine-readable Arabic/Persian corpus — 10k+ texts |
| 13 | KITAB project (text reuse) | REST/bulk + viewer | JSON / TSV | none | CC-BY | Text-reuse graph: who copied whom — intertextual plots |
| 14 | al-Maktaba al-Shamela (Shamela) 🚩 | scrape / .bok dumps | proprietary .bok / HTML | none | Unclear/no formal license | ~7k Islamic books (fiqh, hadith, tafsir, history, adab) |
| 15 | Qatar Digital Library (QDL) | IIIF + OAI-PMH | IIIF manifests / METS | none | Mostly free reuse (check) | British Library Gulf/Arabic mss & India Office records |
| 16 | Library of Arabic Literature (NYU) 🚩 | scrape | HTML / print | none | Open-access editions vary | Bilingual classical Arabic editions — translation reference |
| 17 | HathiTrust (Arabic/Persian holdings) | OAI / Data API 🚩 | metadata; full text gated | partner key | © / public-domain split | Scanned MENA print; bulk needs partner access |
| 18 | Princeton / Cambridge Islamic mss (IIIF) | IIIF | IIIF manifests / JPEG | none | CC / mixed | High-res manuscript images for illumination, marginalia |
| 19 | Shia / Noor (al-maktaba) & Ganjoor (Persian) | REST (Ganjoor) / scrape | JSON (Ganjoor) | none | Ganjoor: open | Ganjoor = full classical Persian poetry API (Hafez, Rumi…) |
| 20 | Perseus / Open Persian (Roshan, PARSA) | bulk / Git | TEI-XML | none | CC-BY | Digital Persian/New-Persian texts, lexica |
| 21 | Islamic Manuscripts at Michigan / FIHRIST (UK union) | SRU / scrape | MARC / TEI | none | Catalog open | Union catalog of Islamic mss in UK collections — discovery |

### China (beyond ctext.org)

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 22 | CBETA (Chinese Buddhist Electronic Tripitaka) | bulk / Git / REST | TEI-XML / app | none | CC-BY-NC-SA (mostly) | Full Chinese Buddhist canon — cosmology, jataka, ritual |
| 23 | CBDB (China Biographical Database, Harvard/AS/PKU) | REST API + SQLite/SQL dump | JSON / SQLite / MS Access | none | CC-BY-NC-SA | ~500k historical Chinese persons — kinship, office, networks |
| 24 | Academia Sinica (Scripta Sinica 漢籍電子文獻) 🚩 | scrape / login | HTML | sometimes | Restricted | Classical Chinese histories, dynastic records |
| 25 | MARKUS / DocuSky (Leiden/Taiwan) | webapp + REST-ish | XML / JSON | none | Academic free | Markup + named-entity tagging for classical Chinese |
| 26 | Dharma Drum Buddhist Studies (DDBC/DILA) authority DBs | REST/LOD + SPARQL | JSON / RDF / TEI | none | CC-BY | Person/place/time authority for Buddhist Asia — gazetteer |
| 27 | Zhonghua / Kanripo (漢籍リポジトリ) | Git / IIIF / REST | plaintext / TEI | none | CC / mixed | Kanripo: Git-versioned Chinese classics (Siku-based) |
| 28 | Chinese Text Project (ctext) API *(baseline)* | REST | JSON | optional key | CC-BY-SA (data) | Pre-Qin → Qing classics; included for parity |
| 29 | Tang/Song poetry corpora (chinese-poetry GitHub) | bulk / Git | JSON | none | MIT-ish | 300k+ classical Chinese poems — quotation & naming |

### Japan / Southeast Asia

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 30 | Japan Search (ジャパンサーチ, NDL) | REST + SPARQL | JSON / RDF | none | Metadata CC0 (items vary) | Cross-domain aggregator: 20M+ Japanese cultural items |
| 31 | Aozora Bunko (青空文庫) | bulk / Git / scrape | XHTML / TXT (Shift-JIS) | none | Public domain | Full-text public-domain Japanese literature |
| 32 | NDL Digital Collections (国立国会図書館) | IIIF + OAI + API | IIIF / JSON | none | Mixed (PD + gated) | Scanned Japanese books, ukiyo-e, old maps |
| 33 | SEAlang Library | REST-ish / scrape | dict / corpus | none | Academic free | Dictionaries + corpora: Thai, Lao, Khmer, Burmese, Vietnamese… |
| 34 | ECAI (Electronic Cultural Atlas Initiative) 🚩 | scrape / GIS | shapefile / KML | none | Mixed | Historical Asian gazetteers & cultural atlases |
| 35 | SOAS / Khmer & Thai heritage portals 🚩 | scrape / IIIF | IIIF / PDF | none | Mixed | Angkor inscriptions, palm-leaf mss, Thai chronicles |
| 36 | Vietnamese Nôm Preservation Foundation | scrape / bulk | Unicode / images | none | Free use | Chữ Nôm texts, Nôm-Quốc-ngữ dictionaries |
| 37 | Indonesia: Khastara (Perpusnas) / SEADELI 🚩 | scrape / IIIF | IIIF / PDF | none | Gov't mixed | Javanese/Malay mss, lontar, wayang/hikayat sources |
| 38 | Myanmar / Pali Tipitaka (VRI / SuttaCentral) | REST (SuttaCentral) / bulk | JSON / TEI | none | CC0 / CC-BY (SC) | SuttaCentral API: Pali canon + multilingual parallels |

### Africa

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 39 | Aluka (now in JSTOR/Artstor) 🚩 | scrape / login | HTML / images | subscription | Restricted | African heritage sites, struggle archives, manuscripts |
| 40 | World Digital Library (now at LOC) | IIIF + (legacy) API | IIIF / JSON | none | Mostly PD / partner | Global incl. deep African mss, maps, early prints |
| 41 | Timbuktu / SAVAMA-DCI & HMML vHMML 🚩 | scrape / IIIF (vHMML) | IIIF / images | login (vHMML) | Restricted/research | West African Arabic & Ajami manuscripts |
| 42 | EAP (Endangered Archives Programme, BL) | IIIF + OAI / scrape | IIIF / metadata | none | Mostly open (check) | Digitized at-risk African/global archives & oral records |
| 43 | DISA / South African archives (Aluka-adjacent) 🚩 | scrape | PDF / HTML | none | Mixed | Anti-apartheid, periodicals, social history |
| 44 | African Storybook / oral-tradition corpora | REST-ish / scrape | EPUB / TXT / audio | none | CC-BY | Multilingual African folktales (open-licensed) |
| 45 | ALA / African Language Archive & ELAR (SOAS) 🚩 | scrape / login | audio / ELAN | login | Restricted-by-depositor | Endangered-language recordings, oral epics |

### Latin America

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 46 | Biblioteca Virtual Miguel de Cervantes | OAI-PMH + scrape | XML / HTML / TEI | none | Mostly free | Hispanic literature, chronicles of the Indies |
| 47 | BNDigital (Biblioteca Nacional do Brasil) 🚩 | scrape / IIIF? | PDF / images | none | Gov't mixed | Brazilian periodicals, colonial mss, hemeroteca |
| 48 | INAH / Mediateca (Mexico) 🚩 | scrape / IIIF | IIIF / images | none | Gov't mixed | Codices, archaeology, ethnography of Mesoamerica |
| 49 | World Digital Library — Mesoamerican codices | IIIF | IIIF / JPEG | none | Mostly PD | Codex Mendoza, Borgia, Dresden (Maya) high-res |
| 50 | FAMSI / Maya Hieroglyphic & Mesoweb 🚩 | scrape | PDF / images | none | Academic free | Maya glyph catalogs, Popol Vuh, codex commentary |
| 51 | Memórias / Biblioteca Digital Mundial mirrors | IIIF / scrape | IIIF | none | Mixed | LatAm maps, early printing, indigenous-language doctrinas |
| 52 | Endangered Languages / AILLA (Texas) 🚩 | scrape / login | audio / TXT | login | Depositor-set | Indigenous American oral literature recordings |

### Oceania / Indigenous

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 53 | Trove (National Library of Australia) | REST | JSON / XML | **API key (free)** | Metadata mixed; PD newspapers | Massive: newspapers, books, mss, oral histories |
| 54 | DigitalNZ | REST | JSON | **API key (free)** | Per-record (mixed) | NZ aggregator: Māori taonga, archives, images |
| 55 | Te Ara — Encyclopedia of NZ | scrape / some data | HTML | none | CC-BY-NC (text) | Curated Māori myth, history, biography essays |
| 56 | AIATSIS (Aust. Aboriginal & Torres Strait) 🚩 | scrape / catalog | HTML / restricted | login | Culturally restricted | Aboriginal languages, mss, oral tradition (access protocols) |
| 57 | Pacific Manuscripts Bureau (PAMBU) / ANU 🚩 | scrape | microfilm/PDF | none | Mixed | Pacific Islands mission & colonial records, oral histories |
| 58 | Paradisec (Pacific & regional endangered langs) | OAI / REST-ish | audio / metadata | some login | CC / depositor | Oceanic oral epics, chants, language recordings |
| 59 | NZETC (NZ Electronic Text Collection) | bulk / scrape | TEI-XML | none | Mostly free | Full-text NZ/Pacific historical texts incl. Māori |

### Cross-cutting global

| # | Source | Access | Format | Auth | License (approx.) | Story value |
|---|--------|--------|--------|------|-------------------|-------------|
| 60 | Internet Archive | REST + bulk + S3-like | JSON / many | optional key | PD / CC / mixed | Universal fallback for scanned texts, audio, film |
| 61 | UNESCO Memory of the World | scrape 🚩 | HTML | none | Catalog open | Curated list of world-significant documentary heritage |
| 62 | World Historical Gazetteer (WHG) | REST + bulk | JSON / LPF GeoJSON | optional | CC-BY | Historical place names across time — period-accurate maps |
| 63 | Pleiades (ancient places) | REST + bulk | JSON / CSV / RDF | none | CC-BY | Ancient world gazetteer (Mediterranean+; expanding) |
| 64 | GeoNames | REST | JSON / XML | **username (free)** | CC-BY | Modern global toponyms, admin hierarchy, alt names |
| 65 | OpenStreetMap / Overpass API | REST (Overpass QL) | JSON / XML | none | ODbL | Live geographic features for setting realism |
| 66 | Wikidata | SPARQL + REST | JSON / RDF | none | CC0 | Universal entity graph: people, places, events, links |
| 67 | DBpedia / EventKG | SPARQL + bulk | RDF / JSON | none | CC-BY-SA | Cross-lingual events & timelines for plotting history |
| 68 | Wiktionary / etymology dumps (etymwn, Kaikki) | bulk / REST | JSON / dump | none | CC-BY-SA | Word origins & cognates across languages — naming/lore |
| 69 | Behind the Name | REST | JSON | **API key (free tier)** | Restricted (API ToS) | Given-name etymology & usage by culture |
| 70 | GBIF (Global Biodiversity) | REST | JSON / DwC | optional | CC-BY / CC0 | Real flora/fauna by region & era — ecosystem worldbuilding |
| 71 | NASA APIs (APOD, exoplanet archive, JPL Horizons) | REST | JSON / CSV | **key (DEMO ok)** | US gov PD | Astronomy/ephemerides for hard-SF and sky accuracy |
| 72 | DPLA & Europeana *(parity anchors)* | REST | JSON | **key (free)** | Metadata CC0 | Aggregator cross-checks; Europeana reaches E. Europe |

---

## Detailed entries

### South Asia / India

#### 1. GRETIL — Göttingen Register of Electronic Texts in Indian Languages
- **Official name:** GRETIL (Universität Göttingen / SUB Göttingen).
- **URL:** `http://gretil.sub.uni-goettingen.de/` (also a "gretil-corpus" GitHub mirror exists).
- **Coverage:** The single most important free aggregation of Sanskrit (plus Prakrit, Pali, Tamil, etc.) e-texts: Vedas, Upaniṣads, Mahābhārata, Rāmāyaṇa, Purāṇas, kāvya, philosophy, tantra, śāstra.
- **Access:** No real API — **bulk download** of files and **scrape**. A TEI-XML conversion of much of GRETIL is distributed on GitHub.
- **Format:** Plaintext (HK/IAST/Devanagari), HTML, TEI-XML in the converted corpus.
- **Auth / rate limit:** None / be polite when scraping.
- **License:** Per-text; mostly free for scholarly use, individual files note source/encoder. Verify before redistribution.
- **Story value:** Bulk raw mythology and epic narrative to mine for plots, deities, names, cosmology.

#### 2. SARIT — Search and Retrieval of Indic Texts
- **URL:** `https://sarit.indology.info/` and GitHub `sarit/`.
- **Coverage:** Critically encoded Sanskrit literary & philosophical texts (e.g., Arthaśāstra, alaṅkāra, Nyāya).
- **Access:** **Git / bulk** TEI-XML; web reader (eXist-db) is scrape-able.
- **Format:** TEI-XML (well-structured).
- **License:** CC-BY (mostly) — check per text.
- **Story value:** Clean structured editions good for NLP, citation, and motif extraction.

#### 3. Digital Corpus of Sanskrit (DCS)
- **URL:** `http://www.sanskrit-linguistics.org/dcs/`.
- **Coverage:** Sandhi-split, lemmatized, morphologically and (partly) syntactically tagged Sanskrit corpus.
- **Access:** Web query + **downloadable data**; programmatic-ish.
- **Format:** Tabular / JSON-ish / SQL.
- **License:** CC-BY-SA (verify).
- **Story value:** Best source for *word-level* Sanskrit data — perfect for a naming/etymology engine.

#### 4. Indian Culture Portal — indianculture.gov.in 🚩
- **Official name:** Indian Culture Portal (Ministry of Culture, IGNCA-built).
- **URL:** `https://indianculture.gov.in/`.
- **Coverage:** Manuscripts, rare books, e-books, photo archives, gazetteers, intangible heritage, festivals, cuisine, textiles, folktales, freedom-struggle records.
- **Access:** **Scrape** (no documented public API). Some manuscript images may be IIIF-served — verify.
- **Format:** HTML, PDF, images.
- **License:** Government Open Data License – India (GODL) on much content; per-item rights vary. 🚩 Reuse terms uneven.
- **Story value:** Enormous "texture" layer — daily life, ritual, regional folklore beyond canonical epics.

#### 5. Digital Library of India (DLI) 🚩
- **Status:** Original DLI / IIIT-Hyderabad portal is **largely defunct**; content survives mainly as Internet Archive mirrors and various rehosts.
- **Coverage:** Hundreds of thousands of scanned books in Sanskrit and Indian vernaculars, colonial-era gazetteers.
- **Access:** Practically **archive.org** today (see #7) or scrape mirrors.
- **Format:** DjVu, PDF, OCR TXT (often poor OCR).
- **License:** Mixed / mostly public domain by age.
- **Story value:** Deep vernacular and out-of-print material unavailable elsewhere.

#### 6. Murty Classical Library of India (MCLI) 🚩
- **Publisher:** Harvard University Press.
- **URL:** `https://www.murtylibrary.com/`.
- **Coverage:** Facing-page critical translations from Bangla, Hindi, Kannada, Marathi, Pali, Panjabi, Persian, Prakrit, Sanskrit, Tamil, Telugu, Urdu.
- **Access:** **Scrape / print only**; copyrighted. 🚩 No bulk text.
- **License:** © Harvard UP.
- **Story value:** Authoritative *translations* — use as reference/quotation source, not a data feed.

#### 7. Internet Archive — Indian texts collections
- **URL / API:** `https://archive.org/advancedsearch.php?...&output=json`; metadata `https://archive.org/metadata/{id}`.
- **Coverage:** Mass-scanned Indic books (incl. former DLI), colonial ethnography, gazetteers, censuses.
- **Access:** **REST** (advanced search + metadata + download).
- **Format:** JSON metadata; items as PDF/DjVu/TXT/EPUB.
- **Auth / rate:** Optional S3-style keys for upload; reads are open with polite limits.
- **License:** Public domain / CC / mixed per item.
- **Story value:** Single most practical programmatic gateway to scanned Indian material.

#### 8. Tamil Virtual Academy & Project Madurai
- **URLs:** `https://www.tamilvu.org/`; `https://www.projectmadurai.org/`.
- **Coverage:** Sangam classics, Tirukkuṟaḷ, Śaiva/Vaiṣṇava devotional, epics (Silappatikaram).
- **Access:** **Bulk download** (Project Madurai offers Unicode/PDF) + scrape.
- **Format:** Unicode TXT, HTML, PDF.
- **License:** Project Madurai = free for non-commercial sharing with attribution.
- **Story value:** Core of classical Tamil narrative & poetry — Dravidian myth and ethos.

#### 9. Telugu / TDIL vernacular corpora 🚩
- **Sources:** TDIL (Technology Development for Indian Languages, MeitY) data center; AU-KBC; university corpora.
- **Coverage:** Telugu (and other Indian-language) text/lexical corpora, parallel data.
- **Access:** **Bulk** via TDIL data portal (often registration) / scrape. 🚩 Access friction.
- **Format:** TXT, annotated corpora.
- **License:** Government, mixed; check redistribution.
- **Story value:** Lexical raw material for Telugu/Dravidian linguistics & naming.

#### 10. Sanskrit Heritage Engine (INRIA)
- **URL:** `https://sanskrit.inria.fr/`.
- **Coverage:** Morphological analyzer, declension/conjugation generator, reader, lexicon (MW-linked).
- **Access:** **CGI/REST-style** endpoints (designed for tools).
- **Format:** HTML / structured responses.
- **License:** Free for academic use.
- **Story value:** A live *engine* — inflect invented Sanskritic names correctly, generate plausible vocabulary.

#### 11. Vedic concordances / DH tools (Pandanus, VedaWeb)
- **VedaWeb:** `https://vedaweb.uni-koeln.de/` — **REST API** over the Rigveda with morphology & translations.
- **Coverage:** Rigveda (VedaWeb) with lemma/morph search; Pandanus = botanical/plant-name DB in Sanskrit lit.
- **Format:** JSON (VedaWeb API).
- **License:** CC-BY (verify).
- **Story value:** Deep query into the oldest layer of Indo-Aryan myth and ritual language.

---

### Middle East / Islamic world

#### 12. OpenITI — Open Islamicate Texts Initiative
- **URL:** GitHub `OpenITI/` (corpus releases), Zenodo DOIs for versioned dumps.
- **Coverage:** The largest machine-readable premodern **Arabic** corpus (plus Persian, Ottoman growing) — history, hadith, fiqh, adab, geography, biographical dictionaries.
- **Access:** **Git / bulk** releases; structured by author/book/version URIs.
- **Format:** OpenITI **mARkdown** (lightweight plaintext markup) / plaintext.
- **License:** Texts CC-BY-NC-SA / mixed; metadata open. Verify per text.
- **Story value:** Foundational corpus for Islamicate history, chronicles, and biography mining.

#### 13. KITAB project (text reuse)
- **URL:** `https://kitab-project.org/`.
- **Coverage:** Quantitative **text-reuse** detection across the OpenITI corpus.
- **Access:** Downloadable reuse data (TSV/JSON) + visualization; some API/passim outputs.
- **Format:** TSV / JSON / passim alignments.
- **License:** CC-BY (verify).
- **Story value:** Maps *intertextuality* — which historian copied whom — great for "competing accounts" plotting.

#### 14. al-Maktaba al-Shamela (Shamela) 🚩
- **URL:** `https://shamela.ws/`.
- **Coverage:** ~6,000–8,000 classical Islamic books across the disciplines (tafsir, hadith, fiqh, sira, history, language, adab).
- **Access:** **Scrape** website; or use legacy `.bok`/`.bok`/SQLite library dumps circulating in the community. 🚩 No official API or clear license.
- **Format:** Proprietary `.bok` (older), `.epub`, HTML; OpenITI re-encodes much of it.
- **License:** **Unclear / not formally licensed** — treat cautiously; prefer OpenITI's cleaned versions where overlapping.
- **Story value:** Sheer breadth of the Islamic textual tradition in one place.

#### 15. Qatar Digital Library (QDL)
- **URL:** `https://www.qdl.qa/`.
- **Coverage:** British Library Arabic scientific manuscripts + India Office Records on the Gulf, Arabia, Persia, the Indian Ocean.
- **Access:** **IIIF** (Presentation/Image) + **OAI-PMH** metadata harvest.
- **Format:** IIIF manifests, JPEG/JP2, METS/MODS metadata, bilingual (Ar/En) descriptions.
- **Auth / rate:** None documented; polite use.
- **License:** Much content free to reuse (BL terms) — **verify per item**.
- **Story value:** Richly catalogued Gulf/Indian-Ocean history with images — colonial intrigue, trade, science.

#### 16. Library of Arabic Literature (LAL, NYU Press) 🚩
- **URL:** `https://www.libraryofarabicliterature.org/`.
- **Coverage:** Critical Arabic editions with English translation (classical adab, poetry, travel, biography).
- **Access:** **Scrape**; some titles open-access PDFs, most are print/commercial. 🚩
- **License:** Mixed; open-access editions exist.
- **Story value:** Trustworthy translations of major Arabic works — narrative reference.

#### 17. HathiTrust (Arabic / Persian / Ottoman holdings) 🚩
- **URL / API:** `https://www.hathitrust.org/`; **Bibliographic API** + **Data API** + OAI.
- **Coverage:** Scanned MENA-language print across member libraries.
- **Access:** Metadata via Bib API (open); **full-text/page images gated**; bulk via the HathiTrust Research Center requires **membership/credentials**. 🚩
- **Format:** Metadata JSON/XML; page images for in-copyright items restricted.
- **License:** Public-domain vs in-copyright split; non-US PD complicated.
- **Story value:** Modern Arabic/Persian print runs, periodicals, reference works.

#### 18. Princeton / Cambridge / Leiden Islamic manuscripts (IIIF)
- **Examples:** Princeton Islamic Mss (`https://dpul.princeton.edu/`), Cambridge Digital Library, Leiden Digital Collections.
- **Coverage:** Qur'ans, scientific, literary, and historical Islamic manuscripts.
- **Access:** **IIIF** manifests; often discoverable via collection pages.
- **Format:** IIIF / JP2 / JPEG.
- **License:** CC / mixed (Cambridge often CC-BY-NC).
- **Story value:** Visual material — illumination, bindings, marginal notes, owner seals.

#### 19. Ganjoor (Persian poetry) + Shia/Noor libraries
- **Ganjoor URL / API:** `https://ganjoor.net/`; **REST API** `https://api.ganjoor.net/`.
- **Coverage:** Comprehensive classical **Persian poetry**: Ferdowsi, Rumi, Hafez, Saadi, Nezami, Khayyam, etc., with metadata, meters, and recitations.
- **Access:** **REST JSON API** (well-documented), plus offline DB dumps.
- **Format:** JSON; SQLite/MySQL dumps.
- **License:** Open / CC (verify); community-driven.
- **Story value:** Best programmatic Persian-poetry source — quotations, ghazal structure, imagery.

#### 20. Roshan / PARSA & Persian Digital Library
- **URL:** Roshan Institute / "Persian Digital Library" (PDL) on GitHub.
- **Coverage:** TEI-encoded New Persian texts and lexica.
- **Access:** **Git / bulk** TEI-XML.
- **License:** CC-BY.
- **Story value:** Structured Persian prose/poetry for NLP and citation.

#### 21. FIHRIST (UK union catalogue of Islamic mss) + Islamic Mss at Michigan
- **URLs:** `https://www.fihrist.org.uk/`; `https://www.lib.umich.edu/collections/...islamic`.
- **Coverage:** Union manuscript catalog (FIHRIST = discovery); Michigan = digitized Islamic mss.
- **Access:** FIHRIST: **SRU/scrape**, TEI records; Michigan: IIIF.
- **Format:** TEI / MARC / IIIF.
- **License:** Catalog data open; images mixed.
- **Story value:** Find *which* manuscript of a work exists where — provenance & variant hunting.

---

### China (beyond ctext.org)

#### 22. CBETA — Chinese Buddhist Electronic Text Association
- **URL:** `https://www.cbeta.org/`; GitHub `cbeta-org/` for XML.
- **Coverage:** Full **Chinese Buddhist canon** (Taishō, Xuzangjing, and more) — sutras, vinaya, commentaries, jātaka, cosmological texts.
- **Access:** **Git / bulk** TEI-XML; online reader (CBETA Online) with API-ish endpoints.
- **Format:** CBETA TEI-XML / plaintext / app DB.
- **License:** CC-BY-NC-SA (mostly); attribution required.
- **Story value:** Vast cosmology, hells/heavens, demons, miracle tales — deep fantasy/mythic source.

#### 23. CBDB — China Biographical Database
- **URL:** `https://projects.iq.harvard.edu/cbdb`; with Harvard / Academia Sinica / Peking University.
- **Coverage:** ~**500,000** historical Chinese individuals (Tang–Qing focus) with kinship, social associations, offices, postings, entry methods.
- **Access:** **Online query + REST API**; downloadable **standalone SQLite / MS Access / SQL** database.
- **Format:** JSON (API), SQLite/Access dumps.
- **License:** CC-BY-NC-SA.
- **Story value:** Instant historically grounded character networks — families, factions, careers, rivalries.

#### 24. Academia Sinica — Scripta Sinica (漢籍電子文獻資料庫) 🚩
- **URL:** `http://hanchi.ihp.sinica.edu.tw/`.
- **Coverage:** The Twenty-Four/Twenty-Five Histories, classics, and a large premodern Chinese corpus.
- **Access:** **Scrape**, often **login/IP-restricted**. 🚩 No open API.
- **Format:** HTML.
- **License:** Restricted access.
- **Story value:** Authoritative dynastic histories — events, edicts, biographies for period accuracy.

#### 25. MARKUS / DocuSky (markup & analysis tooling)
- **URLs:** `https://dh.chinese-empires.eu/markus/`; `https://docusky.org.tw/`.
- **Coverage:** Tools (not corpora) for tagging classical Chinese: named entities, dates, places, references; DocuSky hosts user corpora.
- **Access:** **Web app + REST-ish**; export XML/JSON.
- **Format:** TEI/XML, JSON.
- **License:** Academic free.
- **Story value:** Turn raw classical Chinese into structured entities (people/places/dates) for worldbuilding DBs.

#### 26. Dharma Drum / DILA authority databases
- **URL:** `https://authority.dila.edu.tw/`; Buddhist Studies Person/Place/Time Authority DBs.
- **Coverage:** Authority records for Buddhist persons, places, time periods, and a historical **gazetteer of China** (CHGIS-linked).
- **Access:** **REST / Linked Open Data + SPARQL** endpoints.
- **Format:** JSON / RDF / TEI.
- **License:** CC-BY.
- **Story value:** Reconcile names/places/dates across Buddhist Asia — a backbone gazetteer/authority.

#### 27. Kanripo / Zhonghua-style classics repos
- **URL:** `https://www.kanripo.org/` (Kanseki Repository).
- **Coverage:** Git-versioned premodern Chinese classics (Siku Quanshu-based catalog), aligned to CBETA where relevant.
- **Access:** **Git** + **IIIF** image links + simple REST.
- **Format:** Plaintext / TEI / KR-markup.
- **License:** CC / per-text.
- **Story value:** Versioned, citable classical Chinese texts you can diff and pin.

#### 28. Chinese Text Project (ctext) — baseline parity
- **URL / API:** `https://ctext.org/`; documented **REST API** (`/api`).
- **Coverage:** Pre-Qin and Han classics through later texts; large library.
- **Access:** **REST JSON** (rate-limited; optional API key/account raises limits).
- **License:** Data CC-BY-SA; some texts URN-stable.
- **Story value:** Included for parity — the cleanest API entry to core Chinese classics.

#### 29. chinese-poetry & classical corpora (GitHub)
- **URL:** GitHub `chinese-poetry/chinese-poetry` and related repos.
- **Coverage:** 300,000+ Tang/Song poems, Song ci, Yuan qu, Shijing, Lunyu, couplets.
- **Access:** **Bulk / Git**.
- **Format:** JSON.
- **License:** MIT-ish / open (verify).
- **Story value:** Drop-in quotation bank and naming/imagery source for Chinese settings.

---

### Japan / Southeast Asia

#### 30. Japan Search (ジャパンサーチ)
- **URL / API:** `https://jpsearch.go.jp/`; **REST API** and **SPARQL** endpoint.
- **Coverage:** National cross-domain aggregator (NDL-led): 20M+ items from libraries, museums, archives, broadcasters.
- **Access:** **REST** (search API) + **SPARQL** (LOD).
- **Format:** JSON / RDF.
- **License:** Metadata largely **CC0**; item rights vary.
- **Story value:** One stop for Japanese material across every domain — discovery + linked data.

#### 31. Aozora Bunko (青空文庫)
- **URL:** `https://www.aozora.gr.jp/`; GitHub `aozorabunko/aozorabunko`.
- **Coverage:** Public-domain Japanese literature (Sōseki, Akutagawa, Dazai, folktale collections, etc.).
- **Access:** **Bulk / Git / scrape**.
- **Format:** XHTML, TXT (legacy Shift-JIS / ruby markup).
- **License:** Public domain (expired-copyright works).
- **Story value:** Full-text classic Japanese fiction & essays — style, plot, period voice.

#### 32. NDL Digital Collections (国立国会図書館デジタルコレクション)
- **URL:** `https://dl.ndl.go.jp/`.
- **Coverage:** Scanned Japanese books, ukiyo-e, old maps, periodicals, premodern works.
- **Access:** **IIIF** + **OAI-PMH** + a search API.
- **Format:** IIIF / JSON / images.
- **License:** Public-domain items open; many in-copyright items gated. 🚩 (partial)
- **Story value:** Edo/Meiji print culture, woodblock imagery, historical maps.

#### 33. SEAlang Library
- **URL:** `http://www.sealang.net/`.
- **Coverage:** Dictionaries and text corpora for **Thai, Lao, Khmer, Burmese, Vietnamese, Mon, Shan, Lahu**, and more.
- **Access:** **Web query / REST-ish / scrape**; some downloadable resources.
- **Format:** Dictionary entries, concordances.
- **License:** Academic free use (verify per resource).
- **Story value:** The go-to lexical layer for mainland Southeast Asian languages — naming & idiom.

#### 34. ECAI — Electronic Cultural Atlas Initiative 🚩
- **URL:** `http://ecai.org/`.
- **Coverage:** Historical gazetteers, cultural atlases, Silk Road and maritime Asia datasets.
- **Access:** **Scrape / GIS downloads** (aging infrastructure). 🚩
- **Format:** Shapefile / KML / TMG.
- **License:** Mixed.
- **Story value:** Spatial-historical layers for Asian trade routes & cultural diffusion.

#### 35. Khmer / Thai heritage portals (SOAS, EFEO, inscriptions) 🚩
- **Examples:** Khmer inscriptions corpus (e.g., "SEAlang/SEAclassics", Cambodian inscriptions DB), Thai National Library, palm-leaf digitization projects.
- **Coverage:** Angkorian inscriptions, palm-leaf manuscripts, Thai royal chronicles.
- **Access:** **Scrape / IIIF** (project-dependent). 🚩
- **Format:** IIIF / PDF / TEI.
- **License:** Mixed.
- **Story value:** Primary epigraphy and chronicles — foundation myths of mainland SE Asian states.

#### 36. Vietnamese Nôm Preservation Foundation
- **URL:** `http://www.nomfoundation.org/`.
- **Coverage:** Chữ Nôm and Hán-Nôm texts (e.g., Tale of Kiều), Nôm lexicography, digitized woodblocks.
- **Access:** **Scrape / bulk**; online Nôm lookup tools.
- **Format:** Unicode (Nôm/Han), images, dictionaries.
- **License:** Free educational use.
- **Story value:** Vietnamese classical literature & script — unique East/SE-Asian crossover.

#### 37. Indonesia/Malay: Khastara (Perpusnas) & SEA digital mss 🚩
- **URLs:** `https://khastara.perpusnas.go.id/`; British Library Southeast Asian digitized mss; DREAMSEA project.
- **Coverage:** Javanese, Malay, Balinese, Batak manuscripts; lontar (palm-leaf); hikayat, babad, wayang sources.
- **Access:** **Scrape / IIIF** (DREAMSEA & BL provide IIIF). 🚩
- **Format:** IIIF / PDF / images.
- **License:** Gov't / project mixed.
- **Story value:** Malay/Javanese court chronicles & myth — gamelan-world fantasy material.

#### 38. SuttaCentral + Pali Tipitaka (VRI)
- **URL / API:** `https://suttacentral.net/`; **REST API** (`https://suttacentral.net/api/...`); GitHub `suttacentral/`.
- **Coverage:** Complete **Pali Canon** plus Āgama parallels in Chinese/Sanskrit/Tibetan, multilingual translations.
- **Access:** **REST JSON** + bulk data on GitHub.
- **Format:** JSON, with segment-level parallels.
- **License:** Texts/translations largely **CC0** (Bhikkhu Sujato et al.) / CC-BY — verify per text.
- **Story value:** Early Buddhist narrative (jātakas, suttas), parables, and cosmology with cross-language parallels.

---

### Africa

#### 39. Aluka (now within JSTOR / Artstor) 🚩
- **URL:** via `https://www.jstor.org/` (Aluka collections).
- **Coverage:** "African Cultural Heritage Sites," "Struggles for Freedom in Southern Africa," African plants, manuscripts.
- **Access:** **Login / subscription**; scrape blocked. 🚩
- **License:** Restricted (institutional).
- **Story value:** Curated African heritage & liberation-era primary sources.

#### 40. World Digital Library (WDL) — now at the Library of Congress
- **URL:** `https://www.loc.gov/collections/world-digital-library/`; legacy `wdl.org` redirected.
- **Coverage:** Global, with strong **African** manuscripts, maps, early prints, and oral-tradition documentation contributed by national libraries.
- **Access:** LOC provides **JSON** (`?fo=json`) and **IIIF**; legacy WDL API deprecated.
- **Format:** JSON / IIIF.
- **License:** Mostly public domain / partner-cleared.
- **Story value:** Trustworthy, well-described non-Western primary documents with images.

#### 41. Timbuktu manuscripts — SAVAMA-DCI & HMML vHMML 🚩
- **URLs:** `https://www.vhmml.org/` (HMML reading room); SAVAMA-DCI (Mali) digitization.
- **Coverage:** West African **Arabic and Ajami** manuscripts (Timbuktu, Djenné) — law, science, Sufism, history, poetry.
- **Access:** vHMML = **free account / login**, IIIF-like viewer; bulk restricted. 🚩
- **Format:** Images / IIIF; catalog metadata.
- **License:** Research access; reuse restricted.
- **Story value:** The legendary Saharan scholarly tradition — rich, underused setting & lore.

#### 42. EAP — Endangered Archives Programme (British Library)
- **URL:** `https://eap.bl.uk/`.
- **Coverage:** Digitized at-risk archives worldwide, heavy African/Asian/Latin-American representation — registers, photographs, oral-history transcripts, vernacular print.
- **Access:** **IIIF** + metadata; some **OAI** / scrape.
- **Format:** IIIF / images / PDF.
- **License:** Mostly open for non-commercial reuse — **verify per project**.
- **Story value:** Hyper-local primary material from communities rarely digitized elsewhere.

#### 43. DISA & South African digital archives 🚩
- **URLs:** DISA (Digital Innovation South Africa) `https://disa.ukzn.ac.za/`; SAHA (South African History Archive).
- **Coverage:** Anti-apartheid periodicals, struggle documents, social history.
- **Access:** **Scrape**; PDFs. 🚩
- **License:** Mixed.
- **Story value:** 20th-c. South African political and social narrative.

#### 44. African Storybook & open folktale corpora
- **URL:** `https://www.africanstorybook.org/`; related: Global African Storybook, StoryWeaver (multilingual).
- **Coverage:** Openly licensed African folktales and children's stories in 200+ languages.
- **Access:** **REST-ish / scrape**; EPUB/PDF downloads.
- **Format:** EPUB / PDF / TXT / illustrations.
- **License:** **CC-BY** (mostly).
- **Story value:** Directly reusable African oral-tradition narratives across many languages.

#### 45. ELAR (SOAS) & African language archives 🚩
- **URL:** `https://www.elararchive.org/`.
- **Coverage:** Endangered-language documentation incl. African oral epics, ritual speech, song.
- **Access:** **Login**, depositor-set protocols; ELAN/audio. 🚩
- **License:** Restricted by depositor; some open.
- **Story value:** Authentic oral-performance material (where access granted) — chant, epic, proverb.

---

### Latin America

#### 46. Biblioteca Virtual Miguel de Cervantes
- **URL:** `https://www.cervantesvirtual.com/`.
- **Coverage:** Spanish & Spanish-American literature, history, "Biblioteca Americana," chronicles of the Indies, indigenous-language doctrinal texts.
- **Access:** **OAI-PMH** + scrape; some TEI.
- **Format:** XML / HTML / TEI / PDF.
- **License:** Mostly free access (per item).
- **Story value:** Colonial chronicles, conquest narratives, early American history in Spanish.

#### 47. BNDigital — Biblioteca Nacional do Brasil 🚩
- **URLs:** `https://bndigital.bn.gov.br/`; **Hemeroteca Digital** `https://hemerotecadigital.bn.gov.br/`.
- **Coverage:** Brazilian newspapers/periodicals (Hemeroteca), colonial manuscripts, maps, iconography.
- **Access:** **Scrape**; IIIF in places. 🚩 No strong public API.
- **Format:** PDF / images / IIIF.
- **License:** Gov't, mixed.
- **Story value:** Brazilian press and colonial documents — Lusophone-Atlantic history.

#### 48. INAH / Mediateca (Mexico) 🚩
- **URL:** `https://mediateca.inah.gob.mx/`.
- **Coverage:** Mesoamerican archaeology, codices, ethnographic photos, audio, colonial documents.
- **Access:** **Scrape / IIIF**. 🚩
- **Format:** IIIF / images / audio.
- **License:** Gov't mixed (some open, some restricted reuse).
- **Story value:** Aztec/Maya/Mixtec material culture and codices — pre-Columbian worldbuilding.

#### 49. Mesoamerican codices (WDL / institutional IIIF)
- **Examples:** Codex Mendoza (Bodleian, IIIF), Codex Borgia, **Dresden Codex** (SLUB Dresden, IIIF), Codex Borbonicus, Florentine Codex (LOC/WDL).
- **Access:** **IIIF** at holding institutions.
- **Format:** IIIF / high-res JPEG.
- **License:** Mostly public domain (age); host terms vary.
- **Story value:** The actual pictorial codices — calendrics, deities, ritual, the Maya astronomical tables.

#### 50. FAMSI / Mesoweb / Maya glyph resources 🚩
- **URLs:** `http://www.famsi.org/`; `http://www.mesoweb.com/`.
- **Coverage:** Maya hieroglyphic catalogs, dictionaries, Popol Vuh editions, codex commentaries, Linda Schele drawings.
- **Access:** **Scrape**; PDF libraries. 🚩
- **License:** Academic/free for study.
- **Story value:** Deep reference for Maya myth (Popol Vuh), glyphs, and iconography.

#### 51. Latin American maps, doctrinas & early printing (aggregated)
- **Sources:** John Carter Brown Library (Archive of Early American Images), LOC, WDL, Primeros Libros (early Mexican imprints) `https://primeroslibros.org/`.
- **Coverage:** 16th–17th-c. American imprints, indigenous-language catechisms, conquest-era maps.
- **Access:** **IIIF / scrape**; Primeros Libros offers page images.
- **Format:** IIIF / images / TXT.
- **License:** Mostly public domain.
- **Story value:** First books of the Americas, including Nahuatl/Quechua/Maya-language texts.

#### 52. AILLA — Archive of the Indigenous Languages of Latin America 🚩
- **URL:** `https://ailla.utexas.org/`.
- **Coverage:** Audio/text recordings of indigenous American oral literature, narratives, songs.
- **Access:** **Login**; depositor-set access levels. 🚩
- **Format:** Audio / transcripts / ELAN.
- **License:** Depositor-controlled.
- **Story value:** Authentic indigenous oral narrative (where access granted).

---

### Oceania / Indigenous

#### 53. Trove (National Library of Australia)
- **URL / API:** `https://trove.nla.gov.au/`; **REST API v3** at `https://api.trove.nla.gov.au/`.
- **Coverage:** Newspapers (huge digitized run), books, manuscripts, maps, images, oral histories, Aboriginal & Torres Strait Islander material.
- **Access:** **REST** — requires a **free API key** (registration).
- **Format:** JSON / XML.
- **Rate:** Keyed; reasonable-use limits.
- **License:** Metadata mixed; **digitized newspapers largely public domain**; items vary.
- **Story value:** Unmatched depth of Australian historical press and primary sources.

#### 54. DigitalNZ
- **URL / API:** `https://digitalnz.org/`; **REST API** `https://api.digitalnz.org/`.
- **Coverage:** Aggregator across NZ libraries, museums, archives — Māori taonga, photos, newspapers (Papers Past), audio.
- **Access:** **REST** with **free API key**.
- **Format:** JSON.
- **License:** Per-record (mixed; many open).
- **Story value:** One-call gateway to Aotearoa/NZ cultural heritage incl. Māori material.

#### 55. Te Ara — The Encyclopedia of New Zealand
- **URL:** `https://teara.govt.nz/`.
- **Coverage:** Authored encyclopedia: Māori myth & tradition, settlement, biography, environment.
- **Access:** **Scrape**; some structured exports.
- **Format:** HTML (rich).
- **License:** Text typically **CC-BY-NC** (verify); images vary.
- **Story value:** Clean, reliable Māori mythology & NZ history essays for grounding.

#### 56. AIATSIS 🚩
- **URL:** `https://aiatsis.gov.au/`.
- **Coverage:** Australian Aboriginal and Torres Strait Islander languages, manuscripts, recordings, oral tradition.
- **Access:** **Catalog scrape**; much content under **cultural access protocols / login**. 🚩
- **License:** Culturally restricted (ICIP); respect protocols — **do not scrape sacred/restricted material**.
- **Story value:** Foundational Aboriginal cultural knowledge — handle with care and consent.

#### 57. Pacific Manuscripts Bureau (PAMBU) / ANU Pacific 🚩
- **URL:** `https://pambu.anu.edu.au/`.
- **Coverage:** Pacific Islands mission records, colonial administration, traders' journals, oral-history transcriptions.
- **Access:** **Scrape / microfilm-derived PDFs**. 🚩
- **License:** Mixed.
- **Story value:** Primary documentation of Pacific island histories and contact narratives.

#### 58. PARADISEC
- **URL:** `https://www.paradisec.org.au/`.
- **Coverage:** Endangered languages & music of the Pacific and beyond — chants, epics, oral literature recordings.
- **Access:** **OAI / REST-ish** catalog; some open, some login.
- **Format:** Audio / metadata / transcripts.
- **License:** CC / depositor-set.
- **Story value:** Oceanic oral-performance corpus — song, myth, language.

#### 59. NZETC — New Zealand Electronic Text Collection
- **URL:** `https://nzetc.victoria.ac.nz/`.
- **Coverage:** Full-text NZ and Pacific historical works, including Māori-language texts and early ethnography (e.g., Grey's mythology).
- **Access:** **Bulk / scrape**; TEI.
- **Format:** TEI-XML / HTML.
- **License:** Mostly free use (per item).
- **Story value:** Searchable full text of classic NZ/Pacific sources incl. recorded Māori traditions.

---

### Cross-cutting global

#### 60. Internet Archive
- **URL / API:** `https://archive.org/`; advanced search JSON, `/metadata/{id}`, scraping API, S3-like `ia` CLI.
- **Coverage:** Universal — scanned books (every region), audio, film, software, web (Wayback).
- **Access:** **REST + bulk**; optional keys for upload/large pulls.
- **Format:** JSON + every media type.
- **License:** Public domain / CC / mixed per item.
- **Story value:** The catch-all when a national portal lacks an API — usually mirrors it.

#### 61. UNESCO Memory of the World 🚩
- **URL:** `https://www.unesco.org/en/memory-world`.
- **Coverage:** Register of documentary heritage of world significance (nominations, descriptions).
- **Access:** **Scrape**; no data API. 🚩
- **Format:** HTML / PDF.
- **License:** Catalog/descriptions open.
- **Story value:** Curated shortlist pointing you to the world's most significant documents and where they live.

#### 62. World Historical Gazetteer (WHG)
- **URL / API:** `https://whgazetteer.org/`; **REST API** + bulk **Linked Places Format (LPF)** GeoJSON.
- **Coverage:** Place names **across time** with temporal attestations and links to other gazetteers.
- **Access:** **REST + bulk**; optional account for contributions.
- **Format:** JSON / LPF GeoJSON.
- **License:** **CC-BY**.
- **Story value:** Period-correct place names and locations — avoid anachronistic geography.

#### 63. Pleiades
- **URL / API:** `https://pleiades.stoa.org/`; JSON per place, bulk dumps, RDF.
- **Coverage:** Ancient-world places (originally Greco-Roman; expanding to ancient Near East, etc.).
- **Access:** **REST + bulk + RDF**.
- **Format:** JSON / CSV / RDF.
- **License:** **CC-BY**.
- **Story value:** Authoritative ancient toponyms and coordinates for historical fiction.

#### 64. GeoNames
- **URL / API:** `https://www.geonames.org/`; REST web services.
- **Coverage:** ~12M modern place names worldwide, admin hierarchy, alternate names, population, elevation.
- **Access:** **REST** — requires a **free username** parameter; daily credit limits.
- **Format:** JSON / XML; full **bulk dumps** downloadable.
- **License:** **CC-BY**.
- **Story value:** Realistic modern settings, multilingual place-name variants for naming.

#### 65. OpenStreetMap / Overpass API
- **URL / API:** Overpass `https://overpass-api.de/api/interpreter` (Overpass QL); Nominatim for geocoding.
- **Coverage:** Live global map features — roads, rivers, buildings, POIs, admin boundaries.
- **Access:** **REST** (no key; shared instances rate-limited — self-host for heavy use).
- **Format:** JSON / XML.
- **License:** **ODbL** (attribution + share-alike for derived DBs).
- **Story value:** Ground real-world settings in accurate geography and infrastructure.

#### 66. Wikidata
- **URL / API:** `https://query.wikidata.org/sparql`; REST/MediaWiki API; bulk dumps.
- **Coverage:** Universal structured knowledge graph — people, places, events, works, with cross-language labels and source links.
- **Access:** **SPARQL + REST + bulk**.
- **Format:** JSON / RDF.
- **License:** **CC0**.
- **Story value:** Glue layer — reconcile any entity across all the regional sources above.

#### 67. DBpedia / EventKG
- **URLs:** `https://dbpedia.org/sparql`; EventKG (L3S) RDF dumps.
- **Coverage:** Structured Wikipedia knowledge; **EventKG** = cross-lingual events & temporal relations from Wikipedia/Wikidata/news.
- **Access:** **SPARQL + bulk**.
- **Format:** RDF / JSON.
- **License:** CC-BY-SA.
- **Story value:** Build historical **timelines** and event chains for plotting across cultures.

#### 68. Wiktionary / etymology datasets
- **Sources:** Wiktionary dumps; **etymwn** (Etymological Wordnet); **Kaikki.org** machine-readable Wiktionary (JSONL).
- **Coverage:** Word definitions, pronunciations, **etymologies**, cognates across thousands of languages.
- **Access:** **Bulk** (Kaikki JSONL, dumps) + Wiktionary REST.
- **Format:** JSON / JSONL / dumps.
- **License:** **CC-BY-SA**.
- **Story value:** Construct believable invented words/names rooted in real linguistic patterns.

#### 69. Behind the Name
- **URL / API:** `https://www.behindthename.com/`; documented **REST API**.
- **Coverage:** Etymology, meaning, history, and cultural usage of given names (and surnames via Surname site).
- **Access:** **REST** — **free API key** (rate-limited tiers).
- **Format:** JSON / XML.
- **License:** Data under site ToS (not open) 🚩 — fine for app use within limits, not for redistribution.
- **Story value:** Culturally appropriate character names with real meaning across regions.

#### 70. GBIF — Global Biodiversity Information Facility
- **URL / API:** `https://www.gbif.org/`; **REST API** `https://api.gbif.org/v1/`.
- **Coverage:** ~2B+ species occurrence records + taxonomic backbone, by location and (for occurrences) date.
- **Access:** **REST** (open; key only for large downloads/account).
- **Format:** JSON / Darwin Core.
- **License:** Records CC0 / CC-BY / CC-BY-NC (per dataset).
- **Story value:** Populate a region's real flora & fauna for ecologically grounded worldbuilding.

#### 71. NASA APIs
- **URLs:** `https://api.nasa.gov/` (APOD, etc.); **Exoplanet Archive** TAP; **JPL Horizons** ephemerides; SBDB.
- **Coverage:** Astronomy imagery, exoplanet catalog, precise solar-system ephemerides, small-body data.
- **Access:** **REST/TAP** — `DEMO_KEY` works; free **API key** for higher limits.
- **Format:** JSON / CSV / VOTable.
- **License:** US-government public domain.
- **Story value:** Accurate skies, planets, and orbital mechanics for hard SF.

#### 72. DPLA & Europeana (parity anchors)
- **URLs:** `https://dp.la/` (REST API, free key); `https://www.europeana.eu/` (REST API, free key; reaches Eastern Europe, Baltics, Balkans).
- **Coverage:** Large aggregators (US / Europe) — included as cross-check and for Eastern-European reach.
- **Access:** **REST**, free API keys.
- **Format:** JSON.
- **License:** Metadata **CC0**; items vary.
- **Story value:** Reconciliation and gap-filling against the regional sources above; Europeana adds Slavic/Baltic/Balkan material.

---

## Practical notes for the platform

- **Cleanest programmatic wins (real JSON REST, keys easy/none):** Ganjoor (Persian poetry), SuttaCentral (Pali), CBDB (Chinese biography), ctext, Japan Search, Trove (key), DigitalNZ (key), Internet Archive, Wikidata/SPARQL, World Historical Gazetteer, Pleiades, GeoNames (username), GBIF, NASA, chinese-poetry/OpenITI/CBETA/Aozora via Git bulk.
- **Best for primary *images* (IIIF):** Qatar Digital Library, NDL (Japan), EAP, INAH/Mediateca, Mesoamerican codices at host institutions, DREAMSEA (SE Asia mss).
- **Heaviest friction (🚩 scrape/login/unclear license):** Shamela, Academia Sinica Scripta Sinica, Indian Culture Portal, Aluka/JSTOR, vHMML/Timbuktu, AIATSIS, AILLA/ELAR/PARADISEC (depositor-gated), BNDigital, INAH (reuse), HathiTrust full text.
- **Cultural-sensitivity flag:** AIATSIS, AILLA, ELAR, PARADISEC, and many oral-tradition archives carry **Indigenous Cultural & Intellectual Property** protocols. Treat restricted/sacred material as off-limits absent explicit permission; this is an ethical constraint, not just a technical one.
- **Bulk corpora to ingest first (high story density, open-ish):** OpenITI (Arabic/Persian), CBETA (Chinese Buddhist), GRETIL/SARIT/DCS (Sanskrit), Project Madurai (Tamil), chinese-poetry, Aozora (Japanese), SuttaCentral (Pali), African Storybook (folktales), NZETC (NZ/Pacific).
- **Geo/timeline backbone:** Wikidata + World Historical Gazetteer + Pleiades + GeoNames + DILA/CHGIS gazetteer + EventKG, reconciled via Wikidata QIDs.

> Re-verify every endpoint, auth requirement, rate limit, and especially **license** before ingesting or
> redistributing. Several "APIs" above are IIIF/OAI/SPARQL rather than REST JSON, and a few portals
> (DLI, legacy WDL) have moved or partly died since training.

# Public-Domain & Full-Text Literature Sources

> Domain focus: **the actual novels/stories/texts** (full source material), plus the
> metadata catalogs that index them. Compiled for a "story source material" platform.
>
> ⚠️ **VERIFICATION STATUS — READ FIRST.** This catalog was compiled from model knowledge
> (knowledge cutoff January 2026). In this session **all network tools were unavailable**
> (WebSearch, WebFetch, and outbound HTTP via shell were denied), so **none of the
> endpoints, rate limits, or license terms below were live-verified against their 2026
> state.** Treat every endpoint, limit, and term as *expected / last-known* and re-confirm
> with a live request before relying on it in production. Items most likely to drift
> (rate limits, auth requirements, daily quotas) are flagged inline with ⚠️.
>
> Last compiled: 2026-06-20

---

## Quick-reference table

| # | Source | Type | Access method | Format(s) | Auth | License | Full text? |
|---|--------|------|---------------|-----------|------|---------|------------|
| 1 | Project Gutenberg (via Gutendex) | Texts + metadata | REST (Gutendex), bulk mirror, OPDS | TXT, EPUB, HTML, JSON meta | None | Public domain (US) | ✅ Full text |
| 2 | Standard Ebooks | Texts | OPDS feed, bulk, GitHub | EPUB, AZW3, TXT, TEI-ish XML | None | Public domain (CC0 markup) | ✅ Full text |
| 3 | Wikisource | Texts | MediaWiki Action API + REST | Wikitext, HTML, JSON | None (key optional) | CC BY-SA 4.0 / PD | ✅ Full text |
| 4 | Open Library | Metadata (+ IA links) | REST + bulk dumps | JSON | None | Data: CC0 | ◐ Metadata; text via IA |
| 5 | Internet Archive | Texts + metadata | advancedsearch + metadata + download APIs | TXT, EPUB, PDF, DjVu, JSON | None (S3-style keys for write) | Mixed (per-item) | ✅ Full text (PD items) |
| 6 | HathiTrust | Metadata + limited text | Bibliographic API, Data API | JSON, page images, OCR (gated) | Partner/key for Data API | Mixed; access-restricted | ◐ Mostly metadata + gated text |
| 7 | Google Books | Metadata (+ some text) | REST API | JSON | API key (optional, raises quota) | Mixed; snippets unless PD | ◐ Metadata; full text only for PD/free |
| 8 | Folger Shakespeare (Folger Digital Texts) | Texts | Static endpoints / bulk download | TXT, HTML, XML (TEI), PDF, DOC | None | CC BY-NC | ✅ Full Shakespeare |
| 9 | PoetryDB | Texts | REST | JSON, text | None | Public domain content | ✅ Full poems |
| 10 | Poetry Foundation | Texts (site) | Website / scraping only | HTML | None API | Copyrighted (mixed) | ◐ Read on site; no open API |
| 11 | 青空文庫 Aozora Bunko (JP) | Texts | Bulk (GitHub/Git), per-work HTML/zip | TXT (Shift-JIS), XHTML | None | Public domain / CC | ✅ Full text (Japanese) |
| 12 | Gallica / BnF (FR) | Texts + metadata | SRU, IIIF, OAI-PMH, Document API | JPEG, ALTO/OCR XML, TXT, IIIF | None | Mixed (PD marque) | ✅ Full text (OCR, French+) |
| 13 | Deutsches Textarchiv (DE) | Texts | REST/DDC, OAI-PMH, bulk | TEI-P5 XML, TXT, HTML | None | CC BY-SA / CC BY-NC | ✅ Full text (German) |
| 14 | Biblioteca Virtual Miguel de Cervantes (ES) | Texts + metadata | OAI-PMH, web | HTML, TEI, PDF | None | Mixed | ✅ Full text (Spanish) |
| 15 | Perseus Digital Library | Texts | Hopper site, CTS API, bulk (GitHub) | TEI XML, TXT | None | CC BY-SA / CC BY-NC-SA | ✅ Full classical texts |
| 16 | Sacred-Texts / mythology corpora | Texts | Website / scraping; some bulk | HTML, TXT | None | Mostly PD | ✅ Myth/epic full texts |
| 17 | Grimm / Andersen / folktale corpora | Texts | Via Gutenberg, Wikisource, GitHub | TXT, JSON | None | Public domain | ✅ Full fairy-tale texts |
| 18 | DPLA (Digital Public Library of America) | Metadata | REST API | JSON | API key (free) | Data: CC0 | ◐ Metadata; links out |
| 19 | Europeana | Metadata (+ links) | REST API | JSON | API key (free) | Data: CC0 | ◐ Metadata; links out |
| 20 | Open Library Inside / IA full-text search | Text search | search-inside API | JSON | None | per-item | ✅ Searches full text |

Legend: ✅ full source text available · ◐ metadata-only or gated/partial text.

---

## 1. Project Gutenberg + Gutendex

- **Official name:** Project Gutenberg; **Gutendex** (community JSON API mirror of the PG catalog).
- **URLs / endpoints:**
  - Gutendex: `https://gutendex.com/books/` (e.g. `?search=dickens`, `?languages=en,fr`,
    `?topic=children`, `?author_year_start=1800`, `?ids=1342,11`, `?sort=popular`).
  - Main site / mirrors: `https://www.gutenberg.org/`, robust mirror list at
    `https://www.gutenberg.org/MIRRORS.ALL`.
  - Per-book files: `https://www.gutenberg.org/files/{id}/...` and
    `https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt`.
  - Catalog feeds: RDF/XML bulk catalog (`https://www.gutenberg.org/cache/epub/feeds/`),
    OPDS feed (`https://www.gutenberg.org/ebooks/search.opds/`).
- **Coverage:** ~70,000+ full-text ebooks (≈75k by 2026 ⚠️). Mostly English, but
  substantial French, German, Finnish, Dutch, Italian, Portuguese, Spanish, Chinese and
  others. Works are US-public-domain (pre-1929 by the time of compilation, plus older).
- **Access method:** REST JSON (Gutendex), OPDS, direct file download, full bulk mirror
  (rsync/HTTP), RDF catalog dump.
- **Data format:** Plain text (UTF-8 and Latin-1), EPUB, Kindle, HTML; metadata as JSON
  (Gutendex) or RDF/XML (official catalog).
- **Auth / API key:** None.
- **Rate limits:** Gutendex has no documented hard limit but is a small volunteer service —
  be polite (cache, low concurrency). ⚠️ PG itself **blocks automated bulk crawling of the
  main web host**; for bulk you MUST use a mirror or the published catalog dumps, not scrape
  `gutenberg.org`.
- **License / terms:** Texts are public domain in the US; the Project Gutenberg *trademark*
  and the small PG license header impose conditions if you redistribute *with* the PG
  branding. Strip the header/trademark to use the bare public-domain text freely.
- **Value for story creation:** ⭐ Top-tier. Clean full novels, plays, poems, folktales —
  the workhorse source of raw narrative text. Includes Grimm, Andersen, Homer, Beowulf, etc.

---

## 2. Standard Ebooks

- **Official name:** Standard Ebooks.
- **URLs / endpoints:**
  - OPDS catalog: `https://standardebooks.org/opds` (and `/opds/all`).
  - RSS/Atom new-releases feed; per-book pages `https://standardebooks.org/ebooks/{author}/{title}`.
  - Source markup on GitHub: `https://github.com/standardebooks` (one repo per book, TEI-ish XHTML/CSS).
- **Coverage:** Curated, carefully typeset editions of public-domain works; on the order of
  ~1,000+ titles (smaller, high-quality subset of Gutenberg-class works). English-dominant.
- **Access method:** OPDS feed (machine-readable catalog), direct EPUB/AZW3/TXT download,
  Git clone of source repos, bulk.
- **Data format:** EPUB3, AZW3 (Kindle), advanced/compatible EPUB, plain TXT; source is
  semantic XHTML close to TEI.
- **Auth / API key:** None.
- **Rate limits:** No formal API limits; respect the OPDS feed and avoid hammering. ⚠️ verify.
- **License / terms:** All releases are public domain; Standard Ebooks dedicates its own
  editorial/markup contributions to the public domain (CC0). Effectively unrestricted reuse.
- **Value for story creation:** ⭐ Excellent. Best-quality, well-structured full texts; the
  semantic markup makes chapter/section parsing easy. Smaller catalog than Gutenberg.

---

## 3. Wikisource

- **Official name:** Wikisource (Wikimedia project), per-language subdomains.
- **URLs / endpoints:**
  - Action API: `https://en.wikisource.org/w/api.php` (e.g.
    `?action=query&prop=extracts|revisions&rvprop=content&format=json&titles=...`).
  - REST: `https://en.wikisource.org/w/rest.php/v1/page/{title}`.
  - Per-language hosts: `de.wikisource.org`, `fr.wikisource.org`, `zh.wikisource.org`, etc.,
    plus multilingual `wikisource.org`.
  - Bulk: Wikimedia dumps at `https://dumps.wikimedia.org/`.
- **Coverage:** Huge multilingual library of transcribed public-domain texts (literature,
  religious/sacred texts, historical documents, plays, poetry). 70+ language editions.
- **Access method:** MediaWiki Action API, REST API, OAI-PMH (limited), full XML dumps.
- **Data format:** Wikitext, rendered HTML, JSON (via API). Quality varies (proofread vs not;
  "Validated"/"Proofread" page-status flags help).
- **Auth / API key:** None for reads (optional OAuth/key for higher-volume etiquette).
- **Rate limits:** Wikimedia API etiquette — set a descriptive `User-Agent`, serial requests,
  use `maxlag`. ⚠️ Honor the Wikimedia user-agent policy or get blocked.
- **License / terms:** Mostly CC BY-SA 4.0 on the transcriptions; underlying works are public
  domain. Attribution + share-alike applies to the wiki text layer.
- **Value for story creation:** ⭐ Strong for multilingual and harder-to-find texts (sacred
  texts, regional folklore). Markup cleanup needed; coverage and quality uneven.

---

## 4. Open Library

- **Official name:** Open Library (Internet Archive project).
- **URLs / endpoints:**
  - Search: `https://openlibrary.org/search.json?q=...`.
  - Works/editions: `https://openlibrary.org/works/{OLID}.json`, `/books/{OLID}.json`.
  - Books API: `https://openlibrary.org/api/books?bibkeys=ISBN:...&format=json&jscmd=data`.
  - Covers: `https://covers.openlibrary.org/b/id/{id}-L.jpg`.
  - Bulk dumps: `https://openlibrary.org/developers/dumps`.
- **Coverage:** ~20M+ book records (metadata) spanning all periods/languages; links to
  readable/borrowable copies on Internet Archive where available.
- **Access method:** REST JSON, bulk data dumps.
- **Data format:** JSON metadata; cover images.
- **Auth / API key:** None.
- **Rate limits:** Be reasonable; ⚠️ heavy automated use should prefer the bulk dumps.
- **License / terms:** Catalog data is CC0 / open. Linked book *content* follows IA's
  per-item terms (PD vs lending).
- **Value for story creation:** ◐ Metadata/discovery layer (find a work, get its IA id),
  not a full-text source by itself. Pair with Internet Archive for the actual text.

---

## 5. Internet Archive

- **Official name:** Internet Archive (archive.org).
- **URLs / endpoints:**
  - Advanced search: `https://archive.org/advancedsearch.php?q=...&fl[]=identifier&output=json`.
  - Metadata: `https://archive.org/metadata/{identifier}`.
  - File download: `https://archive.org/download/{identifier}/{file}`.
  - Full-text "search inside": `https://ia.../BookReader/...search` style endpoints.
  - Scholar/Books interfaces and the `internetarchive` Python CLI/library.
- **Coverage:** Millions of digitized books/texts, many languages and centuries; includes
  scans of works not on Gutenberg. Quality ranges from clean to raw OCR.
- **Access method:** REST (search + metadata + download), S3-like API for uploads,
  `internetarchive` CLI, bulk.
- **Data format:** Plain text (`*_djvu.txt`), EPUB, PDF, DjVu, full-text OCR; JSON metadata.
- **Auth / API key:** None for reading public items; S3-style keys for upload/write.
- **Rate limits:** No hard public number, but throttling exists; ⚠️ be gentle, use the
  metadata API rather than scraping pages, and cache.
- **License / terms:** **Per-item** — public domain, CC, or in-copyright (lending only).
  You must check each item's rights; do not assume PD.
- **Value for story creation:** ⭐ Huge full-text reservoir, especially for obscure/older/
  non-English works. OCR cleanliness varies; rights vary per item (filter carefully).

---

## 6. HathiTrust

- **Official name:** HathiTrust Digital Library.
- **URLs / endpoints:**
  - Bibliographic API: `https://catalog.hathitrust.org/api/volumes/...` (brief/full JSON).
  - Data API: `https://www.hathitrust.org/data_api` (page images, OCR, METS) — gated.
  - HathiTrust Research Center (HTRC) for computational/non-consumptive analysis.
- **Coverage:** ~17M+ volumes (largest academic digitized corpus); many languages. A large
  fraction is in-copyright and **not** full-text downloadable.
- **Access method:** Bibliographic REST API (open); Data API (restricted, needs credentials
  / partner status); HTRC capsules for "non-consumptive" research on restricted text.
- **Data format:** JSON metadata; page images + OCR text + METS (Data API, gated).
- **Auth / API key:** Bibliographic API is open; **Data API requires authenticated
  partner/institutional access** (OAuth keys). ⚠️ Strong access gating.
- **Rate limits:** Defined per access tier / agreement. ⚠️ verify with your credentials.
- **License / terms:** Mixed; in-copyright items are access-restricted. Public-domain volume
  access is broader but still governed by HathiTrust terms.
- **Value for story creation:** ◐ Excellent *discovery* + some PD full text, but the openly
  downloadable full-text portion is limited; most value needs institutional access. Not a
  drop-in open full-text source.

---

## 7. Google Books

- **Official name:** Google Books API.
- **URLs / endpoints:**
  - Volumes: `https://www.googleapis.com/books/v1/volumes?q=...`.
  - Single volume: `https://www.googleapis.com/books/v1/volumes/{volumeId}`.
- **Coverage:** Tens of millions of titles, all languages/eras. Full text only for
  public-domain or explicitly free titles; otherwise snippets/previews.
- **Access method:** REST JSON.
- **Data format:** JSON metadata; for PD/free books, links to EPUB/PDF and limited text
  access fields.
- **Auth / API key:** Works without a key at low volume; **an API key (free) raises quotas**
  and is recommended. OAuth needed for user-bookshelf operations.
- **Rate limits:** ⚠️ Default ~1,000 requests/day/project without extra quota; tune in Google
  Cloud console. Verify current numbers.
- **License / terms:** Mixed/per-volume; honor Google Books API ToS. Full-content access only
  where the volume is PD/free.
- **Value for story creation:** ◐ Strong metadata + good for confirming PD status and finding
  EPUB/PDF of PD titles. Not a bulk full-text feed.

---

## 8. Folger Shakespeare (Folger Digital Texts)

- **Official name:** Folger Shakespeare Library — Folger Digital Texts / "The Folger
  Shakespeare."
- **URLs / endpoints:**
  - `https://www.folger.edu/explore/shakespeares-works/...` and
    `https://shakespeare.folger.edu/` per-play pages with download links.
  - Folger Digital Texts downloads: TXT/HTML/XML(TEI)/PDF/DOC per play, plus a complete set.
  - (Historically a Folger API existed at `www.folgerdigitaltexts.org`; ⚠️ confirm the
    current host/endpoint — Folger has reorganized its site.)
- **Coverage:** The complete works of Shakespeare (all plays + poems/sonnets), professionally
  edited, with line/act/scene structure and encoded characters.
- **Access method:** Direct file download (per work + complete corpus); machine-readable
  TEI-XML; previously a simple API for fetching texts/word indices.
- **Data format:** Plain text, HTML, **TEI-P5 XML** (richly tagged: speakers, line numbers,
  stage directions), PDF, DOC.
- **Auth / API key:** None.
- **Rate limits:** None significant for the static downloads. ⚠️ verify if using any API host.
- **License / terms:** **CC BY-NC** (non-commercial reuse with attribution). ⚠️ The NC clause
  matters for a commercial story platform — Shakespeare's text is PD, but the *Folger edition/
  encoding* is CC BY-NC. For commercial use, prefer PD-only editions (Gutenberg/MIT) or
  confirm licensing.
- **Value for story creation:** ⭐ Gold-standard structured Shakespeare (great for
  scene/character parsing). Watch the NC license for commercial products.

---

## 9. PoetryDB

- **Official name:** PoetryDB.
- **URLs / endpoints:** `https://poetrydb.org/`
  - By author: `https://poetrydb.org/author/Emily%20Dickinson`.
  - By title: `https://poetrydb.org/title/Ozymandias`.
  - Combined / field selection: `https://poetrydb.org/author,title/Shakespeare;Sonnet`.
  - Line counts, random: `https://poetrydb.org/linecount/14`, `https://poetrydb.org/random/5`.
  - List authors: `https://poetrydb.org/author`.
- **Coverage:** Thousands of poems (~3,000+) from classic public-domain poets (English-language
  canon: Shakespeare, Dickinson, Keats, Frost-era PD, etc.).
- **Access method:** REST JSON (very simple, path-based query DSL).
- **Data format:** JSON (title, author, lines[], linecount); `.text` output option for plain.
- **Auth / API key:** None.
- **Rate limits:** None documented; small open service — cache and be polite. ⚠️ verify.
- **License / terms:** Underlying poems are public domain; the project/code is open
  (MIT-licensed software). Effectively free to use.
- **Value for story creation:** ⭐ Easiest poetry full-text API; great for epigraphs, verse
  inserts, poetic source material. Limited to its (English, classic) corpus.

---

## 10. Poetry Foundation

- **Official name:** Poetry Foundation (poetryfoundation.org).
- **URLs / endpoints:** Website only (`https://www.poetryfoundation.org/poems/...`). **No
  official public API.** A well-known Kaggle dataset of scraped Poetry Foundation poems exists
  for research.
- **Coverage:** Very large modern + classic poetry archive, including many **in-copyright**
  contemporary poems.
- **Access method:** Web reading / scraping only (no documented API).
- **Data format:** HTML.
- **Auth / API key:** N/A.
- **Rate limits:** N/A (respect robots.txt / ToS if scraping).
- **License / terms:** ⚠️ Much content is copyrighted; reuse is restricted. Not a safe bulk
  source for a commercial platform.
- **Value for story creation:** ◐ Great for human browsing/discovery; **not** an open
  full-text source. Prefer PoetryDB/Gutenberg/Wikisource for reusable poetry text.

---

## 11. 青空文庫 Aozora Bunko (Japanese)

- **Official name:** 青空文庫 (Aozora Bunko).
- **URLs / endpoints:**
  - `https://www.aozora.gr.jp/` (per-work HTML + zipped TXT).
  - Bulk repository (GitHub): `https://github.com/aozorabunko/aozorabunko` (full content +
    `list_person_all_extended_utf8.csv` index).
  - Community JSON index (Aozora "API"-style): `https://pubserver1.herokuapp.com/` style
    mirrors / `https://github.com/aozorahack` tooling. ⚠️ confirm current mirror.
- **Coverage:** ~16,000+ Japanese public-domain literary works (Natsume Sōseki, Akutagawa,
  Dazai, Miyazawa, etc.).
- **Access method:** Per-work download, **full bulk via Git/GitHub**, community APIs.
- **Data format:** Plain text (often **Shift-JIS**; UTF-8 in the GitHub repo), XHTML with
  ruby/furigana markup.
- **Auth / API key:** None.
- **Rate limits:** Use the GitHub repo for bulk rather than crawling the site. ⚠️ verify.
- **License / terms:** Public domain or Aozora's CC-style terms (per-work; check the work's
  rights footer). Most are PD.
- **Value for story creation:** ⭐ The definitive open Japanese literature corpus. Mind the
  encoding and ruby markup when extracting clean text.

---

## 12. Gallica / BnF (French)

- **Official name:** Gallica (Bibliothèque nationale de France digital library).
- **URLs / endpoints:**
  - SRU search: `https://gallica.bnf.fr/SRU?operation=searchRetrieve&query=...`.
  - Document/IIIF APIs: `https://gallica.bnf.fr/iiif/ark:/12148/{ark}/...`,
    OCR text via `.../texteBrut`, page images, pagination/OAI services.
  - OAI-PMH: `https://oai.bnf.fr/oai2/OAIHandler`.
  - data.bnf.fr for linked-data author/work metadata.
- **Coverage:** Millions of digitized documents — books, manuscripts, periodicals, maps —
  predominantly French but multilingual; deep historical range.
- **Access method:** SRU, IIIF Image/Presentation, OAI-PMH, document/OCR REST endpoints, bulk.
- **Data format:** JPEG/IIIF images, **ALTO/OCR XML**, plain OCR text (`texteBrut`), JSON/XML
  metadata.
- **Auth / API key:** None for the open APIs.
- **Rate limits:** Be reasonable; ⚠️ heavy IIIF/OCR pulling should be throttled. Verify.
- **License / terms:** Mixed; many items carry the French **"marque PD"** (public domain).
  Commercial reuse of some digitizations has historically had conditions — check per item.
- **Value for story creation:** ⭐ Premier French-language full-text/OCR source, plus rare
  historical material. OCR quality varies by scan age.

---

## 13. Deutsches Textarchiv (DTA, German)

- **Official name:** Deutsches Textarchiv (German Text Archive), BBAW.
- **URLs / endpoints:**
  - `https://www.deutschestextarchiv.de/` with REST/DDC query interface, per-work TEI/TXT/HTML
    downloads, and a documented API/`/api/` + OAI-PMH endpoint.
  - Corpus bulk download of the full TEI corpus.
- **Coverage:** ~1,500–4,500+ carefully edited German works (~1600–1900), forming a balanced
  reference corpus of German.
- **Access method:** REST query API, OAI-PMH, full bulk corpus download.
- **Data format:** **TEI-P5 XML** (high quality), plain text, HTML.
- **Auth / API key:** None.
- **Rate limits:** None significant for bulk; ⚠️ verify API etiquette.
- **License / terms:** Mostly **CC BY-SA** (some CC BY-NC); underlying works PD. Attribution +
  share-alike on the editions.
- **Value for story creation:** ⭐ Best-structured open German literary corpus; excellent for
  clean, linguistically tagged full text.

---

## 14. Biblioteca Virtual Miguel de Cervantes (Spanish)

- **Official name:** Biblioteca Virtual Miguel de Cervantes (BVMC).
- **URLs / endpoints:**
  - `https://www.cervantesvirtual.com/` per-work pages with HTML/PDF/TEI.
  - OAI-PMH endpoint for metadata harvesting; linked-data `data.cervantesvirtual.com`.
- **Coverage:** Large Spanish/Iberian + Latin American literature collection (Cervantes, Lope,
  Golden Age, modern PD authors), plus catalan/other Iberian languages.
- **Access method:** OAI-PMH (metadata), web download (full text), some TEI.
- **Data format:** HTML, **TEI XML**, PDF; OAI metadata as Dublin Core / MARC-XML.
- **Auth / API key:** None.
- **Rate limits:** ⚠️ verify; harvest via OAI-PMH rather than scraping.
- **License / terms:** Mixed; many items reusable but **check per-item rights** (some
  digitizations restricted).
- **Value for story creation:** ⭐ Leading open Spanish-language full-text library. Less of a
  clean single REST API; OAI + page download is the main path.

---

## 15. Perseus Digital Library

- **Official name:** Perseus Digital Library (Tufts).
- **URLs / endpoints:**
  - Hopper: `http://www.perseus.tufts.edu/hopper/`.
  - **CTS API** (Canonical Text Services) via the Scaife viewer / `https://scaife.perseus.org/`.
  - Bulk/source on GitHub: `https://github.com/PerseusDL` (canonical-greekLit, canonical-latinLit).
- **Coverage:** Greek and Latin classical texts (Homer, Iliad/Odyssey, Hesiod, Virgil, Ovid,
  etc.) with originals + many English translations; plus Arabic/other collections.
- **Access method:** CTS API (URN-addressable passages), website, full bulk via GitHub.
- **Data format:** **TEI XML** (canonical, citation-addressable), plain text.
- **Auth / API key:** None.
- **Rate limits:** Use GitHub bulk for large pulls; ⚠️ verify CTS endpoint etiquette.
- **License / terms:** Mostly **CC BY-SA / CC BY-NC-SA** depending on text; many translations
  reusable with attribution. Check per text.
- **Value for story creation:** ⭐ Best structured source for Greek/Roman myth + epic
  (Iliad, Odyssey, Aeneid, Metamorphoses) with passage-level addressing.

---

## 16. Mythology / sacred-text corpora (Internet Sacred Text Archive et al.)

- **Official name:** Internet Sacred Text Archive (sacred-texts.com) and similar mythology
  repositories.
- **URLs / endpoints:** `https://www.sacred-texts.com/` (HTML pages by tradition);
  no formal API. Many texts also mirror to Gutenberg/Wikisource.
- **Coverage:** World mythology, religion, folklore, epics — Mahabharata, Ramayana, Gilgamesh,
  Eddas, Kalevala, Popol Vuh, Egyptian/Mesopotamian myth, etc.
- **Access method:** Website / scraping; many individual texts also obtainable from Gutenberg
  or Wikisource (preferred, cleaner).
- **Data format:** HTML, some plain text.
- **Auth / API key:** None.
- **Rate limits:** Respect the site; prefer the Gutenberg/Wikisource copies for bulk.
- **License / terms:** Underlying texts mostly **public domain** (old translations); the
  archive's own pages are PD-leaning but verify.
- **Value for story creation:** ⭐ Convenient one-stop index for myth/epic source texts. For
  reuse, pull the equivalent Gutenberg/Wikisource edition where possible.

### Specific epics — where to get clean full text

| Epic | Best open full-text source(s) |
|------|-------------------------------|
| Iliad / Odyssey | Gutenberg (multiple translations), Perseus (Greek + Eng), Standard Ebooks |
| Aeneid / Metamorphoses | Gutenberg, Perseus (Latin + Eng) |
| Mahabharata / Ramayana | Gutenberg (Ganguli/Griffith translations), Wikisource, sacred-texts |
| Epic of Gilgamesh | Gutenberg / Wikisource (PD translations) |
| Beowulf | Gutenberg (multiple translations), Standard Ebooks |
| Nibelungenlied | Gutenberg (German + Eng), Deutsches Textarchiv |
| Eddas / Norse myth | Gutenberg, sacred-texts, Wikisource |
| Kalevala | Gutenberg (Finnish + Eng) |

---

## 17. Fairy-tale / folktale corpora (Grimm, Andersen, etc.)

- **Sources:**
  - **Grimm's Fairy Tales** — Project Gutenberg (full English translations + German originals
    via DTA/Gutenberg-DE), Wikisource.
  - **Hans Christian Andersen** — Gutenberg (English translations), Wikisource, and Danish
    PD sources.
  - **Aesop, Andrew Lang's "Colour" Fairy Books, Perrault, Arabian Nights (1001 Nights)** —
    all on Project Gutenberg in full.
  - Curated machine-readable folktale datasets exist on **GitHub/Kaggle/Hugging Face**
    (e.g. cleaned Grimm/Andersen JSON corpora) — convenient but ⚠️ verify license/provenance
    of each dataset before commercial use.
- **Access / format:** Plain text / EPUB (Gutenberg), JSON (datasets), wikitext/HTML
  (Wikisource).
- **Auth / rate / license:** None / polite / public domain (the classic tales themselves are PD;
  watch *specific modern translations* which may still be in copyright).
- **Value for story creation:** ⭐ Core narrative-structure material (clear motifs, archetypes,
  morphology — pairs well with Propp/ATU analysis). Abundant and fully open.

> **Narrative-structure note:** for *analysis* corpora (not raw text) see the **ATU
> (Aarne–Thompson–Uther) tale-type index** and **Propp's morphology** — useful schemas for
> tagging the above tales, though the indices themselves are reference works, not open APIs.

---

## 18. DPLA (Digital Public Library of America)

- **Official name:** Digital Public Library of America.
- **URLs / endpoints:** `https://api.dp.la/v2/items?q=...&api_key=...`.
- **Coverage:** ~40M+ aggregated metadata records from US libraries/archives/museums (links
  out to the holding institution for the actual object).
- **Access method:** REST JSON.
- **Auth / API key:** **Free API key required** (request via email/endpoint). ⚠️ confirm the
  2026 key-request flow.
- **Rate limits:** Generous but defined per key. ⚠️ verify.
- **License / terms:** Metadata under CC0; objects governed by source institutions.
- **Value for story creation:** ◐ Discovery/aggregation only — finds where a text lives, not
  the text itself.

---

## 19. Europeana

- **Official name:** Europeana.
- **URLs / endpoints:** `https://api.europeana.eu/record/v2/search.json?wskey=...&query=...`
  (Search API), plus Record, Entity, IIIF/Newspapers (full-text) APIs.
- **Coverage:** ~50M+ European cultural-heritage objects (texts, images, etc.) aggregated
  across EU institutions; strong multilingual + historical newspapers full text.
- **Access method:** REST JSON; Newspapers/Fulltext API for OCR text.
- **Auth / API key:** **Free API key (`wskey`) required.**
- **Rate limits:** Defined per key. ⚠️ verify.
- **License / terms:** Metadata CC0; objects per-provider rights (filter by `REUSABILITY=open`).
- **Value for story creation:** ◐ Mostly metadata/discovery; the Newspapers full-text API does
  provide OCR text for some collections (useful for period/historical flavor).

---

## 20. Internet Archive / Open Library full-text search ("search inside")

- **Official name:** IA "Search Inside" / Open Library Inside.
- **URLs / endpoints:** Open Library "Search Inside" (`/search/inside`) and per-book
  BookReader search endpoints on archive.org.
- **Coverage:** Full-text search across millions of IA-digitized books.
- **Access method:** REST JSON (search results with matching snippets + page refs).
- **Auth / API key:** None.
- **Rate limits:** ⚠️ throttled; for analysis prefer pulling `_djvu.txt` of PD items directly.
- **License / terms:** Per-item (see Internet Archive entry).
- **Value for story creation:** ◐ Powerful for *finding* passages/themes across a huge corpus;
  combine with item download for the full PD text.

---

## Practical recommendations for the platform

**Tier 1 — build on these for reusable full text (open, clean, low-friction):**
1. **Project Gutenberg via Gutendex** — primary English + multilingual novel/story corpus.
2. **Standard Ebooks** — highest-quality structured editions (subset).
3. **PoetryDB** — drop-in poetry full text.
4. **Wikisource** — multilingual breadth + sacred/folk texts (mind CC BY-SA attribution).
5. **Perseus** — structured Greek/Latin myth & epic.

**Tier 2 — language-specific full text:**
- **Aozora Bunko** (JP), **Gallica** (FR), **Deutsches Textarchiv** (DE),
  **Biblioteca Virtual Cervantes** (ES).

**Tier 3 — discovery / metadata (pair with a full-text source):**
- **Open Library**, **Google Books**, **DPLA**, **Europeana**, **HathiTrust** (mostly
  gated), **Internet Archive** (full text but per-item rights).

**Licensing watch-list for a *commercial* product:**
- **Folger** Shakespeare is **CC BY-NC** — use a PD Shakespeare edition for commercial use.
- **Wikisource / DTA / Perseus** transcriptions carry **CC BY-SA / share-alike / NC** on the
  edition layer even when the work is PD — attribute and check NC.
- **Internet Archive / Gallica / Cervantes** are **per-item** — never assume PD; filter on
  rights metadata.
- Strip the **Project Gutenberg license header/trademark** to use the bare PD text freely.

**Engineering notes:**
- Prefer **bulk dumps / Git mirrors** (Gutenberg mirrors, Standard Ebooks GitHub, Aozora
  GitHub, Wikimedia dumps, DTA/Perseus corpora, Open Library dumps) over live scraping — most
  of these services explicitly ask you not to crawl their web frontends.
- Normalize encodings (Aozora = Shift-JIS; older Gutenberg = Latin-1) and **strip
  license/boilerplate headers** before indexing.
- TEI sources (Folger, DTA, Perseus, Standard Ebooks markup) give you free
  chapter/scene/speaker structure — preserve it for narrative parsing.

---

### ⚠️ Re-verification checklist (do this with live network access before production use)
- [ ] Confirm Gutendex is online and current book count.
- [ ] Confirm Google Books daily quota and whether a key is now mandatory.
- [ ] Confirm Folger's current API host/endpoint and license (CC BY-NC).
- [ ] Confirm HathiTrust Data API access tiers/credentials.
- [ ] Confirm DPLA + Europeana API-key request flow still active.
- [ ] Confirm Aozora community API/mirror URL (the Heroku-style mirrors drift).
- [ ] Re-check per-item rights filters for Internet Archive, Gallica, and Cervantes.
- [ ] Verify Standard Ebooks / Wikisource current rate-limit + user-agent policies.

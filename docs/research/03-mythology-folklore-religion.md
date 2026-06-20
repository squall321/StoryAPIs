# World Mythology, Folklore, Legend & Religion — Data Sources / APIs / Text Corpora

> **Focus domain:** World mythology, folklore, legend, and religion across ALL traditions — the richest motif source for fiction (deities, archetypes, story structures, motifs, creatures).
>
> **Compiled:** 2026-06-20

---

## ⚠️ UNVERIFIED — compiled from training knowledge; to be live-verified

**Live network verification could NOT be performed for this document.** All outbound-network tools (`WebSearch`, `WebFetch`, `Bash`/`curl`, `PowerShell`/`Invoke-WebRequest`) were **denied by sandbox permissions** in the environment where this catalog was compiled. Every entry below is reconstructed from **prior knowledge (training cutoff Jan 2026)** of these well-documented sources and is **NOT confirmed against the live 2026 state** of each site.

Treat all of the following as **provisional / to-be-verified**:

- Exact endpoint paths, base URLs, and whether an API still exists.
- Whether an API key is required *today* and how to obtain it.
- Current rate limits and quotas.
- Current license terms (these change; many "free" scholarly corpora have restrictive small print).
- Whether a service has migrated, gone offline, or been replaced.

**Re-run with network access enabled** before relying on any endpoint for production. Items known to be **scrape-only** or **restrictively licensed** are flagged with 🚩.

---

## QUICK-REFERENCE TABLE (top sources)

| # | Source | Tradition / Scope | Access method | Format | Auth? | License (provisional) | Flag |
|---|--------|-------------------|---------------|--------|-------|------------------------|------|
| 1 | Sacred-Texts.com (sacred-texts.com) | ALL traditions (aggregator) | Scrape / static HTML; DVD bulk | HTML/TXT | No | Public domain texts; site compilation 🚩 | 🚩 scrape |
| 2 | Theoi.com | Greek | Scrape-only | HTML | No | © site, PD source texts | 🚩 scrape |
| 3 | Perseus Digital Library (perseus.tufts.edu) | Greek/Roman classics | REST/CTS API + bulk (GitHub) | XML-TEI/JSON | No | CC BY-SA 3.0/4.0 | — |
| 4 | Sefaria API (sefaria.org/developers) | Jewish (Tanakh, Talmud, Midrash) | REST API + bulk (GitHub) | JSON/CSV | No (key optional) | CC0 / CC-BY / mixed | — |
| 5 | SuttaCentral (suttacentral.net) | Buddhist (Pali, Chinese, Tibetan) | REST API + bulk (GitHub) | JSON/Bilara | No | CC0 / CC-BY (varies) | — |
| 6 | AlQuran.cloud API (alquran.cloud) | Islamic (Quran) | REST API | JSON | No | Free/open (verify) | — |
| 7 | Quran.com API (api.quran.com) | Islamic (Quran) | REST API | JSON | No (key for v4) | Mixed/open | — |
| 8 | Bible-API.com | Christian (Bible) | REST API | JSON | No | PD translations | — |
| 9 | API.Bible (scripture.api.bible) | Christian (2500+ versions) | REST API | JSON | **Yes (key)** | Per-version 🚩 | 🚩 some restricted |
| 10 | ETCSL (etcsl.orinst.ox.ac.uk) | Sumerian literature | Scrape / bulk TEI-XML | XML/HTML | No | Academic non-commercial 🚩 | 🚩 license |
| 11 | GRETIL (gretil.sub.uni-goettingen.de) | Sanskrit/Indic corpus | Bulk download | TXT/TEI/HTML | No | Per-text; mostly open | — |
| 12 | ctext.org (Chinese Text Project) | Chinese (Shanhaijing etc.) | REST API + web | JSON | **Yes (free)** | CC BY-SA (varies) | — |
| 13 | Wikidata / Wikipedia (SPARQL + REST) | ALL (structured metadata) | SPARQL + REST API + dumps | JSON/RDF | No | CC0 (data) / CC BY-SA | — |
| 14 | Avesta.org | Zoroastrian (Avesta, Pahlavi) | Scrape / static HTML | HTML/TXT | No | PD source texts 🚩 site | 🚩 scrape |
| 15 | Multilingual Folktale DB (mftd.org) | Folktales + ATU indexing | Scrape / web DB | HTML | No | Mixed/PD 🚩 | 🚩 scrape |
| 16 | CBETA (cbeta.org) | Chinese Buddhist canon | Bulk (GitHub) + reader | XML-TEI | No | CC BY-NC-SA 🚩 NC | 🚩 NC |
| 17 | CODECS / van Hamel (vanhamel.nl) | Celtic/Irish | Web DB + scrape | HTML | No | CC BY (verify) | partial 🚩 |
| 18 | Mythopedia / Godchecker / Encyclopedia Mythica | ALL (encyclopedic) | Scrape-only | HTML | No | © proprietary 🚩 | 🚩 scrape+© |
| 19 | GRETIL / SARIT / DCS (Sanskrit) | Hindu/Vedic/Buddhist | Bulk / API | TEI/CoNLL-U | No | Mostly CC | — |
| 20 | Wikisource (per-language) | ALL public-domain texts | REST/MediaWiki API + dumps | JSON/XML/TXT | No | CC BY-SA / PD | — |

> ⭐ **Best general strategy:** Use **Wikidata SPARQL** for structured deity/creature/motif metadata across all traditions; **Sacred-Texts.com** + **Wikisource** + **Perseus/GRETIL/ETCSL/SuttaCentral** for full primary texts; **ATU + Thompson Motif-Index + mftd.org** for cross-cultural motif/type tagging.

---

# 0. CROSS-TRADITION AGGREGATORS & STRUCTURED METADATA

## 0.1 Sacred-Texts.com 🚩 scrape
- **Official name:** Internet Sacred Text Archive (ISTA).
- **URL:** https://sacred-texts.com
- **Coverage:** The single largest free aggregator of public-domain religious, mythological, and folkloric texts on the web — thousands of full texts across Hinduism, Buddhism, Christianity, Judaism, Islam, Zoroastrianism, Norse/Germanic, Celtic, Greek/Roman, Egyptian, African, Native American, Oceanic, Pacific, esoteric, alchemy, grimoires, etc.
- **Access method:** **Scrape-only** — static HTML, predictable directory structure (e.g., `/neu/`, `/hin/`, `/cla/`, `/cel/`). No API. Full archive historically sold as a **DVD/ISO bulk download**.
- **Data format:** HTML (older texts often plain inline text); some OCR artifacts.
- **Auth:** None.
- **Rate limits:** None published; crawl politely.
- **License:** Underlying texts are public domain; the **site's compilation/markup is © J.B. Hare estate** 🚩 — scraping for derived work is generally fine for the PD texts themselves, but don't redistribute the site's HTML wholesale.
- **Story value:** ⭐ The default first stop for almost any tradition's primary myths in English translation. Eddas, Kalevala, Mabinogion, Popol Vuh, Egyptian Book of the Dead, Bulfinch, Frazer's Golden Bough, etc.
- **VERIFY:** Site still up; DVD availability; exact directory paths.

## 0.2 Wikidata (SPARQL + REST) ⭐
- **Official name:** Wikidata.
- **URL:** https://query.wikidata.org (SPARQL); https://www.wikidata.org/w/api.php (MediaWiki/REST).
- **Coverage:** Structured, multilingual metadata for tens of thousands of deities, mythological creatures, heroes, and texts. Useful classes/queries: `instance of` deity (Q178885), mythological figure (Q4271324), legendary creature (Q2239243), and tradition-specific subsets (Greek deity Q22989102, Norse deity, Hindu deity Q3520523, etc.).
- **Access method:** **SPARQL endpoint** (best for cross-tradition subsets), **REST/MediaWiki API**, and **bulk JSON/RDF dumps**.
- **Data format:** JSON, RDF/Turtle, SPARQL results.
- **Auth:** None (User-Agent required; respect query timeout ~60s).
- **Rate limits:** SPARQL has a query-time limit; be considerate. WDQS may throttle heavy queries.
- **License:** **CC0** for the data itself ⭐ — the most permissive option in this whole catalog.
- **Story value:** ⭐⭐ Build a normalized "deity graph" / cross-cultural pantheon table: domains, family relations, equivalents across cultures, symbols, attributes. Ideal backbone for a relational story-source DB.
- **VERIFY:** Exact Q-IDs; WDQS endpoint stability.

## 0.3 Wikipedia / Wikisource (MediaWiki REST API)
- **URL:** `https://{lang}.wikipedia.org/w/rest.php` and `/api/rest_v1`; Wikisource analogously.
- **Coverage:** Wikipedia = encyclopedic summaries + category trees (e.g., "Category:Mythological creatures"). Wikisource = full **public-domain primary texts** in many languages (Eddas, Kalevala, classic translations).
- **Access:** REST + Action API + dumps (dumps.wikimedia.org).
- **Format:** JSON, wikitext, HTML; dumps as XML/SQL.
- **Auth:** None.
- **License:** Wikipedia **CC BY-SA**; Wikisource texts **public domain** (per source) ⭐.
- **Story value:** Fast structured summaries + reliable PD full texts. Category trees are excellent for enumerating creatures/deities per tradition.

## 0.4 Encyclopedia Mythica / Mythopedia / Godchecker 🚩 scrape + ©
- **URLs:** https://pantheon.org (Encyclopedia Mythica); https://mythopedia.com; https://www.godchecker.com
- **Coverage:** Curated encyclopedic entries on deities, heroes, creatures across most world pantheons (Godchecker is especially broad and irreverent; Mythopedia is well-organized by pantheon).
- **Access:** **Scrape-only**, no public API.
- **License:** **Proprietary © each site** 🚩 — use for research/inspiration, not redistribution. Facts aren't copyrightable but their prose is.
- **Story value:** Quick orientation and "who's who" per pantheon; cross-link to PD primary sources.

## 0.5 Folktale Type & Motif Indexes (ATU / Thompson) ⭐
- **ATU (Aarne–Thompson–Uther) type index:** The standard catalog of international folktale **types** (e.g., ATU 300 "The Dragon-Slayer", ATU 333 "Little Red Riding Hood", ATU 510A "Cinderella"). Published as Uther's *The Types of International Folktales* (2004). 🚩 **Copyrighted print work** — no official open API; numbering is referenced freely but the full annotated index is © FF Communications.
- **Thompson Motif-Index of Folk-Literature:** Six-volume classification of narrative **motifs** (e.g., B11 "Dragon", D700 "Disenchantment", F got. supernatural). The text is **public domain (pre-1964 ed.)**; digitized versions exist (e.g., via archive.org and some university hosts). ⭐ Searchable scans/transcriptions.
- **Access:** Mostly scrape / PDF / static lookups. **mftd.org** (below) and some academic projects expose ATU/motif tagging.
- **Story value:** ⭐⭐ The Rosetta Stone for *story structure and motif* — lets you tag any myth/folktale by reusable narrative components and find cross-cultural variants of the same plot.

## 0.6 Multilingual Folktale Database (mftd.org) 🚩 scrape
- **URL:** http://www.mftd.org
- **Coverage:** Searchable database of folktales in many languages, indexed by **ATU type** with parallel/translated versions — great for finding variants of a tale across cultures.
- **Access:** **Web DB / scrape-only** (no documented API).
- **Format:** HTML.
- **License:** Mixed; many texts PD, site compilation 🚩.
- **Story value:** ⭐ Find every cultural variant of a given tale type side by side — perfect for "remix" sourcing.

## 0.7 D'Aulaire / Bulfinch / Frazer (public-domain mythography)
- **D'Aulaire's Book of Greek/Norse Myths:** 🚩 still in copyright (20th c.) — not a data source, listed because the prompt mentions it; use PD equivalents (Bulfinch) instead for reuse.
- **Bulfinch's Mythology** (PD), **Frazer's *The Golden Bough*** (PD), **Edith Hamilton** (🚩 in copyright). Available full-text on sacred-texts, Gutenberg, Wikisource.
- **Story value:** Ready-made narrative retellings and comparative-mythology frameworks (Frazer = dying-and-rising god, scapegoat, sacred king motifs).

## 0.8 Project Gutenberg / Internet Archive (bulk PD texts)
- **URLs:** https://gutenberg.org (+ gutendex.com JSON API); https://archive.org (REST/Advanced Search API + IIIF).
- **Coverage:** Vast public-domain holdings — translated myth/folklore collections (Grimm, Andrew Lang's Fairy Books, Lady Gregory's Irish myths, etc.).
- **Access:** Gutendex REST/JSON; Archive.org REST + bulk.
- **License:** **Public domain** ⭐ (Gutenberg license trademark caveat on the header text only).
- **Story value:** Bulk-downloadable, clean-ish full texts for training/ingest.

---

# 1. GREEK & ROMAN

## 1.1 Theoi Greek Mythology (theoi.com) 🚩 scrape
- **URL:** https://www.theoi.com
- **Coverage:** ⭐ The most comprehensive single site on Greek deities, daemons, nymphs, heroes, and creatures, with extensive **quoted primary-source passages** (Hesiod, Homer, Ovid, Apollodorus, Nonnus, etc.) organized per figure.
- **Access:** **Scrape-only**, no API. Stable URL structure per deity.
- **Format:** HTML.
- **License:** Site text © Theoi 🚩; quoted sources are PD translations.
- **Story value:** ⭐⭐ Best-organized deity/creature reference for Greek; each entry already aggregates the relevant ancient citations.

## 1.2 Perseus Digital Library (perseus.tufts.edu) ⭐
- **URL:** http://www.perseus.tufts.edu; data on GitHub (PerseusDL canonical-greekLit / canonical-latinLit).
- **Coverage:** Full Greek and Latin classical corpus with Greek/English/Latin parallel texts, morphological analysis, and commentary — Homer, Hesiod, the tragedians, Ovid, Virgil, Apollodorus, Pausanias, etc.
- **Access:** **CTS (Canonical Text Services) API**, Scaife Viewer, **bulk TEI-XML on GitHub** ⭐.
- **Format:** TEI-XML, JSON via CTS.
- **Auth:** None.
- **License:** **CC BY-SA 3.0/4.0** ⭐ (per-text; check each).
- **Story value:** ⭐⭐ Authoritative full primary texts of the Greco-Roman mythological canon, machine-readable.
- **VERIFY:** CTS endpoint availability vs. Scaife Viewer migration.

## 1.3 Other Greek/Roman
- **ToposText (topostext.org):** Geo-referenced ancient texts/places — good for mapping myth to geography. Scrape/some data export.
- **Open Greek and Latin / Scaife Viewer:** Modern successor corpus; CC BY-SA.
- **Dictionary of Greek and Roman Biography and Mythology** (Smith, PD): full text on sacred-texts/archive.

---

# 2. NORSE / GERMANIC

## 2.1 Eddas & Sagas (sacred-texts + Wikisource)
- **Texts:** *Poetic Edda* (Codex Regius — Völuspá, Hávamál, etc.), *Prose Edda* (Snorri Sturluson — Gylfaginning, Skáldskaparmál), *Heimskringla*, Icelandic sagas.
- **URLs:** sacred-texts.com `/neu/` (Bellows, Brodeur translations, PD); Wikisource; **heimskringla.no** (Old Norse + Scandinavian).
- **Access:** Scrape / static; **Icelandic Saga Database (sagadb.org)** offers multiple languages.
- **Format:** HTML/TXT.
- **License:** PD translations (Bellows 1923, Brodeur 1916). ⭐
- **Story value:** ⭐⭐ Cosmology (nine worlds), Ragnarök, Odin/Thor/Loki cycles, dwarves, giants, Yggdrasil — core Western fantasy DNA.

## 2.2 Skaldic Project (skaldic.org)
- **Coverage:** Scholarly edition of skaldic poetry with kennings database — invaluable for **poetic metaphor/kenning** mining.
- **Access:** Web DB; some structured export. 🚩 verify license (academic).
- **Story value:** Kennings = a generator of evocative compound imagery ("whale-road" = sea).

## 2.3 Germanic / Continental
- *Nibelungenlied*, *Beowulf* (Old English — PD translations on Gutenberg/sacred-texts), Grimm's *Deutsche Mythologie* (PD).

---

# 3. CELTIC / IRISH / WELSH

## 3.1 CODECS / van Hamel (vanhamel.nl)
- **Official name:** CODECS — Collaborative Online Database and e-Resources for Celtic Studies (A. G. van Hamel Foundation).
- **URL:** https://www.vanhamel.nl/codecs/
- **Coverage:** ⭐ Bibliographic + textual database for medieval Celtic literature — Irish (Ulster Cycle, Mythological Cycle, Fenian Cycle), Welsh, Breton, Scottish Gaelic.
- **Access:** Web DB; **Semantic MediaWiki** backend (so MediaWiki/SMW API likely queryable). Some scrape.
- **Format:** HTML; SMW/RDF possible.
- **License:** CC BY (verify) — partial 🚩.
- **Story value:** ⭐ Authoritative index of Irish/Welsh tale corpus and editions.

## 3.2 CELT (UCC, celt.ucc.ie)
- **Coverage:** Corpus of Electronic Texts — full Irish historical/literary texts (Táin Bó Cúailnge, Lebor Gabála Érenn, annals) in TEI.
- **Access:** Scrape / TEI-XML downloads. Format: TEI/HTML.
- **License:** Free for academic use; **some restrictions on redistribution** 🚩 verify.
- **Story value:** ⭐⭐ Cú Chulainn, the Tuatha Dé Danann, the four invasions of Ireland — primary texts.

## 3.3 Mabinogion & Welsh
- **The Mabinogion** (Lady Charlotte Guest tr., PD) on sacred-texts `/neu/celt/`; Wikisource. *Culhwch and Olwen*, the Four Branches.
- **Story value:** ⭐ Welsh mythos, Arthurian roots, Annwn (otherworld).

## 3.4 Other
- Lady Gregory's *Gods and Fighting Men* / *Cuchulain of Muirthemne* (PD, Gutenberg). Yeats' folklore collections (PD).

---

# 4. SLAVIC & BALTIC

## 4.1 Slavic
- **Sources:** No single canonical primary corpus survives (Christianization erased much); reconstructed from chronicles (*Primary Chronicle*), folk tales (Afanasyev's *Russian Fairy Tales* — PD), and *byliny* (epic songs about bogatyrs).
- **URLs:** sacred-texts has Ralston's *Russian Folk-Tales* (PD); Afanasyev collections on archive.org/Gutenberg.
- **Story value:** ⭐ Baba Yaga, Koschei the Deathless, Perun, Veles, the firebird, Domovoi, rusalka, Vasilisa.
- **Access:** Scrape / PD bulk.

## 4.2 Baltic (Lithuanian/Latvian)
- **Sources:** Latvian **dainas** (folk songs — the massive Krišjānis Barons collection, *Latvju dainas*; digitized at **dainuskapis.lv** 🚩 verify). Lithuanian mythology reconstructed (Dievas, Perkūnas, Laima, Žemyna).
- **Access:** Scrape / specialized archives.
- **Story value:** ⭐ One of Europe's best-preserved pagan folk-song traditions; nature deities, thunder god Perkūnas.

---

# 5. FINNISH / FENNO-UGRIC

## 5.1 Kalevala
- **Text:** *The Kalevala* (Elias Lönnrot's compiled epic) — Crawford (1888) and Kirby (1907) English translations are **PD**.
- **URLs:** sacred-texts `/neu/kveng/` ; Gutenberg; Finnish original via **SKVR (Suomen Kansan Vanhat Runot)** — the database of old Finnish folk poetry at **skvr.fi** ⭐ (searchable, possibly with data export — verify).
- **Access:** Scrape / PD bulk; SKVR is a structured DB.
- **License:** PD translations.
- **Story value:** ⭐⭐ Väinämöinen, the Sampo, Louhi, runo-singing magic, the world-egg cosmogony — a complete epic plus its raw folk-poetry sources.

---

# 6. EGYPTIAN

## 6.1 Texts & Databases
- **Pyramid Texts, Coffin Texts, Book of the Dead:** Budge translations (PD) on sacred-texts `/egy/`. 🚩 Budge is outdated scholarship — flag for accuracy, fine for inspiration.
- **Thesaurus Linguae Aegyptiae (aaew.bbaw.de / tla.bbaw.de):** ⭐ Scholarly corpus of Egyptian texts with lemmatization. Access: web DB + some data; **academic license** 🚩 verify.
- **Ramses / Deir el-Medina databases:** specialist.
- **Story value:** ⭐⭐ Osiris/Isis/Set/Horus cycle, Ra's solar journey through the Duat, Ma'at, the weighing of the heart, Apep the chaos serpent.

---

# 7. MESOPOTAMIAN — SUMERIAN / AKKADIAN / BABYLONIAN

## 7.1 ETCSL — Electronic Text Corpus of Sumerian Literature 🚩
- **Official name:** ETCSL.
- **URL:** https://etcsl.orinst.ox.ac.uk
- **Coverage:** ⭐ The standard digital corpus of **Sumerian literature** — Inanna's Descent, Enki and Ninhursag, Enuma Elish-adjacent material, Gilgamesh Sumerian poems, hymns, debate poems, proverbs. Transliteration + English translation.
- **Access:** Web + **bulk TEI-XML download** of the whole corpus ⭐.
- **Format:** TEI-XML, HTML.
- **Auth:** None.
- **License:** **Academic / non-commercial use** terms 🚩 (Oxford; cite required). Project is essentially archival/frozen.
- **Story value:** ⭐⭐ World's oldest literature — descent-to-underworld archetype, divine councils, flood myth, creation.
- **VERIFY:** Current license clause; corpus download link.

## 7.2 ORACC (Open Richly Annotated Cuneiform Corpus)
- **URL:** http://oracc.museum.upenn.edu
- **Coverage:** Modern, actively maintained annotated cuneiform corpora (Akkadian, Sumerian) across many sub-projects.
- **Access:** Web + **JSON data downloads** per project; some API. Format: JSON/ATF/TEI.
- **License:** **CC BY-SA** (mostly) ⭐ — more permissive than ETCSL.
- **Story value:** ⭐ Royal inscriptions, omens, god lists, Akkadian epics.

## 7.3 Gilgamesh / Enuma Elish
- **Epic of Gilgamesh:** PD translations (R. Campbell Thompson, etc.) on sacred-texts/archive; standard Babylonian version. *Enuma Elish* (creation), *Atrahasis* (flood), *Descent of Ishtar*.
- **Story value:** ⭐⭐ The hero's-journey ur-text; flood narrative predating Genesis; Marduk vs. Tiamat (chaoskampf).

---

# 8. HINDU / VEDIC (Indic)

## 8.1 GRETIL (Göttingen Register of Electronic Texts in Indian Languages) ⭐
- **URL:** https://gretil.sub.uni-goettingen.de
- **Coverage:** ⭐ Massive archive of **Sanskrit (and other Indic) e-texts** in transliteration/Devanagari — Vedas, Upanishads, Mahabharata, Ramayana, Puranas, Bhagavad Gita, Tantras, etc.
- **Access:** **Bulk download** (per-text files). Format: plain text / HTML / TEI.
- **Auth:** None.
- **License:** Per-text; mostly free academic, many openly reusable ⭐ (verify individual headers).
- **Story value:** ⭐⭐ The core Hindu canon in machine-readable form.

## 8.2 Mahabharata / Ramayana / Puranas (English, PD)
- **Mahabharata:** Kisari Mohan Ganguli full English translation (PD) on sacred-texts `/hin/maha/` ⭐ — all 18 parvas.
- **Ramayana:** Griffith verse translation (PD); Dutt prose.
- **Puranas:** Wilson's *Vishnu Purana*, etc. (PD) on sacred-texts.
- **Rig Veda:** Griffith translation (PD).
- **Story value:** ⭐⭐ Two of the world's largest epics — avatars of Vishnu, the Pandavas/Kauravas war, Rama vs. Ravana, churning of the ocean of milk, vast deva/asura cast.

## 8.3 DCS (Digital Corpus of Sanskrit) / SARIT
- **DCS (digitalcorpussanskrit.org):** Morphologically/syntactically annotated Sanskrit corpus. Access: web + **CoNLL-U data download** ⭐. License CC.
- **SARIT (sarit.indology.info):** TEI editions of Indic texts. CC BY-SA.
- **Story value:** ⭐ Annotated text for NLP / motif extraction.

---

# 9. BUDDHIST

## 9.1 SuttaCentral (suttacentral.net) ⭐
- **URL:** https://suttacentral.net ; API at https://suttacentral.net/api ; data on **GitHub (suttacentral/bilara-data, sc-data)**.
- **Coverage:** ⭐ Early Buddhist texts across canons — **Pali Tipitaka**, Chinese Āgamas, Tibetan, Sanskrit — with parallels and multiple translations (Bhikkhu Sujato, etc.).
- **Access:** **REST API** + **bulk JSON/Bilara on GitHub** ⭐.
- **Format:** JSON, Bilara (segmented JSON), HTML.
- **Auth:** None.
- **License:** Translations by Sujato are **CC0** ⭐; root texts and others vary (CC-BY).
- **Story value:** ⭐⭐ Jataka birth-stories (past lives of the Buddha — a huge folktale trove), cosmology (realms, Mount Meru), Mara the tempter.

## 9.2 CBETA (cbeta.org) 🚩 NC
- **Official name:** Chinese Buddhist Electronic Text Association.
- **URL:** https://www.cbeta.org ; data on **GitHub (cbeta-org)**.
- **Coverage:** ⭐ The **entire Chinese Buddhist canon** (Taishō Tripiṭaka 大正藏, Manji 卍續藏, etc.) — tens of thousands of texts.
- **Access:** **Bulk TEI-XML download** (GitHub) + online reader (CBETA Online). Format: TEI-XML.
- **License:** **CC BY-NC-SA** 🚩 (non-commercial) — flag for commercial products.
- **Story value:** ⭐ Sutras, vinaya, avadana tales, Journey-to-the-West source material (Xuanzang), bodhisattva narratives.

## 9.3 Tipitaka / Other
- **Access to Insight (accesstoinsight.org):** Curated Theravada translations 🚩 scrape, free-distribution license.
- **84000 (84000.co):** Tibetan Kangyur in translation. CC BY-NC (verify) 🚩.
- **BDRC (Buddhist Digital Resource Center, bdrc.io):** Tibetan/Buddhist text scans + metadata API. CC.

---

# 10. CHINESE

## 10.1 Chinese Text Project (ctext.org) ⭐
- **URL:** https://ctext.org ; API docs https://ctext.org/tools/api
- **Coverage:** ⭐ Pre-modern Chinese texts — **Shanhaijing 山海经 (Classic of Mountains and Seas)**, Shijing, Zhuangzi, Liezi, Soushen Ji 搜神記 (records of the strange), Fengshen Yanyi, etc.
- **Access:** **REST API (JSON)** + web + data export.
- **Format:** JSON; some plain text.
- **Auth:** **Free API key** required for API access.
- **License:** **CC BY-SA** for many texts (varies per text) ⭐.
- **Story value:** ⭐⭐ The *Shanhaijing* is a bestiary goldmine (hundreds of mythical creatures/gods); zhiguai "strange tales" tradition; cosmic mythology (Pangu, Nüwa, Houyi).

## 10.2 Journey to the West / Classic Novels
- **Journey to the West 西游记:** Public-domain English (some) and original Chinese on ctext/Wikisource. Sun Wukong, the pilgrimage, Buddhist-Daoist pantheon.
- **Investiture of the Gods (Fengshen Yanyi):** the Chinese "creation of the gods" novel.
- **Story value:** ⭐⭐ Monkey King = one of world myth's great trickster-hero arcs; vast deity roster.

## 10.3 Other
- **Daoist canon (Daozang):** partial digitizations; **Kanripo / Kanseki Repository (kanripo.org)** — bulk Chinese classics in TEI on GitHub ⭐ (open). Soushen Ji (In Search of the Supernatural).

---

# 11. JAPANESE

## 11.1 Kojiki & Nihon Shoki
- **Kojiki** (古事記): Chamberlain translation (PD) on sacred-texts `/shi/kj/` ⭐. **Nihon Shoki** (日本書紀): Aston translation (PD).
- **Access:** Scrape / PD bulk; Japanese originals via **J-TEXTS (j-texts.com)** and Aozora Bunko.
- **Story value:** ⭐⭐ Shinto cosmogony, Izanagi/Izanami, Amaterasu and the cave, Susanoo vs. the Yamata-no-Orochi, the imperial origin myth.

## 11.2 Yokai databases
- **Yokai.com (yokai.com):** ⭐ Excellent illustrated encyclopedia of Japanese yokai by Matthew Meyer. **Scrape-only**, © proprietary 🚩.
- **The Obakemono Project / Mizuki Shigeru references:** secondary.
- **Nichibunken Yokai Database (国際日本文化研究センター, nichibunken.ac.jp):** ⭐ Academic database of yokai folklore records. Web DB / scrape; Japanese. 🚩 verify license.
- **Story value:** ⭐⭐ Thousands of named spirits/monsters with descriptions — a ready-made creature catalog.

## 11.3 Folktales
- Lafcadio Hearn's *Kwaidan* and Japanese ghost-story collections (PD). Ozaki's *Japanese Fairy Book* (PD).

---

# 12. KOREAN

## 12.1 Foundational texts
- **Samguk Yusa 三國遺事 (Memorabilia of the Three Kingdoms):** the key source for Korean foundation myths (Dangun, Jumong, the Egg-born kings). **Samguk Sagi 三國史記.** Tangun myth.
- **Access:** Korean DBs — **한국사데이터베이스 (db.history.go.kr)**, **한국고전종합DB (ITKC, db.itkc.or.kr)** — see companion catalog `01-korea-east-asia.md`. Scrape / partial Open API. 🚩 KOGL/verify.
- **Story value:** ⭐ Dangun (bear-woman origin), dragon kings, foundation eggs, 설화 (seolhwa) folktales.

## 12.2 설화 (folk narrative) collections
- **한국구비문학대계 (Compendium of Korean Oral Literature):** large oral-folklore archive (AKS). Web DB 🚩 scrape/verify license.
- **Encyclopedia of Korean Folk Culture (folkency.nfm.go.kr):** National Folk Museum. Web + some data.
- **Story value:** ⭐ Dokkaebi (goblins), gumiho (nine-tailed fox), tiger tales, shaman (muga) narratives like Princess Bari.

---

# 13. PERSIAN / ZOROASTRIAN / IRANIAN

## 13.1 Avesta.org 🚩 scrape
- **URL:** https://www.avesta.org
- **Coverage:** ⭐ The **Avesta** (Yasna, Yashts, Vendidad, Gathas) + **Pahlavi texts** (Bundahishn — Zoroastrian creation/cosmology, Denkard, Arda Viraf) in English translation (Darmesteter, Mills, West — PD).
- **Access:** **Scrape-only**, static HTML.
- **License:** PD source translations; site compilation 🚩.
- **Story value:** ⭐⭐ Ahura Mazda vs. Angra Mainyu (the original cosmic dualism), the Amesha Spentas, fravashis, the world-saviour (Saoshyant), eschatology that shaped later traditions.

## 13.2 Shahnameh (Book of Kings)
- **Text:** Ferdowsi's epic — Warner & Warner and Helen Zimmern (PD) English translations on sacred-texts/archive.
- **Story value:** ⭐⭐ Rostam and Sohrab, the Simurgh, Zahhak the serpent-king, Jamshid — Persia's national epic, vast heroic/legendary cycle.

## 13.3 Other
- **TITUS (titus.uni-frankfurt.de):** Avestan/Old Iranian + many ancient-language corpora. Academic 🚩.

---

# 14. ABRAHAMIC

## 14A. JEWISH

### 14A.1 Sefaria API (sefaria.org) ⭐
- **URL:** https://www.sefaria.org ; API docs https://developers.sefaria.org ; data on **GitHub (Sefaria/Sefaria-Export)**.
- **Coverage:** ⭐⭐ Tanakh, Mishnah, Talmud (Bavli/Yerushalmi), Midrash, Kabbalah (Zohar), Halakha, commentaries — with interlinked source connections, Hebrew + English.
- **Access:** **REST API (JSON)** + **bulk download (GitHub, JSON/CSV)** ⭐.
- **Auth:** None (optional key for higher limits).
- **Rate limits:** Reasonable; documented.
- **License:** Original texts **public domain / CC0**; many translations **CC BY** or CC0; some modern translations restricted 🚩 (per-text license field provided in API ⭐).
- **Story value:** ⭐⭐ Midrashic legend (Lilith, the Golem, Leviathan/Behemoth, angels/demons, Solomon and Asmodeus), Aggadah — a massive, interconnected narrative corpus with the best API in this catalog.

### 14A.2 Other Jewish
- *Legends of the Jews* (Louis Ginzberg, PD) — systematic retelling of rabbinic legend, on sacred-texts/archive. ⭐
- **Tanach.us**, **Open Siddur Project** (CC).

## 14B. CHRISTIAN / BIBLE

### 14B.1 Bible-API.com
- **URL:** https://bible-api.com
- **Coverage:** Bible text by reference (e.g., `/john 3:16`). Public-domain translations (WEB, KJV, etc.) + some others.
- **Access:** **REST API (JSON)**, no key. Simple.
- **License:** **PD translations** ⭐.
- **Story value:** Quick programmatic verse retrieval.

### 14B.2 API.Bible (scripture.api.bible) 🚩
- **URL:** https://scripture.api.bible (American Bible Society / Digital Bible Library).
- **Coverage:** ⭐ 2,500+ Bible versions in 1,600+ languages.
- **Access:** **REST API, API key required.**
- **License:** **Per-version, many restricted/copyrighted** 🚩 (PD ones reusable; modern translations are not).
- **Story value:** Breadth of versions/languages; pick PD versions for reuse.

### 14B.3 Other Bible APIs / data
- **bible.helloao.org / bolls.life / GetBible v2 (getbible.net):** free JSON Bible APIs (PD/open translations). ⭐
- **ESV API, Biblia.com (Logos):** 🚩 key + usage limits, copyrighted text.
- **Apocrypha / Pseudepigrapha:** Book of Enoch, Jubilees, Gospel of Thomas, Nag Hammadi library (Gnostic) — PD/Robinson translations on sacred-texts `/chr/` and `/gno/`. ⭐ Rich for angels, Watchers, alternative cosmologies.

## 14C. ISLAMIC

### 14C.1 AlQuran.cloud API (alquran.cloud) ⭐
- **URL:** https://alquran.cloud/api
- **Coverage:** Quran — Arabic text, many translations, multiple recitation audio editions, tafsir links.
- **Access:** **REST API (JSON)**, **no key**.
- **License:** Free/open (verify per-translation) ⭐.
- **Story value:** Prophetic narratives (Yusuf, Musa, the People of the Cave), Iblis, jinn, angels.

### 14C.2 Quran.com API (api.quran.com)
- **URL:** https://api.quran.com (v4) ; corpus from **Tanzil** and **QUL**.
- **Access:** **REST API (JSON)**; some endpoints need a (free) client credential.
- **License:** Quran Arabic open; translations vary 🚩.
- **Story value:** Same as above, richer metadata (verse-by-verse, word-by-word morphology via Quranic Arabic Corpus, corpus.quran.com).

### 14C.3 Hadith / Other
- **sunnah.com / Hadith API (e.g., hadithapi.com):** hadith collections (Bukhari, Muslim). 🚩 verify license/key.
- **Qisas al-Anbiya (Stories of the Prophets), Tales of the Prophet, One Thousand and One Nights (Arabian Nights):** Burton/Lane/Payne translations (PD) on sacred-texts `/isl/` — ⭐⭐ jinn, Aladdin, Sinbad, Scheherazade frame-tale.

---

# 15. AFRICAN (Sub-Saharan & North)

## 15.1 Yoruba / Ifá
- **Sources:** Ifá divination corpus (Odu Ifá — 256 odu, each with verses/stories), Orisha mythology (Olodumare, Obatala, Ogun, Shango, Oshun, Eshu the trickster).
- **Texts:** Some PD on sacred-texts `/afr/`; academic collections (Wande Abimbola). 🚩 Much is oral / restrictive / sacred.
- **Story value:** ⭐⭐ Eshu/Elegua trickster, divination-as-narrative, a pantheon that traveled to the Americas (Santería, Candomblé, Vodou).

## 15.2 Akan / Anansi
- **Sources:** Anansi (Ananse) spider-trickster tales (Ghana/Ashanti); Rattray's *Akan-Ashanti Folk-Tales* (PD), *Jamaica Anansi Stories* (Beckwith, PD).
- **Story value:** ⭐⭐ The archetypal African trickster; "spider stories" frame the very concept of story (Anansesem).

## 15.3 Other African
- **Zulu/Nguni:** Callaway's *Nursery Tales, Traditions and Histories of the Zulu* (PD); uNkulunkulu, Unkulunkulu. **Dahomey/Fon:** Herskovits. **San/Bushman:** Bleek & Lloyd folklore (PD, |kaggen the mantis). **Egyptian** (see §6). **Mami Wata** water-spirit tradition (pan-African).
- **Story value:** ⭐ Creation myths, trickster animals, ancestor spirits.
- **Access:** Mostly PD scrape (sacred-texts `/afr/`, archive.org); much is oral, undigitized, or culturally sensitive 🚩.

---

# 16. NATIVE NORTH AMERICAN

## 16.1 Sources
- **Texts:** sacred-texts `/nam/` ⭐ — large regional collections (e.g., Erdoes/Ortiz–style compilations are © but many BAE *Bureau of American Ethnology* reports are PD). Schoolcraft, Boas (Tsimshian/Kwakiutl), Mooney (Cherokee — *Myths of the Cherokee*, PD), Matthews (Navajo).
- **Story value:** ⭐⭐ Trickster cycles (Coyote, Raven, Iktomi the spider), emergence/creation myths, Thunderbird, the world-on-turtle's-back.
- **Access:** PD scrape; **Smithsonian/BAE annual reports** (PD) on archive.org.
- **License/ethics:** 🚩 Many narratives are culturally restricted or sacred; PD legal status ≠ ethical free use. Flag for sensitivity.

---

# 17. MESOAMERICAN

## 17.1 Popol Vuh (Maya K'iche')
- **Text:** *Popol Vuh* — creation epic; Goetz/Morley (after Recinos) and earlier Brasseur; Wikisource/sacred-texts `/nam/maya/` host PD-era translations. (Tedlock/Christenson are © modern.)
- **Story value:** ⭐⭐ The Hero Twins (Hunahpu & Xbalanque) vs. the lords of Xibalba, multiple creations of humanity, the ballgame in the underworld.

## 17.2 Aztec / Nahua
- **Sources:** *Florentine Codex* (Sahagún — Anderson & Dibble tr., partly available), Codex collections; Aztec pantheon (Quetzalcoatl, Tezcatlipoca, Huitzilopochtli, Tlaloc, Mictlantecuhtli). **Amoxcalli / Codex digitizations** (BnF, World Digital Library).
- **Story value:** ⭐⭐ Five Suns cosmology, feathered serpent, sacrifice/cosmic-debt mythos, journey through Mictlan.
- **Access:** Scrape / digitized codices (IIIF); modern translations 🚩 ©.

---

# 18. SOUTH AMERICAN / ANDEAN

- **Sources:** Inca mythology (Viracocha, Inti, Pachamama, the Ayar brothers); *Huarochirí Manuscript* (the major Quechua mythological text — Salomon/Urioste tr. © ; older partial PD). Amazonian (Yanomami, Tupi-Guarani) — largely ethnographic.
- **Story value:** ⭐ Creation from Lake Titicaca, sky/sun deities, world-age destructions.
- **Access:** Scrape / academic 🚩.

---

# 19. POLYNESIAN / OCEANIC / MICRONESIAN

## 19.1 Sources
- **Texts:** sacred-texts `/pac/` ⭐ — Maori (Grey's *Polynesian Mythology*, PD), Hawaiian (*Kumulipo* creation chant — Beckwith tr.; Fornander), Tahitian, Samoan/Tongan. Beckwith's *Hawaiian Mythology* (PD).
- **Story value:** ⭐⭐ Māui the trickster-demigod (fishing up islands, snaring the sun, seeking immortality), Pele the volcano goddess, Tangaroa/Kanaloa, Rangi & Papa (sky-father/earth-mother separation), Hina.
- **Access:** PD scrape (Grey, Beckwith, Fornander on archive/sacred-texts).
- **Ethics:** 🚩 Some genealogical/sacred chants are culturally protected.

---

# 20. ABORIGINAL AUSTRALIAN

## 20.1 Sources
- **Concept:** The **Dreaming / Dreamtime** (Tjukurpa, Altjira) — ancestral creation narratives tied to land (songlines).
- **Texts:** Some PD ethnography (Spencer & Gillen; K. Langloh Parker's *Australian Legendary Tales*, PD); the Rainbow Serpent, Bunyip, Baiame, Wandjina.
- **Story value:** ⭐ Landscape-as-narrative, ancestral beings, totemic origins.
- **Access:** PD scrape (limited).
- **Ethics:** 🚩🚩 Strongly culturally restricted — much Aboriginal knowledge is sacred, gendered, or community-owned; legal PD ≠ permission. Flag prominently.

---

# 21. SOUTHEAST ASIAN

- **Indian-derived epics:** Local *Ramayana* variants — **Ramakien** (Thai), **Reamker** (Khmer), **Hikayat Seri Rama** / **Kakawin Ramayana** (Indonesian/Javanese), **Phra Lak Phra Lam** (Lao). Hanuman-centric.
- **Indigenous:** Philippine epics (**Hudhud**, **Darangen** — UNESCO; **Biag ni Lam-ang**), Vietnamese (Lạc Long Quân & Âu Cơ origin, **Lĩnh Nam chích quái**), Balinese Barong/Rangda, Javanese wayang.
- **Story value:** ⭐⭐ Hybrid Hindu-Buddhist-animist pantheons; shadow-puppet (wayang) narrative tradition; naga, garuda, rakshasa localized.
- **Access:** Scrape / academic / some PD; mostly undigitized 🚩.

---

# 22. CENTRAL ASIAN / TURKIC / MONGOLIAN / SIBERIAN

- **Sources:** **Epic of Manas** (Kyrgyz — one of the world's longest epics), **Epic of King Gesar** (Tibetan/Mongolian), **Jangar** (Kalmyk), Mongolian *Secret History of the Mongols*; Tengri sky-god, shamanism (Erlik, the world tree). Turkic creation myths.
- **Story value:** ⭐ Sky-god Tengri, shamanic cosmology, vast oral epics, the wolf-ancestor (Ashina/Asena) motif.
- **Access:** Scrape / academic; *Secret History* in PD-ish translations 🚩.

---

# 23. CREATURE / BESTIARY DATABASES (cross-tradition)

- **The Medieval Bestiary (bestiary.ca):** ⭐ Illustrated database of medieval bestiary creatures with manuscript sources. Scrape; © site, PD images 🚩.
- **Aberdeen Bestiary (abdn.ac.uk/bestiary):** single manuscript, full transcription + images. Academic, IIIF.
- **Shanhaijing 山海经** (see §10.1) — Chinese creature compendium.
- **Yokai databases** (see §11.2).
- **A Book of Creatures (abookofcreatures.com):** broad cross-cultural cryptid/creature blog 🚩 scrape, ©.
- **Wikidata "legendary creature" (Q2239243) subset** (see §0.2) ⭐ — best structured cross-cultural creature list.
- **Story value:** ⭐⭐ Direct creature catalogs for bestiary/monster generation.

---

# 24. PUBLIC-DOMAIN MODERN MYTHOS

## 24.1 Cthulhu Mythos (Lovecraft)
- **Sources:** H. P. Lovecraft's fiction entered the **public domain** in the US for pre-1929 works, and his major corpus is widely treated as PD (status historically contested but practically open). Full texts on **hplovecraft.com**, Wikisource, Gutenberg Australia, **The H.P. Lovecraft Archive**.
- **Coverage:** The Great Old Ones (Cthulhu, Azathoth, Nyarlathotep, Yog-Sothoth), the Necronomicon, Miskatonic University, cosmic horror cosmology.
- **Access:** Scrape / PD bulk.
- **License:** **Public domain** (US, pre-1929) ⭐; later collaborators/expansions may be ©; "Cthulhu Mythos" shared universe is broadly open.
- **Story value:** ⭐⭐ A complete, freely usable modern pantheon + cosmology + grimoire framework purpose-built for fiction.

## 24.2 Other open modern mythos
- **Public-domain pulp:** Robert E. Howard's Conan/Hyborian (early stories entering PD progressively 🚩 check year), Clark Ashton Smith. **SCP Foundation (scp-wiki.wikidot.com):** collaborative modern creature/anomaly mythos, **CC BY-SA** ⭐ (fully reusable with attribution). **Backrooms** lore (CC BY-SA).
- **Story value:** ⭐ SCP especially is a vast, license-clean (CC BY-SA) corpus of original creatures/entities.

---

# 25. COMPARATIVE-MYTHOLOGY FRAMEWORKS (for motif/structure tagging)

- **Frazer, *The Golden Bough*** (PD): dying-and-rising god, scapegoat, sacred king, sympathetic magic.
- **Campbell, *The Hero with a Thousand Faces*** 🚩 (© — monomyth concept referenceable, text not reusable).
- **Propp, *Morphology of the Folktale*** (31 narrative functions) 🚩 (© translation; the function list is widely cited).
- **Dumézil's trifunctional hypothesis** (Indo-European myth structure) 🚩 ©.
- **Thompson Motif-Index + ATU** (see §0.5) ⭐ — the practical tagging vocabulary.
- **Story value:** ⭐⭐ These give you the *abstract structures* (functions, motifs, archetypes) to index every concrete myth against — the core of a "story source" engine.

---

## ACCESS-METHOD SUMMARY (planning cheat-sheet)

**Best clean APIs (reusable license):**
- Wikidata SPARQL (**CC0**) — structured metadata ⭐⭐
- Sefaria (**JSON REST + bulk**, per-text license field) ⭐⭐
- SuttaCentral (**JSON REST + GitHub**, CC0/CC-BY) ⭐⭐
- Perseus (**CTS + TEI on GitHub**, CC BY-SA) ⭐⭐
- AlQuran.cloud / Quran.com (**JSON REST**, open Arabic)
- Bible-API.com / GetBible / bolls (**JSON REST**, PD translations)
- ctext.org (**JSON REST, free key**, CC BY-SA)
- ORACC (**JSON**, CC BY-SA)
- DCS / SARIT (Sanskrit, CC)

**Best bulk downloads (PD/open):**
- GRETIL (Sanskrit), ETCSL (🚩 NC), CBETA (🚩 NC-SA), Kanripo (Chinese, open), Wikisource dumps, Gutenberg/Gutendex, Internet Archive.

**Scrape-only (no API) 🚩:**
- Sacred-Texts, Theoi, Avesta.org, mftd.org, Mythopedia/Godchecker/Encyclopedia Mythica, Yokai.com, Nichibunken yokai DB, bestiary.ca, a-book-of-creatures.

**License watch-outs 🚩:**
- ETCSL (academic NC), CBETA (CC BY-**NC**-SA), 84000 (NC), API.Bible & ESV (per-version ©), modern translations of Popol Vuh / Huarochirí / Florentine Codex (©), Edith Hamilton / D'Aulaire / Campbell / Propp (©).
- **Ethical (not just legal) flags** 🚩🚩: Aboriginal Australian, Native American, Yoruba/Ifá, Polynesian sacred chants — public-domain status does NOT equal community permission; flag for cultural sensitivity review.

---

*End of catalog. UNVERIFIED — compiled from training knowledge (cutoff Jan 2026); to be live-verified by the main thread with network access. Re-confirm every endpoint, key requirement, rate limit, and license before production use.*

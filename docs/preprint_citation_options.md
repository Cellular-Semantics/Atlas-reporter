# Citation traversal for fresh preprints — options

**Problem.** atlas_chat's reporting workflow assumes the atlas paper is in EuropePMC / Semantic Scholar. For a fresh bioRxiv preprint (e.g. Steele et al. 2026, used here), neither is true: `get_pmc_supplemental_material` returns nothing, and ASTA `snippet_search` scoped to the atlas paper has no CorpusId to hit. The pilot reports for the spatial skin atlas worked around this by giving each agent the JATS XML directly, but blockquotes are then atlas-only — referenced literature appears as paraphrased inline cites, not as validated quoted evidence.

This doc surveys options for fixing that, both heavy (build a local snippet index) and light (better orchestration). It also notes which pieces already exist in `~/Documents/GitHub/paperqa2_cyberian`.

---

## What ASTA actually does (and why it can't be reproduced trivially)

`mcp__Asta_semanticscholar__snippet_search` returns: snippets of paragraph-length text from indexed papers, each carrying a `paper.corpusId`, `score`, `section`, and crucially **`annotations.refMentions`** — character-offset spans where a snippet cites another paper, resolved to a CorpusId. That's what lets it answer "give me sentences in cited papers that mention X" downstream.

To replicate locally for a fresh preprint we need three things:

1. Text chunked by section, with stable offsets
2. Inline citations resolved to canonical IDs (DOI → CorpusId / PMID / PMCID)
3. Per-chunk relevance scoring (BM25, embedding cosine, or LLM rerank)

Semantic Scholar's lag from bioRxiv post to CorpusId assignment varies — Google Scholar reportedly indexes biorxiv within 2 days, Semantic Scholar tends to be slower (~1–4 weeks, anecdotal). So waiting is sometimes acceptable, but for fresh atlases the workflow needs a local path.

---

## Existing tools

### 1. Allen AI `s2orc-doc2json` ([github](https://github.com/allenai/s2orc-doc2json))
- `jats2json` parses JATS XML to S2ORC schema (sections, body_text with cite_spans, bib_entries with DOIs)
- `pdf2json` runs PDF → GROBID → S2ORC
- Output format is exactly what Semantic Scholar consumes
- Status: maintained but slow-moving; works fine for biorxiv JATS

### 2. GROBID ([kermitt2/grobid](https://github.com/kermitt2/grobid))
- Heavyweight ML-based PDF → TEI XML
- ~0.87–0.90 F1 on PMC/bioRxiv reference extraction
- Needed only when JATS isn't available (biorxiv gives JATS, so we can skip)

### 3. PaperQA2 ([Future-House/paper-qa](https://github.com/Future-House/paper-qa))
- RAG over local PDFs with Crossref/Semantic Scholar metadata enrichment
- Three-phase agent: keyword query → candidate retrieval → chunk embed + rank
- Citation graph traversal built in
- Heavier than needed if we just want chunked snippets, but a strong reference implementation

### 4. pubmed_parser / lxml (lightweight)
- Plain JATS → structured dict
- 100-line job, no ML

### 5. OpenAlex
- Citation graph, free API, often picks up biorxiv preprints faster than Semantic Scholar (because it ingests biorxiv directly)
- Doesn't give snippets, only metadata + references
- Useful for the "expand from atlas → cited papers" step even when ASTA is blind to the atlas itself

### 6. Crossref
- DOI → metadata + references (when publishers deposit them, which biorxiv does)
- Free, no auth, fast

---

## What `paperqa2_cyberian` already has

Located at `/Users/do12/Documents/GitHub/paperqa2_cyberian/paperqa2_cyberian/`:

| File | LOC | Purpose |
|---|---|---|
| `parse_jats_citations.py` | 553 | JATS → sentence-level citation associations, resolved to DOI/PMID/PMCID. **This is the missing piece for our preprint problem.** |
| `extract_asta_refs.py` | 197 | Pull `refMentions` out of ASTA snippet_search responses with sentence context |
| `retrieve_chunks.py` | 144 | Local sentence-transformer embedding retrieval over chunked papers |
| `cyberian_llm.py` | 226 | LLM wrapper used for chunk reranking |
| `cache.py` | 42 | Disk cache layer |
| `.claude/skills/paperqa/SKILL.md` | — | Three-step skill: embed retrieve → Haiku rerank → synthesize cited answer |

Planning docs in `paperqa2_cyberian/planning/` already cover the relevant territory: `citation_traversal.md`, `contextual_retrieval.md`, `embedding_skill.md`, `query_decomposition.md`.

So **the engineering largely exists** — what's missing is integration into `atlas_chat` and a clean handoff: a way for the report-synthesis subagent to query a locally-indexed atlas paper the same way it queries ASTA.

---

## Options

### Option A — Lightweight orchestration (no new infrastructure)

For each fresh-preprint atlas:

1. Manual / scripted pre-step: download JATS + supp via the playwright path already proven on Steele 2026.
2. Run `parse_jats_citations.py` from `paperqa2_cyberian` once at project setup → emit `projects/{name}/source/citations.json` (sentences with ref_ids + resolved DOIs).
3. Synthesize-report subagent: prompt it to use the citations JSON as its evidence corpus. Blockquotes drawn from JATS sentences; "(Author, Year)" citations resolved via the citations JSON.
4. Validation hook updated to accept blockquotes from `citations.json` sentences (not just `atlas_full_text.txt`).

**Pros:** ~half a day of work; reuses what exists; preserves the existing report-validation contract.
**Cons:** No retrieval — agent has to grep the JATS itself; no quoted evidence from *referenced* papers, only from the atlas paper itself.

### Option B — Local ASTA-style snippet index (per project)

Add a skill `local-paper-index <jats-path>` that:

1. Parses JATS → S2ORC-shape JSON (using `s2orc-doc2json` or the existing parser)
2. Splits body into ~paragraph-sized chunks; embeds with sentence-transformers (already in `retrieve_chunks.py`)
3. Resolves every inline citation's DOI → CorpusId via the Semantic Scholar /paper API (this still works — only the atlas itself is missing, not the references)
4. Emits a JSON store with the same shape as a serialised ASTA response: `{paper, snippet:{text, section, annotations:{refMentions:[{corpusId, char_start, char_end}]}}}[]`

The synthesize-report agent then has *two* retrieval tools: ASTA for indexed literature and `local_snippet_search(atlas_id, query)` for the fresh preprint, returning identically-shaped objects.

**Pros:** Clean parity between fresh and indexed papers; downstream prompts don't change; reference-paper quotes become possible because each refMention's CorpusId can be passed to ASTA `get_paper`.
**Cons:** Real engineering — a new skill plus a query API. ~2–3 days.

### Option C — Just use PaperQA2 directly

Wrap PaperQA2 as a subagent. Index the JATS + any cited papers that have open-access PDFs (via OpenAlex / Crossref → unpaywall). Let PaperQA2 do retrieval + citation tracking. Report-synthesis becomes "ask PaperQA2 for the markers / location / function of cell type X, with citations".

**Pros:** Strongest off-the-shelf RAG; handles citation graph natively; the user already has paperqa2_cyberian wiring.
**Cons:** Less control over the report format and validation contract; PaperQA2's answer style is conversational, not template-locked; another moving piece in the stack. Also blockquote validation gets harder because PaperQA2 paraphrases.

### Option D — Push ingestion to OpenAlex / Crossref and wait

Submit the atlas DOI to OpenAlex (they accept biorxiv DOIs ~immediately); use OpenAlex + Crossref for the citation graph and identifier resolution. Don't index the atlas paper text locally — leave that to the manual JATS read. Use ASTA only for the cited *references*, which are presumably older and indexed.

**Pros:** Smallest delta from current workflow.
**Cons:** Still no quoted evidence from references, only the atlas; same shape of output as the pilot run.

### Option E — "Just better instructions" (the simple option)

You raised this yourself. Rework the report-synthesizer prompt to:

1. Treat the JATS XML as the primary corpus, but explicitly require the agent to traverse Steele's reference list (which is in the JATS) and run ASTA `get_paper` or `snippet_search` on each referenced DOI to gather quotable text from those cited papers.
2. Stage the resulting external snippets as a second `all_summaries.json` evidence file (alongside `atlas_full_text.txt`).
3. Allow blockquotes from either file in validation.

No new infrastructure. Just a tightened orchestration loop with the agent doing the equivalent of citation traversal manually via the existing MCP tools. Each report would do ~5–15 extra MCP calls.

**Pros:** Probably the right "ship it" answer for the spatial skin atlas pilot. Zero new code.
**Cons:** Doesn't scale: 107 cell types × 10 ref-papers × 1 MCP call each = ~1000 calls; rate limits and cost. Also doesn't fix the underlying gap for future atlases.

---

## Recommendation

For the **spatial skin atlas right now**: Option E — adjust the synthesizer prompt to require post-hoc reference traversal via ASTA `get_paper` on each referenced DOI in Steele's JATS, and to capture quotable evidence from those into `all_summaries.json`. That gets us validated cross-paper blockquotes for the remaining 97 reports without new infrastructure.

For the **general atlas_chat improvement**: Option A as a fast win, then Option B if the team plans to ingest more fresh preprints (HDCA, BICAN, etc. will keep hitting this). Option B mostly means lifting `paperqa2_cyberian` into a callable skill — the JATS parser, embeddings, and refMention extractor are already written.

PaperQA2 directly (Option C) is heavier than needed unless atlas_chat moves toward more open-ended literature Q&A.

---

## Open questions before committing

1. ~~Do we want blockquotes from *referenced* papers~~ **— Resolved: yes.** The validation contract — every blockquote must be an exact substring of the evidence corpus — is retained, and the corpus grows to include chunks from cited papers (not just the atlas). PaperQA2-style chunks are larger (paragraph- to section-sized, ~2–3k chars) but a quoted sentence is still a substring of its containing chunk, so `report_checker.py`'s substring check still works without modification. Implication: the local snippet store must persist **full chunk text**, not just metadata or hashed embeddings — otherwise validation has nothing to scan.
2. How much should atlas_chat depend on `paperqa2_cyberian`? **— Held over.** Leaning toward centralised (single library install, atlas_chat calls into it as a dependency) rather than copying files, but the decision can wait until the integration work starts. Either path keeps `paperqa2_cyberian` as the source of truth for the parser, embeddings, and chunker.
3. ~~Validation corpus location~~ **— Resolved: project-wide chunk store.** All chunks live under `projects/{name}/chunks/` (or similar single location) — shared across cell types, no duplication. **Refinement:** when a report is actually written, the specific chunks the report blockquotes can be extracted/copied into `traversal_output/{cell_type}/` so each report's validation corpus is self-contained (cheap substring scan over a small file, rerunnable in isolation). The master store is the canonical source; the per-cell-type extract is a derived artefact, written at report-synthesis time. This keeps both properties: one shared chunk index for retrieval, and self-contained validation per report.

### Implications for Option B design

The substring-validation requirement constrains the local snippet store shape:

- Each chunk is stored as plain text on disk (not just an embedding vector). Embeddings sit alongside for retrieval.
- Chunks should be **whole paragraphs or whole sections**, not sentence-fragments. A larger chunk window means a quoted sentence from the chunk is still trivially a substring, and chunk boundaries don't accidentally cut a quotable sentence in half. PaperQA2's default chunk size (~3000 chars with 100-char overlap) is in the right ballpark.
- When `report_checker.py` runs, it concatenates all chunk-text files in the evidence corpus and does the same `quote in text` check it does today — no schema change needed.
- The ASTA-shape wrapper (snippet object with `paper`, `score`, `section`, `annotations.refMentions`) is only needed for the *retrieval API* shape, not for the validation corpus. The two can be the same file (chunks-with-metadata) or split (chunks for validation + index for retrieval).

This means Option B is even smaller than first sketched: build a chunker that emits paragraph-sized snippets-with-metadata, embed them with the existing `retrieve_chunks.py` machinery, expose `local_snippet_search(paper_id, query) → snippets[]` returning ASTA-shaped objects, and let `report_checker.py` scan the same chunk files. No fork of the validation logic.

---

## Appendix — bioRxiv programmatic access (why we used Playwright)

We used Playwright to download `paper.jats.xml` and `supp.pdf` because `curl` got blocked by Cloudflare. The intent here is *not* an excuse for keeping Playwright — it's the wrong tool if there's a real API. Here's the actual landscape.

### What bioRxiv exposes

| Endpoint | What it returns | CF-gated? |
|---|---|---|
| `api.biorxiv.org/details/biorxiv/{doi}/na/json` | Metadata (title, authors, abstract, jatsxml URL) | **No** — works via curl. We already used this. |
| `api.biorxiv.org/pubs/biorxiv/{interval}/{cursor}` | Listings, OAI-PMH style harvesting | No |
| `www.biorxiv.org/content/early/.../<id>.source.xml` | JATS XML (full text) | **Yes** — served via Highwire behind CF |
| `www.biorxiv.org/content/.../v1.full.pdf` | Main PDF | Yes |
| `www.biorxiv.org/content/biorxiv/.../DC1/embed/media-N.pdf` | Supplementary files | Yes |
| `s3://biorxiv-src-monthly/` | Monthly TDM dump of all JATS + PDFs | No (S3 auth, requester-pays) |

So: **the metadata API is free and uncomplicated, but the actual full-text URLs the metadata returns are CF-protected**. The bioRxiv "TDM" page is honest about this — for programmatic bulk access they direct you to S3.

### Realistic options for atlas_chat

1. **`curl_cffi` / `cloudscraper` with browser TLS fingerprint.** A 10-line Python function: hit `api.biorxiv.org/details/...` for metadata + JATS URL, then fetch the JATS URL via `curl_cffi` (which impersonates Chrome's TLS stack). For Steele 2026 this would have worked without a real browser. Caveat: brittle if CF tightens. `cloudscraper` has gone in and out of working over the years.
2. **EuropePMC mirror, when available.** EuropePMC ingests many bioRxiv preprints (with lag). When indexed, `mcp__artl-mcp__get_europepmc_full_text` returns clean Markdown — no CF, no parsing, MCP-native. Worth checking *first* even for fresh-ish preprints. Steele 2026 isn't there yet but a 2-month-old preprint usually is.
3. **AWS `s3://biorxiv-src-monthly` (requester-pays).** ~6 TB total, monthly snapshots; ~$0.09/GB egress. Overkill for single-paper fetch but the right answer if atlas_chat starts ingesting many preprints — a single monthly sync, then everything is local. Probably impractical for routine use.
4. **Playwright (what we did).** Works, but pulls in a headless browser dependency. Fine as a fallback when the other methods fail; bad as the default.

### Recommendation for the workflow

A small helper `fetch_preprint(doi)` that tries, in order:
1. EuropePMC via existing MCP (`get_europepmc_full_text`) — preferred when available
2. bioRxiv metadata API → JATS URL → fetch with `curl_cffi`
3. Playwright fallback only if the above fail

This keeps Playwright as a safety net rather than the primary path. Worth a half-day if Option A/B above gets built — it's the natural source step that feeds the local JATS parser.

---

## Sources

- [allenai/s2orc-doc2json](https://github.com/allenai/s2orc-doc2json) — JATS/PDF → S2ORC JSON
- [Future-House/paper-qa](https://github.com/Future-House/paper-qa) — PaperQA2 RAG library
- [PaperQA2 cookbook](https://futurehouse.gitbook.io/futurehouse-cookbook/paperqa)
- [grobid](https://github.com/kermitt2/grobid) — PDF → TEI XML
- [GROBID benchmark on bioRxiv ~0.90 F1](https://grobid.readthedocs.io/en/latest/End-to-end-evaluation/)
- Local: `paperqa2_cyberian/paperqa2_cyberian/parse_jats_citations.py`, `extract_asta_refs.py`, `retrieve_chunks.py`
- Local: `paperqa2_cyberian/.claude/skills/paperqa/SKILL.md`
- [bioRxiv machine access / TDM page](https://www.biorxiv.org/tdm) — describes API + S3 bucket
- [bioRxiv API root](https://api.biorxiv.org/) — metadata endpoints (no CF)
- [bioRxiv S3 TDM announcement (2020)](https://connect.biorxiv.org/news/2020/04/18/tdm)
- [curl_cffi](https://github.com/lexiforest/curl_cffi) — TLS-fingerprint-impersonating HTTP client
- [VeNoMouS/cloudscraper](https://github.com/venomous/cloudscraper) — Cloudflare bypass library (works intermittently)
- ["How to download bioRxiv on a budget"](https://sitlabs.org/writing/biorxiv.html) — community write-up on practical access

# Retrieval test — work so far

**August 2026, branch `test/retrieval-matrix`.** Status: Stage 1 is built and ready to run
but **has not been run**. Setting it up produced two findings that matter more than the
measurement it was built for, and one of them changes how the measurement has to be scored.

Plan: `planning/retrieval_matrix_plan_2026-08.md`. Items:
`planning/retrieval_test_items_draft_2026-08.md`, frozen to `experiments/items.json`.

---

## What was built

- **Item set frozen** — 57 items parsed to `experiments/items.json` with id, group,
  question, answer, gold span, abstraction tag and paper. 24 carry a verbatim span, which
  is what Stage 1 needs; the rest (C synthesis, D citation, E supplement, F absent) belong
  to later stages.
- **`experiments/corpus.py`** — paper text and chunking shared by every arm, so arms differ
  only in ranking, not in what they read. Citations are stripped from the tree rather than
  from the string, and paragraphs are walked in document order.
- **`experiments/norm.py`** — two normalisations. `norm` for display-faithful matching;
  `norm_loc` (letters only) for deciding whether a span is present, applied uniformly
  across arms because ASTA renders superscript references as loose digits and our JATS walk
  drops them.
- **`experiments/stage1.py`** — the four arms (document order, BM25, MiniLM dense, ASTA
  snippet search), cost-to-answer scoring, and the permutation null.

Corpus sizes, which turn out to matter: **Gopee 152 chunks / ~25,900 tokens; Suo 113 chunks
/ ~16,900 tokens.** A whole atlas paper fits in context for a few cents.

All 24 gold spans verified present in their paper's text, none straddling a chunk boundary.

---

## Finding 1 — within a paper, ASTA does not retrieve, it only reorders

Three deliberately unrelated queries against the same paper:

- "hair follicle placode timing"
- "macrophage angiogenesis VEGFA endothelial"
- "statistics reproducibility software versions"

Each returns **72 chunks. The same 72 chunks.** Identical sets, 72/72 pairwise overlap.
Only the ordering changes — and it changes sensibly, the top hit differing appropriately
per query.

Total text returned is ~26,400 tokens against the paper's own ~25,900.

**So `limit` is not a retrieval control for paper-scoped search — it is a truncation
control.** There is no setting at which snippet search fetches less of the paper; it can
only save tokens if you trust the ranking and cut. That makes the ranking quality the
entire question, which is what Stage 1 measures, and it retires the idea that snippet
search reduces what has to be read.

## Finding 2 — ASTA's copy is near-complete; the apparent gap was mostly my extraction

**An earlier draft of this document reported 89% coverage and claimed ASTA and PMC were
different renderings of the paper. Both were wrong.** Decomposed properly:

Starting point: 60 of 545 PMC "sentences" appeared to be absent from ASTA's 72 chunks.

| Cause | Sentences | Whose fault |
|---|---|---|
| Figure and table legends | ~45 | **mine** — extraction bug |
| Split across two ASTA chunks | 12 | neither; the text is there |
| Genuinely absent from ASTA | 10 | ASTA ingest |

**Figure legends.** `<fig>` elements sit *inside* body `<p>` elements in this JATS, so
`itertext()` spliced legend text onto the end of prose paragraphs — "…archived at
Zenodo.**Fig. 2Human prenatal HF development.a, Representative images…**". The three
largest missing runs each begin exactly at such a splice. ASTA does not index figure
legends, quite reasonably. Fixed by stripping `fig` / `table-wrap` /
`supplementary-material` subtrees before extracting text.

With captions excluded: **478 of 500 prose sentences present, 96%.**

**Chunk-boundary splits.** 12 of the remaining 22 are sentences straddling two ASTA
chunks. The content is present; no single chunk holds the whole sentence. This is a
scoring problem, not a coverage problem — see below.

**Genuine gaps: 10 sentences.** ASTA covers PMC prose sentences 7 through 498 of 499,
contiguously. The dominant gap is the **first seven sentences of the Main text** — the
opening of the introduction — with one further run of four in "Epidermal placode and
matrix formation". A contiguous run at the very head of the document looks like an ingest
offset rather than a rewrite.

**On the version hypothesis: no evidence.** The one thing I had cited as text ASTA holds
and PMC lacks turned out to be the PMC **abstract**, which the body walker excludes. With
that removed there is nothing pointing at a published-versus-accepted-manuscript
difference. Comparing against a publisher PDF would test it directly, at the cost of
introducing PDF extraction error; on the current evidence it is not worth doing.

**Effect on the gold spans:** of the five that appeared missing, two were chunk-boundary
splits and three are genuine gaps (A1, A3 in the introduction run; B1 in the placode run).

### Consequence for scoring

Two independent reasons not to use exact substring matching, so the scorer now measures
**word 5-gram coverage of the span at a 0.8 threshold, accumulated over everything read so
far**:

- a span split across chunks is available to a reader holding both, but the chunks arrive
  separated in rank order, so a joined string is not contiguous — an n-gram measure loses
  only the few grams spanning the seam;
- it tolerates rendering differences between sources, which removes the need for a separate
  source-neutral scorer.

Under it, 18 of 21 Gopee spans are available to ASTA, and 21 of 21 to the PMC-reading arms
(the sanity check the scorer has to pass).

### Consequence for the pipeline

Weaker than I first reported, but not nothing. ASTA does not index figure legends, and
misses a small contiguous run at the head of the document. Figure legends carry
cluster-to-name mappings and marker panels in atlas papers, so anything relying on ASTA
alone will not see them. The local index, built from PMC JATS, does — provided its own
extraction keeps captions rather than splicing them into prose.

## Incidental fixes and corrections

Found while building, worth recording:

- **`_jats_parser` reference parsing is publisher-specific.** It handles
  `<element-citation>` only. Suo (AAAS via Europe PMC) uses `<mixed-citation>` with the DOI
  in `ext-link/@xlink:href`, so all 103 of its references resolve to empty — silently. Any
  AAAS-sourced paper contributes no followable citation edges to a local index. Deserves a
  ticket; it is why no citation-following items were drawn from Suo.
- **Body-level paragraphs were being missed.** A section walker that only descends into
  `<sec>` loses main-text paragraphs that sit directly under `<body>`, which is how Suo is
  structured. Fixed in `corpus.py`; worth checking whether the production chunker has the
  same gap.
- **Superscript reference markers glue to the preceding word** ("16 PCW19"), so naive span
  matching fails. Stripping `<xref ref-type="bibr">` from the tree is the clean fix.
- **A correction to something I asserted earlier:** I reported that the macrophage subset
  labels in Supplementary Table 22 looked swapped. They are not. SLC40A1 appears only in
  the iron-recycling block, with VCAM1 and CD5L below it. The MHC-II-looking top of that
  block is an artefact of ranking by `scores` rather than by effect size.

---

## What is ready, and what is not

**Ready to run now:** Stage 1 over `document`, `lexical` and `local` — three arms reading
the identical PMC text, 24 items, exact-span scoring, permutation null. This answers
whether dense ranking beats BM25 beats reading from the front, and how much the
abstraction tags cost each.

**Needs the new scorer first:** the ASTA arm.

**Not started:** Stage 2 (reading, model varies) and Stage 3 (supplements).

## Reproducing

```bash
cd ../retrieval-matrix
uv sync --extra local-index --extra supplements
uv run python -c "import sys; sys.path.insert(0,'experiments'); import stage1"
```

`experiments/papers/` holds the two JATS files; nothing in `experiments/` is intended to
merge.

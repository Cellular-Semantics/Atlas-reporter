# Retrieval experiments on `test/retrieval-matrix` — what was done, in order

**Branch is experimental. Nothing here is built to merge except the write-ups themselves.**

Four lines of work ran on this branch, partly in parallel and with unfortunate overlapping
names. This page is the map. Each entry says what the work asked, what it found, and where to
look. Read this page and then only the documents you need.

If you want one document rather than a map: **`citation_traversal/README.md`** is
self-contained for the citation-following work, which is the most recent and the most
directly relevant to atlas-reporter's primary aim.

---

## The four lines of work

| # | line of work | question | where |
|---|---|---|---|
| 1 | **Ranking** | Inside one paper, is ranked retrieval worth anything over reading from the front? | report §4 |
| 2 | **Reading** | Given a slice of text, does a model answer correctly, and can its quotes be trusted? | report §5 |
| 3 | **Grounded naming** | Can we author realistic, answerable questions across *many* cell types, and what does a quote requirement buy? | report §6 |
| 4 | **Citation traversal** | Can we follow citations out of an atlas paper — reach the cited paper, retrieve evidence, and check the claim? | `citation_traversal/` |

**Lines 1–3 now have one integrated write-up:
`experiments/retrieval_tests_report_2026-09.md`.** It replaces the nine separate
plan-and-results documents those lines used to have, which are archived unchanged at
`experiments/archive_2026-09_superseded_writeups/`. Read the report, not the archive — three
figures in the old documents do not match the data, and one class of result in them is now
known to be unsound (report §7). The summaries below are kept as a map and are correct as far
as they go, but the report is the authority.

Line 4 is unaffected and still lives in `planning/citation_traversal/`.

Naming warning, since it caused real confusion: **line 3 and line 4 both used "Stage 3"
labels while running concurrently in the same worktree.** The report drops stage numbering
entirely and maps the old names in its §11.3. The supplement-derived "Stage 3" designed in the
archived handoff is a **fifth** thing that was never run.

---

## 1. Ranking — is ordering a paper worth anything?

Report §4 (Test 1); constraints found while building it in §3 · no model calls, fully
deterministic · data in `experiments/results/`

Five ways of ordering one paper's chunks, measured as tokens-to-answer.

- **Ranking is worth roughly 10×** over reading from the front (~350–450 tokens vs 3,514).
- **The embedding does not beat BM25** on typical questions — medians are a wash. Plain keyword
  search would do the job with no API key and no 500 MB model.
- **Variance is the real finding.** BM25 and the embedding each have items costing more than
  reading the whole paper (13k, 19k tokens). ASTA's worst case is 3.1k. Inside a paper its
  value is consistency: never best, never a disaster.
- Setting this up produced two findings that outlived it: **within a paper ASTA reorders rather
  than retrieves**, and an apparent coverage gap in ASTA's copy turned out to be mostly a
  defect in our own extraction.

## 2. Reading — does the model answer, and are its quotes real?

Report §5 (Test 2) · 231 reads, 42 items × 3 conditions × 2 models · data in
`experiments/stage2/`

- **Nothing was invented** — no read produced a quote with no source in the context. Four
  wrong answers in 231 reads, all on one item.
- **Absence is reported reliably** — 18/18 when the passage was genuinely withheld.
- **Haiku splices quotes across non-adjacent passages; Sonnet never does.** All 13 splices are
  Haiku's (the old write-up said 10; it predates the ASTA condition). Splices fail
  exact-substring quote validation, so this argues against Haiku for
  evidence gathering regardless of cost.
- **A 2k slice and the whole paper are equivalent on accuracy.** The case for retrieval is
  cost, not accuracy.
- **Citation-following scored 0/12, correctly declined** — because our corpus stripped the
  reference list. That gap is what line 4 went on to address.
- The archived write-up opens with a corrections note retracting two findings from an earlier
  draft. Six scoring defects were found during this run, all biased against the readers; the
  report's §7 catalogues all nine found across lines 1–3.

## 3. Grounded naming — realistic questions across many cell types

Report §6 (Test 3) · **two full runs: 660 reads, 355 judge verdicts, 55 items × 6 conditions ×
2 reader models** · data in `experiments/stage3b/`, name roster in `experiments/roster/`

Lines 1 and 2 used 42 items drawn mostly from one cell type. Testing the pipeline properly
needs many questions across many cell types, phrased as the authors phrase things and known to
be answerable — which requires knowing what the authors actually call each cell type.

- **Requiring a verbatim quote eliminated unsourced answering entirely**: with no context the
  reader declined 55/55 in both runs, and across all 660 reads there were zero fabricated
  quotes.
- **A 1.9k retrieved slice ties the whole paper on accuracy** — but the whole paper is fetched
  once and reused across questions, so it was about **three times cheaper per question**.
  Retrieval's saving depends on how many questions are asked of one paper.
- **The reader model moved results more than any retrieval choice** (net 40-to-6 between runs,
  against a five-item spread across retrieval conditions), and the two models fail differently:
  one declines, the other produces sourced wrong answers that quote validation cannot catch.
- Four of the 55 items are defective, so 44/55 is a floor and not a benchmark.

## 4. Citation traversal — following references out of the atlas paper

**`citation_traversal/README.md` is self-contained; start there.** Companions, all in the
same folder: `citation_traversal/aims.md`,
`citation_traversal/reaching_the_cited_paper.md`,
`citation_traversal/do_cited_papers_support_the_claims.md`,
`citation_traversal/retrieving_the_evidence.md`. Code and data in
`experiments/citation_traversal/`.

- Separated two aims that had been conflated: **enrichment** (learn more about a cell type than
  the atlas paper says — atlas-reporter's primary aim) and **verification** (does a cited paper
  support the assertion attached to it).
- **Reaching the right paper is solved**: 0 resolution errors in 174 citations; the failure mode
  is silence (10% unresolved), never a wrong target.
- **Searching the whole literature fails; searching the atlas paper's reference list works** —
  1–6 of 19 vs **19 of 19**. Then a paper-scoped search returns the supporting passage 97% of
  the time it exists. The design this implies is two hops.
- **Coverage is the binding constraint**: only 70% of supporting passages are in ASTA at all,
  with misses concentrated in **introductions**, **figure captions**, and one abstract-only
  paper. Introductions are also where the citations most worth following live.
- **Citations are not always sound**: of 19 claims read against the full text of their sources,
  12 supported, 5 partial, 1 not supported, **1 flatly contradicted** — and all 19 pass our
  current quote and reference validation.
- **Access is the outer limit.** Of the atlas paper's 109 references, 38 yield full text from
  PMC, 56 are held by ASTA, 57 by either — and 48% by neither. Availability flags overstate
  access by a third. ASTA is the broader route but its copy drops introductions and captions,
  so the waterfall trades coverage against text quality. See
  `citation_traversal/paper_availability.md`.

---

## Supporting documents, not experiments

| document | what it is |
|---|---|
| `supplement_corpus_findings_2026-08.md` | What a real supplementary-material corpus looks like — 22 papers, eight publishers. Reachability, retrieval routes, failure modes, cost. |
| `../experiments/archive_2026-09_superseded_writeups/` | The nine superseded documents for lines 1–3, archived unchanged with a README mapping each to the section that replaced it. Kept for their reasoning and worked examples; **do not quote figures from them**. |
| `ROADMAP_pre_2026-08_superseded.md` | Superseded. |

---

## Findings that recur across every line of work

Worth stating once, because each was rediscovered independently:

1. **Scoring harnesses fail closed — usually.** Thirteen scoring defects have been found on
   this branch: nine across lines 1–3, four in line 4. Twelve made retrieval or the reader look
   *worse* than it was. The thirteenth ran the other way — treating one marked sentence as the
   only evidence for an answer, which understated retrieval coverage and excused reader
   declines (report §7.1). Check a new scorer's bias deliberately, in both directions, rather
   than waiting to notice it. None of the thirteen was caught by a test.
2. **Never derive answer keys from prose.** Keys should come from markup, a table lookup, or an
   explicitly stated intended answer. Regex over prose cannot tell an answer from an aside.
3. **Quote validity is not correctness.** `correct`, `grounded-but-wrong`, and `fabricated` are
   three different outcomes and must stay separate. Line 4 added a fourth: `attributable but
   contradicted by the source`.
4. **Different services serve different renderings of the same text.** Split subscripts,
   de-hyphenated line breaks, dropped characters, and occasionally a different version of the
   paper. Exact-substring quote validation therefore needs to record which rendering a quote
   came from. Three independent measurements now say this.
5. **A decline is not a failure**, and whether it is correct depends on the question type.

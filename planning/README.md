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
| 1 | **Ranking** | Inside one paper, is ranked retrieval worth anything over reading from the front? | `retrieval_stage1_*` |
| 2 | **Reading** | Given a slice of text, does a model answer correctly, and can its quotes be trusted? | `retrieval_stage2_*` |
| 3 | **Grounded naming** | Can we author realistic, answerable questions across *many* cell types, and what does a quote requirement buy? | `retrieval_stage3b_results_2026-08.md` |
| 4 | **Citation traversal** | Can we follow citations out of an atlas paper — reach the cited paper, retrieve evidence, and check the claim? | `citation_traversal/` |

Naming warning, since it caused real confusion: **line 3 and line 4 both used "Stage 3"
labels while running concurrently in the same worktree.** Line 3 is "Stage 3b" and its data is
in `experiments/stage3b/`. Line 4 has since been renamed to describe itself and lives entirely
in `planning/citation_traversal/` and `experiments/citation_traversal/`. The
supplement-derived "Stage 3" designed in `HANDOFF_stage3_extended_test.md` is a **fifth** thing
that was never run.

---

## 1. Ranking — is ordering a paper worth anything?

`retrieval_stage1_results_2026-08.md` · setup findings in `retrieval_stage1_setup_findings_2026-08.md`
· plan in `retrieval_matrix_plan_2026-08.md` · no model calls, fully deterministic

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

`retrieval_stage2_results_2026-08.md` · plan in `retrieval_stage2_plan_2026-08.md`
· 231 reads, 42 items × 3 conditions × 2 models

- **Fabrication is essentially absent** — 1 fabrication and 3 wrong answers in 210 reads.
- **Absence is reported reliably** — 18/18 when the passage was genuinely withheld.
- **Haiku splices quotes across non-adjacent passages; Sonnet never does.** All 10 splices are
  Haiku's. Splices fail exact-substring quote validation, so this argues against Haiku for
  evidence gathering regardless of cost.
- **A 2k slice and the whole paper are equivalent on accuracy.** The case for retrieval is
  cost, not accuracy.
- **Citation-following scored 0/12, correctly declined** — because our corpus stripped the
  reference list. That gap is what line 4 went on to address.
- The document opens with a corrections note retracting two findings from an earlier draft.
  Five scoring defects were found during the run, all biased against the readers.

## 3. Grounded naming — realistic questions across many cell types

`retrieval_stage3b_results_2026-08.md` · 167 reads, 77 judge verdicts, 55 items × 3 conditions
· data in `experiments/stage3b/`, name roster in `experiments/roster/`

Lines 1 and 2 used 42 items drawn mostly from one cell type. Testing the pipeline properly
needs many questions across many cell types, phrased as the authors phrase things and known to
be answerable — which requires knowing what the authors actually call each cell type.

- **Requiring a verbatim quote eliminated unsourced answering entirely**: with no context the
  reader declined 55/55, and across 167 reads there were zero fabricated quotes and zero
  substitutions.
- **A 1.9k retrieved slice scored 49/55 against 51/55 for the whole paper**, confirming the
  equivalence finding on a broader item set.
- Most residual failures were defects in the items, not reader errors.

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
| `retrieval_test_items_draft_2026-08.md` | The original 57-item question set, human-readable, grouped by question type (literal, located, synthesis, citation-following, supplement, absent). |
| `HANDOFF_stage3_extended_test.md` | Design for a supplement-derived test that was **never run**. Its "hard-won rules" section is still the best single list of scoring traps on this branch. |
| `retrieval_matrix_plan_2026-08.md` | The original plan for lines 1–2. Useful for what was deliberately excluded. |
| `ROADMAP_pre_2026-08_superseded.md` | Superseded. |

---

## Findings that recur across every line of work

Worth stating once, because each was rediscovered independently:

1. **Scoring harnesses fail closed.** Every scoring defect found on this branch — five in line
   2, four in line 4 — made retrieval or the reader look *worse* than it was. Check a new
   scorer's bias deliberately rather than waiting to notice it.
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

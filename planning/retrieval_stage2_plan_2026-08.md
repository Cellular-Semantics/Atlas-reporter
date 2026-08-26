# Stage 2 plan — does a model actually answer, and what does it cost?

**Branch `test/retrieval-matrix`.** Follows `planning/retrieval_stage1_results_2026-08.md`.
Not yet started.

---

## 1. Why this is a different measure

Stage 1 measured **availability** — how much text you read before the answer is present.
Stage 2 measures **whether a model produces the right answer from a given context**, which
Stage 1 cannot see, in three specific ways:

- **Present but missed.** The span is in context and the model still answers wrongly.
  Stage 1 counts that as a success.
- **Absent but answered.** Stage 1 has nothing to say about fabrication. It is the failure
  mode that gets *worse* as models get better at sounding right, and the F items exist to
  measure it.
- **More context can hurt.** Availability is monotone: read more, you can only gain.
  Correctness is not. If it were, this stage would be unnecessary and we could infer
  everything from Stage 1.

It also **tests the assumption underneath every Stage 1 number** — that a chunk containing
the gold span lets a reader answer. If that turns out to be weak, Stage 1's rankings need
re-reading.

## 2. Design

Not incremental reading. Fix a set of **context budgets**, fill each from the top of an
arm's ordering, and ask the question once per cell.

**Budgets:** ~500, ~2,000, ~8,000 tokens, and the **whole paper** (~24,000).
The whole-paper condition is the ceiling on both axes — best possible availability, worst
possible cost — and it is the strategy we are implicitly testing against.

**Arms carried forward from Stage 1:** `hybrid` (best local median and mean), `asta` (best
tail), and `document` (the baseline that competes). BM25 and dense alone are dropped —
hybrid dominates both on medians and inherits the better parent per tag, so carrying all
five would multiply model calls without adding a decision.

**Models:** Haiku and Sonnet. Opus only on items where they disagree.

**Items:** roughly 40, which is where Stage 2 pays off — it unlocks three groups Stage 1
could not score at all:

| Group | Why Stage 1 could not use them | What Stage 2 gets |
|---|---|---|
| C (synthesis) | answer spans several passages, no single span | whether the model combines them |
| D (citation-following) | the answer is a reference, not a span | whether the citing claim's source is recoverable |
| F (unanswerable) | nothing to locate | fabrication rate |
| A, B (span items) | already scored | present-but-missed rate; validates the span proxy |

Roughly 40 items × 3 arms × 4 budgets × 2 models ≈ 960 calls at the full crossing. Trim
first: run A/B/F at all budgets, and C/D only at the two larger budgets and whole paper,
since small budgets cannot hold multi-passage answers by construction.

## 3. Scoring

- **A, B, D, E** — auto-scored. Answers are gene lists, numbers, named entities or DOIs;
  compare as sets against the gold answer. No judge needed.
- **C** — needs a judge. Model judge with the gold answer in hand, hand-check a sample.
- **F** — scored on refusal versus fabrication. An answer that hedges but still asserts
  counts as fabrication; only an explicit "the paper does not say" is a pass.
- **Grounding** — where the model quotes support, check the quote is in the supplied
  context using `report_checker.check_quotes`. Catches the case where the answer is right
  but the support is invented.

## 4. What it decides

- **Whether the whole-paper strategy wins.** A whole atlas paper is ~24,000 tokens. If
  Haiku over the whole paper matches Sonnet over a curated 2,000-token context, the
  architecture simplifies enormously and per-paper batching becomes the obvious design.
- **Whether ASTA's tail advantage survives contact with a model.** Stage 1 says ASTA is
  never a disaster and hybrid sometimes is. If the model recovers from a bad context by
  saying so rather than guessing, the tail matters less than it looks.
- **How hard absence has to be enforced.** If good models fabricate on F items even at
  generous budgets, then a per-aspect "not found" record cannot be a prompt instruction —
  it has to be a required output field with a validator behind it.
- **Whether the span proxy holds**, and so how much weight Stage 1 can carry.

## 5. Deliberately not in Stage 2

- **Supplements** — Stage 3. The E items cannot be answered from body text at all, and
  averaging them in would corrupt both.
- **Cross-paper retrieval** — needs a corpus, not two papers.
- **Query decomposition** — Stage 1 found keyword reduction changed nothing (352 → 352),
  which is indirect evidence against query engineering as a lever. A direct test belongs
  after the reading question is settled.

## 6. Note on the results-first idea

Prioritising results sections over the rest of the body was measured and does not pay:
median 3,374 against document order's 3,514, which is just the four intro chunks, and a
worse tail. The reason is structural — papers are already ordered results-before-methods,
so document order never reaches Methods before finding a results answer.

Where a section prior should pay is **figure legends and supplementary tables**, which do
not compete with body text on document order because they are separate artefacts. ASTA
does not index legends at all, and atlas papers put cluster-to-name mappings and marker
panels in them. That belongs in Stage 3, and it is a stronger case than body-text
reordering ever was.

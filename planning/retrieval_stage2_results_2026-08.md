# Stage 2 results — does a model answer, and can its quotes be trusted?

**August 2026, branch `test/retrieval-matrix`.** Complete: **210 reads plus three judge passes**, 42 items × 3
conditions × 2 models, run as Claude Code subagents on quota (no API billing).

Follows `planning/retrieval_stage1_results_2026-08.md`. Raw data in `experiments/stage2/`
(contexts, answers, scores, quote audit).

---

## Summary

**Read the corrections note first (§4b).** An earlier draft of this document reported two
findings that the corrected scoring does not support. Both are retracted below.

1. **Fabrication is essentially absent, and wrong answers are rare.** 1 fabrication and 3
   wrong answers in 210 reads, plus 2 partials — six non-correct outcomes in total,
   concentrated on two items (B9 and C5). Sonnet's only errors are two reads of B9.
2. **Absence is reported reliably.** On the 21 items where the passage was deliberately
   withheld, both models said so 18 times out of 18 that it was genuinely missing.
3. **Haiku splices quotes; Sonnet never does.** All 10 spliced quotes in the run are
   Haiku's. This is measured directly against the supplied text and is unaffected by the
   answer-key problems below.
4. **Citation-following is impossible from body text — 0/12 for both models**, correctly
   declined. Our corpus strips the reference list.
5. **The 2k slice and the whole paper are equivalent on accuracy** (Sonnet 21/21 vs 20/21).
   The case for the slice is cost — 10× fewer tokens — not accuracy.
6. **ASTA trails the local hybrid at equal token budget** (18/21 vs 20/21, both models),
   because its chunks are ~2× larger — 5 passages vs 11 for the same ~1,800 tokens — and
   its copy of the paper is lossier. Stage 1's "ASTA has the best tail" holds for ranking
   position but does not survive a fixed *token* budget.

**Retracted from the earlier draft:**

- ~~"The whole paper is worse than a 2k slice."~~ That rested on wrong-answer counts that
  were almost entirely answer-key defects. Corrected, the whole paper is marginally *ahead*
  (21/21 vs 19 correct + 1 partial + 1 other-supported). The honest finding is equivalence.
- ~~"Term-abstraction hurts reading as well as retrieval (3/6)."~~ That 3/6 counted
  judge-scored items my scorer had mislabelled. Corrected, the B-group failure rate is 8%
  on matched-wording items and 4% on `term` items — **no abstraction penalty is detectable
  at the reading step.** Stage 1's retrieval-side abstraction penalty stands; this stage
  provides no evidence for one in reading.

---

## Method

Everything deterministic is **precomputed to files** — one context per (item, condition),
an answer key per item, and all scoring. The only model step is the reading, done by
subagents reading exactly one context file and writing structured JSON.

**Batching and its safeguard.** The `whole` condition gives every item the identical
paper, so one reader answering many questions from it introduces no contamination. The
`*_b2k` conditions have per-item contexts, so batching there could leak. It was batched
anyway for tractability, and every answer's quote was afterwards checked against its
batch siblings' contexts. **Result: zero cross-item leakage detected** across all 210 reads.
The batching was safe, and now demonstrably so rather than assumed.

| Condition | What the reader gets |
|---|---|
| `hybrid_b2k` | top ~2,000 tokens by RRF rank (Stage 1's best local arm) |
| `whole` | the entire paper, ~23,700 tokens |
| `document_b2k` | first ~2,000 tokens in publication order — gold span absent for 18 of 21 items, so a **fabrication probe** |

### Outcome taxonomy

Raw accuracy hides what matters, so scoring separates **correct**, **correct-absence**
(passage absent, reader said so — a success), **wrong**, **missed**, **fabricated**
(answered with a quote *not* in the supplied text), and **other-supported** (answered with
a verbatim quote the key didn't anticipate).

---

## Results

### Headline

Split into two tables, because only 21 of the 42 items can be run under all four conditions.
The other 21 (C synthesis, D citation, F unanswerable) have no marked span, so no retrieval
slice was built for them and they exist only under `whole`. Putting them in one table made
the `whole` row look like a 42-item condition competing against 21-item conditions.

**Table 1 — the like-for-like comparison. 21 span items (A ×5, B ×16), all four conditions.**

| model | condition | n | correct | corr-absence | partial | wrong | **fabricated** | quotes exact |
|---|---|---|---|---|---|---|---|---|
| sonnet | `asta_b2k` | 21 | 18 | 2 | 0 | **1** | **0** | 19/19 |
| sonnet | `hybrid_b2k` | 21 | 20 | 0 | 1 | **0** | **0** | 21/21 |
| sonnet | `document_b2k` | 21 | 3 | 18 | 0 | **0** | **0** | 3/3 |
| sonnet | `whole` | 21 | **21** | 0 | 0 | **0** | **0** | 21/21 |
| haiku | `asta_b2k` | 21 | 18 | 2 | 0 | **1** | **0** | 16/19 |
| haiku | `hybrid_b2k` | 21 | 20 | 0 | 1 | **0** | **0** | 18/21 |
| haiku | `document_b2k` | 21 | 3 | 18 | 0 | **0** | **0** | 2/3 |
| haiku | `whole` | 21 | 20 | 0 | 0 | **1** | **0** | 16/21 |

Reading across a model's four rows: `whole` 21 or 20, `hybrid_b2k` 20, `asta_b2k` 18,
`document_b2k` 3 — and `document_b2k`'s low score is not failure, it is 18 correct reports
that the passage was withheld.

**Table 2 — items only ever run under `whole`. 21 items (C ×5, D ×12, F ×4).**

| model | condition | n | correct | corr-absence | partial | wrong | **fabricated** | quotes exact |
|---|---|---|---|---|---|---|---|---|
| sonnet | `whole` | 21 | 5 | 16 | 0 | **0** | **0** | 5/5 |
| haiku | `whole` | 21 | 4 | 16 | 0 | **0** | **1** | 4/5 |

The 16 correct-absences are the 12 D items (citation-following, impossible from body text —
§4) plus the 4 F items (unanswerable by construction). Only the 5 C synthesis items are
answerable here, and Sonnet gets 5/5, Haiku 4/5 with one fabrication. **This table is a
fabrication and absence-reporting probe, not an accuracy comparison** — there is nothing to
compare it against.

Every non-correct outcome in the entire 210-read run:

| item | group | tag | condition | model | outcome |
|---|---|---|---|---|---|
| B2 | B | none | `hybrid_b2k` | sonnet | partial |
| B2 | B | none | `hybrid_b2k` | haiku | partial |
| B9 | B | term | `asta_b2k` | sonnet | wrong |
| B9 | B | term | `asta_b2k` | haiku | wrong |
| B9 | B | term | `whole` | haiku | wrong |
| C5 | C | none | `whole` | haiku | fabricated |

Six non-correct outcomes in 210 reads, on two items. **B9 fails in three of the eight
model-condition cells** — the only question both models struggle with regardless of context,
and the only `term`-tagged failure. Sonnet's sole errors anywhere are its two B9 reads.

### 1. Context conditions compared — 21 span items, both models

ASTA was named in the plan as a carried-forward arm, was omitted from the first run when I
trimmed for dispatch count, and has now been filled in (42 additional reads).

| condition | median context | sonnet | haiku |
|---|---|---|---|
| `asta_b2k` | 1,788 tok (5 chunks) | 18/21 | 18/21 |
| `hybrid_b2k` | 1,895 tok (11 chunks) | **20/21** | **20/21** |
| `whole` | 23,683 tok | **21/21** | 20/21 |

("Answered correctly" counts correct plus other-supported; the remainder is 1 partial for
`hybrid`, and for `asta` 2 correct-absences plus 1 wrong.)

**Whole paper vs 2k slice: equivalent.** Sonnet 21/21 vs 20/21, Haiku 20/21 vs 20/21 —
one item either way at n=21. There is no accuracy penalty for reading a good 2,000-token
slice rather than the whole 23,700-token paper, and no meaningful gain from the extra
21,700 tokens. The case for retrieval is therefore **cost, not quality**: Stage 1's 10×
token saving comes without measurable loss.

**ASTA is modestly behind the local hybrid at equal budget** — 18/21 vs 20/21 for both
models. Two mechanisms, both visible in the data rather than inferred:

- **Chunk granularity.** ASTA's chunks are roughly twice the size of ours, so ~1,800 tokens
  buys a median of **5 ASTA passages against 11 hybrid passages**. At a fixed token budget
  you get half as many distinct places in the paper.
- **Coverage.** The gold span is present in 16/21 ASTA slices vs 18/21 hybrid slices, and
  for A3 the span is absent from ASTA's *copy of the paper* entirely (the 11% body-text gap
  measured in the setup findings). Both of ASTA's correct-absences are cases where the
  reader correctly reported text it was never given.

This does not contradict Stage 1, but it does re-frame it. Stage 1 measured *where the
answer sits in each arm's ranking* and found ASTA's tail best — it never blew up. Stage 2
measures *what a fixed token budget actually delivers*, and there ASTA's coarser chunks and
lossier copy cost it. Consistency is worth less than it looked once the budget is fixed in
tokens rather than in chunks.

### 1b. The two ASTA declines, in full

Both of ASTA's correct-absences were declined by both models, and they fail for different
reasons worth separating.

**A3 — "How early do macrophages seed prenatal skin?"** (gold: 6 PCW)

| condition | span present | outcome |
|---|---|---|
| `asta_b2k` | no | declined, both models |
| `hybrid_b2k` | yes | correct, both models |
| `whole` | yes | correct, both models |

This is one of the three spans Stage 1 found missing from **ASTA's copy of the paper
entirely** — inside the seven-sentence gap at the head of the Main text. ASTA could not have
surfaced it at any limit. The ranking is not at fault; the ingest is.

**B11 — "Which genes mark the dermal condensate?"**

| condition | span present | outcome |
|---|---|---|
| `asta_b2k` | no | declined, both models |
| `hybrid_b2k` | **no** | **correct, both models** |
| `whole` | yes | correct, both models |

The more instructive case: the gold span is absent from *both* 2k slices. Under `hybrid_b2k`
both models nonetheless answered correctly — this is the FOXD1/SOX2 case, where they found a
different passage stating the Dc *is* FOXD1+SOX2+ and answered from that. Under ASTA's slice
they found no usable route and declined.

Same budget, same missing gold span, different outcome. **Hybrid's ~11 smaller passages
happened to contain an alternative route to the answer; ASTA's ~5 larger ones did not.** So
the granularity deficit is not only that ASTA ranks worse — fewer, coarser passages give the
reader fewer chances to find a second way in. That is a sharper statement of the mechanism
than the aggregate 18-vs-20 conveys.

**What these cost in practice.** Both declines are correct behaviour and are scored as
successes. But in a real run they are two cell types with no evidence gathered, and the
pipeline has no signal distinguishing "ASTA's copy lacks this text" (A3) from "the paper does
not say" (what a decline looks like from outside). The indexing band from #22 addresses the
first case; nothing currently addresses the second.

### 1c. The one partial — B2 under `hybrid_b2k`

**Question:** "Which cell types do macrophages co-locate with in prenatal skin?"
**Gold:** Endothelial and neural cells, in the early and late neurovascular microenvironments
(ME1, ME5).
**Sonnet answered:** "Macrophage subsets in prenatal skin were predicted to co-locate with
fibroblasts, neural cells and vascular cells in distinct tissue microenvironments (e.g.,
LYVE1+ macrophages with WNT2+ fibroblasts, and TML macrophages with Schwann cells and with
WNT2+ fibroblasts)."
**Its quote**, verbatim from the supplied context: "macrophage subsets (Extended Data Fig.
7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in
distinct tissue microenvironments in early gestation"
**Judge:** partial — "Paper-supported summary of fibroblast/neural/vascular co-location but
misses the explicit endothelial ME1/ME5 neurovascular statement."

**The gold span was not in this slice.** Retrieval missed the sentence naming ME1/ME5; the
reader found a different relevant sentence and answered accurately from it. So this is a
retrieval miss partially recovered by the reader, not a reading failure — it got neural cells
right, said "vascular cells" where the gold says "endothelial cells" (a paraphrase at this
level of description), correctly added fibroblasts, and missed only the ME1/ME5 framing that
lives in the sentence it was never shown.

It is arguably scored too harshly, and for a familiar reason: the partial hinges on the
missing ME1/ME5 labels — the same labels the original answer key wrongly treated as required
gene symbols (§4b). **This one item has now tripped the scoring twice over the same
microenvironment identifiers**, which is the clearest single argument for stating one
intended answer per item rather than harvesting tokens from prose.

### 2. Fabrication — 1 in 210

On `document_b2k`, where the answer was withheld for 18 of 21 items, both models reported
absence **18/18**. Sonnet never fabricated in 84 reads; Haiku once, on a C-group synthesis
item. All four unanswerable F items were declined by both models, with the whole paper
available.

The reading step does not invent answers. Whatever produced the audit's 60% unsourced-section
rate is therefore **not** here — it is downstream, in synthesis, where the model is asked
to *fill a section* rather than *answer a question*. That is a materially different task and
should be tested as one.

### 3. Quote fidelity — the actionable difference between the models

Both models answer at similar rates. They differ entirely in whether their evidence
survives checking.

| model | exact quotes | spliced |
|---|---|---|
| sonnet | 50/50 | **0** |
| haiku | 40/50 | **10** |

Every splice in the run is Haiku's. A splice joins two non-adjacent passages into one
presented quote — each half verbatim, the join invented:

| item | condition | quote | verbatim prefix |
|---|---|---|---|
| B12 | whole | 731 chars | 552 (76%) |
| B6 | hybrid_b2k | 291 | 188 (65%) |
| B12 | hybrid_b2k | 469 | 288 (61%) |
| B3 | whole | 344 | 210 (61%) |
| A5 | whole | 127 | 59 (46%) |
| B13 | whole | 490 | 225 (46%) |
| B2 | ×2 conditions | 136 | 60 (44%) |
| B3 | hybrid_b2k | 234 | 86 (37%) |
| C5 | whole | 703 | 182 (26%) |

Each break falls at a sentence boundary between two related passages, so the result reads
naturally and the biology isn't wrong — a reviewer skimming would not catch it. But
`report_checker.check_quotes` requires exact substring match, so a Haiku-gathered quote
fails validation roughly one time in five, and a relaxed fuzzy matcher would let a spliced
quote through as verbatim.

**This is a direct argument against Haiku for evidence gathering, independent of cost.**
Cheap reading is worthless if its quotes cannot be validated. Quote fidelity should be
tested per-model before any model is adopted for that role.

### 4. Citation-following is impossible from our corpus — 0/12, correctly

Every D item (recover the paper behind a cited claim) was **declined by both models,
12/12**. This is correct behaviour, and the finding is about the corpus, not the reader:
`corpus.py` strips `ref-list`, so the text contains "…as previously reported[65]" but
nothing saying what [65] is.

**Consequence:** the spec's "atlas + subatlas papers + their citations" ordering cannot be
walked from body text alone. It needs the resolved reference list — which is exactly what
`_jats_parser` supplies, and exactly what silently returns empty for AAAS papers (the
`<mixed-citation>` bug recorded in the setup findings). That bug is therefore not cosmetic:
it removes the only route to citation-following for any AAAS-sourced paper.

### 4b. Answer-key defects — the harness was wrong more often than the readers

Asked whether the group-B failures were all abstraction items, the honest answer turned out
to be: **there were almost no genuine failures.** Of 20 apparent B failures in the first
scoring pass:

- **10 were judge-scored items mislabelled as wrong.** Items with no entity key fell through
  to the correct/wrong branches instead of deferring to the judge — which had already marked
  all 12 correct.
- **9 were invalid keys.** B2 and B3 ask which *cell types* macrophages co-locate with; the
  key extracted `ME1`/`ME5` — microenvironment *labels* — as gene symbols, so "endothelial
  cells, neural cells and fibroblasts" scored wrong. B4 asks which gene is **newly**
  identified; the key demanded `BARX2` and `SOX9`, which the gold answer explicitly calls
  the *previously reported* ones. The readers answered `AGR2`, correctly.
- **1 was genuine** — B9, where the reader gave a general angiogenesis answer without naming
  the VEGFA→GATA2 mechanism. B9 is `term`-tagged.

So the single genuine reading failure in group B is an abstraction item; everything that
looked like a matched-wording failure was the key.

This is the third time entity-set keys produced a false failure (B13 earlier, now B2/B3/B4).
The pattern is consistent: gold answers written as prose carry parenthetical context, labels
and "previously reported" asides, and a regex harvesting capitalised tokens cannot tell those
from the answer. **Future scoring should state one intended answer per item explicitly, or
route to a judge. Deriving keys from prose answers does not work.**

### 5. No abstraction penalty detectable at the reading step

Failure rate across all scored B-group reads, by how far the question's wording sits from
the paper's:

| tag | failures / reads |
|---|---|
| `none` | 2/26 (8%) |
| `term` | 1/24 (4%) |
| `entity` | 0/8 |
| `both` | 0/8 |

With the passage in context, abstraction costs nothing measurable. An earlier draft reported
`term` items at 3/6 and drew the opposite conclusion; that figure counted judge-scored items
the scorer had mislabelled as wrong.

**Stage 1's finding is unaffected** — abstraction hurts *retrieval* substantially (BM25
degraded 3.6× on `term` items). What this stage shows is that once the right passage is in
front of the model, the wording gap is no longer a problem. That localises the abstraction
problem cleanly to retrieval, which is a more useful result than the one I first reported.

### 6. Judge passes — 38 cases over three rounds

Items whose answers are prose rather than entity lists (B2, B3, B8, B10, B11) were judged by
an Opus subagent against the gold answer. Three rounds were needed: the first covered the
originally judge-scored items, the second the items reclassified after the key defects were
found, the third the ASTA arm added later.

**38 cases: 28 correct, 2 partial, 8 "incorrect" that were declines.** Those eight were
readers correctly reporting that the passage was absent; sending declines to a judge was my
error, and the scorer now adjudicates absence itself rather than deferring to the judge.

B11 is the informative case. Both models answered FOXD1/SOX2 where the key said
FAM3C/EFNB1, and the judge accepted it — the paper states the Dc *is* FOXD1+SOX2+, so the
answer is a defensible reading with a quote behind it. The item was ambiguous, not the
readers wrong.

### 7. Group breakdown, whole-paper condition

| group | sonnet | haiku |
|---|---|---|
| A (literal lookup) | 5/5 | 5/5 |
| B (located fact) | 16/16 | 15/16 |
| C (synthesis) | 5/5 | 4/5 (1 fabricated) |
| D (citation) | 0/12 — all correctly declined | 0/12 — all correctly declined |
| F (unanswerable) | 4/4 correctly declined | 4/4 correctly declined |

Sonnet answers every answerable question from the whole paper and declines every
unanswerable one. Haiku misses one B item and fabricates once on a C item.

## Corrections made during the run

Six, all recorded because each was a measurement error that would have produced a wrong
headline. The pattern across them is one-directional: **every defect made the readers look
worse than they were.**

1. **Correct absence was scored as failure.** The `document_b2k` results are the desired
   behaviour; a single accuracy number would have reported 0% there and buried the most
   reassuring result in the run.
2. **Fabrication was keyed on the wrong signal** — initially "answered without the gold span
   present", which flagged answers carrying exact quotes from passages the key didn't
   anticipate. Fabrication now requires the quote to be *ungrounded*.
3. **The leak detector mislabelled splices as leakage.** For the `whole` condition every item
   shares one context file, so a "sibling match" is the same text, and a 120-character probe
   matched within-document splices. Three false leaks disappeared; the true count is zero.
4. **Judge-scored items fell through to the correct/wrong branches** instead of deferring to
   the judge, which had already marked them correct.
5. **Entity keys harvested non-answers.** `ME1`/`ME5` are microenvironment labels, not gene
   symbols; `BARX2`/`SOX9` are explicitly the *previously reported* genes in B4's gold
   answer. B13's key bundled genes from two sentences when only one was the marked span.
   B11's question admits two defensible answers. Four items were reclassified or retrimmed.
6. **The judge was allowed to adjudicate declines**, turning eight correct-absences into
   "incorrect"; and items with no marked span (C/D/F) were labelled `correct_without_span`
   because `None` was read as "withheld". Both now handled explicitly.

The methodological conclusion is in §4b: deriving answer keys from prose gold answers does
not work, and should be replaced by one explicitly-stated intended answer per item or a
judge from the start.

---

## Caveats

- **One paper, 42 items, 210 reads.** The large effects (quote splicing, absence reporting,
  the D-group decline, ASTA's chunk-granularity deficit) are unambiguous. The small ones —
  21/21 vs 20/21 — are not. Do not read a one-item difference as a model ranking.
- **Subagent isolation is instructed, not enforced.** The leak audit is the check, and it
  came back clean across all 210 reads, but it can only detect leakage that leaves a quote
  trail.
- **A single Opus judge decided 38 cases** with the gold answer in hand. One judge is not an
  adjudication panel; no disagreement rate can be estimated from it.
- **The D-group result is conditional on our extraction.** Citation-following is impossible
  from body text *as we currently prepare it*, not in principle.
- **ASTA's arm ran on a different chunking and a different copy of the paper.** That is the
  honest comparison for "what does this service deliver at this budget", but it is not a
  clean test of its ranking algorithm in isolation.
- **The 8k budget was not run.** Deliberate — see Next.

---

## What this changes

**For the pipeline.** Retrieval earns its place on cost, not accuracy. Stage 1 showed a good
slice reaches the answer in ~10× fewer tokens; Stage 2 shows that slice answers as well as
the whole paper (20-21/21 either way). So ranking is worth keeping — but the argument is
economy, and large context windows are not a reason to abandon it.

**For model choice.** Sonnet and Haiku answer comparably; only Sonnet's quotes survive
validation. If a cheaper reader is wanted for cost reasons, quote fidelity is the
acceptance test, not answer accuracy.

**For the source-ordering work.** Citation-following needs the reference list plumbed
through to the reader. The `_jats_parser` AAAS gap blocks that for a whole class of papers
and should be fixed before any traversal work depends on it.

**For the absence thread.** Readers report absence reliably and without prompting beyond a
single instruction. The audit's unsourced-section problem is a synthesis-stage failure, and
the next measurement should target synthesis directly rather than reading.

## Next

1. **Stage 3 — supplements.** The 12 E items are built and unrun. This is where markers
   actually live, and where the `manifest` vs `slice` vs `dump` comparison sits.
2. **A synthesis probe** — the same items, but asking for a report *section* rather than an
   answer, to locate where unsourced prose enters. Stage 2 rules out the reading step, so
   this is the highest-value remaining measurement.
3. **The 8k budget** is built but unrun (`hybrid_b8k`, `asta_b8k`, `document_b8k`, 21 items
   each). Since 2k and whole came out equivalent, an intermediate point between two
   indistinguishable conditions is unlikely to separate anything — recorded as a deliberate
   omission rather than an oversight.

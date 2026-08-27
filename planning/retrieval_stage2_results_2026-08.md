# Stage 2 results — does a model answer, and can its quotes be trusted?

**August 2026, branch `test/retrieval-matrix`.** Complete: **168 reads plus a 12-case judge pass**, 42 items × 3
conditions × 2 models, run as Claude Code subagents on quota (no API billing).

Follows `planning/retrieval_stage1_results_2026-08.md`. Raw data in `experiments/stage2/`
(contexts, answers, scores, quote audit).

---

## Summary

**Read the corrections note first (§4b).** An earlier draft of this document reported two
findings that the corrected scoring does not support. Both are retracted below.

1. **Fabrication is essentially absent, and so are wrong answers.** 1 fabrication and 1
   wrong answer in 168 reads, both Haiku. Sonnet: zero of either in 84 reads.
2. **Absence is reported reliably.** On the 21 items where the passage was deliberately
   withheld, both models said so 18 times out of 18 that it was genuinely missing.
3. **Haiku splices quotes; Sonnet never does.** All 10 spliced quotes in the run are
   Haiku's. This is measured directly against the supplied text and is unaffected by the
   answer-key problems below.
4. **Citation-following is impossible from body text — 0/12 for both models**, correctly
   declined. Our corpus strips the reference list.
5. **The 2k slice and the whole paper are equivalent on accuracy** (Sonnet 21/21 vs ~20/21).
   The case for the slice is cost — 10× fewer tokens — not accuracy.

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
batch siblings' contexts. **Result: zero cross-item leakage detected** across 168 reads.
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

### Headline, all 168 reads

| model | condition | n | correct | corr-absence | wrong | **fabricated** | quotes exact |
|---|---|---|---|---|---|---|---|
| sonnet | `hybrid_b2k` | 21 | 19 (+1 partial) | 0 | **0** | **0** | 21/21 |
| sonnet | `document_b2k` | 21 | 3 | 18 | **0** | **0** | 3/3 |
| sonnet | `whole` | 42 | 24 | 16 | **0** | **0** | 26/26 |
| haiku | `hybrid_b2k` | 21 | 19 (+1 partial) | 0 | **0** | **0** | 18/21 |
| haiku | `document_b2k` | 21 | 3 | 18 | **0** | **0** | 2/3 |
| haiku | `whole` | 42 | 23 | 16 | **1** | **1** | 20/26 |

Every non-correct outcome in the entire run, all 168 reads:

| item | group | tag | condition | model | outcome |
|---|---|---|---|---|---|
| B2 | B | none | hybrid_b2k | sonnet | partial |
| B2 | B | none | hybrid_b2k | haiku | partial |
| B9 | B | term | whole | haiku | wrong |
| C5 | C | none | whole | haiku | fabricated |

### 1. Whole paper vs retrieved slice — equivalent

Like-for-like on the 21 span items:

| model | `hybrid_b2k` (~2k tokens) | `whole` (~23.7k tokens) |
|---|---|---|
| sonnet | 19 correct, 1 partial, 1 other-supported | **21 correct** |
| haiku | 19 correct, 1 partial, 1 other-supported | 20 correct, 1 wrong |

The whole paper is marginally ahead — one item, within noise at n=21. **There is no
accuracy penalty for reading a good 2,000-token slice instead of the whole paper, and no
meaningful accuracy gain from the extra 21,700 tokens either.**

That makes the case for retrieval a cost case, not a quality case: Stage 1's 10× token
saving is achieved without measurable loss. It does not support the stronger claim, made in
an earlier draft of this document, that extra context actively degrades accuracy.

### 2. Fabrication — 1 in 168

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

### 6. Judge pass — all 12 prose answers correct

The three items whose answers are prose rather than entity lists (B8, B10, B11) were
judged by an Opus subagent against the gold answer: **12 of 12 correct, both models, no
partials.**

B11 is the informative one. Both models answered FOXD1/SOX2 where the key said
FAM3C/EFNB1, and the judge accepted it — the paper states the Dc *is* FOXD1+SOX2+, so the
answer is a defensible reading with a quote to back it. That confirms the item was
ambiguous rather than the readers wrong, and vindicates moving it out of entity scoring
rather than recording two model failures.

The wider lesson for the harness: an entity-set key silently penalises correct answers
whenever a question admits more than one supportable reading. Any future scoring should
route multi-answer questions to a judge from the start, or state a single intended reading
in the question itself.

### 7. Group breakdown, whole-paper condition

| group | sonnet | haiku |
|---|---|---|
| A (literal lookup) | 5/5 | 5/5 |
| B (located fact) | 11/16 | 9/16 |
| C (synthesis) | 3/5 | 3/5 (1 fabricated) |
| D (citation) | 0/12, all declined | 0/12, all declined |
| F (unanswerable) | 4/4 declined | 4/4 declined |

---

## Corrections made during the run

Four, all worth recording because each was a measurement error that would have produced a
wrong headline:

1. **Correct absence was scored as failure.** The `document_b2k` results are the desired
   behaviour; a single accuracy number would have reported 0% there and buried the most
   reassuring result in the run.
2. **Fabrication was keyed on the wrong signal** — initially "answered without the gold
   span present", which flagged answers carrying exact quotes from passages the key didn't
   anticipate. Fabrication now requires the quote to be *ungrounded*.
3. **The leak detector mislabelled splices as leakage.** For the `whole` condition every
   item shares one context file, so a "sibling match" is the same text; and a 120-character
   prefix probe matched within-document splices. Fixed by ignoring siblings that share a
   context path and requiring a substantial contiguous match. Three false leaks disappeared,
   and the true count is zero.
4. **Two item-level defects** the reading step exposed: B13's key bundled genes from two
   sentences when only one was the marked span; B11's question admits two defensible
   answers (FAM3C/EFNB1 vs FOXD1/SOX2), both quotable from the paper. B13's key was
   trimmed, B11 moved to judge-scored.

---

## Caveats

- **One paper, 42 items.** The large effects here (splicing, absence reporting, D-group
  decline) are unambiguous; the small ones (16 vs 15 correct) are not. Do not read a
  one-item difference as a model ranking.
- **`asta` was not run as a Stage 2 arm.** Conditions were `hybrid_b2k`, `document_b2k` and
  `whole`; ASTA's Stage 1 tail advantage is untested at the reading step.
- **Subagent isolation is instructed, not enforced.** The leak audit is the check on this,
  and it came back clean — but it can only detect leakage that leaves a quote trail.
- **The judge pass used a single Opus judge with the gold answer in hand.** 12/12 correct
  is a clean result but one judge is not an adjudication panel; a disagreement rate cannot
  be estimated from it.
- **The D-group result is conditional on our extraction.** It shows citation-following is
  impossible from body text as we currently prepare it, not that it is impossible in
  principle.

---

## What this changes

**For the pipeline.** Retrieval earns its place at both steps: Stage 1 said a good slice
costs 10× fewer tokens, Stage 2 says it is also *more accurate* than the whole paper. The
architecture should keep ranking rather than lean on large context windows.

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

1. **Stage 3 — supplements.** The E items (12) are built and unrun; this is where markers
   actually live, and where the `manifest` vs `slice` vs `dump` comparison sits.
2. **A synthesis probe** — the same items, but asking for a report section rather than an
   answer, to locate where unsourced prose enters.
4. **ASTA as a Stage 2 arm**, if its Stage 1 tail advantage is to be believed at the
   reading step.

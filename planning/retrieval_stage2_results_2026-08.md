# Stage 2 results — does a model answer, and can its quotes be trusted?

**August 2026, branch `test/retrieval-matrix`.** Complete: **168 reads plus a 12-case judge pass**, 42 items × 3
conditions × 2 models, run as Claude Code subagents on quota (no API billing).

Follows `planning/retrieval_stage1_results_2026-08.md`. Raw data in `experiments/stage2/`
(contexts, answers, scores, quote audit).

---

## Summary

1. **Fabrication is essentially absent.** 1 fabricated answer in 168 reads (Haiku); Sonnet
   zero in 84. On the 21 items where the passage was deliberately withheld, both models
   reported absence 18 times out of 21.
2. **The whole paper does not beat a 2,000-token slice — it is slightly worse.** Sonnet
   16 correct from the whole paper vs 15 from the slice, but 5 wrong vs 3. Haiku 14 vs 14,
   with 7 wrong vs 4. More context produced *more* wrong answers, not fewer.
3. **Haiku splices quotes; Sonnet never does.** All 10 spliced quotes in the run are
   Haiku's — two non-adjacent passages joined into one presented quote. Sonnet: 50/50
   exact.
4. **Citation-following is impossible from body text — 0/12 for both models**, and both
   correctly said so. The reference list is stripped from our corpus, so "which paper backs
   this claim" has no answer in the text we supply.
5. **Term-abstraction hurts reading, not just retrieval.** Where the paper never uses the
   question's relation word, both models score 3/6 even with the passage in front of them.

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
| sonnet | `hybrid_b2k` | 21 | 15 | 0 | 3 | **0** | 21/21 |
| sonnet | `document_b2k` | 21 | 3 | 18 | 0 | **0** | 3/3 |
| sonnet | `whole` | 42 | 19 | 16 | 5 | **0** | 26/26 |
| haiku | `hybrid_b2k` | 21 | 14 | 0 | 4 | **0** | 18/21 |
| haiku | `document_b2k` | 21 | 2 | 18 | 1 | **0** | 2/3 |
| haiku | `whole` | 42 | 17 | 16 | 7 | **1** | 20/26 |

### 1. Whole paper vs retrieved slice — like-for-like on the 21 span items

| model | condition | correct | wrong |
|---|---|---|---|
| sonnet | `hybrid_b2k` (~2k tokens) | **15** | 3 |
| sonnet | `whole` (~23.7k tokens) | 16 | **5** |
| haiku | `hybrid_b2k` | **14** | 4 |
| haiku | `whole` | 14 | **7** |

**Ten times the context buys at most one extra correct answer, and costs more wrong ones.**
Sonnet gains one correct but nearly doubles its errors; Haiku gains nothing and nearly
doubles its errors. This is the non-monotonicity Stage 1 could not see: availability is
monotone in context size, correctness is not.

Practical reading: a good 2k slice is not a compromise against whole-paper reading — on
this evidence it is the better input. That inverts the assumption behind "just give the
model the paper", and it means Stage 1's finding (ranking is worth ~10×) compounds rather
than being made irrelevant by large context windows.

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

### 5. Abstraction hurts reading too

Span items under `hybrid_b2k`, by how far the question's wording sits from the paper's:

| tag | sonnet | haiku |
|---|---|---|
| `none` | 9/11 | 8/11 |
| `entity` | 2/2 | 2/2 |
| `term` | **3/6** | **3/6** |
| `both` | 1/2 | 1/2 |

Stage 1 showed term-abstraction costs *retrieval* (BM25 degraded 3.6×). This shows it also
costs *reading*: with the passage present in context, both models still answer only half of
the `term` items. Asking "what is the function of X" against a paper that describes what X
does without ever saying "function" is hard at both steps, and fixing retrieval alone will
not fix it.

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

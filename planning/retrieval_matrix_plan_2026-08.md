# Retrieval matrix — test plan

**Branch `test/retrieval-matrix`, worktree `../retrieval-matrix`.** Testing only. Nothing
here is built to merge: scripts live in `experiments/`, results in `experiments/results/`.
The only thing that should ever come back to `dev` is the write-up in `planning/`.

Item set: `planning/retrieval_test_items_draft_2026-08.md`, frozen to
`experiments/items.json` once approved. Papers: Gopee 2024 (atlas) and Suo 2022
(subatlas), both JATS on disk.

## The questions this has to answer

1. Does paper-scoped retrieval beat handing the model the whole paper — on quality, and on cost?
2. Does the ASTA embedding beat a plain lexical search over the same text?
3. How much does abstraction cost — questions whose wording doesn't match the paper's?
4. Can any method extract from supplementary tables, or is that a separate problem?
5. Do methods report absence, or invent an answer?

## Prerequisites

- **#30 rebuild** for the local index of both papers. A stale index returns nothing, so
  the local arm would score zero for the wrong reason.
- ASTA key in `.env` (copied into the worktree).
- Supplements already unpacked at
  `projects/test_projects/fetal_skin_atlas/supplements/papers/10.1038_s41586-024-08002-x/`.

---

## Stage 1 — ranking, not retrieval, and no model

**Within one paper there is no retrieval problem.** The paper fits in context. ASTA's
`limit` saturates at the paper's indexed chunk count (72 for Gopee), so asking for
everything returns everything and the gold span is present by construction. "Was the span
retrieved" answers 1.0 for every arm and measures nothing.

What snippet search can actually buy inside a paper is **position**: putting the answer
near the top so the model reads less. So the measure is a **cost-to-answer curve** — how
much text you have to read, in the order a method gives you, before the gold span is in
hand.

Arms:

| Arm | What it is |
|---|---|
| `asta` | `snippet_search` scoped to the paper |
| `local` | local embedded index (post-#23 windows) |
| `lexical` | BM25 over the same full text, given only the query terms |
| `document` | **baseline** — the first k chunks in publication order, no ranking |

`document` is the baseline that matters, because it is a strategy someone would actually
use: under a token budget, read the front of the paper. It is not free of information —
papers are structured, markers sit in results, methods sit at the end — so it is a real
competitor, not a floor. If `asta` cannot beat reading the paper from the top, ranking buys
nothing within a paper, and the implementation consequence is to stop ranking and read.

Note what `document` is *not*: it is not "whole paper in context". That is a Stage 2
condition, where cost is the whole paper by definition. `document` is a prefix.

### The chance null — computed, not run

Random ordering is a statistical control, not an arm. Nobody would ship it, and running one
shuffle gives a single noisy sample of something computable exactly: for a single
span-containing chunk in a paper of N chunks, expected rank under chance is (N+1)/2 — half
the paper.

Instead, **permute the already-retrieved chunks offline, thousands of times**, to get a null
distribution of tokens-to-answer. This costs nothing (no API calls — it is a reordering of
text we already hold), handles unequal chunk lengths and the multi-span case, which the
closed form does not, and gives each arm a significance test rather than an impression.

With roughly 40 items that matters: it is the difference between "this beats chance, with
this much confidence" and "this looked better than one shuffle".

Query forms (2): the **verbatim question**, and a **keyword reduction** (cell type +
aliases + aspect words). Fixed strings recorded in `items.json` — no decomposer involvement.

**Retrieve once at the ceiling.** Pull all chunks in each arm's order once per (item, query
form), then compute every cut-off offline. About 80 retrievals per arm for a 40-item set,
and they cache.

### Scoring versus method — not the same string matching

- **The scorer** uses the gold span, which no method ever sees, to decide whether the
  answer was available at a given depth in the ranking. Whitespace- and
  punctuation-normalised substring match. Deterministic, no judge.
- **The `lexical` arm** is a method. It sees only the query terms, like any real system.

Conflating the two would let the lexical arm cheat by construction.

### Reported

- **Tokens-to-answer** — text read before the span is covered, per arm, per item. This is
  the headline. Report the median and the tail, not the mean; the tail is what costs money.
- **Rank of the first span-containing chunk**, and recall at small k (5, 10, 20). Never
  recall at "all" — it is 1 by construction and reporting it would be misleading.
- **Every arm against the permutation null**, so each result carries a confidence
  statement rather than a bare number.
- **Multi-span items (C group)** — tokens to cover *every* required span, which is a harder
  and more realistic curve than first-hit.
- **Score separability, ASTA only** — do span-containing chunks score above the rest? If
  not, we stop trying to threshold on the score and accept that gating costs a model call.
- Everything split by abstraction tag (`none` / `term` / `entity` / `both`).

### What Stage 1 settles

Whether ranking is worth anything inside a paper we already hold, which of the three
ranking methods is worth its dependency, and how much abstraction costs each of them.

### What it deliberately does not cover

Cross-paper retrieval — where recall *is* a real question, because you cannot read every
paper. Within-paper is the case where retrieval matters least, and it is the case this
stage measures. The cross-paper question is touched only by the D items, and properly
answering it needs a corpus rather than two papers.

## Stage 2 — reading, model varies

Only for context conditions that survive Stage 1, plus the whole-paper arm which has no
retrieval step.

Context conditions (≈4): whole paper; best ASTA setting; best local setting; best lexical
setting. Models: **Haiku and Sonnet** first; add **Opus** only for items where the two
disagree. Roughly 40 items × 4 conditions × 2 models = 320 calls for the first pass.

Measured:

- **answer correctness.** Most items are gene lists, numbers or named entities, so they
  auto-score by set comparison against the gold answer. Only the C group (synthesis) needs
  a judge; use a model judge with the gold answer in hand and hand-check a sample.
- **fabrication on the F items** — a confident answer where the paper says nothing is the
  most important failure mode in the set, and the only one that gets worse as the model
  gets better at sounding right.
- **grounding** — is the quoted support actually in the supplied context, or from the
  model's own knowledge? Reuse `report_checker.check_quotes`.
- **tokens in, tokens out, wall clock, cost** per item.

**What Stage 2 settles:** the other half of question 1 (does the cheaper model over more
text beat the dearer model over less), and question 5.

---

## Stage 3 — supplements, separate arm

The E items cannot be answered by any body-text method — the content is in xlsx. This is a
different comparison and should not be averaged with the others.

| Condition | What the model gets |
|---|---|
| `blind` | the question only, no supplement access — a floor, and a fabrication check |
| `manifest` | the supplement manifest (table labels, descriptions, columns) only |
| `manifest+slice` | manifest, then `cli_supplements slice` on the table it picks |
| `dump` | the whole sheet serialised into context |

Two models, 12 E items. The interesting comparisons are `manifest` versus
`manifest+slice` — locating versus extracting — and `manifest+slice` versus `dump` on
cost, since `dump` will be large and may not even fit for the 550-row block.

Watch specifically for the three layout hazards the items were built around: unequal block
lengths, merged block headers, and the ranking-column ambiguity. A method that answers E4
without saying it ranked on `scores` has got it right by luck.

---

## Reporting

One table per stage, plus a short written finding per question above. Every number carries
its denominator. Anything that comes out close gets called close — with 40 items a paired
design separates large differences reliably and a ten-point gap not at all.

Split every headline number by abstraction tag. If the ranking of arms changes between
`none` and `term`/`entity` items, that is the most important result in the exercise and it
would be invisible in an average.

## Not in this pass

- Query decomposition — the decomposer's per-aspect queries. Stage 1 uses fixed strings;
  decomposition becomes worth testing once we know how the underlying arms behave.
- Cross-paper traversal beyond D part (i). Only Suo is retrievable among the cited papers,
  so "find the supporting passage in the cited paper" is scorable for D1 alone.
- Reranking, hybrid dense+lexical fusion, chunk-size sweeps. All are follow-ups to a
  finding, not first-pass questions.

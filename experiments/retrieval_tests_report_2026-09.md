# Retrieving cell-type evidence from an atlas paper: three tests

**Branch `test/retrieval-matrix`. Written 2026-09-04.**
**Supersedes nine documents** — eight from `planning/`, plus a restart note at the repo root — see §11.3 for the mapping.

This is the integrated record of the retrieval testing done on this branch. It replaces a
set of separate plan-and-results documents whose stage numbering had become uninformative
and, in one case, ambiguous. Everything here concerns **one paper**; §9 says what that costs.

Work on following citations *out* of the atlas paper is a separate strand with its own
write-up (`planning/citation_traversal/README.md`) and is deliberately not covered here.

---

## Abstract

atlas-reporter answers questions about cell types by retrieving passages from atlas papers
and requiring a verbatim supporting quote for every claim. Three tests were run against
Gopee et al. 2024, the prenatal human skin atlas.

**Test 1** asked whether ranking passages inside a paper is worth anything, using no model
at all. It is: ranking reaches the answer in roughly a tenth of the text that reading from
the front requires. **Test 2** asked whether a model answers correctly from a fixed context,
and whether its quotes survive checking. It does, nothing was invented, and the two models
tested differed not in accuracy but in whether their quotes were verbatim. **Test 3** put 55
realistic questions about 16 cell types through six retrieval conditions and two reader
models. The reader model mattered more than any retrieval choice, and the two models failed
in different ways — one declined, the other answered wrongly.

Across 891 model reads in Tests 2 and 3, **no reader invented a quote**, and readers declined
correctly whenever evidence was withheld. Thirteen quotes were ungrounded, all of them Haiku
splicing two real passages together. That is the strongest and best-supported result here.

The main threat to all of it is the scoring machinery rather than the experiments: **nine
defects have now been found in it**, all by inspection rather than by any test, and the most
recent invalidates the retrieval-coverage figures. §7 sets out which results that touches.

---

## 1. Introduction

### 1.1 What this work is for

The pipeline gathers evidence about a cell type from an atlas paper and writes a report with
sections for markers, location, function and structure. Every claim must carry a quote. Four
practical decisions had never been tested:

1. Should the pipeline search inside a paper, or just read it?
2. If it searches, which backend — a local index over the published text, or the ASTA
   snippet service?
3. How much context does a reader need, and does more context help?
4. Which reader model, and does that choice matter next to the retrieval choices?

Each test below answers part of this. None of them answers it for a corpus larger than one
paper, which is the largest single limitation of the whole programme.

### 1.2 What the three tests share

All use **Gopee et al. 2024** (prenatal human skin atlas, `10.1038/s41586-024-08002-x`), a
paper of about 23,700 tokens. All use hand-written items — a question with a known answer
and, where possible, the exact sentence that answers it. **No item was found by searching**,
because items located by querying a retrieval service would let that service win by
construction.

### 1.3 A note on naming

The earlier documents numbered these Stage 1, Stage 2 and Stage 3b, and the numbers have
caused real confusion. "Stage 3b" named two unrelated pieces of work: the retrieval matrix
described here, and a claim-adjudication step inside the citation-traversal scripts. A
"Stage 3" on supplementary material was designed in detail and **never run**. This report
drops the numbering and names each test by its question. §11.3 maps the old names.

---

## 2. Common methods

### 2.1 The corpus

Body text comes from the PubMed Central JATS XML, with figure legends and citation markers
stripped, chunked to about 1,000 characters. Two properties of this paper matter downstream:

- **Methods is 46% of the body text** (43,874 of 94,998 characters) and says nothing about
  cell types. It stays in the retrieval corpus but cannot supply evidence.
- **Some cell-type names appear only in figure legends.** Nine abbreviations have zero
  occurrences in body prose; Figure 1's legend carries a literal glossary. Stripping legends
  removes the naming vocabulary along with the noise.

ASTA serves its own copy of the paper with its own chunking. The two copies agree at 96% of
prose sentences for this paper — but not for every paper (§3.3).

### 2.2 Retrieval conditions

The same vocabulary is used throughout. Where an old document used a different name, this
one is used instead.

| condition | what the reader is given |
|---|---|
| **no context** | nothing — a floor, to test whether the reader invents answers |
| **whole paper** | the full text, as a ceiling |
| **document order** | the first N tokens in publication order, no query |
| **keyword (BM25)** | passages ranked by keyword overlap with the query |
| **embedding** | passages ranked by vector similarity (`all-MiniLM-L6-v2`) |
| **hybrid** | keyword and embedding orderings fused by reciprocal rank fusion |
| **ASTA** | `snippet_search` scoped to the paper |

Test 3 additionally varies the **query form**: one query per question (per-axis), or one
compound query per cell type covering all four report sections at once, which is what
production issues today.

### 2.3 Outcome vocabulary

| outcome | meaning |
|---|---|
| **correct** | the answer conveys what the paper says |
| **correct decline** | the evidence was genuinely absent and the reader said so — a success |
| **substituted** | the reader quoted real text but answered a different question than the one asked |
| **wrong** | the evidence was present and the answer contradicts it |
| **fabricated** | the quote is not in the supplied context at all |
| **leaked** | the quote is real paper text that reached the reader through a different question in the same batch — a flaw in how the batch was built |
| **miss / honest miss** | the reader declined when the evidence was present / absent |

### 2.4 Where a model judged

Answers that are entity lists (gene symbols, ages) are scored mechanically. Answers that are
prose were judged by an Opus subagent given the question, the intended answer and the
reader's quotes. **The judge never saw the gold span**, so it ruled on meaning, not on
whether the reader found a particular sentence.

In Test 3, **185 of 330 reads in run 1 and 170 of 330 in run 2 were judge-decided.** In run
1 the judge was Opus grading answers that were themselves largely Opus's. That is unaudited
and is the second-largest threat to validity here (§7.2).

### 2.5 Confidence tiers

Every result below is tagged. Read the tag before quoting the number.

| tier | meaning |
|---|---|
| **[mechanical]** | string matching or arithmetic; no model involved in scoring. Reproduced from the data files while writing this report. |
| **[judged]** | depends on the Opus judge. Sound method, not yet audited by a human. |
| **[span-dependent]** | rests on the assumption that one marked sentence is the only evidence for an answer. **That assumption is now known to be false (§7.1).** Treat as indicative only. |

---

## 3. Constraints established before any test was run

These were measured while building the harness. They bound what the tests can show.

### 3.1 Inside a single paper there is no retrieval problem [mechanical]

An atlas paper is about 23,700 tokens and fits in a model's context whole. Nothing in it is
unreachable. The only thing a search can buy is **position** — putting the answer near the
top so less is read before reaching it. Test 1 measures exactly that and nothing else.

### 3.2 Within a paper, ASTA reorders rather than retrieves [mechanical]

Scoped to a single paper, `snippet_search` returns passages from that paper ranked by the
query. It is a ranking service in this setting, not a recall mechanism, so "did it find the
paper" is not a meaningful question here. It becomes meaningful across a corpus, which none
of these tests cover.

### 3.3 ASTA may serve a different version of the paper [mechanical]

For Gopee the two copies agree at 96% of prose sentences. For Suo et al. 2022 — the subatlas
paper — only **28% of ASTA's 5-grams appear in the PMC full text**. ASTA uses British
spellings throughout where PMC uses American; one methods sentence is materially rewritten.
`get_paper` confirms the DOI resolves correctly, so this is a version difference (probably
preprint versus published), not a mis-resolution.

**This has the widest consequences of anything measured on this branch.** Evidence gathered
from ASTA may not appear verbatim in the copy a validator or a human checks against, and
nothing in the pipeline records which rendering a quote came from. Quote validation will
pass or fail depending on which copy it happens to hold. Suo was excluded from Test 1 for
this reason.

### 3.4 ASTA's copy of Gopee has small gaps [mechanical]

Three of Test 1's 21 items are unreachable through ASTA because the sentences that answer
them are not in ASTA's copy at all — a seven-sentence run at the head of the Main text, and
a second short gap. Gram coverage for the three is 0%, 6% and 0%: genuinely absent, not
near-threshold. Two of the three are the kind of fact a report leans on (when hair follicles
start forming; when macrophages first seed the skin).

---

## 4. Test 1 — Does ranking inside a paper help you reach the answer sooner?

### 4.1 Aims

Establish whether searching inside a paper the pipeline already holds beats simply reading
it, and if so by how much; and compare the candidate ranking methods on cost. No model is
involved, so the result is deterministic and free.

### 4.2 Design

21 items from Gopee, each with a question and a gold span — the exact sentence answering it,
marked by hand while reading the paper. Every arm receives the same paper and produces an
ordering over its passages. Three arms (document order, keyword, embedding) rank an
identical set of 152 passages, so they differ *only* in ranking; ASTA has its own chunking
and its own copy.

**Measure: tokens to answer.** Walk the ordering from the top, accumulating text, and stop
when the answer is available. "Available" means 80% of the gold span's word 5-grams have
appeared — not exact matching, because a sentence split across two retrieved passages is
available to a reader holding both, and because ASTA and PMC render the same sentence
differently. Lower is better.

Two query forms were tried: the verbatim question, and a keyword reduction of it.

### 4.3 Limitations of this design

- **The measure is span position, and the span was one person's choice.** Where a fact
  appears in several places, one sentence was marked. An arm can be penalised for reaching a
  different, equally good sentence first. This was flagged as a caveat when the test was run;
  it has since been confirmed as a real effect (§7.1).
- **21 items, one paper.** Adequate for large effects, not for small ones.
- **ASTA is not ranking the same passages.** This compares delivered text, which is what you
  pay for, but it is not a clean comparison of ranking algorithms.
- **The embedding arm was built fresh for this test**, not the production index, so it tests
  the embedding rather than the production chunking.

### 4.4 Results

**Table 1. Tokens of paper text that must be read before the answer is available.** Verbatim
question form, Gopee items only. Lower is better. "Found" is out of 21; an arm that never
reaches the answer is excluded from the statistics. Two reference points anchor the table:
reading the whole paper is 23,683 tokens, and a random ordering reaches the answer at a
median of 11,830. Percentiles use the index convention `value[int(p × (n−1))]`. [mechanical]

| arm | found | median | p75 | p90 | max | mean |
|---|---|---|---|---|---|---|
| random ordering | — | 11,830 | | | | |
| document order | 21/21 | 3,514 | 5,723 | 6,908 | 7,264 | 3,996 |
| keyword (BM25) | 21/21 | 352 | 603 | 6,463 | 13,316 | 1,995 |
| embedding | 21/21 | 355 | 718 | 4,607 | 18,832 | 1,797 |
| hybrid (RRF) | 21/21 | **240** | 1,196 | 3,605 | 16,003 | 1,537 |
| ASTA | 18/21 | 445 | **696** | **3,072** | **3,105** | **803** |

**Table 2. How many of the 21 questions are answered within the first k passages.**
[mechanical]

| arm | k=1 | k=3 | k=5 | k=10 | k=20 |
|---|---|---|---|---|---|
| document order | 1 | 2 | 2 | 3 | 9 |
| keyword | 9 | 14 | 16 | 17 | 18 |
| embedding | 7 | 14 | 16 | 17 | 17 |
| ASTA | **13** | **15** | 16 | **18** | 18 |

**Table 3. Median tokens to answer, split by how far the question's wording sits from the
paper's.** `none` — question and paper use the same words. `term` — the paper never uses the
question's relation word (asking for "markers" where the text just names genes). `entity` —
the cell type is named differently. `both` — both at once. [mechanical]

| wording gap | items | document | keyword | embedding | hybrid | ASTA |
|---|---|---|---|---|---|---|
| none | 11 | 2,921 | **231** | 355 | 231 | 443 |
| term | 6 | 5,962 | 838 | **393** | 393 | 444 |
| entity | 2 | 4,858 | 337 | 304 | **205** | 639 |
| both | 2 | 3,537 | 6,773 | 10,886 | 8,599 | **2,396** |

Reducing the question to keywords changed nothing: keyword 352 → 352, embedding 355 → 380,
ASTA 445 → 446.

### 4.5 Conclusions

**Ranking is worth roughly ten times, and reading from the front is not competitive.** 3,514
tokens against 240–445. This is the clearest result in the test and it is deterministic.

**The embedding does not beat keyword search on typical questions.** Medians are a wash. If
typical-case cost were the only requirement, plain keyword search would do it with no network
dependency, no API key and no 500 MB model.

**Variance, not the median, is the real finding.** Keyword search and the embedding each have
items costing more than reading the entire paper (13,316 and 18,832 tokens). ASTA's worst
case is 3,105. On means — which is what an unattended run over a hundred cell types actually
pays — ASTA leads by more than twice. Its value inside a paper is consistency: never the
best, never a disaster.

**Fusing the two local arms improves the typical case but does not fix the blow-ups.** Hybrid
takes the best median at 240, and rescues cases where only one parent fails, but on items
where both parents rank badly for different reasons it lands between them rather than beating
them.

**A wording gap between question and paper hurts retrieval substantially** — keyword search
degrades about 3.6× on `term` items — and the embedding absorbs it, as intended.

**Query engineering is not the lever.** Keyword reduction changed nothing at all.

### 4.6 What this test does not license

It says nothing about whether a reader can *answer* from what is retrieved — only about where
the answer sits in the ordering. It says nothing about retrieval across a corpus, which is the
case where recall is a genuine question rather than a non-issue. And a difference of 352
versus 355 at n=21 is not a difference.

---

## 5. Test 2 — Does a model answer correctly from a fixed context, and can its quotes be trusted?

### 5.1 Aims

Test 1 measured where the answer sits. This measures whether a model produces the right
answer from a given context — which Test 1 cannot see — in three specific ways: the answer is
present and the model still gets it wrong; the answer is absent and the model answers anyway;
and whether more context helps or hurts. It also tests the assumption underneath every Test 1
number, that a passage containing the gold span lets a reader answer.

### 5.2 Design

42 items, 231 reads: 21 items with a marked span run under every condition, plus 21 items
(synthesis, citation-following, and deliberately unanswerable) that have no single span and
so run only on the whole paper. Two models, Sonnet and Haiku, run as Claude Code subagents.

Everything deterministic is precomputed to files; the only model step is the reading, done by
subagents that read one context file and write structured JSON.

The **document order** condition is a fabrication probe: the gold span is absent for 18 of the
21 items, so the correct behaviour is to decline.

### 5.3 Limitations of this design

- **One paper, 42 items.** Large effects are unambiguous; one-item differences are not.
- **Subagent isolation is instructed, not enforced.** A leak audit is the check and it came
  back clean, but it can only detect leakage that leaves a quote trail.
- **A single judge decided 38 cases.** One judge is not a panel; no disagreement rate can be
  estimated.
- **The synthesis, citation and unanswerable items ran only on the whole paper**, so that
  table is an absence-reporting probe rather than an accuracy comparison.

### 5.4 Results

**Table 4. Outcomes for the 21 items that have a marked answer sentence.** Every read is one
item under one condition with one model. "Context" is the median size of what the reader was
given. [mechanical for fabricated/spliced; [judged] for the correct/substituted split on the
five prose items]

| model | condition | n | correct | correct decline | substituted | partial | wrong | context |
|---|---|---|---|---|---|---|---|---|
| Sonnet | ASTA 2k | 21 | 16 | 2 | 2 | 0 | 1 | ~1,788 tok |
| Sonnet | ASTA 8k | 21 | 17 | 0 | 3 | 0 | 1 | ~7,719 tok |
| Sonnet | hybrid 2k | 21 | 19 | 0 | 1 | 1 | 0 | ~1,895 tok |
| Sonnet | document order 2k | 21 | 3 | 18 | 0 | 0 | 0 | ~1,891 tok |
| Sonnet | whole paper | 21 | **21** | 0 | 0 | 0 | 0 | 23,683 tok |
| Haiku | ASTA 2k | 21 | 16 | 2 | 2 | 0 | 1 | ~1,788 tok |
| Haiku | hybrid 2k | 21 | 19 | 0 | 1 | 1 | 0 | ~1,895 tok |
| Haiku | document order 2k | 21 | 3 | 18 | 0 | 0 | 0 | ~1,891 tok |
| Haiku | whole paper | 21 | 20 | 0 | 0 | 0 | 1 | 23,683 tok |

Across all 231 reads: 143 correct, 72 correct declines, 9 substituted, 4 wrong, 3 partial.

**Table 5. Quote fidelity — are the quotes the readers gave actually in the text they were
given?** A splice joins two non-adjacent passages into one presented quote: each half is
verbatim, the join is invented. "Invented" would be a quote with no source in the context at
all. Counted per read over the 159 reads that carried a quote. [mechanical]

| model | reads | carried a quote | spliced | invented | leaked |
|---|---|---|---|---|---|
| Sonnet | 126 | 90 | **0** | 0 | 0 |
| Haiku | 105 | 69 | **13** | 0 | 0 |

The separate quote audit over 210 reads agrees: 125 exact quotes, 72 declines, 13 splices,
zero leaks.

Splices ran from 26% to 76% verbatim prefix; every break fell at a sentence boundary between
two related passages, so the result reads naturally and the biology is not wrong.

**Table 6. What happens when the context is widened over a copy of the paper with a gap.**
Two items where ASTA declined at a 1.8k budget, re-run at 7.7k. [mechanical]

| item | ASTA 1.8k | ASTA 7.7k | why |
|---|---|---|---|
| "Which genes mark the dermal condensate?" | declined | **correct** | the answer sentence sits at rank 7; the wider window reaches it |
| "How early do macrophages seed prenatal skin?" | declined | **substituted** | the answer is in the paragraph missing from ASTA's copy; no budget can reach it |

### 5.5 Conclusions

**The reading step does not invent answers. [mechanical]** With the answer withheld, both
models reported absence 18 times out of 18. No read produced a quote with no source in the
context. All four deliberately-unanswerable items were declined by both models.

> **Correction.** The archived write-up reports "1 fabrication in 210 reads", from Haiku, on a
> synthesis item. That outcome does not exist in the scored data. The read in question is the
> worst of Haiku's splices — 703 characters of which 182 are verbatim — reclassified once
> splicing and invention were separated. The honest statement is that nothing was invented and
> thirteen quotes were spliced.

**A good 2,000-token slice answers as well as the whole paper. [judged]** Sonnet 21/21 versus
20/21; Haiku 20/21 versus 20/21. One item either way at n=21 is not a difference. **So
retrieval's case is cost, not accuracy** — Test 1's tenfold token saving comes without
measurable loss.

**Quote fidelity is where the two models differ, and it is the actionable difference.
[mechanical]** Both answer at similar rates. All 13 splices in the run are Haiku's; Sonnet
produced none. Since quote validation requires an exact substring match, a Haiku-gathered
quote fails validation roughly one time in five — and a relaxed fuzzy matcher would let a
spliced quote through as verbatim. This is a direct argument against a cheap reader for
evidence gathering, independent of cost.

**More context is not automatically safer. [mechanical]** Widening ASTA's window from 1.8k to
7.7k converted an honest decline into a confident, quote-backed, wrong answer, because the
wider window supplied a plausible substitute for a passage the copy does not contain. The
narrow window was safer precisely because it was too thin to support a substitute. Raising
the limit is not a remedy for a coverage gap; it turns a visible gap into an invisible one.

**Citation-following is impossible from body text as we prepare it. [mechanical]** All 12
items asking which reference backs a claim were declined by both models, correctly: the
extraction strips the reference list, so the text says "as previously reported[65]" and
nothing about what [65] is.

**A wording gap costs retrieval but not reading. [judged]** With the passage in front of the
model, failure rates by wording gap are 2/26, 1/24, 0/8 and 0/8. Test 1's abstraction penalty
is real and localises cleanly to retrieval.

### 5.6 What this test does not license

The equivalence of a 2k slice and the whole paper is at n=21 on one paper — it supports "no
detectable penalty", not "identical". The citation-following result is about our extraction,
not about what is possible in principle. And the model comparison covers Sonnet and Haiku
only; it says nothing about the models used in Test 3.

---

## 6. Test 3 — Can a reader answer realistic cell-type questions across retrieval conditions and models?

### 6.1 Aims

Tests 1 and 2 used 42 items built around a handful of cell types — principally one macrophage
subset — and phrased by us rather than taken from the authors' own wording. This test widens
to realistic report questions and asks three things that production actually varies: does the
retrieval backend matter; does one compound query per cell type work as well as one query per
report section; and does the reader model matter next to either.

The governing requirement is that **every assertion carry a verbatim quote from the supplied
context**. This replaces an earlier design that treated the reader's background knowledge as a
confound to subtract. Background knowledge is not the enemy — the pipeline needs it to expand
abbreviations and read tables — what matters is that conclusions are traceable. This turns
grounding into a substring check.

### 6.2 Design

**55 items over 16 cell types and four report sections** (markers, location, function,
structure), each question phrased using names grounded in the paper's own vocabulary. 41 items
have evidence in the paper. **14 ask about structure or morphology, which this paper does not
describe** — for those the correct answer is an explicit decline.

The cell-type vocabulary is not in the paper: it is the header row of the supplement's
logistic-regression sheets, 86 refined labels. Of those, 46 are named anywhere in text or
figure legends, 20 have at least two body-prose passages, and **16 survived reading every
passage** to become usable items.

**55 items × 6 conditions × 2 reader models = 660 reads.**

| condition | backend | query form | context |
|---|---|---|---|
| no context | — | — | 0 — a fabrication floor |
| whole paper | — | — | 9,652 tokens, shared by all questions |
| local, per-question | local hybrid | one query per question | ~1,904 tok each |
| local, per-cell-type | local hybrid | one compound query per cell type, shared by its 4 questions | ~1,881 tok each |
| ASTA, per-question | ASTA | one query per question | ~1,896 tok each |
| ASTA, per-cell-type | ASTA | one compound query per cell type | ~1,892 tok each |

The compound query is production's, rendered verbatim including its defects: it says "fetal"
where the paper says "prenatal", uses a `/` separator that collides with the label, and
repeats the label when the resolved name matches.

**Two runs on identical items, contexts and batching.** Run 1's readers were dispatched
without a pinned model, inherited the session model, and the session model changed mid-run —
so run 1's reader differs by condition (see Table 9). Run 2 pinned Sonnet throughout. Run 1 is
therefore unusable as a clean six-condition matrix on its own, but is directly useful as a
model comparison. Models were recovered afterwards from the session transcripts, not from
memory.

### 6.3 Limitations of this design

- **One paper.** The figure-legend glossary, the 46% Methods fraction and the near-absence of
  morphology may be conventions of this journal rather than universals.
- **Four of the 55 items are defective** (§6.5), so 44/55 is a floor, not a benchmark.
- **Run 1's reader model varies by condition**, so run-1 numbers cannot be compared *across*
  conditions — only against run 2 within a condition.
- **ASTA coverage cannot be measured** with exact substring matching, because ASTA renders
  the text differently.
- **One judge model** across both runs, grading its own answers in run 1.

### 6.4 Results

**Table 7. Outcomes by context and reader model.** Present items (n=41) are those the paper
answers; absent items (n=14) are the structure questions it does not. "Answered wrong"
combines substituted and leaked reads — cases where the reader asserted something the
evidence does not support. Context is tokens per question. [judged, except the no-context row
and the fabrication counts, which are mechanical]

| context | tokens | model | right | **wrong** | declined | correctly declined (of 14) |
|---|---|---|---|---|---|---|
| none | 0 | Opus | 0 | 0 | 41 | 14 |
| none | 0 | Sonnet | 0 | 0 | 41 | 14 |
| whole paper | 9,652 | Opus | 38 | **0** | 3 | 13 |
| whole paper | 9,652 | Sonnet | 32 | **3** | 6 | 12 |
| local, per-question | 1,904 | Opus | 36 | **0** | 5 | 13 |
| local, per-question | 1,904 | Sonnet | 32 | **3** | 6 | 12 |
| local, per-cell-type | 1,881 | Fable | 34 | **1** | 6 | 13 |
| local, per-cell-type | 1,881 | Sonnet | 27 | **3** | 11 | 12 |
| ASTA, per-question | 1,896 | Opus | 39 | **0** | 2 | 14 |
| ASTA, per-question | 1,896 | Sonnet | 30 | **4** | 7 | 12 |
| ASTA, per-cell-type | 1,892 | Opus | 34 | **0** | 7 | 14 |
| ASTA, per-cell-type | 1,892 | Sonnet | 31 | **4** | 6 | 14 |

**Table 8. Totals out of 55, as usually quoted.** Same data as Table 7, collapsed. Run 1's
model varies by row (Table 9), so its column should not be read as a ranking of conditions.
[judged]

| context | run 1 (mixed) | run 2 (Sonnet) |
|---|---|---|
| no context | 14 | 14 |
| whole paper | 51 | 44 |
| local, per-question | 49 | 44 |
| local, per-cell-type | 47 | 39 |
| ASTA, per-question | 53 | 42 |
| ASTA, per-cell-type | 48 | 45 |

**Table 9. Which model actually read each condition in run 1**, recovered from session
transcripts. This is why run 1 is a model comparison and not a matrix. [mechanical]

| condition | dominant model | mix |
|---|---|---|
| no context, whole paper, local per-question | Opus 5 | clean |
| ASTA, per-question | Opus 5 | 92% Opus / 8% Fable |
| ASTA, per-cell-type | Opus 5 | 88% Opus / 12% Fable |
| **local, per-cell-type** | **Fable 5** | 87% Fable / 13% Opus |
| all judge batches | Opus 5 | clean |

**Table 10. Where the two runs disagreed**, item by item, across the five conditions with
context. [judged]

| | count |
|---|---|
| run 1 right, run 2 wrong | 40 |
| run 2 right, run 1 wrong | 6 |
| of run 1's 40, attributable to a batching leak in run 2 | 4 |

**Table 11. Failure type by report section**, run 2, pooled across the five conditions with
context. [judged]

| section | missed | substituted | leaked | overreached | total |
|---|---|---|---|---|---|
| markers | 13 | 3 | 2 | 0 | 18 |
| function | 11 | 7 | 2 | 0 | 20 |
| location | 6 | 1 | 2 | 0 | 9 |
| structure | 2 | 0 | 0 | 7 | 9 |

**Table 12. Context cost per question, as the workflow actually runs it.** The whole paper is
supplied once and reused; a per-question slice is fetched for each question. Measured from the
job files the readers were given. [mechanical]

| condition | context in the prompt | questions it serves | per question |
|---|---|---|---|
| whole paper | 9,652 tok once | all 55 | ~175 tok |
| local/ASTA, per-question | ~1,900 tok each | 1 | ~1,900 tok |
| local/ASTA, per-cell-type | ~1,900 tok each | 4 | ~475 tok |

### 6.5 Four items are defective

Found by reading the failures rather than by any check. All four make the test harder than it
should be, and in two of them the readers' refusals were **more accurate than the intended
answer**.

| item | problem | should be |
|---|---|---|
| placode markers | the "markers" are receptors named in a ligand–receptor prediction, not a marker panel | absent |
| fibroblast markers | the label is too broad; the paper gives only subset markers | absent |
| capillary arteriole markers | all the markers come from an organoid comparison | absent |
| two structure-absent items | one item uses a sentence as *location* evidence while the same sentence scores as overreach on *structure* | the location/morphology boundary needs stating in the item |

Two of these failed in every condition. **The test caught the item authoring, not the reader.**
Expected set after revision: about 37 present and 18 absent.

### 6.6 Conclusions

**The quote requirement holds absolutely. [mechanical]** 660 reads, two models, zero
fabricated quotes, and a 55/55 decline rate with no context in both runs. This is cheap to
enforce and checkable without a judge. It should be the production contract.

**On one paper, retrieval buys cost, not accuracy — but read Table 12 before costing it.
[judged]** A 1.9k slice ties the 9.7k whole paper. However, because the whole paper is fetched
once and reused across questions while slices are fetched per question, **the whole paper was
about three times cheaper per question** in this run. For a report asking many questions of one
paper, reading it whole is both the cheapest option and within two questions of the best.
Retrieval earns its place when the paper is too large to hold, or when the corpus is larger
than one paper.

**Splitting the query by report section helps the local index and not ASTA. [judged]** Five
items better on the local index, three worse on ASTA. Neither is large. The compound query's
own defects — "fetal" for "prenatal", the `/` separator — are worth fixing regardless.

**The reader model moved results more than any retrieval choice. [judged]** A net 40-to-6
disagreement between runs, against a five-item spread between retrieval configurations. Tuning
retrieval while leaving the reader unpinned optimises the smaller term.

**The two models fail in different ways, and only one way is dangerous. [judged]** Opus never
answered wrongly in 205 reads with context; its failures are refusals. Sonnet gave three or
four wrong answers in every condition. Both would pass quote validation, because in every case
Sonnet quoted real text — it answered the question its quoted passage answered rather than the
one asked. **Our validation cannot catch this.** Opus's bad outcome is a gap in the report;
Sonnet's is a plausible, well-sourced, wrong sentence.

**Substitution has one mechanism, and more context feeds it. [judged]** Every substituted read
quoted something true, verbatim and on-topic that was not the asked-for claim. More context
supplies more true things to pick wrongly from, which is why the whole paper does not beat a
1.9k slice.

**The report template asks for something this source cannot give. [judged]** One of 16 cell
types has real morphological content. This is a transcriptomic atlas: it says where cells are
and what they do, not what they look like. Structure must come from cited papers or from free
search; until then the honest output is an explicit "not found", which both readers produce
well.

**Failures concentrate by report section, not by retrieval condition. [judged]** Pooling
across conditions: markers fail mostly by missing the answer, function mostly by substitution,
structure almost entirely by overreach. That is a more actionable split than any per-condition
total.

### 6.7 What this test does not license

**44/55 is a floor, not a benchmark** — four items are wrong and two of them defeat every
condition. **Run 1's column in Table 8 is not a ranking of retrieval conditions**, because its
reader changes between rows; the ASTA per-question row scoring highest is confounded with it
being read almost entirely by Opus. **The Fable result is a single row** and should not be
planned around. And nothing here tests retrieval across more than one paper.

---

## 7. Threats to validity

### 7.1 Nine scoring defects have been found, all by inspection

None was caught by a test, because the scoring code lives in `experiments/`, which the
project's rules exempt from tests, type checking and linting. That exemption is right for a
prototype. These scorers stopped being prototypes some time ago — every conclusion in this
report passes through them — but kept the exemption. That gap is where nine defects fit.

| # | defect | found in | direction |
|---|---|---|---|
| 1 | correct declines scored as failures | Test 2 | reader looked worse |
| 2 | fabrication keyed on "answered without the gold span present" rather than on the quote being ungrounded | Test 2 | reader looked worse |
| 3 | splices within one document mislabelled as cross-item leakage | Test 2 | reader looked worse |
| 4 | judge-scored items fell through to the mechanical correct/wrong branches | Test 2 | reader looked worse |
| 5 | answer keys harvested from prose picked up labels and "previously reported" asides as required answers | Test 2 | reader looked worse |
| 6 | the judge was allowed to adjudicate declines, which it calls incorrect for having no answer | Test 2 | reader looked worse |
| 7 | the leak check was scoped to one job file, though readers were given several in sequence, so real contamination was reported as fabrication | Test 3 | reader looked worse |
| 8 | a quote closed with an added full stop counted as fabrication | Test 3 | reader looked worse |
| 9 | **a single marked sentence treated as the only evidence for an answer** | Test 3, found 2026-09-03 | **retrieval looked worse; reader excused** |

Defects 1–8 all ran the same way: every one made the reader look worse than it was. Defect 9
runs the other way, and is the most consequential.

**Defect 9 in detail.** `span_in_context` decides whether a decline is a reader failure or a
retrieval failure, and produces the coverage figures. It assumes the marked sentence is the
only route to the answer. Checked directly: **of 61 reads where the marked sentence was absent
from the context, 53 were still judged correct for run 1 and 41 for run 2.** In the large
majority of cases the sentence was missing and the answer was derivable anyway.

Two consequences. The **coverage figures are lower bounds, not measurements** — a condition
scoring 19/41 on "gold span retrieved" was still answering most questions correctly. And the
**miss versus honest-miss split is unreliable in the direction that excuses the reader**:
declines are forgiven as retrieval failures on evidence that mostly does not support that.

This was anticipated. Test 1's caveats say "the measure is span position, and the span was my
choice". Test 2 met it directly and handled it, adding an `other-supported` outcome for
answers grounded in a passage the key did not anticipate — and recording a case where both
models answered correctly from a slice the marked sentence was absent from. Test 3's scorer
did not carry that category forward. **The defect is a regression, not a new discovery.**

Everything tagged [span-dependent] in this report rests on it. That is: the coverage lines in
Test 3, and the miss/honest-miss attribution. No headline total is affected, because both
kinds of decline count as not-correct.

### 7.2 The judge is unaudited, and in run 1 graded its own work

More than half of Test 3's outcomes were set by an Opus judge. In run 1 that judge was grading
answers largely produced by Opus. No disagreement rate can be estimated from a single judge,
and self-preference is a live possibility for the 40-to-6 margin.

A reviewable dossier now exists for this: `experiments/stage3b/examples_disagreements.md` (the
45 cases the model comparison rests on) and `examples_for_review.md` (all 194 judged cases).
Each case gives the question, the intended answer, the marked sentence and where it sits, every
quote each reader gave with its verification status and location, and the judge's verdict and
reason. **Until a human works through these, treat every [judged] result as a strong signal
rather than a measurement.**

### 7.3 Four numbers in this report differ from the superseded documents

Recorded rather than silently corrected.

| quantity | old document | recomputed here | why |
|---|---|---|---|
| fabricated quotes, Test 2 | 1 | **0** | the read was Haiku's worst splice, reclassified once splicing and invention were separated as outcomes |
| Haiku splices, Test 2 | 10 | **13** | the ASTA condition was added after that table was written; three of its splices were never folded in |
| random-ordering baseline, Test 1 | 12,003 | **11,830** | the baseline is a permutation estimate and varies by seed |
| ASTA p75 / p90, Test 1 | 486 / 1,720 | **696 / 3,072** | percentile index convention; the underlying values are identical |

None changes a conclusion. All other figures reproduced exactly from the data files.

---

## 8. Discussion

### 8.1 What is established

**Requiring a verbatim quote works, and it is the cheapest control available.** Across 891
model reads in Tests 2 and 3, no reader invented a quote; thirteen were spliced, all by one
model. With no context, readers declined
55 times out of 55, twice. With the evidence deliberately withheld, they reported absence 18
times out of 18. This is mechanical, reproduced, and consistent across four models.

**Within one paper, retrieval is an economy measure and not an accuracy measure.** Ranking
reaches the answer in about a tenth of the tokens; a good 2,000-token slice answers as well as
the whole 23,700-token paper. Both tests agree.

**But per-question retrieval is not automatically the economical choice.** Because the whole
paper is fetched once and reused across questions, it was about three times cheaper per
question than fetching a slice for each. The saving from retrieval depends on how many
questions are asked of one paper, which no earlier document accounted for.

**Model choice dominates retrieval choice, and the axis that matters is not accuracy.** The
two comparisons made — Sonnet against Haiku, and Opus against Sonnet — both came out on quote
and answer *safety* rather than on how many questions were answered. Haiku answers as well as
Sonnet but splices its quotes, so they fail validation. Sonnet answers fewer questions than
Opus and, when it fails, produces sourced wrong answers rather than refusals. In both cases
the cheaper model's failure mode is the one validation cannot catch.

**More context is not automatically safer.** Widening ASTA's window turned an honest decline
into a confident wrong answer; substitution rises with the amount of true-but-irrelevant
material available. This is the clearest argument against "just give it everything".

### 8.2 What these results do not support

This section exists because these conclusions have been over-read on other branches.

**"ASTA retrieval is weak."** Not supported. The coverage figures that suggest it are the ones
defect 9 invalidates: the condition that looked worst on coverage produced the highest score in
run 1. What *is* supported is narrower — at a fixed token budget ASTA delivers about half as
many distinct passages as our chunking, and its copy of some papers differs from the published
version.

**"44 out of 55 is the system's accuracy."** Not supported. It is a floor on one paper with
four known-bad items, under a scoring harness with nine known defects, more than half of it
decided by an unaudited judge.

**"Opus is better than Sonnet at this task."** Over-stated. What was measured is a 40-to-6
disagreement on one paper, judged by Opus, in a run where Opus's own condition assignments were
partly confounded with the model changing mid-run. The *direction* is consistent and the
failure-mode difference is a real and important distinction. The magnitude is not established.

**"Whole-paper reading beats retrieval."** Not supported as a general claim. It ties on
accuracy and wins on cost **for a 23,700-token paper when many questions are asked of it**.
A larger paper, or a corpus, changes this completely.

**"Retrieval was tested."** Only within a single paper, where there is no recall problem by
construction. The case where retrieval actually matters — finding evidence across many papers —
has not been tested here at all.

**"The pipeline does not fabricate."** Supported for the *reading* step and not beyond it. An
earlier audit found unsourced prose at a high rate; Test 2 rules out reading as its source and
points at synthesis, where the model is asked to fill a section rather than answer a question.
That is a different task and has never been measured.

---

## 9. Limitations

**One paper, throughout.** Everything here is Gopee et al. 2024. Several structural findings —
the figure-legend glossary, Methods at 46% of body text, the near-absence of morphology — may
be conventions of this journal and this kind of atlas. The one time a second paper was looked
at, it produced the version mismatch in §3.3, which suggests papers differ in ways that matter.

**The item sets are small and were written by one person.** 21, 42 and 55 items. Large effects
are clear; a one- or two-item difference is not a difference. Four of the 55 in Test 3 were
subsequently found to be wrong, which is a rate worth assuming holds for the sets that have not
been re-examined.

**Scoring is the weakest link, not the experiments.** Nine defects, none caught by a test.

**No test covers synthesis.** Every test here asks a question and scores an answer. The
pipeline's actual failure — unsourced prose in reports — appears at the point where a model
fills a report section, which is a different task and untested.

**No test covers more than one paper**, which is where retrieval stops being an economy
measure and becomes a recall problem.

---

## 10. Further tests needed

In rough priority order.

1. **Pin the scorer with regression tests.** Hand-built fixtures for each outcome — a splice, a
   leak, a decline on an answerable item, a multi-part answer whose marked sentence is missing —
   asserting the classification. This is the only thing that stops defect number ten, and it is
   cheap.
2. **Hand-review the 45 disagreement cases** in `examples_disagreements.md`. This settles the
   judge question, which is the largest remaining doubt about the model comparison.
3. **Let an item carry one marked sentence per claim** in a multi-part answer, then recompute
   the coverage figures and the miss attribution. No new reads are needed.
4. **Revise the four defective items** and re-score. Three are reclassifications needing no new
   reads.
5. **Measure synthesis directly** — the same items, but asking for a report section rather than
   an answer. Test 2 rules out reading as the source of unsourced prose, so this is the
   highest-value unmeasured thing in the pipeline.
6. **Repeat the item-set construction on a second paper**, to find out whether any of §6.2's
   attrition pattern generalises.
7. **Record which rendering a quote came from**, so validation is not at the mercy of which copy
   of a paper is held. §3.3 makes this a correctness issue, not a tidiness one.
8. **Index figure legends as their own segments.** They carry the naming vocabulary that body
   prose lacks.
9. **Test retrieval across a corpus.** Out of scope for this branch's single-paper work; the
   citation-traversal strand covers part of it, and an enrichment test is planned separately.

Two things were built and deliberately not run: an intermediate 8k context budget in Test 2
(between two conditions that came out indistinguishable, so unlikely to separate anything), and
the supplement-derived test designed in the old handoff, which was overtaken by the citation
work.

---

## 11. Appendix

### 11.1 Where the data lives

```
experiments/results/stage1.json          Test 1 — every item × arm × query form
experiments/results/stage1_hybrid.json   Test 1 — the fused arm
experiments/stage2/                      Test 2 — contexts, answers, scores, quote audit
experiments/stage3b/                     Test 3 run 2 (Sonnet) — items, contexts, jobs,
                                         answers, verdicts, scores
experiments/stage3b/runs/run1-mixed/     Test 3 run 1 (Opus/Fable) — kept for the model
                                         comparison; reads the same contexts
experiments/stage3b/examples*.md         judged cases written out for human review
experiments/roster/                      the grounded name and synonym roster
experiments/session_logs_cache/          cached Claude Code session logs (untracked)
```

Directory names still carry the old stage numbers. They are left alone so that paths in the
archived documents continue to resolve.

### 11.2 Reproducing

```bash
# Test 1 — deterministic, no API keys
uv run python experiments/run_stage1.py

# Test 3 — scoring and reports from the answers already on disk
uv run python experiments/stage3b/score.py   --dir experiments/stage3b
uv run python experiments/stage3b/report.py  --dir experiments/stage3b
uv run python experiments/stage3b/compare_runs.py \
    --run1 experiments/stage3b/runs/run1-mixed/final.json --label1 opus \
    --run2 experiments/stage3b/final.json --label2 sonnet \
    --provenance experiments/stage3b/runs/run1-mixed/reader_provenance.json

# Test 3 — regenerate the human-review dossiers
uv run python experiments/stage3b/examples.py --only-disagreements
uv run python experiments/stage3b/examples.py
```

Re-running the reads themselves needs `ASTA_API_KEY` and a Claude Code session; methods are in
the archived Test 3 document, §5.9.

### 11.3 Old names to new

| old name | what it was | where it is now |
|---|---|---|
| Stage 1 | ranking inside a paper, no model | §4, Test 1 |
| Stage 2 | reading from a fixed context | §5, Test 2 |
| Stage 3 | a supplement-derived test | **designed, never run** — §10 |
| Stage 3b | the retrieval matrix | §6, Test 3 |
| "Stage 3b" in `experiments/citation_traversal/` | claim adjudication against cited papers | a **different** piece of work — `planning/citation_traversal/` |

The superseded documents are archived unchanged at
`experiments/archive_2026-09_superseded_writeups/`, with a README mapping each to the section
that replaces it.

### 11.4 Scoring rules learned the hard way

Carried forward from the archived handoff, because they are the accumulated cost of the nine
defects and any new scoring code should start from them.

1. Do not derive answer keys from prose. State one intended answer per item, or route to a
   judge.
2. Whether the marked sentence reached the context is not a boolean about whether the answer
   was available — see defect 9.
3. Whether a decline is correct depends on the group the item is in.
4. Grounded is not the same as correct. Keep "quote not in context" and "quote real but does
   not support the claim" separate.
5. Never send a decline to a judge; it will be called incorrect for having no answer.
6. Items resolved mechanically must not fall through into a judged branch, or the reverse.
7. Scope the leak check to what one reader agent actually saw, not to one job file.
8. Added sentence-final punctuation is not fabrication.
9. Pin `model:` on every subagent, and record it. Recover it from session transcripts
   afterwards rather than reporting it from memory.

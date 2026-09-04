# Stage 1 results — is ranking inside a paper worth anything?

**August 2026, branch `test/retrieval-matrix`.** Complete. No LLM was involved at any
point; every number is deterministic and reproducible from `experiments/run_stage1.py`,
with raw output in `experiments/results/stage1.json`.

---

## 1. The question

When the pipeline needs evidence about a cell type from a paper it already holds, it
currently runs a snippet search and reads what comes back. That assumes searching inside a
paper is better than just reading the paper. Nobody had tested it.

An atlas paper is about 24,000 tokens — small enough to put in a model's context whole. So
inside a single paper there is **no retrieval problem**: nothing is unreachable. The only
thing a search can buy you is **position** — putting the answer near the top so you read
less of the paper before you have it.

Stage 1 measures exactly that, and nothing else.

## 2. What an item is

An item is a question with a known answer, and a **gold span**: the exact sentence in the
paper that answers it. Both were produced by *reading* the paper — enumerating every
attributed claim and every findings sentence and marking them by hand. Crucially, no
search was used to find them. If items were located by querying ASTA, ASTA would win the
comparison by construction.

Example — item **B13**:

> **Question:** Which genes identify TREM2+ microglia-like macrophages?
> **Gold span:** "yolk-sac derived TREM2+ macrophages that share an expression profile
> (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs"
> **Answer:** P2RY12, CX3CR1, OLFML3

21 items were used, all from Gopee et al. 2024 (the prenatal skin atlas). The wider set of
57 covers synthesis, citation-following, supplement extraction and unanswerable questions;
those need a model to score and belong to Stages 2 and 3. Only items carrying a single
verbatim span can be scored without one, which is what makes Stage 1 free.

## 3. The arms — five ways to order a paper

Every arm receives the **same paper** and produces an **ordering** over its chunks. They
differ only in how they sort. Three of them (`document`, `lexical`, `local`) read an
identical chunk set — 152 chunks of ~1,000 characters, built from the PMC JATS with figure
legends and citation markers stripped — so they differ *only* in ranking. ASTA has its own
chunking and serves its own copy of the text.

| Arm | What it does | Why it's here |
|---|---|---|
| `document` | Publication order: chunk 1, 2, 3… No query involved. | The baseline that competes. "Just read the paper" is a real strategy, and papers are structured — results in the middle, methods at the end — so it is not a dumb floor. |
| `lexical` | **BM25.** Classic keyword scoring: chunks rank by how many query terms they contain, weighted so rare terms count more and long chunks are not unfairly favoured. Purely literal — no notion of meaning. | The cheap option. No network, no API key, no model. |
| `local` | **Dense embedding.** Each chunk and the query are converted to a vector by `all-MiniLM-L6-v2`; chunks rank by cosine similarity. Scores meaning rather than words, so it can match "what does X do" to a sentence that never says "function". | The thing we currently pay for in the local index. |
| `asta` | `snippet_search` scoped to the paper via Semantic Scholar. Its own chunking, its own copy of the text, its own ranking. | What the pipeline uses today. |
| chance | Not run — computed. The chunks are permuted 2,000 times to get the distribution of cost under an ordering that knows nothing. | Turns every other number into "better than chance by this much" rather than a bare figure. |

**Embeddings, in one line:** BM25 asks "does this chunk contain the query's words?"; the
dense arm asks "does this chunk mean something similar to the query?". That difference is
the whole story of section 6.

For each arm two query forms were tried: the **verbatim question**, and a **keyword
reduction** of it (stopwords removed).

## 4. The measure — tokens to answer

Walk the ordering from the top, accumulating text, and stop when the answer is available.
Report how much you read to get there. **Lower is better.**

"Available" means **80% of the gold span's word 5-grams** have appeared in everything read
so far. Not an exact string match, for two reasons:

- A sentence split across two retrieved chunks is available to a reader holding both, but
  the chunks arrive separated in rank order so a joined string is not contiguous. An
  n-gram measure loses only the few grams spanning the seam.
- ASTA and PMC render the same sentence differently, so exact matching would penalise an
  arm for text it never had.

Tokens are estimated at 4 characters each.

### How to read the tables

- **Every number is a token count** — how much of the paper you had to read. Lower is
  better.
- **Two reference points anchor everything:** the whole paper is **23,683 tokens**, and
  chance is **12,003**. An arm scoring 400 is finding the answer in under 2% of the paper.
- **"Found" is out of 21.** A dash means the arm never reached the answer.
- **Median tells you the typical case; p90 and max tell you the bad case.** They disagree
  here, and that disagreement is the main result.

---

## 5. Results

### Headline — tokens to answer, verbatim question form

| Arm | Found | Median | p75 | p90 | Max | Mean |
|---|---|---|---|---|---|---|
| chance | — | 12,003 | | | | |
| `document` | 21/21 | 3,514 | 5,723 | 6,908 | 7,264 | 3,995 |
| `lexical` (BM25) | 21/21 | **352** | 603 | 6,463 | 13,316 | 1,995 |
| `local` (dense) | 21/21 | 355 | 718 | 4,607 | 18,832 | 1,796 |
| `asta` | 18/21 | 445 | **486** | **1,720** | **3,105** | **802** |

Read this as: *typically* BM25 and the embedding get you there in ~350 tokens and ASTA in
~445, but BM25's and the embedding's worst cases cost more than reading the entire paper,
while ASTA's worst case is 3,105.

### Answered within the first k chunks

| Arm | k=1 | k=3 | k=5 | k=10 | k=20 |
|---|---|---|---|---|---|
| `document` | 1 | 2 | 2 | 3 | 9 |
| `lexical` | 9 | 14 | 16 | 17 | 18 |
| `local` | 7 | 14 | 16 | 17 | 17 |
| `asta` | **13** | **15** | 16 | **18** | 18 |

ASTA puts the answer in the very first chunk for 13 of 21 questions.

### By abstraction tag — median tokens

The tag records how far the question's wording sits from the paper's. `none` = they match.
`term` = the paper never uses the question's relation word (asking for "markers" where the
text just names genes). `entity` = the cell type is named differently (asking about
"pre-dermal condensate cells" where the text says "pre-Dc"). `both` = both at once.

| Tag | Items | `document` | `lexical` | `local` | `asta` |
|---|---|---|---|---|---|
| `none` | 11 | 2,921 | **231** | 355 | 443 |
| `term` | 6 | 5,962 | 838 | **393** | 444 |
| `entity` | 2 | 4,858 | 337 | **304** | 639 |
| `both` | 2 | 3,537 | 6,773 | 10,886 | **2,396** |

### Every item

| id | tag | doc | bm25 | dense | asta | question |
|---|---|---|---|---|---|---|
| A1 | none | 206 | 206 | 355 | — | When do prenatal hair follicles start forming? |
| A2 | none | 5316 | 603 | 380 | 442 | At what age does prenatal skin lose scarless healing? |
| A3 | none | 443 | 179 | 355 | — | How early do macrophages seed prenatal skin? |
| A4 | none | 2417 | 231 | 231 | 444 | When do sebaceous and apocrine gland cells mature? |
| A5 | none | 3095 | 199 | 718 | 392 | Which markers define the dermal papilla (Dp)? |
| B1 | none | 2699 | 222 | 222 | — | Where are Treg cells found, and from what age? |
| B2 | none | 1683 | **13316** | 618 | 3105 | Which cell types do macrophages co-locate with? |
| B3 | none | 6908 | 375 | 4694 | **49** | What do TML macrophages co-locate with besides endothelium? |
| B4 | none | 2921 | 222 | 222 | 406 | Which gene newly identified in DPYSL2+ basal cells…? |
| B5 | none | 3514 | 485 | 314 | 446 | Which genes are expressed as pre-Dc cells aggregate? |
| B6 | none | 3754 | 240 | 240 | 446 | Which ligand–receptor pair drives pre-Dc migration? |
| B8 | term | 6908 | 1324 | 434 | 152 | Function of TML macrophages in relation to skin nerves? |
| B9 | term | 7264 | 6463 | 4607 | 696 | Role of macrophages in blood vessel formation? |
| B10 | term | 2699 | 222 | 222 | 486 | What does CXCL14 do in matrix cells? |
| B11 | both | 3979 | **13119** | **18832** | 3072 | Which genes mark the dermal condensate? |
| B12 | term | 5371 | 2805 | 1151 | 442 | Markers distinguishing prenatal vs adult fibroblasts? |
| B13 | term | 6202 | 235 | 235 | 427 | Which genes identify TREM2+ microglia-like macrophages? |
| B14 | term | 5723 | 352 | 352 | 447 | Genes characterising WNT2+/PEAR1+ fibroblasts? |
| B15 | entity | 3514 | 439 | 175 | 852 | Where do pre-dermal condensate cells migrate to? |
| B16 | both | 3095 | 427 | 2941 | 1720 | Marker profile of the dermal papilla? |
| B17 | entity | 6202 | 235 | 434 | 427 | Genes shared by prenatal skin and brain microglia? |

### Hybrid (added after the first pass)

BM25 and the dense arm score the same chunks, so they fuse with reciprocal rank fusion —
each contributes 1/(60 + rank), so only the orderings matter and no score calibration is
needed. No API calls, minutes of compute.

| Arm | Median | p75 | p90 | Max | Mean |
|---|---|---|---|---|---|
| `hybrid` (RRF) | **240** | 1,196 | 3,605 | 16,003 | 1,537 |
| `lexical` | 352 | 603 | 6,463 | 13,316 | 1,995 |
| `local` | 355 | 718 | 4,607 | 18,832 | 1,796 |
| `asta` | 445 | **486** | **1,720** | **3,105** | **802** |

By tag, it does exactly what was predicted — it inherits whichever parent is better:

| Tag | hybrid | bm25 | dense |
|---|---|---|---|
| `none` | **231** | 231 | 355 |
| `term` | **393** | 838 | 393 |
| `entity` | **205** | 337 | 304 |
| `both` | 8,599 | 6,773 | 10,886 |

**But it does not fix the blow-ups, and that is the point of having run it.** On `both`
items fusion lands *between* its parents rather than beating them: B11 costs 16,003 tokens
against BM25's 13,119 and dense's 18,832. When both arms rank a chunk badly for different
reasons, fusion averages the failure instead of curing it. It does rescue cases where only
one parent fails — B2 goes from BM25's 13,316 to 3,605, pulled up by dense's 618.

So hybrid is the best local arm on typical questions (median 240, mean 1,537) and still
loses the tail to ASTA by a wide margin (p90 3,605 vs 1,720; max 16,003 vs 3,105).

### Query form made no difference

`lexical` 352 → 352, `local` 355 → 380, `asta` 445 → 446. Reducing the question to keywords
changed nothing.

### Per-item winner

BM25 11, ASTA 5, dense 4, document 1.

---

## 6. What this means

**Ranking is worth roughly 10×, and reading from the front is not competitive.** That was
what `document` was there to establish, and it did: 3,514 tokens against ~350–450.

**The embedding does not beat BM25 on typical questions.** Medians are a wash (352 vs 355),
BM25 takes more per-item wins, and on `none` items BM25 is clearly ahead (231 vs 355). If
within-paper ranking were the only requirement, plain keyword search would do it with no
network dependency, no API key and no 500 MB model.

**But variance, not the median, is the real finding.** BM25 and the embedding each have
items costing 13,316 and 18,832 tokens — more than reading the whole paper. ASTA's worst
case is 3,105 and its p90 is 1,720. On means, which is what an unattended run over a
hundred cell types actually pays, ASTA leads by more than 2×. Its value inside a paper is
*consistency*: never the best, never a disaster.

**Abstraction is the mechanism behind the tails, and it behaves as predicted.** On `term`
items BM25 degrades from 231 to 838 while the dense arm holds at 393 — exactly what you
expect when the query's words are absent but its meaning is not. B8 is the clean case: the
paper describes TML macrophages contributing to "synapse formation and axon guidance" but
never calls it a function, and BM25 pays 1,324 tokens where the embedding pays 434. The two
`both` items are where both local arms collapse and ASTA wins by 3–7×.

**Query engineering is not the lever.** Keyword reduction changed nothing at all. That is
indirect evidence against the value of per-aspect query authoring — not a direct test of
it, but not encouraging either.

---

## 7. The three items ASTA could not answer

A1 and A3 sit at PMC sentences 3 and 5, inside a seven-sentence run at the head of the Main
text that ASTA's copy does not carry. B1 is sentence 58, in a second short gap. Gram
coverage for the three is 0%, 6% and 0% — genuinely absent, not near-threshold.

Two of them are exactly the kind of fact a report leans on: when hair follicles start
forming, and when macrophages first seed the skin.

## 8. Why Suo was excluded — the version problem

The test set also contained three items from Suo et al. 2022, the subatlas paper. They are
excluded from everything above, because ASTA serves a **different version** of that paper.

- Only **28% of ASTA's 5-grams** appear in the PMC full text.
- ASTA uses British spellings throughout (haematopoietic ×20, hematopoietic ×0); PMC is the
  reverse (×0 / ×10).
- The same methods sentence is materially rewritten — ASTA's copy names the organs
  explicitly, PMC's does not.
- `get_paper` confirms the DOI resolves to the right paper, so this is a version
  difference, not a mis-resolution. Most likely preprint or accepted manuscript versus
  published.

Gopee's two copies, by contrast, agree at 96% of prose sentences. So it varies by paper and
cannot be assumed away.

**This has the widest consequences of anything in Stage 1.** Evidence gathered from ASTA
may not appear verbatim in the copy a validator or a human checks against, and nothing in
the pipeline records which rendering a quote came from. `check_quotes` will pass or fail
depending on which copy it happens to hold.

---

## 9. Caveats

- **The measure is span position, and the span was my choice.** Where a fact appears in
  several places I marked one. B2 is likely such a case: BM25 spent 13,316 tokens reaching
  *my* sentence about macrophage co-location and may have surfaced an equally good one much
  earlier. Stage 2 tests answerability directly and will show how much this matters.
- **`document` scores are sometimes accidents.** A1's 206 tokens is not a win for reading
  in order; that fact simply lives in the paper's third sentence.
- **21 items, one paper.** Enough for the large effects — the gap to `document`, the tails,
  the `term` split. Not enough for small ones: 352 versus 355 is nothing.
- **Two items per `both` cell.** Suggestive, not established.
- **ASTA is not ranking the same chunks.** The comparison is of delivered text, which is
  what you pay for, but it is not a clean ranking-algorithm comparison.
- **The dense arm was embedded fresh for this work** — our own uniform chunks encoded with
  MiniLM inside the harness, not the production `local_snippet_index`. Deliberate, so the
  three local arms differ only in ranking. It means this tests the embedding, not the
  production index's chunking or its post-#23 windowing.
- **The #23 truncation issue is present here, mildly, and changed nothing.** MiniLM reads
  256 word pieces. Our ~1,000-character chunks run to a median of 179 pieces and p90 of
  245, but **9 of 142** Gopee chunks (6%) exceed the window, keeping 89–93% of their
  content. (For scale, the production 2,800-character chunks that prompted #23 ran to
  493–700 pieces, embedding roughly half.) Checked directly: only two *gold-bearing* chunks
  exceed 256 — B13 and B17, both 278 pieces — and in both the span sits at pieces 5–53 and
  77–107, inside the embedded window. **No gold span was truncated away, and B11's
  18,832-token failure is a genuine ranking failure, not a truncation artefact.** The
  residual risk is second-order: nine partially-embedded chunks carry slightly wrong
  vectors and could sit a place or two out of position, worth a few hundred tokens at
  most.
- **Nothing here concerns cross-paper retrieval**, where recall is a genuine question. This
  is the case where retrieval matters least.

---

## 10. What follows

**An obvious missing arm: hybrid.** BM25 and the embedding already score the *same* chunk
set, so fusing them is a few lines — reciprocal rank fusion needs no score calibration. The
prediction from this data is specific: a hybrid should keep BM25's ~230-token wins on
`none` items and inherit the embedding's ~400-token behaviour on `term` items. The open
question is whether it inherits or cancels the B11-style blow-ups — if both arms rank B11
badly for different reasons, fusion will not save it. Minutes of compute, no API calls, and
it is the arm most likely to resemble what we would actually build.

**For implementation.** Within-paper ranking is worth having. The cheap option is
competitive typically and unreliable occasionally, and ASTA's advantage is entirely in its
tails. Nothing here justifies a network dependency purely for within-paper ranking *if* a
local hybrid can close the tail gap — which is precisely what the hybrid arm would tell us.

**For the version problem.** Recording which rendering a quote came from is a small change
with a clear justification, and should probably become a ticket regardless.

**Stages 2 and 3** — reading (does a model answer correctly from a given context, and does
it fabricate on the unanswerable items) and supplements. Stage 2 also tests the span proxy,
which is the main assumption underneath every number here.

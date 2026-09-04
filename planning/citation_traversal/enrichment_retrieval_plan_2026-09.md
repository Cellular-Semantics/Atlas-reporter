# Plan — retrieving cell-type evidence from the cited literature

**Branch `test/retrieval-matrix`, written 2026-09-03. Not started.**

Follows `planning/citation_traversal/README.md` (what works when following citations) and
`experiments/retrieval_tests_report_2026-09.md` §6 (how readers behave on a single paper).
Both are assumed read; this plan does not re-derive their numbers.

---

## 1. Why this is needed now

The single-paper work has a clear answer: read the atlas paper's full text once and ask
many questions of it. The full text is about 9,650 tokens, it is fetched once and reused
across all questions, and with a strong reader it scores within two questions of the best
retrieval arm. Per question it was about three times cheaper than fetching snippets for
each question separately.

That answer does not transfer to the cited literature. An atlas paper cites around 110
other papers. Reading them all in full is not an option, and about half of them cannot be
read at all — 57 of 109 references are reachable by either PubMed Central or ASTA, and 48%
by neither. So for everything beyond the atlas paper itself we are committed to retrieval,
and the question is which retrieval design.

We have measured one design. The current approach issues a separate query for every
(cell type × aspect) pair against the whole reference list — location, structure, function
and markers asked separately, each searching all cited papers at once. Call this the
**shotgun**. Nobody has tried the obvious alternative: ask once per cell type, get a set of
snippets about that cell type, and then put several questions to that set.

---

## 2. What we already know that constrains the design

Four results from the existing work bear directly on this, two encouraging and two not.

**Short queries win whenever the search covers more than one paper.** Over the atlas
paper's reference list, a short keyword query found the correct paper in the top 20 for
19 of 19 claims and ranked it first for 15, against 18/19 and 11/19 for a full claim
sentence. It also retrieved 23 of 32 supporting passages against 17. Inside a single paper
the advantage reversed and became slight. A bare cell-type name is the short-query form, so
for a search across ~87 papers it is the right shape. This is the main reason to expect the
proposal to work.

**Spreading one snippet budget across papers is what breaks multi-paper search.** Searching
inside one known paper returned the supporting passage 97% of the time it was there.
Searching the reference list returned it 53–72% of the time, because a fixed budget divided
across five papers leaves about four snippets each. A single cell-type query that must also
carry four aspects across several papers makes this tighter, not looser. This is the main
reason to expect the proposal to fail in its simplest form.

**Sharing one query's snippets across several questions has already been part-tested, and
the result was mixed.** In the single-paper matrix, merging the four aspect questions into
one compound query cost 5 questions on our own index and gained 3 on ASTA's. So merging is
not inherently harmful, but it is not free, and the case where it lost was the case where
retrieval was otherwise working well.

**Rich context causes wrong answers, not just missed ones.** The dominant failure in the
single-paper work was the reader quoting something true and on-topic that was not the
answer to the question asked. It got worse as more true material was put in the window, and
our quote validation cannot catch it — the quote is genuine. A snippet set pooled across
many cited papers is the richest possible source of true-but-wrong material, and the
irrelevance is usually invisible: different species, organ, or developmental stage. The
citation work already found the atlas paper's own authors doing this, applying a signalling
mechanism from liver regeneration and a migration result from a lung cancer cell line to
prenatal skin without qualification.

---

## 3. The blocker: we cannot currently score any of this

Neither existing gold set measures what this is for.

| gold set | what it scores | why it does not fit |
|---|---|---|
| 55 single-paper items | answers that are present in the atlas paper | says nothing about other papers |
| 46 verified spans over 19 claims | whether a cited paper supports a claim the atlas paper already makes | verification, not enrichment |

The aim here is enrichment: learning something about a cell type that the atlas paper does
not say. Scored against the verification spans, a retrieval design would be rewarded for
recovering passages backing claims we already have — which is close to the opposite of what
we want, and would make the shotgun look fine while telling us nothing.

`aims.md` states this directly: enrichment is the primary aim and is the one thing never
measured. Building that gold is the harder half of this plan, and it comes first.

---

## 4. Part A — build an enrichment gold set

**Method, copied from the verification work because it produced usable data.** Queries were
written and committed to disk before any cited paper was opened, so nothing could be tuned
to an answer already seen; and the output was verbatim spans rather than verdicts, which
turned every later retrieval measurement into string matching with no judge involved. All
46 spans were machine-verified as exact substrings. Keep both properties.

**Scope.** Six to eight cell types from Gopee et al. 2024, chosen to span the range the
single-paper work exposed: some where the atlas paper is rich (macrophage subsets,
WNT2+ fibroblast), some where it is thin (the vascular and hair-shaft types where the
structure questions had no answer at all). Do not pick only the well-served ones.

**Selection of papers to read.** For each cell type, take every reference cited in a
sentence that mentions it, and — unlike the verification work — **include the introduction**.
The verification work excluded Methods citations because they point at tools and datasets; for enrichment
the intro is where the atlas paper points at the literature defining a cell type, so it is
the part most worth following. Filter to what is actually readable.

**What a curator writes down.** For each cell type, statements the cited papers make about
it that the atlas paper does not, each with a verbatim span and its source DOI. Record
alongside each one:

- whether it is about the same organism, organ and developmental stage as the atlas
  annotation, or is being carried across from another context;
- which section of the source it came from (introduction, results, figure caption), since
  coverage is known to be uneven across these.

That second field is the part the existing gold lacks and the part a report most needs, and
it is why this has to be a human read rather than a model pass.

**Expected size.** Six to eight cell types at maybe 5–15 statements each — of the order of
60–100 items. Comparable effort to the 19-claim adjudication, which read 15 papers in full.

**Machine check before use.** Every span verified as an exact substring of its source, the
same check `verify_gold_spans.py` performs.

---

## 5. Part B — the retrieval comparison

Three designs, on the same cell types and the same gold, plus a ceiling.

| design | hop 1 | hop 2 | what it tests |
|---|---|---|---|
| **shotgun** (baseline) | one query per cell type × aspect over all cited papers | none | current behaviour |
| **pooled** | one short cell-type query over all cited papers | none — the returned snippets are the context for all aspect questions | the proposal as stated |
| **two-hop** | one short cell-type query over all cited papers, used only to choose papers | per-paper retrieval inside each chosen paper, aspects asked separately | the design the existing results point at |
| **ceiling** | — | full text of every readable cited paper for that cell type | how much of the gold is reachable at all |

The two-hop arm exists because the two strongest existing numbers are for its two halves
taken separately: finding the right paper from the reference list (19/19) and finding the
passage once inside it (97%). The pooled design asks hop 1 to do both jobs, and hop 1 is
the weaker one for extracting evidence. If pooled and two-hop score the same, the second
hop is not worth its cost and that is a genuine simplification.

The ceiling arm is not optional. Without it a miss cannot be attributed — "not retrieved"
and "never indexed" are indistinguishable, and coverage is known to be the binding
constraint. Expect it to be well short of 100%: within papers ASTA holds, only 70% of
supporting passages were in the index at all, with introductions and figure captions the
systematic gaps. Introductions being weakest is the awkward part, since this plan
deliberately targets intro citations.

**Reader models.** Opus and Sonnet on every arm, and Fable if the earlier signal holds up.
The single-paper work found the reader model mattered more than the retrieval choice, and
the two models fail differently: Opus declined rather than answered wrongly in 205 reads,
while Sonnet gave 3–4 confidently wrong answers per arm. Both would pass quote validation.
Any recommendation here has to name a model, not just a retrieval design.

**Pin `model:` on every subagent, without exception.** The first single-paper run was
dispatched unpinned, inherited the session model, the session model changed mid-run, and
the result was a matrix whose reader differed by arm plus an unplanned credit spend. Record
the pinned model in the run output and check it against the session transcripts afterwards.

---

## 6. Scoring

Three numbers per arm per model, kept separate because they trade against each other:

- **Yield** — how many gold statements the arm recovered. String matching against the gold
  spans; no judge.
- **Precision** — of the statements the reader asserted, how many are in the gold or are
  defensible additions. Judged.
- **Context integrity** — how many asserted statements were carried across from another
  organism, organ or developmental stage without saying so. Judged, and the number this
  whole exercise exists to watch. The gold's context field is the answer key.

**Every judged number ships with the cases behind it.** More than half the outcomes in the
single-paper matrix were set by an LLM judge, and that judge was Opus grading Opus's own
answers in one of the runs. `experiments/stage3b/examples.py` is the pattern: it writes out
the question, the intended answer, the gold span, each reader's answer, and the judge's
verdict and reasoning, so the calls can be checked by hand. Produce the equivalent here and
treat any aggregate quoted without it as unreported.

Also carry over the scoring rules already paid for: no answer keys taken from prose;
whether the marked sentence reached the context does not tell you whether the answer was
available — see the report's defect 9; a decline is right or wrong
depending on the group the item is in; grounded is not the same as correct; judged items
must not silently fall through; the leak check is scoped to the reader agent rather than
the job file, because agents receive several job files and earlier context stays in the
window. All nine are catalogued in `experiments/retrieval_tests_report_2026-09.md` §7.1,
with the rules restated in its §11.4.
Every one of them, when found, had been making the reader look worse than it was.

---

## 7. What this decides

The outcome should settle three things for the production workflow:

1. Whether traversal issues one query per cell type or one per cell type and aspect.
2. Whether a second, paper-scoped hop earns its cost.
3. Which reader model to pin for traversal, and what accuracy is bought by paying for a
   better one.

If the answer to (1) is "pooled", traversal gets roughly four times cheaper. If yield is
similar but context integrity is worse, it is not a saving, and the report format will need
per-snippet source attribution before pooling can be used at all.

---

## 8. Order and cost

1. **Enrichment gold** (§4) — the long pole, and the only thing here that cannot be
   automated. Nothing downstream is interpretable without it.
2. **Ceiling arm** (§5) — cheap once the gold exists, and it sets the denominator for
   everything else. Run before the retrieval arms, so a poor score can be attributed.
3. **Three retrieval arms × models** (§5).
4. **Examples dossier and write-up** (§6).

Steps 2–4 are mechanical once step 1 is done. The retrieval calls are comparable in volume
to the existing matrix runs; the reading in step 1 is comparable to the 19-claim
adjudication.

**Not in scope.** Repeating any of this on a second atlas paper. Everything here is
Gopee-only, as all the prior work is, and none of it should be quoted as general until it
has been repeated at least once elsewhere.

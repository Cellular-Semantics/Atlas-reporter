# Stage 3b — Retrieval matrix: can a reader answer realistic cell-type questions, and cite them?

**August 2026 · branch `test/retrieval-matrix`**
**Two full runs: 330 reads each (660 total), 355 judge verdicts.**

Data: `experiments/stage3b/` (run 2, Sonnet) and `experiments/stage3b/runs/run1-mixed/`
(run 1, Opus/Fable — kept for model comparison). Roster: `experiments/roster/`. Code: §5.9.

> **Naming.** *3b*, not Stage 3. The supplement-derived Stage 3 in
> `planning/HANDOFF_stage3_extended_test.md` is a different, still-unrun experiment.

---

## Abstract

atlas-reporter answers questions about cell types by retrieving passages from atlas papers
and requiring a supporting quote for every claim. Stages 1 and 2 measured retrieval and
reading on 42 items drawn from essentially one cell type. This stage widens that to **55
items over 16 cell types and four report axes**, grounds every question in the names the
authors actually use, and runs the full matrix: **three retrieval backends × two query
forms, plus a whole-paper ceiling and a no-context floor.**

The governing requirement is that every assertion carry a verbatim quote from the supplied
context. That requirement held completely: in the no-context arm the reader declined
**55/55** in both runs, and after two scorer fixes there were **zero fabricated quotes in
660 reads**.

Whole-paper reading and a 1.9k-token retrieved slice **tie at 44/55**. Splitting the query
by axis beats the production compound query on the local index (44 vs 39) but not on ASTA
(42 vs 45). **Reader model moved results more than any retrieval choice**: Opus scored 6–11
items higher than Sonnet per arm, against a maximum 5-item spread between retrieval
configurations.

---

## 1. Introduction

### 1.1 Where this sits

- **Stage 1 (ranking, no model calls).** Ranking passages within a paper is worth ~10× over
  reading from the front. BM25 ≈ MiniLM on medians; RRF hybrid takes the best median.
  Abstraction in the query costs retrieval ~3.6×.
- **Stage 2 (reading, 231 reads).** Fabrication near-absent (1 in 231). Absence reported
  reliably (18/18). A ~1,900-token local slice reached 20/21, the same as the whole
  23,700-token paper. **Retrieval's case is cost, not accuracy.**

Both used 42 items built around a handful of cell types, principally one macrophage subset,
and phrased by us rather than derived from the authors' own wording.

### 1.2 What this stage tests

The pipeline retrieves evidence with one query per cell type and writes a report with
sections for markers, location, function and structure. Three things were unmeasured:

1. **Does the retrieval backend matter?** Production can use ASTA snippet search or a local
   hybrid index over PMC JATS. Stage 2 compared them on one cell type.
2. **One query or several?** Production issues a single compound query covering all four
   axes (`CLAUDE.md:142`). Per-axis queries were never tried.
3. **Does grounding the cell-type name in the paper's own vocabulary help?** Annotation
   labels are frequently not what the authors write in prose.

Answering any of these needed a bigger, realistic, verifiably-answerable item set — which
in turn needed the name roster (§2, methods in §5.2–5.4).

### 1.3 The governing requirement

An earlier design treated the reader's latent knowledge as a confound to subtract via a
no-context baseline. That was abandoned for something simpler and checkable:

> **Every assertion must be backed by a supporting quote, verbatim from the supplied
> context.**

Latent knowledge is not the enemy — the pipeline depends on it to resolve *fetal* vs
*prenatal*, expand abbreviations and read tables. What matters is that conclusions are
traceable. This turns grounding into a substring check and makes the no-context arm a
fabrication test rather than a baseline.

### 1.4 The matrix

**55 items × 6 arms × 2 reader models = 660 reads.**

| arm | backend | query form | context |
|---|---|---|---|
| `blind` | — | — | none (fabrication floor) |
| `whole` | — | — | full narrative text, 9,651 tok (ceiling) |
| `local` | local RRF hybrid | per-axis | 1,901 tok median |
| `local-comb` | local RRF hybrid | compound (production) | ~2k |
| `asta-sep` | ASTA snippet search | per-axis | ~2k |
| `asta-comb` | ASTA snippet search | compound (production) | ~2k |

41 items have evidence in the paper (judge-scored). 14 ask about structure/morphology, which
this paper does not describe: the correct answer is an explicit decline, scored
deterministically.

---

## 2. The item set (summary; methods in §5)

Gopee et al.'s label vocabulary is not in the paper — it is the header row of the
logistic-regression sheets in the supplement: **86 refined labels**, matching the project's
CAS+ document exactly. Of those:

| | labels |
|---|---|
| roster (refined) | 86 |
| named anywhere in text, body **or** figure legends | 46 |
| ≥2 body-prose passages | 20 |
| **usable after reading every passage** | **16** |

Two structural facts drive that attrition, both with consequences beyond this experiment:

- **Abbreviation expansions exist only in figure legends.** `ASDC`, `DC1`, `DC2`, `LC`, `LE`,
  `LTi`, `HSC`, `MEMP`, `pDC` have zero body-prose occurrences; Fig. 1's legend carries a
  literal glossary. Issue #35 correctly stopped legend text being spliced *into* prose, but
  legends must still be indexed separately or the naming vocabulary is lost.
- **Methods is 46% of body text** (43,874 of 94,998 chars) and says nothing about cell types.
  It stays in the retrieval corpus but cannot be cited as evidence.

**Structure is absent by the nature of the source.** Only the hair placode has real
morphological content. This is a transcriptomic atlas — it says where cells are and what they
do, not what they look like. So the report template's `## Structure / Morphology` section
asks for something this source cannot supply, and structure became the run's **absence arm**.

**Grounded naming needs judgement, not pattern-matching.** Mechanically assembling synonym
candidates produced `Macrophage is also referred to as: … lyve1+ macrophage` — a cell type's
own subsets offered as alternative names. A judgement pass over the candidates accepted 26
and **rejected 11** in six kinds (5 subtype, 2 context-variant, 1 each sibling / broader /
distinct-cell-type / not-a-name). Rejections are retained: they are what a later run must not
re-accept.

---

## 3. Results

### 3.1 The matrix

Run 2, `claude-sonnet-5` reader throughout (verified per job file from session transcripts),
Opus 5 judge.

| | blind | whole | local | local-comb | asta-sep | asta-comb |
|---|---|---|---|---|---|---|
| context | none | 9,651 tok | 1,901 tok | ~2k | ~2k | ~2k |
| present items (41) | 0 | 32 | 32 | 27 | 30 | 31 |
| absent items (14) | 14 | 12 | 12 | 12 | 12 | 14 |
| **all (55)** | **14** | **44** | **44** | **39** | **42** | **45** |

Full outcome taxonomy:

| outcome | blind | whole | local | local-comb | asta-sep | asta-comb |
|---|---|---|---|---|---|---|
| `correct` | 0 | 32 | 32 | 27 | 30 | 31 |
| `correct_decline` | 14 | 12 | 12 | 12 | 12 | 14 |
| `honest_miss` (span never retrieved) | 41 | 0 | 2 | 3 | 2 | 4 |
| `miss` (span present, declined) | 0 | 6 | 4 | 8 | 5 | 2 |
| `substituted` (grounded, wrong claim) | 0 | 3 | 2 | 1 | 3 | 2 |
| `overreach` (asserted absent morphology) | 0 | 2 | 2 | 1 | 2 | 0 |
| `leaked` (harness artefact, §3.5) | 0 | 0 | 1 | 2 | 1 | 2 |
| `fabricated` | **0** | **0** | **0** | **0** | **0** | **0** |

### 3.2 The quote requirement holds absolutely

**Zero fabricated quotes in 660 reads, across both reader models.** In the `blind` arm both
readers declined all 55 items and produced no quotes — despite Gopee being a 2024 *Nature*
paper the models have very likely seen, and despite questions like "where are Langerhans
cells found" being answerable from general knowledge.

Requiring a citation converts grounding from an inference about model behaviour into a
substring check, and it works.

It does **not** make answers correct. `substituted` (quote genuine, claim not the paper's)
occurred 11 times across the five context arms. Grounded and correct remain separate
measurements.

### 3.3 Whole paper vs retrieval: a tie at 1/5 the tokens

`whole` 44/55 and `local` 44/55 are identical. Stage 2's equivalence finding reproduces
across 16 cell types and four axes.

Retrieval ceilings, measured before any model call (gold span present in the supplied
context):

| arm | span retrieved | correct on those |
|---|---|---|
| `local` | 34/41 | 28/34 |
| `local-comb` | 34/41 | 24/34 |
| `asta-sep` | 19/41 | 14/19 |
| `asta-comb` | 16/41 | 13/16 |

**The ASTA ceilings understate it.** ASTA serves a different rendering of the same passages
(e.g. `DPYSL2 + ` for `DPYSL2+`), so an exact-substring span check fails even when the content
is present — which is why `asta-comb` scores 45/55 against a nominal 16/41 ceiling. This is
issue #36 observed directly: rendering-dependent quote matching breaks in both directions.
The ceiling column is trustworthy only for the local arms.

### 3.4 Separate vs combined queries: it depends on the backend

| backend | per-axis | compound | Δ |
|---|---|---|---|
| local hybrid | 44 | 39 | **−5** |
| ASTA | 42 | 45 | **+3** |

The production compound query costs the local index five items and costs ASTA nothing. The
rendered query explains why:

```
Macrophage / macrophage in fetal skin: location, structure, function, markers
```

Four defects: the label repeats when the resolved name matches it (9 of 16 labels); `/`
collides with labels containing `/` (`Cuticle/cortex`); the identical four-axis tail is ~40%
of tokens and distinguishes nothing; and it says **"fetal skin"** where the paper says
**prenatal 125 times and fetal 7**. A lexical index is being asked for a word the paper
barely uses. An embedding-based backend is insensitive to that; BM25 is not.

**Markers is the axis that suffers.** Per axis, present items only:

| axis | whole | local | local-comb | asta-sep | asta-comb |
|---|---|---|---|---|---|
| markers (12) | 10 | 8 | **5** | **6** | 8 |
| location (12) | 10 | 10 | 10 | 11 | 10 |
| function (15) | 10 | 12 | 11 | 11 | 11 |
| structure (2) | 2 | 2 | 1 | 2 | 2 |

Location and function are flat across every configuration. Markers spans 5–10. This is the
axis where the paper's prose is thinnest (the real marker evidence is in the DEG tables) and
where retrieval precision therefore matters most.

### 3.5 Reader model dominates retrieval configuration

Run 1 used a different reader. Both runs share items, contexts, reader contract, scoring code
and judge model, so per-arm differences are attributable to the reader.

| arm | Opus | Sonnet | agree | run-1 reader |
|---|---|---|---|---|
| blind | 14 | 14 | **55/55** | opus-5 |
| whole | 51 | 44 | 46/55 | opus-5 |
| local | 49 | 44 | 48/55 | opus-5 |
| local-comb | 47 | 39 | 45/55 | **fable-5** |
| asta-sep | 53 | 42 | 44/55 | opus-5 |
| asta-comb | 48 | 45 | 46/55 | opus-5 |

**Net across all disagreements: Opus 40, Sonnet 6.**

The reader-model spread (up to 11 items on `asta-sep`) exceeds the spread between any two
retrieval configurations (5 items). Sonnet's losses are concentrated in `substituted` and
`overreach` — it answers where Opus declines. Both agreed perfectly on `blind`.

Run 1 is not a clean matrix in its own right (`local-comb` was Fable, the rest Opus) and is
retained only for this per-arm comparison. Model attribution was recovered from session
transcripts after the fact, not from memory, and is recorded per job file.

### 3.6 Failures are concentrated, and some are ours

Three items failed in **both** context arms in run 1 and remain weak: `G04-placode-markers`
(the paper names receptors in a ligand–receptor prediction, not a marker panel),
`G33-caparteriole-markers` (all markers come from an organoid comparison),
`G37-postn-location`. Two of the three were flagged doubtful when authored. **The items are
defective; the declines are correct behaviour.**

`G45` (dermal condensate structure-absent) drew `overreach` in both runs — "aggregation and
encapsulation" offered as morphology. Since the paper calls the dermal condensate "aggregates
of dermal fibroblasts", the `absent` classification is itself arguable.

**Both hazard items scored correct in both runs.** The judge kept `AGR2` (presented as newly
identified) apart from `BARX2`/`SOX9` (explicitly attributed to prior work) — the answer-key
trap that cost four correction cycles in Stage 2 — and attributed `GJA5` to arterioles rather
than capillary arterioles.

### 3.7 Two scoring defects found, both blaming the reader

Continuing the family catalogued in the Stage 3 handoff; like the previous five, both made the
reader look worse than it was.

**Leak scope was too narrow.** Reader agents were each given up to four job files to process
in sequence, so a context supplied for job file 1 was still in the agent's window at job file
3. The leak check scoped to a single batch, so genuine cross-contamination was reported as
**fabrication**. Fixed by scoping to what each agent actually read
(`agent_job_groups.json`). Six reads reclassified.

**Added sentence-final punctuation counted as fabrication.** One reader copied 134 of 135
characters and closed the quote with a full stop. Dropping a trailing period cannot turn a
splice or an invention into a substring, so allowing it does not weaken the check.

Both fixes together moved every `fabricated` read to zero. The initial score reported three
fabrications; none were real.

---

## 4. Discussion and conclusions

**A quote requirement is a stronger control than a baseline subtraction, and it should be the
production contract.** 660 reads, two models, zero fabrications, and a perfect 55/55 decline
rate with no context. This is cheap to enforce and it is checkable without a judge.

**Retrieval buys cost, not accuracy, on a single paper.** A 1.9k slice ties the 9.7k whole
paper. At this size whole-paper reading should be the default for one paper; retrieval earns
its place when the corpus is larger than one paper.

**Query decomposition helps the local index and not ASTA.** −5 items compound vs per-axis on
local, +3 on ASTA. If the pipeline keeps a lexical/hybrid backend, per-axis queries are worth
the extra calls; the compound query's `fetal`/`prenatal` mismatch alone is a reason to fix it.

**Reader model choice outweighs every retrieval decision measured here.** A 40-to-6 net
disagreement between Opus and Sonnet, against a 5-item ceiling on retrieval-configuration
differences. Tuning retrieval while leaving the reader unpinned is optimising the smaller
term — and this run demonstrated the cost of not pinning it (§5.6).

**The report template asks for something this class of source cannot give.** One of 16 cell
types has real morphological content. Structure must come from cited papers or free search;
until then the honest output is an explicit "not found", which both readers produce well
(24–28 of 28 absence items per run).

**Limits.**

- **One paper.** The legend-glossary pattern, the 46% Methods fraction and the absence of
  morphology may be Nature-atlas conventions rather than universals.
- **The denominator is not sound.** Four of 55 items need revising (§3.6). 44/55 is a floor.
- **ASTA ceilings are not measurable with exact substring matching** (§3.3) — #36 blocks this.
- **One judge model** (Opus 5) across both runs. Judge variance is unmeasured.

### 4.1 Recommended next steps

1. **Pin the reader model everywhere**, in production and in tests. This run's largest effect.
2. **Revise the four items** — `G04`, `G33`, `G37` → `absent`; decide `G45`. Expected set:
   ~37 present / 18 absent.
3. **Fix the compound query or decompose it.** At minimum use the paper's own stage
   vocabulary; the `/` separator and repeated label are free fixes.
4. **Index figure legends as their own segments** (follow-up to #35).
5. **Wire grounded synonyms into CAS+** `synonyms` / `cell_fullname` — the slots exist and are
   empty; the project's CAS+ holds 6 annotations against a roster of 86.
6. **Close #36** so quote validation is rendering-aware; without it ASTA-sourced quotes cannot
   be validated soundly in either direction.
7. **Repeat on a second paper** to test whether §2's attrition pattern generalises.

---

## 5. Methods

### 5.1 Paper and corpus

Gopee NH et al. (2024), *A prenatal skin atlas reveals immune regulation of human skin
morphogenesis*, **Nature**, DOI `10.1038/s41586-024-08002-x`. JATS XML at
`experiments/papers/gopee2024.xml`; supplement store (373 MB, gitignored) in the `dev`
worktree.

`experiments/corpus.py` drops `<fig>`, `<supplementary-material>`, `<boxed-text>` and
`<disp-formula>` before serialising each `<p>`, and walks the body recursively in document
order. **Narrative text** is every paragraph through the last `Discussion` section (37
paragraphs); everything after is Methods and is excluded from evidence. Figure legends are
extracted separately from `<fig>`.

### 5.2 Roster extraction — `experiments/roster.py`

CLI taking the paper XML and the two logistic-regression sheets. Labels are each sheet's
header row minus `LR_assignment` and `original_labels` (the latter holds the *other* species'
annotation in these cross-species tables).

Four candidate rules, each recording its span: **legend glossary** (`ABBR, expansion;`, parsed
from unsplit legend text since entries are shorter than any sentence-length floor); **inline
definitions** (`full name (ABBR)`); **qualified forms** (modifiers preceding a bare label, kept
at ≥2 occurrences, participles and non-biological modifiers excluded); **marker hints**
(`label (GENE+)`, allowing one intervening parenthetical so `outer root sheath (ORS)
(SLC26A7+)` is caught).

Matching is word-bounded and **case-sensitive for tokens ≤5 characters containing a capital** —
without that, `LE` pluralised matches inside "cells" and `Matrix` matches "extracellular
matrix". Emits `ambiguous_label` (competing qualified forms) and `collides_with` (labels for
which this one is a trailing phrase; 20 cases, e.g. `Arterioles` ← `Capillary arterioles`).

### 5.3 Synonym grounding — `synonyms_gopee.yaml`

Judgement pass over the candidates. Rules: the primary name is the form the authors use in
running prose, spelled in full; a synonym must denote **the same set of cells** (subset,
sibling, broader class or other experimental system does not qualify); every accepted synonym
carries a verbatim span; nothing accepted on prior knowledge alone.

`synonyms_check.py` validates every span — accepted **and** rejected — against narrative prose
plus figure legends. A null span is allowed only with an explicit non-textual `source`; the
one case is `LYVE1++ macrophage`, whose double-plus appears only in the supplementary roster.

Query clause, omitted entirely when nothing was accepted:

```
{axis question about PRIMARY} (PRIMARY is also referred to as: A, B.)
```

### 5.4 Item authoring — `items_gopee.yaml`

**Questions generated, gold authored.** Questions come from four axis templates plus the
grounded name clause, so phrasing is controlled. Each item carries one explicitly stated
intended `answer` and the verbatim `span` supporting it — never a key derived from prose by
pattern, the Stage 2 failure mode.

`items_check.py` verifies each span is a substring of the **narrative** text (reporting
separately when a span is Methods-only), enforces that `expect: absent` items carry no span
and use `scoring: absence`, that ids are unique and labels are real. Negative-tested against
five injected faults — paraphrased span, Methods-only span, duplicate id, bogus label,
absence item with a span — and caught all five.

Three items carry a `hazard` note recording an easily-inverted distinction: `G31` (AGR2 new vs
BARX2/SOX9 previously reported, in one sentence), `G39` (`Arterioles` vs `Capillary
arterioles` share nearly every sentence), `G04` (receptors in a ligand–receptor prediction,
not a marker panel).

### 5.5 Arms and contexts — `prep.py`, `prep_matrix.py`

Contexts are precomputed to files so reads are reproducible and the same bytes can be checked
for quotes afterwards.

- `whole` — narrative paragraphs with section headings, 9,651 tok.
- `local` / `local-comb` — RRF hybrid (BM25 + MiniLM, `stage1.py:rrf_order`) over narrative
  chunks, packed to 2,000 tok and **restored to document order** so rank order is invisible.
- `asta-sep` / `asta-comb` — ASTA `snippet_search` via `asta_probe.py` against
  `DOI:10.1038/s41586-024-08002-x`, packed in score order to the same budget.
- Compound arms render `CLAUDE.md:142` verbatim, one retrieval per label shared by that
  label's items, using the grounded primary as `resolved_name` (the template's best case).

### 5.6 Readers and model pinning — `READER_PROMPT.md`, `jobs.py`

Readers are Claude Code subagents, each forbidden from reading any file but its own job file
(the answer key sits in the same directory). Contract: answer only from the supplied context;
copy quotes character for character; **never splice** (one continuous run, no ellipsis
bridging); if the context does not answer, `"found": false` with empty `quotes`, stated to be
correct and expected.

**Model pinning.** Run 1 was dispatched without an explicit model, so subagents inherited the
session model — which changed mid-run, producing a run whose reader differs by arm. Run 2
pins `model: sonnet` on every reader and `model: opus` on every judge. Model attribution for
both runs was recovered from session task transcripts (assistant-message `model` fields) and
recorded in `reader_provenance.json` per job file; run 2 is `claude-sonnet-5` on all 38.

**Do not rely on inheritance for anything whose model you will later report.**

Batching: `blind` 28/job, `whole` 14, retrieved arms 7. Items are dealt round-robin by axis —
consecutive slicing put same-label items together, whose retrieved slices overlap heavily.

### 5.7 Scoring — `score.py`

Everything decidable without a model is decided deterministically, and resolved items **never
reach the judge**. Quotes are normalised for whitespace, dash and quote-character drift; a
spliced quote fails automatically since it is not a substring.

| condition | outcome |
|---|---|
| `expect: absent`, declined | `correct_decline` |
| `expect: absent`, answered with valid quote | → judge |
| `expect: present`, declined, gold span **was** in context | `miss` |
| `expect: present`, declined, gold span **was not** in context | `honest_miss` |
| quote absent from own context, present in a context the same agent read | `leaked` |
| quote absent from every context that agent read | `fabricated` |
| quote verbatim in own context | → judge |

This encodes the five handoff rules — no keys from prose; `expect` tested explicitly not by
truthiness; a decline's correctness is group-dependent; grounded ≠ correct; judge-scored items
may not fall through — plus `leaked` and the punctuation allowance from §3.7. `report.py`
asserts nothing remains `pending`.

### 5.8 Judge — `judge.py`

Cases the scorer could not settle, batched to independent Opus 5 subagents. The judge sees the
question, intended answer, reader's answer, reader's quotes (**already verified verbatim**, so
grounding is not its job) and any hazard note. Verdicts: `correct` / `substituted` / `wrong`,
and for absence items `overreach` vs `correct`. **Declines never reach the judge** — asked to
adjudicate one it calls it incorrect for having no answer (handoff rule 3).

### 5.9 Files and reproduction

```
experiments/
  roster.py                     roster + synonym candidate extractor (CLI)
  roster/gopee2024.json         103 labels, spans for every derived name
  stage3b/
    items_gopee.yaml            55 items, authored gold + spans
    items_check.py              span verifier (CLI, exits 1 on fault)
    synonyms_gopee.yaml         27 labels, 26 accepted / 11 rejected
    synonyms_check.py           span verifier + clause renderer (CLI)
    prep.py / prep_matrix.py    questions + contexts for all six arms
    jobs.py                     reader job files (round-robin by axis)
    READER_PROMPT.md            the reader contract
    score.py / judge.py / report.py
    compare_runs.py             cross-run, cross-model comparison
    reader_provenance.json      model per job file, from transcripts
    agent_job_groups.json       what each reader agent actually read
    answers/ verdicts/ contexts/ jobs/
    runs/run1-mixed/            run 1 (Opus/Fable) — retained, see its README
```

```bash
uv run python experiments/roster.py --xml experiments/papers/gopee2024.xml \
    --fine "<store>/Supplementary Table 11.xlsx" \
    --broad "<store>/Supplementary Table 10.xlsx" --out experiments/roster/gopee2024.json
uv run python experiments/stage3b/items_check.py experiments/stage3b/items_gopee.yaml \
    --roster experiments/roster/gopee2024.json
uv run python experiments/stage3b/synonyms_check.py experiments/stage3b/synonyms_gopee.yaml \
    --xml experiments/papers/gopee2024.xml --render
uv run python experiments/stage3b/prep.py --items ... --synonyms ... --out experiments/stage3b
uv run python experiments/stage3b/prep_matrix.py --dir experiments/stage3b   # needs ASTA_API_KEY
uv run python experiments/stage3b/jobs.py --dir experiments/stage3b
# dispatch readers with an EXPLICIT model, then:
uv run python experiments/stage3b/score.py  --dir experiments/stage3b
uv run python experiments/stage3b/judge.py  --dir experiments/stage3b
# dispatch judges, then:
uv run python experiments/stage3b/report.py --dir experiments/stage3b
uv run python experiments/stage3b/compare_runs.py \
    --run1 experiments/stage3b/runs/run1-mixed/final.json --label1 opus \
    --run2 experiments/stage3b/final.json --label2 sonnet
```

---

## 6. References

**Source papers**

- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin
  morphogenesis". *Nature*. DOI: 10.1038/s41586-024-08002-x
- Suo C et al. (2022). "Mapping the developing human immune system across organs". *Science*.
  DOI: 10.1126/science.abo0510 — second corpus paper, used in §5.1 tooling checks only.

**Prior stages**

- `planning/retrieval_stage1_results_2026-08.md` — ranking within a paper, no model calls.
- `planning/retrieval_stage2_results_2026-08.md` — reading, 231 reads, five judge passes.
- `planning/retrieval_stage1_setup_findings_2026-08.md` — ASTA's copy of the paper, JATS gaps.
- `planning/retrieval_test_items_draft_2026-08.md` — the original 57-item set.
- `planning/HANDOFF_stage3_extended_test.md` — the unrun supplement Stage 3, and the five
  scoring rules referenced in §5.7.

**Issues**

- #35 — JATS extraction: legend splicing, body-paragraph order, AAAS references. Merged
  (PR #37). §2 is the follow-up: legends must be indexed, not merely un-spliced.
- #36 — quote validation pools ASTA and PMC renderings. Open; blocks §3.3.
- #30 — rebuild every local snippet index after #23 and #37.
- #13 — high-quality PDF reference extraction.

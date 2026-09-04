# Handoff — resume here: extended supplement-derived test (Stage 3)

**Written 2026-08-27 to end a long session cleanly.** Everything needed to pick this up in a
fresh context is in this file plus the four documents it names. **You should not need the
prior conversation.**

Branch `test/retrieval-matrix`, worktree `../retrieval-matrix`, all work committed (not
pushed). Nothing here is intended to merge except the `planning/` write-ups.

---

## 1. Read these, in this order, then stop reading

| file | what it gives you |
|---|---|
| this file | state, rules, and the Stage 3 design |
| `planning/retrieval_stage1_results_2026-08.md` | ranking inside a paper (no model calls) |
| `planning/retrieval_stage2_results_2026-08.md` | reading — 231 reads, five judge passes |
| `planning/retrieval_stage1_setup_findings_2026-08.md` | ASTA's copy of the paper, JATS parser gaps |
| `planning/retrieval_test_items_draft_2026-08.md` | the 57-item question set, human-readable |

Do **not** re-derive the Stage 1/2 findings. They are settled and the raw data is on disk.

---

## 2. Where things stand

**Stage 1 (ranking, no LLM).** Ranking inside a paper is worth ~10× over reading from the
front. BM25 ≈ MiniLM on medians; both have tails worse than reading the whole paper. RRF
hybrid takes the best median. Keyword-reducing the query changed nothing.

**Stage 2 (reading, 231 subagent reads on quota).** Settled:

- **Fabrication is near-absent** (1 in 231). Absence is reported reliably: 18/18 when the
  passage was genuinely withheld.
- **Local hybrid at ~1,900 tokens reaches 20/21** — the same as the whole 23,700-token paper
  (21/21 sonnet, 20/21 haiku). Retrieval's case is **cost, not accuracy**.
- **ASTA needs ~7,700 tokens to reach 20/21.** Against the real alternative (local text) it is
  ~4× more expensive, not cheaper.
- **A wider window over a lossy copy is dangerous.** A3 declined honestly at 2k and produced a
  sourced, quote-backed *wrong* answer at 8k, because ASTA's copy lacks the paragraph holding
  the true value (6 PCW). New outcome category `substituted` records this. All 9 substitutions
  in the run are on ASTA.
- **Haiku splices quotes** (13 cases: two non-adjacent passages joined, join invented).
  Sonnet: zero. Splices fail `check_quotes` exact matching. Argues against Haiku for evidence
  gathering regardless of cost.
- **Citation-following scored 0/12** — correctly declined, because our corpus strips
  `ref-list`. Not a model limitation.

**Routing rule that follows (implementation, not experiment):** PMC JATS available → local
index + hybrid + ~2k slice. ASTA only → ASTA, budgeted, band recorded. Neither but OA → PDF
path (#13, unmeasured). Whenever we hold the text, using it is cheaper, more accurate, and
the only way quote validation is sound.

---

## 3. Rules learned the hard way — read before writing any scoring code

This session produced **five scoring defects**, every one of which made the readers look
worse than they were, and each cost a correction cycle. The harness fails closed. Assume any
new scorer does too, and check its bias deliberately rather than waiting to notice.

1. **Never derive answer keys from prose gold answers.** A regex harvesting capitalised
   tokens cannot tell an answer from a parenthetical, a label, or an aside. Real failures:
   `ME1`/`ME5` are microenvironment labels, not genes; `BARX2`/`SOX9` are explicitly the
   *previously reported* genes in B4's gold; B13's gold bundled two sentences when only one
   was the marked span; B11 admits two defensible answers. **Give each item one explicitly
   stated intended answer, or route it to a judge from the start.**
2. **`span_present` is tri-state.** `True` = passage supplied, `False` = deliberately
   withheld, `None` = the item has no marked span at all (C/D/F). Treating `None` as `False`
   twice produced wrong labels — correct C answers as "substituted", correct D declines as
   "missed". Always test `is False` / `is None` explicitly.
3. **A decline is not a failure, and its correctness is group-dependent.** Withheld passage →
   correct. D (citation) and F (unanswerable) → correct, they cannot be answered from the text
   we supply. C (synthesis) → a miss. Never let a judge adjudicate a decline; it will call it
   "incorrect" for having no answer.
4. **Grounded ≠ correct.** A quote that is genuinely in the context makes an answer
   *checkable*, not right. Three outcomes must stay separate: `correct`, `substituted`
   (grounded but not the paper's claim), `fabricated` (quote not in context at all).
5. **Judge-scored items must never fall through** to the entity-scoring branches. They did,
   and 10 already-judged-correct answers were reported as wrong.
6. **Batching rule.** Items sharing an identical context (the whole-paper condition) can be
   batched freely. Items with per-item contexts can be batched only with a leakage check
   afterwards (`stage2_leakcheck.py`) — it came back clean across 231 reads, so batching is
   safe *and demonstrated* rather than assumed.
7. **Items must be found by reading, not searching.** If items are located by querying a
   retrieval method, that method wins by construction.

---

## 4. Stage 3 design — extended test from supplementary material

### Why supplements

Two independent reasons, and the second is the one that fixes rule 1:

- **Markers actually live there.** Body text names a handful of genes; the DEG tables carry
  the real marker evidence, and no body-text retrieval method can reach them.
- **Supplement-derived items have unambiguous gold.** "Top five DEGs for LYVE1+ macrophages
  ranked by `scores`" is a table lookup: entity-scorable, no parentheticals, no judge needed.
  That removes the failure mode that cost this session four correction cycles.

### What is already on disk

`projects/test_projects/fetal_skin_atlas/supplements/papers/10.1038_s41586-024-08002-x/`
(on `dev`; files gitignored, ~373 MB local, manifest committed). 50 indexed tables:
8 `deg_results`, 8 `cell_metadata`, 2 `sample_metadata`, 1 `marker_list`,
1 `cluster_annotation`, 1 `legend`, 29 `other`.

Supplementary Table 22 (macrophage subset DEGs) is already characterised in
`retrieval_test_items_draft_2026-08.md` §E, including its three layout hazards: four merged
column blocks, **unequal block lengths** (550/283/82/41 genes), and the ambiguity of "top
markers" (`scores` vs `logfoldchanges` give different answers; `pvals` is derived from
`scores` and saturates at 0).

### Item generation

Target **~40 items over a wider set of Gopee cell types**, covering structure, function and
markers. Two sources, deliberately kept separate:

- **Marker items from tables** (~25). Generated programmatically from the manifest plus the
  tables: subset → top-N by a *named* column, gene rank, effect size, comparison basis, block
  extent. Gold is a table lookup, so it is exact and machine-checkable.
- **Structure/function items from body text** (~15). Generated by a frontier model *reading
  the paper*, but scored by judge, not by entity key — these are prose answers and rule 1
  applies.

**Generation hazard to design around:** a model that generates items from the body text
produces items findable in the body text by construction. Keep the marker items sourced from
supplements (a different artefact from the search space) and, for the body-text items, have
the generator work section-by-section rather than by querying.

Each item carries: `id`, `question`, one intended `answer`, `scoring` (`entities` | `judge`),
source locator (table + block + column, or section + paragraph), and an abstraction `tag`
(`none` / `term` / `entity` / `both`) — the tag is worth keeping, Stage 1 showed abstraction
costs retrieval 3.6× even though Stage 2 found no reading penalty.

### Conditions

The interesting comparison is *how the supplement is delivered*, not how it is ranked:

| condition | what the reader gets |
|---|---|
| `blind` | question only — floor, and a fabrication check |
| `manifest` | the supplement manifest (table labels, descriptions, columns) only |
| `manifest+slice` | manifest, then `cli_supplements slice` on the table it picks |
| `dump` | the whole sheet serialised into context |
| `body_only` | the ~2k local hybrid slice of body text — tests whether body text can substitute for the table at all |

`body_only` is the one that answers a live pipeline question: reports currently cite markers
from body text; this measures what that costs against the actual DEG evidence.

### What it answers

1. Can the supplement store's content pointers locate *and* extract, or only locate?
2. Does `dump` beat `manifest+slice`, and at what token cost? (The 550-row block may not fit.)
3. Does a reader asked for "top markers" state its ranking column, or silently pick one?
4. How much marker evidence is reachable from body text alone?

### Method — reuse, do not rebuild

`stage2_prep.py` → `stage2_jobs.py` → subagents → `stage2_score.py` → `stage2_leakcheck.py`
works and is debugged. Precompute every context to a file, dispatch one job per batch,
score deterministically. Reader rules are in `experiments/stage2/READER_PROMPT.md` (it already
forbids splicing quotes across non-adjacent passages).

Models: Sonnet as the reference reader. Haiku only if a cheap-reader question is being asked
— and if so, check quote fidelity, not just accuracy.

---

## 5. Small fixes that should land before or alongside Stage 3

- **Record which rendering a quote came from.** ASTA and PMC serve different text; a correct
  quote can fail validation and a substituted one can pass. Small schema change, unblocks
  sound validation across routes.
- **Plumb the reference list through to the reader**, and fix `_jats_parser` for AAAS
  `<mixed-citation>` (it silently returns empty references, so a whole publisher class has no
  targeted citation route). Both block the targeted-vs-shotgun traversal experiment.
- **Check the production chunker** for the two extraction bugs found here: figure captions
  spliced into body paragraphs, and body-level `<p>` elements missed by section-only walkers.

---

## 6. File map

```
experiments/
  corpus.py             paper text + chunking shared by all arms
  norm.py               norm / norm_loc (letters-only locator matching)
  stage1.py             ranking arms, cost-to-answer, permutation null
  run_stage1.py         Stage 1 runner            -> results/stage1.json
  stage2_prep.py        precompute contexts+keys  -> stage2/manifest.json
  stage2_jobs.py        batch job generator       -> stage2/jobs/*.md
  stage2_score.py       deterministic scoring     -> stage2/scores.json
  stage2_leakcheck.py   leakage + quote splicing  -> stage2/quote_audit.json
  asta_probe.py         direct ASTA MCP CLI (pre-existing, from #22)
  papers/               gopee2024.xml, suo2022.xml
  stage2/
    manifest.json       42 items: keys, conditions, scoring mode, notes
    contexts/           every context supplied to a reader
    answers/            231 reader outputs
    judge_verdicts*.json  five judge passes
    scores.json         final classified outcomes
    READER_PROMPT.md    the reader contract
```

Run from the worktree with `uv run python experiments/<script>.py`.
`uv sync --extra local-index --extra supplements` if starting clean.

## 7. Open questions this handoff does not settle

- Targeted vs shotgun citation traversal — blocked on the reference-list fixes above. The
  measure that matters is **attributability** (can the quote be tied to the claim it was
  fetched for), not recall.
- Whether ASTA's missing-opening-paragraphs pattern generalises beyond Gopee — needs a third
  JATS paper; Suo is a poor test because ASTA serves a different version of it.
- Whether the synthesis step is where unsourced prose enters. Stage 2 rules out the reading
  step; the audit found 60% of fetal-skin reports had unsourced sections. **This is the
  highest-value unrun measurement** and is independent of Stage 3.

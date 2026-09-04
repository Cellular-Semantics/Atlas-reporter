# Restart here — Stage 3b retrieval matrix (written 2026-09-01)

Scratch file at repo top level. **Not for commit** — delete once folded into
`planning/`. Worktree `../retrieval-matrix`, branch `test/retrieval-matrix`,
level with `origin/dev` at `495d755`.

Another agent is also working in this worktree (`experiments/citation_traversal/`,
`planning/citation_traversal/`, `planning/README.md` are theirs, not mine).

---

## 1. Read this first

`planning/retrieval_stage3b_results_2026-08.md` — the full write-up, structured as
Abstract / Intro / Results / Discussion / Methods / Refs. **Everything below is a
pointer into it; do not re-derive.**

---

## 2. What was done

Built a grounded name/synonym roster for Gopee et al. 2024, authored 55 items over
16 cell types and 4 axes from it, and ran the full retrieval matrix twice.

**Run 2 (Sonnet reader, Opus judge) — the headline result:**

| | blind | whole | local | local-comb | asta-sep | asta-comb |
|---|---|---|---|---|---|---|
| context | none | 9,651 tok | 1,901 tok | ~2k | ~2k | ~2k |
| **all (55)** | **14** | **44** | **44** | **39** | **42** | **45** |

- Zero fabricated quotes in 660 reads across both runs; 55/55 declines with no context.
- Whole paper ties a 1.9k slice.
- Per-axis vs compound query: −5 on local index, +3 on ASTA.
- **Reader model beat every retrieval choice: Opus vs Sonnet net 40–6.**

---

## 3. State on disk

```
experiments/roster.py, roster/gopee2024.json     name+synonym extractor & output
experiments/stage3b/                             run 2 (Sonnet) — current
experiments/stage3b/runs/run1-mixed/             run 1 (Opus/Fable) — KEEP, has README
planning/retrieval_stage3b_results_2026-08.md    the write-up
```

**Nothing is committed.** All of the above is untracked.

---

## 4. Hard-won rules — read before touching the scorer

Seven scoring defects have now been found across Stages 2 and 3b. **Every one made the
reader look worse than it was.** Assume the next one does too.

1–5 are in `HANDOFF_stage3_extended_test.md` §3 (no keys from prose; `span_present` is
tri-state; a decline's correctness is group-dependent; grounded ≠ correct; judged items
must not fall through). Two new ones:

6. **Leak scope is the reader agent, not the job file.** Agents were given up to 4 job
   files each, so context from file 1 is still in the window at file 3. Scoping the leak
   check to one batch reported real cross-contamination as *fabrication*. See
   `agent_job_groups.json` and `score.py:batch_siblings`.
7. **Added sentence-final punctuation is not fabrication.** A reader copied 134 of 135
   chars and closed the quote with a full stop. `score.py:in_context` allows a trailing
   `.,;:` — this cannot turn a splice or invention into a substring, so the splice check
   is unaffected.

**And the one that cost real money:**

8. **Always pin `model:` on every subagent.** Run 1 was dispatched without it, inherited
   the session model, the session model changed mid-run, and the result was a matrix whose
   reader differed by arm — plus an unexpected credit spend. Model is recovered from
   session transcripts into `reader_provenance.json`; run 2 is `claude-sonnet-5` on all 38
   job files. Never report a model you did not pin.

---

## 5. Known-defective items — fix before quoting 44/55

44/55 is a **floor**, not a benchmark. Four items are wrong (write-up §3.6, §4):

| item | problem | fix |
|---|---|---|
| `G04-placode-markers` | "markers" are receptors in a ligand–receptor prediction | → `absent` |
| `G23-fibroblast-markers` | broad label; paper only gives subset markers | → `absent` |
| `G33-caparteriole-markers` | all markers come from an organoid comparison | → `absent` |
| `G45` / `G55` structure-absent | `G41` uses "part of the inner layers of the HF" as *location* gold, while the same sentence scores as `overreach` on structure | state the location/morphology boundary in the item |

`G04` and `G23` failed in all five context arms and the readers' declines were **more
precise than the gold**. The test caught the authoring, not the reader.

Expected after revision: ~37 present / 18 absent.

---

## 6. Where the drill-down got to (not yet in the write-up)

The write-up has aggregate numbers; §3 needs worked examples adding. What the case
analysis found:

**Substitution has one mechanism.** Every `substituted` read quoted something true,
verbatim and on-topic that was not the asked-for claim. More context supplies more true
things to pick wrongly from — which is why `whole` does not beat a 1.9k slice
(`G03-placode-function`, `G25-fibroblast-function` are the clean examples).

**Opus's 40–6 margin is one behaviour, not general quality.** Sonnet answers the question
a *sentence* answers; Opus answers the question the *passage* answers. Same behaviour
produces both of Sonnet's opposite-looking failure modes:
- over-declines on present items (13 miss + 7 honest_miss) when the evidence lacks a
  functional verb — `G32`: position on a differentiation trajectory *is* the function;
- over-asserts on absence items (4 overreach) when a lexically adjacent sentence exists —
  `G55`: offers "part of the inner layers" as morphology; Opus explicitly names it as
  location, not structure.

Concentrated in **function (19 of 40)** and on the most fragmented contexts (11 asta-sep,
9 local-comb). 4 of the 40 are `leaked` (harness), so the honest margin is **36**.

Sonnet produced **zero fabrications and zero splices** — it is scrupulous about quotes and
conservative about inference. This does not contradict Stage 2's "Haiku splices".

**ASTA's marker weakness is a corpus problem.** ASTA's index includes Methods; ours
excludes it. `G20-lyve1-markers` on asta-sep answered from an antibody-panel methods line.

---

## 7. Next actions, in order

1. **Add worked examples to the write-up §3** — the user asked for explicit queries and
   results; §6 above has the material, it just needs writing in.
2. **Fix the four items**, then re-score (no new reads needed for 3 of them — they are
   reclassifications; `G45`/`G55` need a judge re-run).
3. **Commit.** Nothing is committed yet. Only `planning/` is intended to merge.
4. Unrun, in priority order: pin the reader model in production; fix or decompose the
   compound query (`fetal` vs `prenatal`, `/` separator, repeated label); index figure
   legends as their own segments (#35 follow-up); wire synonyms into CAS+ `synonyms` /
   `cell_fullname`; close #36 so ASTA quotes can be validated at all; repeat the roster
   extraction on a second paper.

---

## 8. Reproduce

```bash
cd /Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix
uv run python experiments/stage3b/score.py  --dir experiments/stage3b
uv run python experiments/stage3b/report.py --dir experiments/stage3b
uv run python experiments/stage3b/compare_runs.py \
    --run1 experiments/stage3b/runs/run1-mixed/final.json --label1 opus \
    --run2 experiments/stage3b/final.json --label2 sonnet \
    --provenance experiments/stage3b/runs/run1-mixed/reader_provenance.json
```

Full pipeline (incl. ASTA retrieval, needs `ASTA_API_KEY`) is in the write-up §5.9.

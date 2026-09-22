# Subatlas overlap measures: one naming, one home — and what that changes in routing

**Date:** 2026-09-22 · **Branch:** `feature/subatlas-routing` (PR #73) ·
**Depends on:** `planning/subatlas_registry_hca_reproductive_2026-09.md`

## Context

The same three divisions have now been written three times, under three sets of
names, each time with its own way of finding a denominator:

| | `feature/subatlas-consistency` | `feature/subatlas-scoring` | `feature/subatlas-routing` |
|---|---|---|---|
| precision side | `within_source_share` | `purity` | `share_of_contribution` |
| recall side | `reverse_share` | `fraction_of_subatlas_set` | `share_of_subatlas_label` |

None of the three is on `dev`. What *is* on `dev` is half the raw material:
`TransferredAnnotation.subatlas_contribution_cells` is populated on all 7,488
transfers of the reproductive atlas, and `SubatlasPaper.cell_sets[]` is defined
in the schema and populated nowhere.

This settles the naming, moves the measurements into CAS+ where the counts
already live, and takes the arithmetic out of routing.

---

## The measures

One row is: atlas cell set **A**, contributing study **S**, and S's own label
**L** for some of the cells in A.

| Field | Numerator | Denominator |
|---|---|---|
| `share_of_subatlas_contribution` | cells in A from S carrying L | cells in A from S, whatever S called them |
| `share_of_subatlas_label` | " | cells S labelled L anywhere in the atlas |
| `share_of_atlas_cell_set` | " | cells in A, from any source |

Each is named after what it divides by, because which denominator is meant is
the only thing anyone ever gets wrong about these. Each says `atlas` or
`subatlas` explicitly.

### The worked example

Every quantity a different order of magnitude, so nothing can be quietly
confused for anything else. **Use these numbers verbatim** in the schema field
descriptions, `docs/subatlas_measures.md`, the routing agent's prompt and the
test fixtures — one example everyone recognises beats four correct ones.

> The atlas integrates subatlas cell set `fu`. **500** of its cells reach the
> atlas. **120** of those go into the atlas cell set `bar`. `bar` holds
> **4,000** cells, **150** of which came from that subatlas.
>
> - `share_of_subatlas_contribution` = 120/150 = **0.80** — of what they put here, this much is `fu`
> - `share_of_subatlas_label` = 120/500 = **0.24** — of their `fu`, this much came here
> - `share_of_atlas_cell_set` = 120/4000 = **0.03** — of `bar`, this much is `fu`

### No F1

The old design gated on the harmonic mean of the first two. The reference case
is the argument against it: for `Endo_ven_apcv`, the cell set the atlas named
after Ulrich 2024's `aPCV`, that label ranks seventh of eight on F1 while
Weigert's `endothelial cell` tops the list — pure because it is uninformative.
One number folds both denominators back together and hides the thing worth
seeing. Both shares are recorded; ordering is by overlap cells; ranking is the
agent's.

---

## Decisions

### 1. Counts come from `obs`, never from summing over the hierarchy

`subatlas_routing.py` currently derives `share_of_subatlas_label`'s denominator
when the registry is absent, by finding a set of cell sets that covers the atlas
once and summing `cell_count` across it. It produces a number indistinguishable
from a counted one that is only as good as the partition behind it.

**Delete it**: `_covering_cell_sets`, `_labelset_totals`,
`subatlas_label_totals`'s derivation path, the `subatlas_label_totals` basis
block on the table, and the partition tests. Where the denominator is absent,
omit `share_of_subatlas_label`, say so on the table, and rank on the other
number — the behaviour the table already has for that case.

The consequence is deliberate: until a project's registry is populated, routing
has only the precision side. That is the correct incentive.

### 2. The measurements live in CAS+, written by the pass that has the counts

All three ratios go on the transferred annotation, beside the counts they divide:

```json
{
  "transferred_cell_label": "aPCV",
  "source_labelset": "celltype_Ulrich2024",
  "source_taxonomy": "DOI:10.1073/pnas.2404775121",
  "cell_count": 37,
  "subatlas_contribution_cells": 332,
  "subatlas_label_total_cells": 2402,
  "share_of_subatlas_contribution": 0.1114,
  "share_of_subatlas_label": 0.0154,
  "share_of_atlas_cell_set": 0.0076
}
```

Storing a number that is one division away from its neighbours needs a reason.
It is the same reason `cell_ratio` is already stored: the file is read directly,
by people and by agents, and a ratio you have to compute is a ratio nobody
checks. The risk in storing it is not drift — nothing prunes transfers — but
staleness across passes, since `subatlas_label_total_cells` arrives from the
registry after `cell_count` arrives from the cell table.

So, two rules, and the second is what makes the first safe:

- **A ratio is written by the pass that writes its denominator.** No provisional
  ratios; absent until computable.
- **`check_cas_annotation.py` recomputes all three on write** and rejects a
  mismatch beyond rounding tolerance. Extend the existing hook rather than
  adding another — it already fires on `cas.json`.

**Settled (PR #74): `cell_ratio` keeps its name.** The rename to
`share_of_atlas_cell_set` was recommended here and then dropped, because
`cell_ratio` appears in two places — on a transferred annotation and on a
composition value — meaning the same thing in both. Renaming one breaks that
parallel and renaming both drags composition into a change that has nothing to
do with subatlas measures. Its description now says outright that it is the
third measure; the explicit name lives in the routing table, where the three
sit side by side. `cell_count` and `subatlas_contribution_cells` keep their
names too.

**Landed in PR #74**, so §2 above is done: the three fields, the worked example
in the schema descriptions and the good fixture, `check_cas_annotation.py`
recomputing all three on write, and `docs/subatlas_measures.md`.

### 3. Routing stops doing arithmetic

With the measures in CAS+, `subatlas_routing.py` carries them through rather
than computing them. What it does becomes exactly: resolve the request, apply
the floor and the synonym exemption, invert to (paper, label), and account for
everything left over.

That gives a clean three-way split — CAS+ measures, the table selects and
arranges, the agent judges — and it is worth stating in the module docstring,
because the temptation to recompute "just this one" will recur.

### 4. The table grows a papers block and loses its repetition

Paper identity is currently repeated on every question: 20 questions for one
study carry 20 copies of its title, author, year and band. The fibroblast run
comes to 185 KB (~46k tokens) largely on that account.

```json
"papers": [
  {
    "subatlas_paper": "DOI:10.1073/pnas.2404775121",
    "doi": "10.1073/pnas.2404775121",
    "first_author": "Ulrich", "year": 2024, "title": "…",
    "status": "local", "asta_band": "full_text",
    "cells_contributed": 41207,
    "n_atlas_cell_sets_reached": 31,
    "n_questions": 12
  }
]
```

Questions refer to a paper by `subatlas_paper` and carry no identity of their
own. The per-paper totals are new information the agent cannot currently see,
and they are what it is actually ranking.

Also:

- **Requested cell sets gain `children` and `context`** (tissue, developmental
  stage), both already assembled by `subject_block.py`. Most of the discordant
  cases turn on telling "the atlas subdivides this" from "the study subdivides
  this", and `children` is what makes the first visible.
- **The atlas paper is named on the table.** It is always in scope, and
  `atlas_only` should be a positive statement in the plan rather than an
  inference from an absence.
- **`dropped` stays rolled up per paper.** A per-cell-set version is a much
  bigger table answering a question nobody has asked; the cell sets where it
  matters most already carry `overlap_cells_dropped` through `atlas_only`.

---

## What gets changed

### Schemas

**`cas_annotation.schema.json`** — add to `TransferredAnnotation`:
`subatlas_label_total_cells`, `share_of_subatlas_contribution`,
`share_of_subatlas_label`; rename `cell_ratio` to `share_of_atlas_cell_set` if
that is agreed. Every field description carries the worked example's terms.

**`subatlas_routing_table.schema.json`** — add `papers[]` and `atlas_paper`;
move identity fields off `Question`; add `children` and `context` to
`RequestedCellSet`; drop `subatlas_label_totals`; rename the claimant fields.

**`subatlas_routing_plan.schema.json`** — unchanged.

### Code

- `services/subatlas_routing.py`: delete the derivation, carry the stored
  measures through, build the papers block, take `children`/`context` from
  `subject_block.build`.
- `.claude/hooks/check_cas_annotation.py`: recompute the three ratios.
- `.claude/agents/route-subatlas-papers.md`: the new names, the worked example,
  and the note that an absent `share_of_subatlas_label` means the project's
  registry is not populated — not that the label went nowhere.

### Docs

- **`docs/subatlas_measures.md`** — new, short: the three measures, the worked
  example, why no F1, why counts come from `obs`. The one place to re-read.
- `docs/pipeline.md` §5b — rewritten for the new split, and §1 for the stored
  measures.

### Tests

Delete: partition discovery, the derived-denominator path, the degraded-basis
assertions.

Change: every assertion naming the old field names.

Add:
- the three ratios read from CAS+ rather than computed;
- `share_of_subatlas_label` absent, and said to be absent, when the registry is
  not populated;
- `check_cas_annotation` rejects a hand-altered ratio, accepts a correct one;
- the papers block: one entry per study, totals correct, no identity left on
  questions;
- the `aPCV` regression against the real numbers — `cell_count` 37,
  `subatlas_contribution_cells` 332, `subatlas_label_total_cells` 2402,
  included by synonym rather than by size.

---

## Order of work

1. The registry on `HCA_reproductive_atlas_v1` (separate plan). Nothing here can
   be tested end to end without it, since the second denominator does not exist
   yet on any project.
2. Schema changes and the recompute hook.
3. The routing service and table.
4. Agent prompt, docs, tests.

---

## Verification

```bash
uv run pytest -m unit --cov
uv run ruff check src/ tests/ && uv run mypy src/

uv run python -m atlas_chat.cli_route \
  --cas projects/test_projects/hca_reproductive/cas.json \
  --accession HCArepro:L4:0204 --out /tmp/routing_table.json
```

Then by hand:

- `Endo_ven_apcv` shows Ulrich 2024's `aPCV` at 37 cells, 0.111 of that study's
  contribution and 0.015 of their label, kept by the synonym exemption, with
  Weigert's `endothelial cell` above it on cells and below it on the second
  share.
- The fibroblast selection (69 cell sets) still comes to ~75 questions, and the
  table is materially smaller than 185 KB once paper identity is deduplicated.
- A project with no registry produces no `share_of_subatlas_label` anywhere and
  says why, rather than deriving one.
- Hand-alter one stored ratio in a `cas.json` and confirm the hook rejects it.

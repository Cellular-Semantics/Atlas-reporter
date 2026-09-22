# Subatlas overlap measures

An atlas built by integrating other studies inherits most of its cells, and
often its names, from those studies. CAS+ records that per cell set: for each
contributing study, which of *that study's* labels the cells carried, and how
many.

Three ratios describe one such overlap. They are easy to confuse, and the
confusion is always the same one — **which denominator?** — so each is named
after what it divides by.

## The three

One row is: atlas cell set **A**, contributing study **S**, and S's own label
**L** for some of the cells in A.

| Field | Numerator | Denominator | Reads as |
|---|---|---|---|
| `share_of_subatlas_contribution` | cells in A from S carrying L | cells in A from S, whatever S called them | of what they put here, this much is L |
| `share_of_subatlas_label` | " | cells S labelled L anywhere in the atlas | of their L, this much came here |
| `cell_ratio` | " | cells in A, from any source | of A, this much is L |

`cell_ratio` is the odd one out in name only: it is `share_of_atlas_cell_set`,
and the routing table surfaces it under that name. It keeps its CAS+ name
because `CompositionValue.cell_ratio` divides the same way and breaking that
parallel would cost more than it buys.

## The worked example

Every quantity a different order of magnitude, so nothing can be quietly taken
for anything else. These same numbers appear in the schema descriptions, the
routing agent's prompt and the test fixtures.

> The atlas integrates subatlas cell set **`fu`**. **500** of its cells reach
> the atlas. **120** of those go into the atlas cell set **`bar`**. `bar` holds
> **4,000** cells, **150** of which came from that subatlas.

| | | |
|---|---|---|
| `share_of_subatlas_contribution` | 120/150 | **0.80** |
| `share_of_subatlas_label` | 120/500 | **0.24** |
| `cell_ratio` | 120/4000 | **0.03** |

## What the combinations mean

| | `share_of_subatlas_label` high | low |
|---|---|---|
| **`share_of_subatlas_contribution` high** | the same population under two names | the atlas cell set absorbed this label along with others from the same study |
| **low** | the atlas split the study's label; this is one piece | partial overlap, usually a boundary between neighbouring populations |

The bottom-left is the common and useful case: the honest finding for a report
is frequently that the contributing study did not draw the distinction the atlas
draws.

## Why `cell_ratio` alone is not enough

Its denominator is the whole cell set, most of which came from studies that
never saw these cells. A low value can mean "this study barely contributed" or
"this study contributed a great deal and smeared its labels across the cell
set", and those call for opposite decisions.

## Why there is no F1

Folding the first two into one number puts back exactly the ambiguity they were
separated to remove. The reference case: `Endo_ven_apcv` on the HCA reproductive
atlas is named after Ulrich 2024's `aPCV`, and on F1 that label ranks *seventh
of eight* — beaten by another study's `endothelial cell`, which scores well by
being too generic to disagree with anything. Both shares are recorded; ranking
is a judgement made against them, not a sort.

## Where the numbers come from

**Counts come from the per-cell table**, never from summing over a set of cell
sets that covers the atlas. Such a sum is only as good as the partition behind
it and produces a number indistinguishable from a counted one. On atlases where
both are possible they agree exactly — which is what makes the shortcut
tempting, and why the rule is worth stating.

The ratios are **stored** in CAS+ rather than computed on read, so the file can
be read directly without arithmetic. Two rules make that safe:

- a ratio is written by the pass that writes its denominator — no provisional
  values, absent until computable;
- `.claude/hooks/check_cas_annotation.py` recomputes all three on write and
  rejects any that disagree beyond rounding.

`subatlas_label_total_cells` comes from a later pass than `cell_count`, since it
needs the contributing-study registry. A transfer that has not reached that pass
carries no `share_of_subatlas_label`, and that is not an error.

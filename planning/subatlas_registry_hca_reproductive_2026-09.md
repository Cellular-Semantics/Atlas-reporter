# Populating the subatlas registry on the reproductive atlas

**Date:** 2026-09-22 · **Runs on:** `origin/HCA_reproductive_atlas_v1` ·
**Unblocks:** `planning/subatlas_measures_and_routing_revision_2026-09.md`

## What is missing

`projects/HCA_reproductive_atlas_v1/cas.json` has no `source.subatlas_papers`.
Its own README already names this as the gap:

> `source.subatlas_papers` is not populated — contributing studies are
> identified per entry by `source_labelset` (the obs column, e.g.
> `celltype_Ulrich2024`) and `source_taxonomy` (a DOI). Anything needing the
> registry, or `SubatlasPaper.cell_sets[]` as the `fraction_of_subatlas_set`
> denominator, has to add it. Both are direct counts from the parquet.

Two things follow from that absence. `share_of_subatlas_label` has no
denominator on any project, so nothing downstream can say whether a
contributing study's label mostly went to the cell set that borrowed its name.
And the routing agent is handed bare DOI strings where it is expected to bring
knowledge of the papers to bear.

## Inputs, all present

`projects/HCA_reproductive_atlas_v1/h5ad_obs/obs.categoricals.parquet` is
committed on that branch — 2.24M cells, 65 columns, pulled by `pull_obs.py`
over HTTP range reads from the Sanger share. **The parquet is enough; the pull
does not need repeating** (it wants the Sanger VPN and ~7 minutes).

One obs column per contributing study, already the labelset name on every
transfer:

| obs column / `source_labelset` | `source_taxonomy` | distinct labels | % of cells labelled |
|---|---|---|---|
| `celltype_GarciaAlonso2021` | `DOI:10.1038/s41588-021-00972-2` | 15 | 3.6 |
| `celltype_GarciaAlonso2022` | `DOI:10.1038/s41586-022-04918-4` | 22 | 8.3 |
| `celltype_HECA` | `DOI:10.1038/s41588-024-01873-w` | 36 | 6.7 |
| `celltype_Lardenois2026` | `DOI:10.1016/j.devcel.2025.09.011` | 19 | 2.8 |
| `celltype_Lorenzi2025` | `DOI:10.1038/s41586-025-09875-2` | 48 | 13.5 |
| `celltype_OvarySanger2026` | *Sanger (newly generated; no DOI)* | 80 | 15.3 |
| `celltype_Ulrich2022` | `DOI:10.1016/j.devcel.2022.02.017` | 12 | 2.2 |
| `celltype_Ulrich2024` | `DOI:10.1073/pnas.2404775121` | 39 | 5.2 |
| `celltype_Weigert2025` | `DOI:10.1038/s41467-024-55440-2` | 12 | 4.6 |

So the study-to-publication mapping is already in the data. The registry is
mostly a matter of lifting it somewhere it can be read once rather than
rediscovered per transfer, and attaching the counts and the bibliographic
detail.

## Two passes, deliberately separate

They have different characters and different failure modes, and the ingest
convention is iterative enrichment anyway.

### Pass 1 — counting, from the parquet

Per study column, a value count. Nothing else.

```
label                = the obs column name, verbatim       e.g. "celltype_Ulrich2024"
cell_sets[]          = {source_labelset, cell_label, n_cells} per distinct value
total_cells          = cells with any value in that column
```

`cell_sets[].n_cells` is the denominator for `share_of_subatlas_label`. It is a
count of cells from that source cell set **present in the atlas**; where the
integration subsampled its source this is not the published cell set's size, and
the schema description should keep saying so.

Then, in the same pass, write onto every transferred annotation:
`subatlas_label_total_cells`, and the three ratios (see the measures plan).
Same pass, because that is the rule that keeps a stored ratio honest.

**Never sum `cell_count` over a set of cell sets to get these.** The hierarchy
happens to validate on this atlas, which is exactly what makes the shortcut
tempting and its result indistinguishable from a counted one.

### Pass 2 — resolving, per study

`doi` is already in `source_taxonomy` for eight of the nine; strip the `DOI:`
prefix. The rest — `first_author`, `year`, `title`, `venue` — comes from
resolving that DOI. `services/subatlas_resolver.py` on `dev` has the discovery
half; there is no CLI.

`celltype_OvarySanger2026` has no publication. It gets a registry entry with
`status: "unresolved"` and no `doi`: an entry saying "this is a real contributor
with nothing to read" is worth more than an absence, and at 15.3% of cells it is
the single largest contributor. Routing already reports it as a ceiling on what
reading can reach.

`status` and `asta_indexing.band` can be left for a later pass — they are about
reachability of text, not about the atlas.

## Consistency checks before anything is copied down

Ordered by how much they would cost to get wrong:

1. **Every `(source_labelset, transferred_cell_label)` pair on a transfer has a
   matching `cell_sets[]` entry.** A missing one means the join key is not what
   we think it is.
2. **`sum(cell_count)` over any set of cell sets covering the atlas once equals
   `cell_sets[].n_cells`** for that label. This is the check the shortcut would
   have been; run as a check it is worth a lot, and on this atlas the hierarchy
   leaves and L1 and L2 all cover 100% of cells, so it can be run three ways.
3. **`subatlas_contribution_cells` reproduces** from the parquet for every
   transfer — the README claims 0 mismatches across all 7,488 today, and the
   regeneration must not break that.
4. **Each ratio recomputes** from its own two counts.
5. **`total_cells` equals `sum(cell_sets[].n_cells)`** per study.

### The row to eyeball

`Endo_ven_apcv` (`HCArepro:L4:0204`, n=4851, synonym `aPCV`), Ulrich 2024:

| label | `cell_count` | `subatlas_contribution_cells` | `subatlas_label_total_cells` |
|---|---|---|---|
| `Capillary` | 197 | 332 | |
| `tPCV` | 73 | 332 | |
| `aPCV` | 37 | 332 | **2401** |

The first three columns are what is in the file today. 2401 is the number this
work adds, and it is the one that says Ulrich's aPCV cells mostly went
somewhere else — the finding that the whole exercise exists to surface.

## Copying down

`test_projects/hca_reproductive/cas.json` is copied byte-identical from the
maintenance branch, and its README says so. That claim is what makes the test
project trustworthy, so re-establish it rather than editing the copy: regenerate
on `HCA_reproductive_atlas_v1`, copy, re-run the schema validation, and update
the README's "what was checked" section with the new counts.

`obs.categoricals.parquet` stays on the maintenance branch — it is 2.24M rows
and nothing in the test project needs it.

## Risks

- **Regenerating `cas.json` risks disturbing what is already correct.** The
  README's independent re-derivation (0 mismatches on `n_cells`, `cell_count`,
  `cell_ratio`, `subatlas_contribution_cells`) is the baseline; a diff of the
  regenerated file against the current one should show only additions, plus the
  `cell_ratio` rename if that is agreed.
- **`celltype_HECA` is a consortium column, not a first-author study.** Its DOI
  resolves to a publication, but the registry `label` is the obs column and the
  two will not look alike. That is the point of keeping `label` verbatim.
- **Two 2026 DOIs** (`Lardenois2026`, and the atlas itself) may be preprints
  whose metadata is thin. Record what resolves and leave the rest absent rather
  than filling it in from the label.

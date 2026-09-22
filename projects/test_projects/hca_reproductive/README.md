# test_projects/hca_reproductive

`project = "test_projects/hca_reproductive"`

The HCA pan-organ female reproductive atlas — Cohen et al. (2026), bioRxiv
`10.64898/2026.06.10.731198`. 2,235,448 cells, 291 donors, 27 datasets, five organs
(ovary, fallopian tube, uterus, cervix, vagina) across the lifespan.

It is here because it is the only project with real **joint** integration provenance:
303 of its 312 cell sets carry `transferred_annotations` — 7,488 entries across 9
contributing studies, with ratios reaching down to 0.0002. That long tail is what any
contributor cutoff has to survive.

## Where `cas.json` came from

Copied verbatim (byte-identical) from `projects/HCA_reproductive_atlas_v1/cas.json` on
branch `origin/HCA_reproductive_atlas_v1`, which is where it is maintained. It was built
there from the atlas h5ad `obs` (2.24M cells × 66 columns, pulled obs-only over HTTP
range reads) plus the authors' supplementary tables, then enriched in place by
`scripts/subatlas_registry.py` with `source.subatlas_papers` and the measures that
depend on it.

That pass edits rather than rebuilds, on purpose: **re-running `build_cas.py` renumbers
311 of the 312 `cell_set_accession`s.** The accession index is node insertion order, and
the committed file predates the `sorted(objcodes)` fix that made that order stable —
`Endo_ven_apcv` moves from `HCArepro:L4:0204` to `HCArepro:L4:0011`. Anything citing an
accession (these docs, the reports, the routing plans) breaks silently. Treat a full
rebuild as an accession-minting event, not a refresh.

Validates against `cas_annotation.schema.json` with 0 errors, on a checkout carrying
PR #74 — the three overlap-measure fields it adds to `TransferredAnnotation` are what
the registry pass writes.

## What was checked before copying

Every count re-derived independently from the source `obs` parquet. Across all 312
annotations and all 7,488 transferred entries: **0 mismatches** on `n_cells`,
`cell_count`, `cell_ratio` and `subatlas_contribution_cells`, with no entry missing and
none spurious.

The subatlas registry pass (`scripts/subatlas_registry.py` on the atlas branch) adds
`source.subatlas_papers` and the two measures it is the denominator for, and re-runs
five checks over the result — all passing:

| Check | Scope |
|---|---|
| Every `(source_labelset, transferred_cell_label)` has a `cell_sets[]` entry | 7,488 transfers |
| `sum(cell_count)` over a covering set equals `cell_sets[].n_cells`, run three ways (leaves, L1, L2) | 849 (covering, label) sums |
| `subatlas_contribution_cells` reproduces from the parquet | 7,488 transfers |
| Each stored ratio recomputes from its own two counts | 22,464 ratios |
| `total_cells` equals `sum(cell_sets[].n_cells)` | 9 studies |

The registry is never used to *derive* a count: summing `cell_count` over a covering set
of cell sets produces a number indistinguishable from a counted one and only as good as
the partition behind it. Run as a check instead, on an atlas where three independent
partitions exist, it is worth a lot.

## Shape worth knowing

- **`cell_label` is the author's verbatim code; `cell_fullname` is the long name.**
  `Endo_ven_apcv` / `Activated post-capillary venous endothelial`.
- **The join key to `obs` is the `celltype_HCA_fine` code**, but it is mostly *implicit*:
  `composition.celltype_HCA_fine` survives on only **2** annotations, the merged-code
  leaves, because the composition prune drops a cell-type entry that merely restates its
  cell set. Everywhere else the code is `cell_label` itself (208 leaves), or named in the
  `comment` of a minted generic leaf (13), with internal nodes the union of the leaves
  below them. `codes_by_accession()` in `scripts/subatlas_registry.py` reconstructs it and
  asserts the result is bijective with the 212 codes in `obs`.
- **Three sets of cell sets each cover 100% of cells** — the 210 leaves, the 9 L1 sets and
  the 33 L2 sets — so any of them is usable as a partition, and a claim can be checked
  three ways. L3 and L4 do *not* cover the atlas (they sum to 2,203,505 and 1,916,341 of
  2,235,448); the hierarchy is ragged and a code may terminate above L4.
- **Labelsets L1–L4 are the master nomenclature** from `cell_ontology_mapping.xlsx`,
  ranks 3→0. Note this is a *third* hierarchy: not the obs clustering tiers
  (`celltype_HCA_lineage ⊃ _broad ⊃ celltype_HCA ⊃ _fine`) and not the obs nomenclature
  tiers (`ontology_level1–4`). See `notes/ANNOTATION_HIERARCHIES.md` on the atlas branch.
- **`source.subatlas_papers` is populated** — 9 studies, 283 cell sets, 1,387,388 labelled
  cells. `label` is the obs column verbatim (`celltype_Ulrich2024`), which is also the
  `source_labelset` on every transfer and the key everything joins on; it will not always
  look like the `first_author` beside it (`celltype_HECA` resolves to Marečková 2024).
  `cell_sets[].n_cells` counts cells from that source cell set **present in the atlas** —
  where the integration subsampled its source, that is not the published cell set's size.
  `celltype_OvarySanger2026` is newly generated Sanger data with no publication: it
  carries `status: "unresolved"` and no `doi`, and at 15.3% of cells it is the single
  largest contributor, so it is a standing ceiling on what reading papers can reach.
- **Every transfer carries all three overlap measures.** `share_of_subatlas_contribution`
  and `cell_ratio` come from the cell table; `share_of_subatlas_label` divides by
  `subatlas_label_total_cells`, which is what the registry made possible. See
  `docs/subatlas_measures.md`.

## The cell set to develop against

`Endo_ven_apcv` / *Activated post-capillary venous endothelial* (`HCArepro:L4:0204`,
n=4851, synonym `aPCV`). Its six contributors split cleanly into the two cases a
consistency step has to tell apart:

| Source | dominant label | `cell_ratio` | `share_of_subatlas_contribution` | `share_of_subatlas_label` |
|---|---|---|---|---|
| Weigert 2025 | `endothelial cell` | 24.1% | 1168/1168 = **100%** | 1168/4780 = 24.4% |
| Ulrich 2022 | `blood vessel endothelial cell` | 8.2% | 396/396 = **100%** | 396/3418 = 11.6% |
| García-Alonso 2021 | `Endothelial ACKR1` | 5.7% | 276/277 = 99.6% | 276/5413 = 5.1% |
| HECA | `Venous` | 5.4% | 263/266 = 98.9% | 263/6662 = 3.9% |
| **Ulrich 2024** | **`Capillary`** | **4.1%** | **197/332 = 59%** | **197/1656 = 11.9%** |
| Ovary Sanger 2026 | `Endo_Cap` | 0.4% | 19/21 = 90% | 19/7359 = 0.3% |

Weigert and Ulrich 2022 are pure but uninformatively coarse — they agree with the atlas
only in the sense that "endothelial cell" agrees with everything, and the second share is
what exposes that: 100% of their contribution, but a quarter and an eighth of their label.
Ulrich 2024 is the interesting one. The atlas's own synonym for this set is `aPCV`, which
is Ulrich 2024's **11% minority** label for these cells, while 59% of them were called
`Capillary`. Any step that just reports the dominant upstream label gets this backwards —
and note that `cell_ratio` alone hides the disagreement entirely.

The sharpest number is on the `aPCV` row rather than the dominant one:

| | `cell_count` | `subatlas_contribution_cells` | `subatlas_label_total_cells` | `share_of_subatlas_label` |
|---|---|---|---|---|
| `Capillary` | 197 | 332 | 1656 | 0.1190 |
| `tPCV` | 73 | 332 | 3680 | 0.0198 |
| **`aPCV`** | **37** | 332 | **2402** | **0.0154** |

Ulrich 2024 applied `aPCV` to 2,402 cells across the atlas and only 37 of them — **1.5%** —
landed in the cell set that borrowed the name. Nothing but the registry denominator says
so. This is also the case against gating on F1: rank all 17 transfers by the harmonic mean
of the two shares and `aPCV` comes **7th**, with Weigert's `endothelial cell` top — pure
because it is uninformative. One number folds both denominators back together and hides
the thing worth seeing.

## Not committed

Per the test-project convention, only `cas.json` and this README are tracked.
`traversal_output/`, `reports/`, `selections/`, `runs/` and `local_index/` are ignored.

Two large inputs live outside the repo and are needed for anything that recomputes counts
or reads papers:

- the `obs` parquet (150 MB) — on the `Atlas-reporter_three` checkout under
  `projects/HCA_reproductive_atlas_v1/h5ad_obs/`, rebuildable via `pull_obs.py` there
  (Sanger VPN required);
- the paper corpus (494 MB) — `Atlas-reporter-corpora/hca_reproductive/`, holding
  retrieved supplements for the atlas and its 21 subatlas publications, plus prose units.
  Rebuildable from its own `corpus.json`.

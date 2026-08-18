# test_projects/fetal_skin_atlas

Test project for the prenatal (fetal) human skin atlas — Gopee et al. (2024),
*Nature*, DOI `10.1038/s41586-024-08002-x`.

## Setup (committed)

`cas.json` — a **hand-built minimal CAS+** for testing (not the full atlas):

- Six annotations: a broad `Macrophage` plus four fine macrophage subsets
  (`TML macrophage`, `Iron-recycling macrophage`, `LYVE1++ macrophage`,
  `MHCII+ macrophage`) and `Dermal papilla`.
- The fine macrophage subsets share `parent_cell_set_accession: FS_macro`, so the
  decomposer gets **real sibling `non_subject_terms`** from the hierarchy.
- Deliberately **no `synonyms` / `marker_gene_evidence`** — this exercises the
  minimal-source path (the grounder derives aliases from the paper).
- Context lives in `composition` (organism human, developmental_stage fetal,
  tissue skin).

## Baselines for diffing

Earlier direct-traversal outputs (pre-decomposer) for coverage comparison:
`/tmp/tml_traversal/` (TML) and `/tmp/dp_test/` (Dermal papilla) — ephemeral, may be
gone after a reboot; the reports under `reports/` here are the current-flow outputs.

## Running

Fresh session in the `query-decomposer` worktree, then a query such as
`all macrophages`, `TML macrophage and dermal papilla`, or a single label. Generated
outputs land under `traversal_output/`, `reports/`, `selections/`, `runs/` (all
git-ignored).

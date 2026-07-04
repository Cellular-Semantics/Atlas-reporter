# PROVISIONAL plan: adopt cxg-author-probe for field probing + cell-type picking

**Date:** 2026-07-04 · **Status:** PROVISIONAL — for comparison, not committed.
Repo: https://github.com/Cellular-Semantics/cxg-author-probe (public, MIT, same
author). Compares against
`plan_cas_migration_bigbang_and_prog_agentic_split_2026-06-24.md` +
`plan_annotations_writer_cas_2026-07-03.md`.

---

## 1. What cxg-author-probe actually is (verified from source, not README)

README says "scaffolding only" — **stale**. `src/` is implemented: `probe.py`,
`picker.py`, `prompt.py`, `pull.py`, `assemble.py`, `cli.py`, generated
`models/_generated.py`, and `readers/` with a real `h5ad.py` (9.5KB) + a reader
Protocol + registry. `zarr.py` / `tiledbsoma.py` are **stubs**.

- **Public API:** `from cxg_author_probe import probe, build_prompt,
  pull_full_column, to_long_table, augment_h5ad`; models `ProbeV1, PicksV1,
  PulledV1, ColumnDescriptor`.
- **Boundary-native:** Layer 0/1 (probe/pull/assemble + `cxg-author` CLI) are
  **pure — no LLM, no network to Anthropic** (cluster-runnable); Layer 2 is an
  optional Anthropic picker; Layer 3 is a Claude plugin (skill +
  `author-category-picker` sub-agent). This is *exactly* our prog/agentic split.
- **Wire format (JSON-schema, generated Pydantic, drift-guarded):**
  - `probe-v1` = per-column `{name, kind, n_unique, sample}` = **our
    describe-columns**, format-agnostic.
  - `picks-v1` = **`picks: [obs column names that are author cell-type fields]`**
    (empty = none). One-sentence `reasoning`, `picker.kind/model`. **Narrow —
    author cell-type columns ONLY.**
  - `pulled-v1` = a fully pulled obs column.
- **Validated:** the cell-type pick was benchmarked (agent_celltype_eval, n=73,
  Jaccard 0.81 vs CL_KG curation).

## 2. Critical scope finding

`picks-v1` classifies **only which columns are author cell-type fields**. It does
**NOT** do: descriptor → CxG mapping (tissue/development_stage/assay/…),
integration / dataset-reference / transferred-label detection, labelset
rank/hierarchy, or cross-tab/composition. So it replaces the *narrow* slice of
our `classify-obs-fields` (the `CANDIDATE_CELL_TYPE_COLS` replacement), not the
whole thing.

---

## 3. What it replaces vs what stays ours

| Component | Our original plan | With cxg-author-probe |
|---|---|---|
| obs pull + describe-columns | build in `anndata-zarr-summary` (zarr only) | **`probe()`** — done, format-agnostic |
| multi-source h5ad/zarr/tiledb (Effort 2) | separate later effort | **reader Protocol** — h5ad done, zarr/tiledb stubs → Effort 2 largely absorbed |
| author cell-type column pick | part of `classify-obs-fields` (to build) | **`picker` / picks-v1** — done + validated |
| full field classification (descriptors→CxG, integration) | `classify-obs-fields` (to build) | **NOT covered — still ours** (see §5 fork) |
| cross-tab → composition | our programmatic | **still ours** |
| CAS schema + writer | ours (`cas_annotation.schema.json` landed) | **still ours, unchanged** |
| the seam / wire format | design our column-profile + classification schemas | **adopt probe-v1 / picks-v1**; add a probe→intermediate mapper |
| prog/agentic boundary | our principle to enforce | **already embodied** by their Layer 0–3 |
| overfit eval for cell-type pick | build corpus + blind eval | **they have one** (n=73) — cell-type pick only |
| generated models + drift guard | schema-first (our convention) | **same** (datamodel-code-generator) |

## 4. Net effect on the original plan

- **Shrinks Effort 1**: describe-columns, the cell-type picker, and the reader
  layer are no longer ours to build. `anndata-zarr-summary`'s describe/pick role
  is superseded (its cross-tab math may still be reused).
- **Absorbs most of Effort 2** (multi-source): one reader Protocol, h5ad now,
  zarr/tiledb behind the same interface — no bespoke per-format loaders.
- **Unchanged**: the CAS schema (landed) and the `annotations_writer` plan. The
  intermediate dict still feeds the writer; only its *upstream producer* changes
  (probe+picks → mapper → intermediate, instead of our describe+classify).
- **Reinforces the modularity thesis** the plan is built on: cxg-author-probe is
  an independent, importable module built on the same pure/LLM split — evidence
  the boundary modularises, and it deletes build surface rather than adding it.

## 5. The fork this forces — where does the REST of field classification live?

`picks` covers cell-type only. Descriptor→CxG + integration/transferred
detection is still needed. Two options:

- **A. Extend cxg-author-probe** — grow picks (picks-v2) into a fuller field
  classification (roles: descriptor+cxg_field, dataset_reference, cluster).
  All field judgment consolidated in one repo (DOS owns both). Widens that
  repo's remit beyond "author cell-type".
- **B. Keep it narrow; classify the rest here** — cxg-author-probe does
  probe + cell-type pick + pull; atlas-reporter runs a *second* agentic pass
  over the **same probe-v1** to tag descriptors→CxG and integration. Two
  judgments, one probe. Keeps their repo focused; CAS-specific judgment stays
  with the CAS writer.

Lean **B** (separation of concerns; their repo's stated scope is author
cell-type; our CxG/integration judgment is CAS-migration-specific). Revisit if
the descriptor classifier proves generally reusable → promote to A later.

## 6. Costs / risks of importing

- **zarr reader is a stub** — HDCA is zarr, so blocked until implemented.
  Mitigation: **contribute the zarr reader** (we already have zarr obs-reading
  code in `anndata-zarr-summary/run.py` to port behind their `ObsReader`
  Protocol). This is the critical-path dependency.
- **Pre-1.0 (v0.1.0), API may churn** — pin a version; the wire schemas are the
  stable contract, so couple to `probe-v1`/`picks-v1`, not internal functions.
- **Two schema ecosystems** — theirs (probe/picks/pulled) + ours (cas). Need a
  thin `probe+picks → intermediate` mapper; that mapper is the only coupling.
- **Plugin vs library** — we want the **library** (`pip install
  cxg-author-probe`) called by our orchestrator, not their Claude plugin
  (avoids two competing skill/agent sets). Their picker sub-agent is optional;
  we can drive picking from our orchestrator against picks-v1.

## 7. Provisional revised sequencing

1. **Keep** landed `cas_annotation.schema.json` + tests (unaffected).
2. **Add dependency** on `cxg-author-probe` (pin); smoke-test `probe()` on a
   local h5ad.
3. **Contribute the anndata-zarr reader** to cxg-author-probe (port run.py obs
   logic behind `ObsReader`). Unblocks HDCA.
4. **Decide fork A/B**; build the descriptor/integration classifier accordingly
   (here, over probe-v1, if B).
5. **Write the `probe+picks → intermediate` mapper** (+ our cross-tab/composition
   over pulled columns).
6. **annotations_writer** per its plan (unchanged) → CAS docs.
7. Retire `anndata-zarr-summary`'s describe/pick role (keep only any reused
   cross-tab math, or move it into the mapper).

## 8. Open questions

1. **Fork A vs B** (§5) — the main one.
2. **Contribute zarr reader upstream vs vendor a reader locally** while upstream
   catches up?
3. **Does `probe-v1.ColumnKind` already flag categorical vs numeric / ID-like?**
   If so it seeds descriptor-vs-ignore for free — check before building the
   second classifier.
4. **Composition cross-tab source** — pull each covariate column via
   `pull_full_column` and cross-tab here, or is there reuse in `assemble`?

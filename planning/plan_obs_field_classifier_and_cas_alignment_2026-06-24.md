# Plan: agentic obs-field classifier + CAS / CxG alignment

**Date:** 2026-06-24
**Status:** design — not yet implemented
**Context:** follow-on from the "baked-in cell-type column allowlist" thread.

---

## Problem

Two hard-coded allowlists in the project decide semantics that should be
*judged* from the data:

1. `run.py::CANDIDATE_CELL_TYPE_COLS` — picks "the" cell-type obs column by
   first name-match. Never inspects values; happily treats `leiden`/`louvain`
   cluster IDs as cell types; overfits to whichever atlas was last seen.
2. `annotations_writer::_PROVENANCE_KEYS = ("n_cells", "studies",
   "top_author_labels")` — routes subatlas-reference fields to
   `label_provenance.json` purely by literal key name. A different integrated
   atlas with a `source_study` / `donor_dataset` column loses the
   reference linkage silently.

Both are the same smell: closed Python lists deciding meaning. We want an
**agentic step that judges each obs field** from its *name + sample values*.

## How the HDCA numbers are actually computed (settled)

`studies` / `top_author_labels` are **plain per-cell obs cross-tabs**, identical
math to `organ`/`germlayer` — no cell_id tracking. The integrated HDCA zarr
(`hdca_v2_20260311_f2.zarr`) carries, per cell:
`refined_celltype × original_author_annotation × study`. Counts sum to
`n_cells` (AMACRINE_CELL: 78 = Sridhar 78; AC 77 + imGlia 1 = 78). The only
thing special about `studies`/`top_author_labels` is *routing*, not derivation.

---

## Decision: align to community standards

- **Cell-type annotation → CAS** (cell-annotation-schema, general + BICAN
  extension). Each cell-type obs column becomes a CAS **labelset**; each
  category value becomes an **annotation** entry.
- **Descriptor field categorisation → CxG** obs standard (target the same
  ontologies CELLxGENE uses).

### CxG descriptor targets (verified against schema 7.1.0)

`obs` ontology fields the classifier should map descriptors onto:

| CxG obs field | Ontology |
|---|---|
| `cell_type_ontology_term_id` | CL |
| `tissue_ontology_term_id` | UBERON |
| `development_stage_ontology_term_id` | HsapDv / MmusDv / UBERON |
| `assay_ontology_term_id` | EFO |
| `disease_ontology_term_id` | MONDO (+ PATO:normal) |
| `sex_ontology_term_id` | PATO |
| `self_reported_ethnicity_ontology_term_id` | HANCESTRO / AfPO |
| `organism_ontology_term_id` | NCBITaxon |

Non-ontology CxG obs fields also worth tagging: `donor_id`, `suspension_type`,
`is_primary_data`, `in_tissue`. (Field name nuance: current schema uses
`self_reported_ethnicity_*`; pre-3.0.0 used `ethnicity_*`.)

### Why CAS fits (general + BICAN extension)

| Our data | CAS slot |
|---|---|
| cell-type obs column (e.g. `refined_celltype`) | `labelsets[]` (`name`, `description`, `annotation_method`, `rank`) |
| a category value (e.g. `AMACRINE_CELL`) | `annotations[]` entry |
| verbatim author label | `annotations[].cell_label` |
| resolved full name (name_resolver) | `annotations[].cell_fullname` |
| CL mapping (ontology-term-lookup) | `annotations[].cell_ontology_term_id` / `cell_ontology_term` |
| report narrative + citations | `annotations[].rationale` / `rationale_dois` |
| markers from report | `annotations[].marker_gene_evidence` (+ `negative_marker_gene_evidence`) |
| **subatlas reference** (`original_author_annotation`=`AC`, `study`=`Sridhar_2020`) | **`annotations[].transferred_annotations[]`** = `{transferred_cell_label, source_taxonomy (PURL/DOI), source_node_accession, algorithm_name, comment}` |
| granularity ("fine") | `labelsets[].rank` (0 = most specific) |
| all remaining original obs | `annotations[].author_annotation_fields` (free key/value) |

**Consequence:** `_PROVENANCE_KEYS` is deleted. Subatlas references become
`transferred_annotations`; `studies` → resolved into `source_taxonomy` PURLs
(reuse subatlas_resolver). Arbitrary obs → `author_annotation_fields`.

### The one real gap → extension needed

CAS has **no slot for cross-tab ratios** ("this cell type is 78% whole_embryo,
47% HsapDv:0000023, …"). This is the "cell ratio corresponding to
tissue/stage/disease" extension flagged by DOS. Proposed: a CAS-extension
object on each annotation, e.g.

```jsonc
"composition": {
  "organ":            [{"value": "whole_embryo", "n": 53, "share": 0.673, "curie": "UBERON:..."}, ...],
  "development_stage":[{"value": "HsapDv:0000023", "share": 0.473, "curie": "HsapDv:0000023"}, ...],
  "study":            [{"value": "Sridhar_et_al_2020_CellPress", "share": 1.0}]   // also feeds transferred_annotations
}
```

Keep verbatim `value`; ontology `curie` additive (existing
`_normalize_covariate_value` behaviour). Open question: formal extension field
vs nested under `author_annotation_fields` (CAS-legal but unstructured).

---

## The classifier orchestration unit

Reframed in CAS/CxG terms. Two pieces:

### 1. `anndata-zarr-summary` skill — add `--describe-columns` (deterministic)

For every **categorical** obs field (scope decision: categoricals only, matches
today): emit `{name, n_categories, first_20_values}`. Cheap — categories array
is one chunk. No judgement here.

### 2. `classify-obs-fields` subagent (judgement; new orchestration unit)

**Input:** describe-columns output (per-field name + n_categories + sample).
**Output:** per-field classification (new schema). For each field:

- **Is it a labelset (holds cell annotations)?** If yes, which kind:
  - `author_labelset` — this atlas's own annotation → drives `label` / primary
    labelset.
  - `transferred_labelset` — labels inherited from a contributing dataset →
    CAS `transferred_annotations` (pairs with a `dataset_reference` field).
  - `cluster_labelset` — `leiden`/`louvain`/`seurat_clusters` →
    `annotation_method: algorithmic` (NOT silently treated as author labels —
    the old trap).
- **`dataset_reference`** — `study`/`source_dataset` → resolves to
  `source_taxonomy` PURLs.
- **Otherwise a descriptor** → map to a **CxG standard field** where possible:
  `tissue` (UBERON), `development_stage` (HsapDv/MmusDv/UBERON), `assay` (EFO),
  `disease` (MONDO), `sex` (PATO), `self_reported_ethnicity` (HANCESTRO),
  `organism` (NCBITaxon), `donor_id`, `suspension_type` — else a free
  `semantic_category` string (open, not enum — see
  [[schema-first-no-enums-on-freetext]]).
- **`ignore`** — per-cell-unique IDs (`n_categories ≈ n_cells`).

Per field also: `confidence`, one-line `evidence`, and the **CxG-field mapping**
(or `null`). The CxG mapping + general categorisation is itself stored (DOS:
"a way to store mappings (if any) to CxG fields or general categorization").

**Two-tier principle:** a small controlled set of *functional roles* drives
routing (labelset kind / dataset_reference / descriptor / ignore); the
*descriptor semantic_category* is open free-text with a recommended CxG-aligned
vocab. Routing stays deterministic; biology stays un-enumerated.

---

## Replaces

- `CANDIDATE_CELL_TYPE_COLS` → classifier picks author_labelset(s) from
  name+values; `--describe-columns` + agent, no name list.
- `_PROVENANCE_KEYS` → `transferred_annotations` (CAS) +
  `author_annotation_fields`.

---

## Open questions (need DOS)

1. **Composition/ratio extension**: formal CAS extension field vs nested in
   `author_annotation_fields`?
2. **Output target**: do we migrate `cell_type_annotations.schema.json` to a
   CAS-shaped schema, or keep the current shape and add a CAS *exporter*? (Lots
   of downstream — report synthesizer, validators — read the current shape.)
3. **CAS flavour**: general schema + a local BICAN-style extension, or adopt
   BICAN extension wholesale (it already has `transferred_annotations`,
   `rank`, `cell_set_accession`, neurotransmitter slots)?
4. **Cell-type role granularity**: confirm the 4-way functional split
   (author / transferred / cluster labelset + dataset_reference).

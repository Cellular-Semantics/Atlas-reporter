---
name: generate-cas
description: Generate a project's CAS+ config (projects/{project}/cas.json) from whatever source(s) are available — a bare list of cell-type labels, a spreadsheet/CSV, an AnnData h5ad/zarr obs, a CELLxGENE dataset, or a paper's supplementary table. Lifts any starting point up to the CAS+ contract so the rest of the workflow has one input shape. Deliberately lightweight; the schema is the spec.
---

# generate-cas

Produce `projects/{project}/cas.json` conforming to
`src/atlas_chat/atlas_chat/schemas/cas_annotation.schema.json`. That schema is the
contract and is **self-documenting** — read its field descriptions and follow them;
do not reproduce them here.

Invoked from workflow Step 1 when a project has no valid `cas.json` yet. CAS+
supersedes the legacy flat `cell_type_annotations.json`.

## Inputs

You are given a **project name** and one or more **sources**. Sources can be any of:
a bare list of cell-type labels, a CSV/XLSX table, an AnnData `.h5ad`/`.zarr` store
(read **obs only** — never the expression matrix), a CELLxGENE dataset, or a paper
supplementary table.

Some fields are not derivable from the data — **ask the user** rather than guess:
- the atlas **DOI** (and title, if not in the source),
- the **organism** (unless present as an obs/table column),
- **field roles** — which column(s) are the **cell-type label(s)**, which are coarser
  **hierarchy / granularity tiers** (→ ranked labelsets), which are **context
  covariates** (organism / developmental stage / tissue → `composition`), which are
  **transferred labels** (another study's cell-type calls → `transferred_annotations`,
  see below), and which to ignore. Confirm the label column even when it looks obvious.
- for each transferred-label column, the **DOI of the study it came from** (or that it
  has no publication).

> A future obs-field classifier (in progress on `cxg-entrypoint-reader-discovery`)
> will propose these field roles automatically; until it lands, ask the user.

### Transferred-label columns

An integrated atlas usually keeps each contributing study's own cell-type calls as
extra obs columns — `celltype_Ulrich2024`, `Sridhar_et_al_2020_CellPress`. These are
**integration provenance**, not context: they say what an upstream study called the
same cells, which is what downstream steps use to judge whether an atlas label agrees
with the labels it was built from, and to seed evidence retrieval from the paper that
actually defines the cell type.

Spot them by name (an author-and-year or study-accession suffix), by being sparse
(empty for every cell the contributing study never saw), and by their values looking
like cell types rather than descriptors. **Ask the user to confirm**, and to give each
one a DOI.

They must not go into `composition` — a descriptor distribution has no paper attached
and no downstream consumer will read it as provenance. Route them to
`transferred_annotations` and register their papers under `source.subatlas_papers`.
Don't hand-build the cross-tab; run the producer:

```bash
# obs already local as CSV/TSV
python -m atlas_chat.cli_cas transfer --cas projects/{project}/cas.json \
  --obs obs.tsv --cell-type-col <label column> --labelset <labelset name> \
  --source "celltype_Ulrich2024=10.1073/pnas.2404775121;Ulrich;2024" \
  --source celltype_OvarySanger2026          # no DOI: unpublished contributing data

# or, for a remote zarr, let anndata-zarr-summary aggregate first
python .claude/skills/anndata-zarr-summary/run.py <zarr-url> \
  --cell-type-col <label column> --transfer-cols celltype_Ulrich2024 ...
python -m atlas_chat.cli_cas transfer --cas projects/{project}/cas.json \
  --transfers zarr_summary/label_transfers__<label column>.json \
  --labelset <labelset name> --source "celltype_Ulrich2024=10.1073/..."
```

Run it once per labelset (`--append` to add sources to a labelset that already has
some). It fills `cell_count`, `cell_ratio` and `source_label_cell_count`, and seeds
`source.subatlas_papers` without clobbering DOIs the resolver has already confirmed.

## Procedure (lightweight)

1. Identify the source(s) and **assay the available fields first** (`pandas`/
   `openpyxl` for tables; `anndata`/`zarr` for obs — obs only, never the matrix; a
   text list directly). For each column record its dtype (categorical vs
   continuous), cardinality, and a few example values. Mark as **auto-excluded** the
   **continuous / numeric** columns (QC metrics such as counts or percent-mito,
   embeddings, per-cell floats) and the **identifier-like / high-cardinality
   categoricals** (cell barcodes, per-cell IDs, index-like columns — distinct-value
   count approaching the cell count): these are not per-label categories and would
   massively bloat `cas.json`.
2. **Present that field inventory to the user** — the candidate columns with their
   dtype / cardinality / example values, and what was auto-excluded and why — and
   **ask them to assign roles**: cell-type label(s), hierarchy / granularity tiers,
   context covariates, transferred labels, or ignore; plus anything not derivable
   (DOI, organism, a DOI per transferred-label column).
   Listing the actual fields lets the user choose from what is really there; confirm
   the label column even when it looks obvious.
3. For each chosen categorical covariate, summarise per label — near-constant → a
   scalar; otherwise keep the distribution (`{author_value, share}`) — which maps
   onto CAS+ `composition`.
4. Map to CAS+ (let the schema descriptions guide the exact shape):
   - `source`: `{doi, title, ...}` (+ `organism`/`links` where known).
   - `labelsets`: one per cell-type column; set `rank` by granularity if known.
   - `annotations`: one per label, `cell_label` = the verbatim label, tied to its
     `labelset`. Carry hierarchy (`parent_cell_set_accession` / lineage), `synonyms`,
     `marker_gene_evidence`, `cell_ontology_term_id` **only if the source already
     provides them** — do not invent them (downstream steps resolve names, markers,
     and ontology terms). Fold CxG-style context (organism / developmental stage /
     tissue) into `composition` with ontology CURIEs where obvious; put remaining
     unmapped author columns in `author_annotation_fields`. Leave
     `transferred_annotations` to `cli_cas transfer` (above) rather than writing it
     by hand — it needs counts you would otherwise have to aggregate yourself.
   - Leave optional fields **absent** when unknown — downstream consumers are
     presence-aware.
5. Write `projects/{project}/cas.json`. The `check_cas_annotation` PostToolUse hook
   validates it against the schema; if it fails, read the errors and rewrite.

## Minimal case

A bare list of labels + a DOI is enough:

```json
{
  "title": "<atlas title>",
  "source": { "doi": "10.xxxx/..." },
  "labelsets": [ { "name": "author_cell_type" } ],
  "annotations": [ { "labelset": "author_cell_type", "cell_label": "<label>" }, ... ]
}
```

## Rules

- **obs only** — never download or read the expression matrix.
- **Do not invent** markers, synonyms, or ontology terms. Carry them only if the
  source states them; otherwise leave absent for downstream steps to fill.
- A transferred-label column belongs in `transferred_annotations` with a DOI, never in
  `composition`. If the user cannot name the source paper, register the contributor
  with no DOI rather than silently dropping the column.
- Prefer asking the user over guessing DOI / organism / which column is the label.
- Output is `projects/{project}/cas.json`; schema compliance is enforced by the hook.

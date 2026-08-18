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
- which column is the **cell-type label** (vs granularity/lineage/covariates), when
  ambiguous.

## Procedure (lightweight)

1. Identify the source type and gather inputs; ask the user for anything missing or
   ambiguous (DOI, organism, which column is the label).
2. Read the source with whatever python libraries fit (`pandas`/`openpyxl` for
   tables; `anndata`/`zarr` for obs — obs only; a text list directly). For per-label
   covariates that are near-constant, summarise as a scalar; otherwise keep the
   distribution (`{author_value, share}`) — this maps onto CAS+ `composition`.
3. Map to CAS+ (let the schema descriptions guide the exact shape):
   - `source`: `{doi, title, ...}` (+ `organism`/`links` where known).
   - `labelsets`: one per cell-type column; set `rank` by granularity if known.
   - `annotations`: one per label, `cell_label` = the verbatim label, tied to its
     `labelset`. Carry hierarchy (`parent_cell_set_accession` / lineage), `synonyms`,
     `marker_gene_evidence`, `cell_ontology_term_id` **only if the source already
     provides them** — do not invent them (downstream steps resolve names, markers,
     and ontology terms). Fold CxG-style context (organism / developmental stage /
     tissue) into `composition` with ontology CURIEs where obvious; put remaining
     unmapped author columns in `author_annotation_fields`.
   - Leave optional fields **absent** when unknown — downstream consumers are
     presence-aware.
4. Write `projects/{project}/cas.json`. The `check_cas_annotation` PostToolUse hook
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
- Prefer asking the user over guessing DOI / organism / which column is the label.
- Output is `projects/{project}/cas.json`; schema compliance is enforced by the hook.

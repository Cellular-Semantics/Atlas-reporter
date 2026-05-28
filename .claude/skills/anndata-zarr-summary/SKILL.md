---
name: anndata-zarr-summary
description: Download `obs/` metadata only from an AnnData-zarr store (remote URL or local path) and produce per-cell-type co-annotation summaries plus an atlas_chat-ready `cell_type_annotations.json`. Never downloads the expression matrix. Supports zarr v2 and v3, http(s)/gs/file URLs, multiple cell-type columns, and caches code arrays so repeat runs are cheap.
---

# anndata-zarr-summary

Pull cell-type co-annotations directly from an AnnData-zarr store without
downloading expression data. Output is designed as a one-stop input for an
`atlas_chat` project.

## When to invoke

User asks for one of:
- "summarise obs metadata from this zarr store"
- "build a `cell_type_annotations.json` from <URL>"
- "what cell types are in this atlas / cross-tab obs columns"
- starting a new atlas_chat project from a published AnnData-zarr

## Usage

```
/anndata-zarr-summary <url-or-path> [options]
```

**Required:**
- `<url-or-path>` — the AnnData-zarr root. Accepts:
  - `https://storage.googleapis.com/bucket/path.zarr`
  - `gs://bucket/path.zarr` (converted to https for fetching)
  - `/local/path/to/file.zarr` (use `file://` scheme or plain path)

**Options:**
- `--cell-type-col COL [COL ...]` — one or more cell-type columns. If
  omitted, the skill auto-picks the first match from:
  `cell_type`, `cell_type_ontology_term_id`, `refined_celltype`,
  `celltype`, `Cluster`, `annotation`, `leiden`, `louvain`, `seurat_clusters`.
  If multiple are given, the skill writes **separate** annotation files per
  column.
- `--covariates COL [COL ...]` — explicit covariate list. Default: auto-pick
  (see "Auto-picking covariates" below).
- `--out-dir DIR` — where to write outputs. Default: `./zarr_summary/`.
- `--doi DOI`, `--title TITLE`, `--url URL` — pub metadata copied into the
  trimmed `source` field. If omitted, fields are written as `null` with a
  note instructing the user to fill them in for atlas_chat.
- `--no-cache` — bypass cache, force re-download.
- `--minimal` — emit only the trimmed `cell_type_annotations.json`, skip the
  full `co_annotations.json`.

## Cache

All downloaded code arrays and category lists are cached under:
```
~/.cache/anndata-zarr-summary/<sha256(url)>/<column>/
```

Cache is keyed by (zarr_url, column). Repeat runs hit the cache and skip
network downloads entirely.

## Workflow

### 1. Detect zarr format version

Fetch `{root}/zarr.json` (v3). If 404, fetch `{root}/.zattrs` (v2). Record
the format version; later steps branch on it.

### 2. Read obs schema

- **v3:** read `{root}/obs/zarr.json` → `attributes['column-order']`,
  `attributes['_index']`, `attributes['encoding-type']` (= `dataframe`).
- **v2:** read `{root}/obs/.zattrs` → same fields.

The schema does *not* tell you which columns are categorical — that's per
column. Fetch each column's group metadata to detect categoricals:
- **v3:** `{root}/obs/{col}/zarr.json` →
  `attributes['encoding-type'] == 'categorical'`
- **v2:** `{root}/obs/{col}/.zattrs` → same

For categorical columns, child paths are:
- categories array: `{col}/categories/`
- codes array: `{col}/codes/`

For non-categorical (numeric) columns the column is a zarr array at the
column path itself (skip — this skill works on categoricals only).

### 3. Pick cell-type column(s)

- Use `--cell-type-col` if given (validate each exists and is categorical).
- Otherwise iterate the candidate list above and pick the **first** that
  exists and is categorical.
- Multiple columns → run the full workflow once per column (separate output
  files).

### 4. Auto-pick covariates

For each categorical obs column other than the cell-type column:
- Read its `categories/` array shape (= `n_categories`).
- **Skip** columns where `n_categories >= n_cells` (per-cell-unique
  identifiers like `library_id`, `barcode`).
- **Warn** when `n_categories > 500` — the cross-tab will still run but the
  per-cell-type output gets large. Surface the warning in skill output, but
  process the column unless the user explicitly excludes it.
- **Include** everything else.

### 5. Download code + category data

For each column to use (cell-type column + covariates):
- Download `categories/` chunk(s). String arrays are typically one chunk.
- Download `codes/` chunks. Count determined from `chunk_shape` in
  `codes/zarr.json` (v3) or `codes/.zarray` (v2). Chunk filenames are:
  - **v3:** `c/0`, `c/1`, … (flat numeric index)
  - **v2:** `c/0.0`, `c/1.0`, … (one digit per dim; obs is 1-D so always
    `.0`)

Each chunk file is independently decompressable. For zstd-compressed
chunks, use `zstandard` library.

Cache layout per column:
```
~/.cache/anndata-zarr-summary/<hash>/<column>/
├── categories.json    (decoded string list)
└── codes.npy          (full int8/int16 numpy array)
```

After first run, all subsequent runs read from cache.

### 6. Decode

- Categories: zstd-decompress chunk → AnnData vlen-utf8 encoding:
  `<4-byte LE count><{4-byte LE length}{utf-8 bytes}...>`.
- Codes: concatenate decompressed chunk bytes → `np.frombuffer(dtype=...)`
  where dtype comes from `zarr.json`'s `data_type` (`int8`, `int16`, `int32`).
  Truncate to first `n_cells` elements (last chunk may pad).

### 7. Cross-tabulate

For each cell-type label and each covariate column, build a `Counter` over
covariate codes among cells with that label. Convert to a sorted list of
`{value, n, share}` triples (top 5 by default — covariates with more than 5
distinct values get truncated to top-5).

### 8. Write outputs

For each cell-type column `<col>`, write two files:

**`co_annotations__<col>.json`** — full distribution:
```json
{
  "<cell_type_label>": {
    "n_cells": 12345,
    "<covariate>": [
      {"value": "X", "n": 12000, "share": 0.972},
      {"value": "Y", "n":   345, "share": 0.028}
    ],
    ...
  },
  ...
}
```

**`cell_type_annotations__<col>.json`** — trimmed, atlas_chat-ready:
```json
{
  "source": {
    "zarr_url": "https://...",
    "obs_column": "<col>",
    "n_cells_total": 4679782,
    "n_categories": 454,
    "extracted_at": "2026-05-19T...",
    "covariates_used": ["broad_celltype", "germlayer", ...],
    "doi": null,
    "title": null,
    "url": null,
    "_note_to_user": "Fill in doi / title / url manually before using this as an atlas_chat project config."
  },
  "annotations": [
    {
      "label": "<cell_type_label>",
      "n_cells": 12345,
      "<covariate>": "X",                       // scalar if share >= 0.95
      "<other_covariate>": [{"value":...,"share":...}, ...]
    },
    ...
  ]
}
```

When `--doi`/`--title`/`--url` are provided, those values populate the
`source` fields and `_note_to_user` is dropped.

### 9. Report summary

```
✓ Zarr v3 detected: <url>
✓ obs schema: 51 columns, n_cells_total = 4,679,782
✓ Cell-type column: refined_celltype (454 categories)
✓ Covariates auto-picked: broad_celltype, germlayer, systems, organ,
  development_stage_ontology_term_id, sex_ontology_term_id, ...
⚠ Skipped library_id (n_categories ≈ n_cells)
⚠ original_author_annotation has 3,385 categories — included, but output
  may be large. Consider --covariates to narrow.
✓ Wrote zarr_summary/co_annotations__refined_celltype.json
✓ Wrote zarr_summary/cell_type_annotations__refined_celltype.json
```

## Implementation

A reference implementation is provided as
`.claude/skills/anndata-zarr-summary/run.py`. Invoke it from the bash tool:

```bash
.venv/bin/python .claude/skills/anndata-zarr-summary/run.py <args>
```

## Rules

- Never download `X/`, `var/`, or any expression data — `obs/` only.
- Always include a `--cache-status` line at the end of the report
  (how many chunks were downloaded vs hit from cache).
- If the zarr root doesn't contain `obs/`, stop with a clear error.
- For private / gated stores: if a chunk fetch returns 401/403, abort with
  a clear "this store requires authentication; this skill does not handle
  auth" message. (Auth handling is the job of a separate skill that resolves
  the URL.)

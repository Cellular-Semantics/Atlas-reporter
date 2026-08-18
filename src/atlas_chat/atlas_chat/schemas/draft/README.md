# schemas/draft — parked schema fragments

Not part of the active atlas_chat contract. These are **not** loaded by
`atlas_chat.schemas.load_schema` (which reads only the `schemas/` root) and are
**not** `$ref`'d by any active schema. They are kept for possible future
folding-in of work from other branches.

## data_provenance.schema.json

Was `$defs.DataProvenance` inside `cas_annotation.schema.json` on branch
`cxg-entrypoint-reader-discovery`. **Removed from the active CAS+ contract in
PR #17** because it was:

- **semi-redundant** — its data-pointer fields (`source_url` / `file_path` /
  `dataset_id`) overlap with `matrix_file_id`, `source.links`, and
  `source.local_text_path`; `obs_column` overlaps with `Labelset.name`.
- **an arbitrary/contingent enum** — `source_type` mixes orthogonal axes
  (format `h5ad`/`zarr`, locality `local`/`published`, platform `cellxgene`/`cap`,
  authoring mode `manual`/`spreadsheet`), reading as accreted from whatever inputs
  the originating branch's annotations writer handled.
- **unconsumed** on the `dev` line.

If provenance-of-extraction is wanted later, prefer either a free-text
`source_type` (recommended values, not a hard enum) or a top-level free-text
`_provenance` block — as used in
`projects/HCA_reproductive_atlas_v1/cell_type_annotations.json`
(`{annotation_table, cl_mapping, note}`).

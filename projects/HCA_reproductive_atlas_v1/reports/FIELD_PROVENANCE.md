# Where `cell_label`, `cell_fullname` and the CL mapping come from

**Scope:** `projects/HCA_reproductive_atlas_v1/cas.json` (312 annotations, 223
with a CL term). Sections 3, 4 and 8 record fixes applied on 2026-10-16; the
problems they describe are no longer live unless marked outstanding. Everything below was re-derived from the input files, not read
off the documentation. Checked 2026-10-16 against CL release 2026-06-08.

---

## 1. The chain

```
h5ad obs  ──────────────┐
  (h5ad_obs/obs.categoricals.parquet, 2.24M cells)
                        ├──►  scripts/build_cas.py  ──►  cas.json
inputs/cell_ontology_mapping.xlsx  (sheet "Final", 238 rows)
                        │
inputs/media-4.xlsx  (sheet "B. HCA_femaleRepSys_v1_celltype")
```

The atlas h5ad is at the `matrix_file_id` URL recorded in `cas.json`; only its
`obs` is used here. `build_cas.py` is marked "Throwaway/draft" in its own
header.

## 2. Field by field

| Field | Source | Mechanism |
|---|---|---|
| `cell_label` (leaves) | `obs.celltype_HCA_fine` | Verbatim object code, so leaves join directly to `obs`. Applied only to leaves where one fine code covers 100% of the cell set (`build_cas.py:281`). |
| `cell_label` (internal nodes) | `cell_ontology_mapping.xlsx` L1–L4 | Internal nodes keep the nomenclature name, so `cell_label == cell_fullname` for them. 104 of 312 annotations are in this state. |
| `cell_fullname` | `cell_ontology_mapping.xlsx` columns L1–L4 | The nomenclature name at that node's tier; set on **every** node before leaves are relabelled (`build_cas.py:292`). |
| `labelset` L1–L4 | same spreadsheet, columns C–F | Tier depth becomes the labelset; L4 is the finest. |
| `cell_ontology_term_id` | spreadsheet column **K** (`cell_type_ontology_term_id`) | `build_cas.py:43`, `r[10]`. |
| `cell_ontology_term` | spreadsheet column **G** (`Perfect match`), falling back to column **I** (`Nearest match`) | `build_cas.py:43`, `cln(r[6]) or cln(r[8])`. |
| `marker_gene_evidence`, `synonyms`, `comment` | `media-4.xlsx` | Markers_positive / Alternative_celltype_labels / Celltype_description. 206 annotations carry markers, 95 carry synonyms. |
| `composition`, `author_annotations`, `transferred_annotations` | `obs` columns | Counted cell distributions, not curated text. |

**Internal nodes inherit their CL term** from the leaf code(s) terminating at
them, and only when those agree — a node whose children disagree gets no term
(`build_cas.py:91-95`). This is why 89 annotations, nearly all L1–L3, have no
CL mapping: they are grouping tiers, not unmapped cell types.

**25 annotations are "minted generic leaves"** — synthesised where an
un-subtyped `celltype_HCA_fine` code shared a nomenclature node with finer
subtypes. They carry a `comment` saying so. 85 annotations carry a `comment`.

## 3. The CL mapping is graded at source — and the grade used to be dropped

> **Status: fixed.** `build_cas.py` now carries the grade through into
> `cell_ontology_match_type`, added to the CAS+ schema on `dev` and merged here.
> The description below is of the state that made the fix necessary.

The spreadsheet does not hold one opinion per row. It holds two:

| column | meaning | populated |
|---|---|---|
| G / H | `Perfect match` + `ID_perfect` | 59 of 238 rows |
| I / J | `Nearest match` + `ID_nearest` | 183 of 238 rows |
| K | `cell_type_ontology_term_id` — the one that ships | 238 of 238 |

Across the 223 annotations that carry a CL term in `cas.json`, **49 rest on a
curator-declared perfect match and 174 on a declared nearest match.** That is
78% of the shipped mappings already flagged as inexact by the atlas team.

`build_cas.py` reads columns G, I and K. It never reads H or J, and it records
nothing about which grade a mapping came from — so `cas.json` presents a
curator's "nearest match, knowingly approximate" and a curator's "perfect
match" in identical form. **This is the single most consequential provenance
loss in the chain**, and it is what the `match_type` column in
`cl_mapping_revisions.tsv` is independently reconstructing.

## 4. The label and the ID were taken from different columns

From `build_cas.py:43`:

```python
sheet[leaf] = {..., "cl_id": cln(r[10]), "cl_label": cln(r[6]) or cln(r[8])}
#                            column K              column G    or  column I
```

The ID comes from column K; the human-readable label comes from column G or I.
Nothing checks that they refer to the same term. In **5 of 238 rows column K
disagrees with both graded columns**, and in exactly those rows `cas.json`
carries an ID and a label naming different cell types:

| row | ships ID | ships label | spreadsheet's own graded answer |
|---|---|---|---|
| `Immune_uNK1` | CL:4052028 | uterine natural killer cell 1, human | `ID_perfect` = CL:4052051 |
| `Immune_uNK2` | CL:4052028 | uterine natural killer cell 2, human | `ID_perfect` = CL:4052052 |
| `Immune_uNK3` | CL:4052028 | uterine natural killer cell 3, human | `ID_perfect` = CL:4052053 |
| `Granulosa_sq_Fetal` | CL:0000501 | squamous granulosa cell | `ID_nearest` = CL:4033083 |
| `Granulosa_AMHneg_Atretic` | CL:0000501 | squamous granulosa cell | `ID_nearest` = CL:4033083 |

In all five the spreadsheet already held the better term in a column the build
script did not read. These are **not curation errors** — they were a pipeline
loss, and the fix was in `build_cas.py`, not in the atlas team's judgement.

> **Status: fixed.** `build_cas.py` now reads the id and the label from the same
> graded pair, preferring the perfect match. All five rows in `cas.json` now
> carry the spreadsheet's own answer.

**One case is different.** `Immune_T_Cyc` ships `CL:0000076` with the label
"cycling T cell", and the spreadsheet agrees with itself: `Nearest match` =
"cycling T cell", `ID_nearest` = `CL:0000076`. But `CL:0000076` *is* **squamous
epithelial cell**; cycling T cell is `CL:4033069`. This one is a genuine error
in the source spreadsheet and needs to go back to the atlas team.

> **Status: worked around, not fixed at source.** `build_cas.py` carries a
> one-entry `SHEET_ID_FIX` override setting `CL:4033069`, and the annotation
> records why in `cell_ontology_mapping_notes`. **The spreadsheet itself is still
> wrong** — remove the override once the atlas team corrects it.

## 5. Normalisations that rewrite identity silently

Three places where a label is altered or re-pointed between sheet and output:

- **`CANON`** (`build_cas.py:34`) rewrites L2 `Stromal-interstitial fibroblast`
  → `fibroblasts`, merging a fetal and an adult stromal tree that the
  singular/plural spelling had forked. Documented in the script.
- **`resolve()`** (`build_cas.py:52`) joins obs codes to sheet rows through
  fallbacks: strip a trailing `+` (`Endo_cap_APCDD1+`), and swap `Fib`↔`Fibs`.
  A code matched this way is recorded as if it matched exactly.
- **Accession numbering** is positional (`HCArepro:L{n}:{i:04d}`), assigned from
  a sorted code list. Accessions are stable only while the code set is — they
  are not durable identifiers across atlas versions.

## 6. What is not recorded anywhere

For any individual CL mapping, `cas.json` cannot answer:

- Was this a perfect or a nearest match? (known at source, dropped — §3)
- Who made it, and when?
- Against which CL release? No CL version is recorded in `cas.json`, the
  spreadsheet, or `build_cas.py`. Terms are reclassified and obsoleted between
  releases, so a mapping with no version is not reproducible.
- On what evidence — marker, morphology, location, or label resemblance?

`cellannotation_schema_version` is `0.1.0-local`, i.e. the file is a local
variant of CAS+, not a released schema version.

## 7. Verification performed

- All 223 CL-bearing annotations were re-derived from
  `cell_ontology_mapping.xlsx` through the rules in §2: **223 reproduced
  exactly, 0 mismatches.** The chain in this document is the real one.
- All 53 CURIEs cited across the two triage TSVs resolve in CL 2026-06-08, and
  every suggested term's label matches its CL label exactly.
- Every `labelset`, `cell_fullname`, `n_cells` and current mapping quoted in the
  TSVs recomputes from `cas.json`; every composition percentage quoted was
  confirmed.
- Cross-check: the only three rows where the spreadsheet holds a perfect-match
  ID differing from what shipped are the three uNK rows — reached independently
  from CL, and agreeing on all three IDs.

## 8. Recommendations

**Done:**

1. ~~Fix `build_cas.py` to take the ID and the label from the same column pair.~~
   Done; resolved 5 of the 6 errors with no curation input.
2. ~~Carry the perfect/nearest grade into `cas.json`.~~ Done, as
   `cell_ontology_match_type` (CAS+ schema, `dev` → this branch).
   **173 of 223 mappings are a broad match; 50 are exact.**

**Outstanding:**

3. **Report `Immune_T_Cyc` to the atlas team** — the id is wrong in the
   spreadsheet itself, and is currently corrected by an override in the build
   script rather than at source.
4. **Record the CL release** a mapping was made against. Still nowhere in the
   chain, so no mapping in this file is reproducible across CL releases.
5. Treat §5's normalisations as reportable: a code joined via a `Fib`/`Fibs`
   fallback should say so.
6. **`build_cas.py` cannot regenerate the shipped `cas.json`.** Running it
   renumbers every `cell_set_accession` and drops the 7,488
   `share_of_subatlas_*` fields that `subatlas_registry.py` adds afterwards. It
   is a draft script, and the file is the product of a pipeline it is only the
   first stage of. The changes here were therefore applied as a surgical patch,
   not a rebuild. Worth resolving before the next structural change.

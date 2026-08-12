# obs table — remote pull + co-annotation summary

**Source:** `https://cellgeni-share.cog.sanger.ac.uk/REQ-69024/integrated_scvi_all_tissues_cellxgene_filtered.h5ad`
(92.8 GB; **obs-only** read via HTTP range requests — matrix never downloaded).
**Pulled:** 2026-07-29 · **2,235,448 cells × 65 obs columns**. Re-pull with `python3 h5ad_obs/pull_obs.py`.
**Download host is Sanger-internal** — connect to the **Sanger VPN** if the pull stalls/403s off-site (noted in `pull_obs.py`).

**Two parquet artifacts:**
- `obs.parquet` (151 MB, all 65 cols) — **git-ignored** (>GitHub limit; reproducible via `pull_obs.py`).
- **`obs.categoricals.parquet` (17.9 MB, 56 cols, zstd)** — committed; drops only the 9 per-cell numeric QC/score columns. Use this for annotation work.

## ⚠️ No CELLxGENE-Discover standard ontology columns

Despite `cellxgene` in the filename (it's formatted for the cellxgene *browser* at reproductivecellatlas.org, **not** the Discover census schema), there are **no `*_ontology_term_id` columns at all** — none of `tissue_ontology_term_id`, `development_stage_ontology_term_id`, `disease_ontology_term_id`, `assay_ontology_term_id`, `cell_type_ontology_term_id`, `self_reported_ethnicity_…`, `sex_…`, `suspension_type`, `is_primary_data`.

Instead the metadata is **HCA-schema-style human-readable free text** (`Organ`, `Developmental_stage`, `Disease`, `Assay_type`, `Cell_enrichment`, `Library_chemistry`, `Sorting_method`, …). To reach CxG/ontology compliance these would need mapping:
`Organ`/`Organ_part`/`Tissue_ROI` → **UBERON**; `Developmental_stage`/`Tanner Stage`/`Postnatal_age_years`/`Gestational_age_pcw` → **HsapDv**; `Disease`/`Clinical_diagnosis` → **MONDO**; `Assay_type` → **EFO**; cell types → **CL** (the manual `cell_ontology_mapping.xlsx` already covers this tier). None of these mappings exist in the object yet.

## Column roles (`column_inventory.csv`)

| role | n cols | columns |
|---|---|---|
| **HCA annotation** | 8 | `celltype_HCA_lineage` (8), `celltype_HCA_broad` (98), **`celltype_HCA_fine` (212)** ★, `celltype_HCA` (149, has `unknown`), `celltype_HCA_ontology_level1–4` (8/24/57/117) |
| **author cell type** | 9 | `celltype_GarciaAlonso2021`, `celltype_GarciaAlonso2022`, `celltype_Ulrich2022`, `celltype_Ulrich2024`, `celltype_Weigert2025`, `celltype_OvarySanger2026`, `celltype_Lardenois2026`, `celltype_Lorenzi2025`, `celltype_HECA` |
| **sample metadata (categorical)** | 40 | Organ, Developmental_stage, Menstrual_stage, Disease, Clinical_diagnosis, Tanner Stage, Donor_id (291), Dataset (27), Assay_type, Tissue_ROI, … |
| **numeric QC / score** | 9 | n_genes, n_counts, percent_mito, doublet_scores, senescence_score, stress_score_vandenBrink, health_score, metabolic_activity, S/G2M_score; `cell_to_exclude` (bool) |

### Canonical annotation column
**Use `celltype_HCA_fine` (212 types)** as the reporter key — it matches the paper's ~210 fine types and 211/250 of the media-4 (Supp Table 2B) catalogue labels. `celltype_HCA` (149) is a coarser alternate with an `unknown` bucket; don't key on it. The ontology_level1–4 columns are the human-readable structured nomenclature (8→24→57→117).

### Notes on flags/metadata
- `cell_to_exclude` is **all False** — this object is already QC-filtered ("…_filtered.h5ad"); the flag carries no signal here.
- `Sex` = female only; `Assay_type` = 10x scRNA-seq only.
- `Developmental_stage` (5): Adult, paediatric, pubertal, + prenatal stages. `Organ` (7). `Disease` (41) / `Clinical_diagnosis` (48) give pathology context.
- `predicted_doublet` is nullable (only 16.3% populated).

## Author cell-type ↔ HCA_fine co-annotation (the name-resolution bridge)

Each cell carries at most one subatlas author label (cells are disjoint by source dataset). The crosstab of `celltype_HCA_fine` × each author column with **cell numbers** is the crosswalk from HCA labels back to original study nomenclature.

- **`coannotation_HCAfine_x_author.csv`** — long format: `celltype_HCA_fine, source_study, source_doi, author_label, n_cells` (3,758 rows). **203 / 212** fine types carry ≥1 author label.
- **`coannotation_rollup_dominant.csv`** — dominant (largest-n) author label per `(HCA_fine × study)` (844 rows) — the compact lookup for name resolution.
- **`coannotation_HCAfine_x_Organ.csv`** (644 rows) and **`coannotation_HCAfine_x_Developmental_stage.csv`** (458 rows) — cell numbers per fine type by organ / life stage.

Example (novel spiral-artery pericyte): `Mesen_Pericyte_EndoSpiralArt` ← GarciaAlonso2021 `PV STEAP4` (506), HECA `ePV_1b` (1359).

### Study → DOI map for author columns
| author column | source study (DOI) | # HCA_fine types annotated |
|---|---|---|
| celltype_OvarySanger2026 | **newly-generated Sanger ovary data** (no external DOI; evidence = atlas preprint) | 131 |
| celltype_Lorenzi2025 | 10.1038/s41586-025-09875-2 (prenatal repro tract) | 111 |
| celltype_GarciaAlonso2022 | 10.1038/s41586-022-04918-4 (gonadal dev) | 104 |
| celltype_Ulrich2024 | 10.1073/pnas.2404775121 (premenopausal uterus) | 96 |
| celltype_HECA | 10.1038/s41588-024-01873-w (Marečková 2024, tentative) | 94 |
| celltype_GarciaAlonso2021 | 10.1038/s41588-021-00972-2 (endometrium) | 89 |
| celltype_Weigert2025 | 10.1038/s41467-024-55440-2 (fallopian tube) | 77 |
| celltype_Ulrich2022 | 10.1016/j.devcel.2022.02.017 (fallopian tube) | 72 |
| celltype_Lardenois2026 | 10.1016/j.devcel.2025.09.011 (gonadal somatic) | 70 |

✅ **`celltype_OvarySanger2026` resolved** — it is the study's **own newly-generated Sanger ovary annotation**, not an external subatlas. Its labels are applied to `ovary_paediatric_sanger` (197k cells), `ovary_adult_sanger` (53k), and Garcia-Alonso 2022 fetal ovary (91k). This is why no `subatlas_pubs` DOI matches — it's new data (the paper's own ovary contribution), so evidence comes from the atlas preprint itself, not an external paper. `celltype_HECA` DOI (Marečková 2024) is still tentative.

### Dataset provenance (from `Dataset` / `dataset` columns — 27 datasets)

The `dataset` column encodes `organ_stage_study`; several `Sanger_*` datasets are **newly generated** for this atlas (no external DOI): Sanger_Endometrium (259k), Sanger_PediatricOvary (238k), Sanger_MenstrualFluid (82k), Sanger_AdultOvary (79k), Sanger_FallopianTube (50k), Sanger_Uterus (39k), + menopause. The rest map to the `subatlas_pubs` DOIs (Lorenzi 2025 287k, Garcia-Alonso 2022 222k, Weigert 2025 150k, **Huang 2023 102k — the one ASTA can't retrieve**, Burns 2026, Garcia-Alonso 2021, Marečková 2024, Liu 2025, Wang 2020, Ulrich 2022/2024, Tan 2022, Guahmich 2023, Wamaitha 2023, Li 2021, Gaylord 2025, Guo 2023, Jones 2024, Wagner 2020, Taelman 2024). Full counts in `obs.categoricals.parquet` (`Dataset.value_counts()`).

## 9 HCA_fine types with NO subatlas author label (HCA-novel or from newly-generated data)

Mostly cervix/vagina (not covered by the author-label subatlases) + one novel population:
`Epi_CervixMucinous`, `Epi_CervixMucinous_Secretory`, `Epi_CervixSquamous`, `Epi_CervixSquamous_Cyc`, `Epi_EctocervixVaginaSquamous`, `Epi_OvarianInclCil`, `Mesen_CervixFibs`, `Mesen_VaginaFibs`, `Mesen_Pericyte_EndoStromalLike_MenstrualFluid`.

→ For these, evidence must come from the atlas preprint / media-4 markers / cervix+vagina subatlases (Guo 2023, Li 2021) rather than author-label transfer.

## Outputs in this dir
- `obs.parquet` — full obs (2.24M × 65)
- `column_inventory.csv` — every column: role, dtype, n_unique, %labelled, examples
- `coannotation_HCAfine_x_author.csv` — full HCA_fine ↔ author-label crosswalk w/ cell counts
- `coannotation_rollup_dominant.csv` — dominant author label per HCA_fine × study
- `coannotation_HCAfine_x_Organ.csv`, `…_Developmental_stage.csv`
- `pull_obs.py` — reproducible remote obs-only puller

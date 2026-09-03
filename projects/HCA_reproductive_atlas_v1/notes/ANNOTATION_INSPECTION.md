# HCA Female Reproductive System Cell Atlas v1 — input inspection

**Atlas:** *An integrated multimodal pan-organ atlas of the female reproductive
system across the lifespan contextualises gynaecological pathologies*
(Cohen, Parraga-Leo, Rodríguez-Montes … Garcia-Alonso, Vento-Tormo).
bioRxiv **10.64898/2026.06.10.731198** (posted 2026-06-12, CC-BY 4.0).

- **Scale:** 2,235,448 high-quality cells · 291 donors · 27 datasets · **210 fine cell types**.
- **Organs:** ovary, fallopian tube, uterus, cervix, vagina.
- **Lifespan:** prenatal (1st/2nd trimester) → paediatric → reproductive age → postmenopausal, plus menstrual cycle (uterus, fallopian tube).
- **Modalities:** scRNA-seq (integrated via scVI), spatial (Visium/Xenium), scATAC-seq, GWAS integration.
- **8 major lineages:** epithelial, mesothelial, mesenchymal, endothelial, immune, granulosa/ovarian-supporting, germ cell, peripheral-nervous (neural crest-derived).
- CELLxGENE objects: https://www.reproductivecellatlas.org/HCAreproductive/v1/
- **Scope note:** the paper focuses on paediatric/adult; for prenatal cross-organ biology it defers to **Lorenzi et al. 2026** (`10.1038/s41586-025-09875-2`), which is one of the subatlases.

## Input file inventory (`inputs/`)

| File | Content | Use for reporter |
|---|---|---|
| `2026.06.10.731198v1.full.pdf` | Preprint main text (45 pp) | Atlas full text / narrative evidence |
| `media-1.docx` | Supplementary Notes 1–2 (extended methods + extended results) | Annotation rationale, nomenclature, novel-population narrative |
| `media-3 (2).xlsx` | **Supp Table 1** — sample/library metadata (scRNAseq samples, new fallopian tube, spatial samples, QC) | Provenance / donor context, not annotations |
| `media-4.xlsx` | **Supp Table 2** — cell classification. **Sheet B is the primary annotation table** | ★ Catalogue source |
| `media-5.xlsx` | **Supp Table 3** — targeted DEG tables | Marker evidence (limited scope, see below) |
| `media-6.xlsx` | GWAS / LDSC / LOO-LDSC-fGSEA results | Disease-association context |
| `media-7.xlsx` | scATAC sample metadata + disease peak–gene links | Regulatory evidence |
| `media-2 (1).pdf` | Supplementary figure PDF | Figures |
| `cell_ontology_mapping.xlsx` | **Manual first-pass CL mapping** (sheet `Final`, 238 cell types) | ★ CL seed mapping |
| `subatlas_pubs` | 22 DOIs (21 unique; 1 dup) of integrated source atlases | Citation-traversal seeds |

## Primary annotation table — `media-4.xlsx` sheet B (Supp Table 2B)

Header (row 6): `celltype_HCA | L1 | L2 | L3 | L4 | Markers_positive | Markers_negative (optional) | Celltype_description | Alternative_celltype_labels`

- **239 fine cell-type rows**, 4-level hierarchy (L1 lineage → L4 fine).
- **219 have positive marker lists** (`;`-delimited gene symbols); 37 have free-text descriptions; many have alternative/computational labels.
- Sheet A is a lighter 3-tier view (lineage / broad / fine, 209 rows).
- L1 lineage breakdown: Mesenchymal 75, Immune 54, Epithelial 53, Supporting-of-Ovary 13, Endothelial 13, Neural-crest 12, Germ 9, Mesothelial 7, Gonadal-somatic 4.

## DEG tables — `media-5.xlsx` (Supp Table 3): **targeted, not genome-wide**

These are **focused subset comparisons**, not per-cell-type one-vs-rest DEGs for all 210 types:

- **3A** `DEGs_macrophages_OnevRest` — macrophage subsets, one-vs-rest (up/down).
- **3B** `DEGs_uftLAM_vs_oLAM_PW` — uterus/fallopian-tube LAM vs ovarian LAM (the novel shared lipid-associated macrophage).
- **3C** `ILC3_NCRhi_Repro_vs_nonRepro` — reproductive NCRhi ILC3 vs non-reproductive mucosa.

→ For most cell types, marker evidence must come from **media-4 sheet B** + snippet traversal, **not** media-5. The DEG tables give deep marker evidence only for macrophages, LAMs, and ILC3s — which happen to be headline novel populations.

## Manual CL mapping — `cell_ontology_mapping.xlsx` sheet `Final`

- **238 cell types**, columns: `celltype_HCA, source_sheet, L1–L4, Perfect match, ID_perfect, Nearest match, ID_nearest, cell_type_ontology_term_id`.
- **59 perfect (exact) matches**, **183 nearest (broad/narrow) matches**; every row has a final `cell_type_ontology_term_id` filled.
- `source_sheet` encodes scope+lineage (e.g. `endothelial_fetal`, `immune_acrosslifespan`) — used to derive fetal vs postnatal scope in the catalogue.
- This is a strong seed for the reporter's CL-mapping step (can validate/refine rather than map from scratch).

## ⚠️ Label mismatches between annotation table and CL mapping (needs reconciliation)

12 labels differ between `media-4` sheet B and the CL mapping. Two classes:

**(a) Trivial `Fib` → `Fibs` typos — safe to auto-reconcile:**
`Mesen_GonadalFib_Undiff`↔`Mesen_GonadalFibs_Undiff`, `Mesen_MesonephricFib_Fetal`↔`…Fibs…`, `Mesen_OvarianFib_Fetal`↔`…Fibs…`, `Mesen_UterusFib_Fetal`↔`…Fibs…`, `Mesen_VaginaFib_Upper_Fetal`↔`…Fibs…`.

**(b) Genuine granularity/naming divergence — needs a human decision:**
- Granulosa: media-4 splits `Granulosa_AMHpos_{Antral,Cumulus,Prenatral,Primary}` and `smallPrenatral`; CL mapping collapses these to `Granulosa_AMHpos_Steroidogenic` / `…_nonSteroidogenic_early` (a coarser grouping).
- Germ cells: media-4 `Germcell_PrimaryOocyte_{Fetal,ZP4}` vs CL `…_{ZP4neg,ZP4pos}` (likely Fetal≈ZP4neg, ZP4≈ZP4pos — unconfirmed).
- `Epi_FallopianSec_OVGP1hi_EstrInd` appears **only** in the CL mapping, not in sheet B.

## Subatlas access via ASTA (Semantic Scholar) — 21 unique DOIs

**19 of 21 confidently traversable.** Two need a fallback (local paper index):
- `10.1126/science.adx0659` — **not indexed in Semantic Scholar** (very recent Science DOI); no CorpusId.
- `10.1093/cei/uxad029` (Huang 2023, endometriosis immune microenv.) — in SS but **non-OA, no PMC, no retrievable snippets**.
- `10.1016/j.devcel.2025.09.011` (Lardenois 2025) — indexed but currently **title/abstract only**, body snippets may be thin.

Full per-paper table (CorpusId, OA status, snippet check) in the ASTA-access section below.

| DOI | First author / year | Short title | CorpusId | OA | Snippets |
|---|---|---|---|---|---|
| 10.1172/jci.insight.195254 | Burns 2026 | Endometrium & decidua map | 284963281 | GOLD | likely |
| 10.1038/s41588-021-00972-2 | Garcia-Alonso 2021 | Endometrium temporal/spatial | 231614910 | HYBRID | likely |
| 10.1038/s41586-022-04918-4 | Garcia-Alonso 2022 | Human gonadal development roadmap | 236378833 | HYBRID | likely |
| 10.1126/science.adx0659 | — | (not in Semantic Scholar) | — | — | **NO** |
| 10.1038/s42003-022-04384-8 | Lustgarten Guahmich 2023 | Ovarian theca subtypes | 255473863 | GOLD | likely |
| 10.1002/ctm2.1219 | Guo 2023 | HPV cervical transition | 257765443 | GOLD | likely |
| 10.1093/cei/uxad029 | Huang 2023 | Endometriosis immune microenv. | 257334717 | **N** | **NO** |
| 10.1126/sciadv.adm7506 | Jones 2024 | Human ovary cellular atlas | 268956537 | GOLD | likely |
| 10.1016/j.devcel.2025.09.011 | Lardenois 2025 | Gonadal somatic sex determination | 282014485 | GREEN | thin (abs only) |
| 10.1038/s41467-020-20358-y | Li 2021 | Vaginal wall (prolapse) | 230508920 | GOLD | likely |
| 10.1038/s41586-025-09875-2 | Lorenzi 2025/26 | Developing repro tract (prenatal ref) | 283930036 | HYBRID | **Y** |
| 10.1038/s41588-024-01873-w | Marečková 2024 | Endometrium reference atlas | 272251688 | HYBRID | likely |
| 10.1172/jci.insight.153921 | Pique-Regi 2022 | Myometrium in parturition | 247312931 | GOLD | likely |
| 10.1016/j.devcel.2024.01.006 | Taelman 2024 | Fetal gonad & repro tract | 267359331 | HYBRID | likely |
| 10.1038/s41556-022-00961-5 | Tan 2022 | Endometriosis scRNA | 263476245 | GREEN | likely |
| 10.1016/j.devcel.2022.02.017 | Ulrich 2022 | Fallopian tube / hydrosalpinx | 263504996 | BRONZE | likely |
| 10.1073/pnas.2404775121 | Ulrich 2024 | Premenopausal uterus | 273703178 | (PMC) | **Y** |
| 10.1038/s41467-020-14936-3 | Wagner 2020 | Ovarian cortex | 211574066 | GOLD | likely |
| 10.1016/j.devcel.2023.07.014 | Wamaitha 2023 | Developing ovary progenitors | 260914233 | HYBRID | likely |
| 10.1038/s41591-020-1040-z | Wang 2020 | Endometrium menstrual cycle | 221723862 | GREEN | likely |
| 10.1038/s41467-024-55440-2 | Weigert 2025 | Fallopian tube (cycle/menopause) | 275303631 | (PMC) | **Y** |

## Headline novel populations (priority report targets from the preprint)

- **Uterine-specific perivascular cells**: `Pericyte EndoSpiralArt` (spiral-artery pericytes, STC2/FLT1+, RERGL−), `Pericyte EndoStromalLike` (RGS5+PDGFRA+MMP11+), `vSMCs large vessel` (RGS5+, uterus-restricted).
- **NCRhi ILC3s** enriched in uterus (Supp Table 3C).
- **Lipid-associated macrophages (LAMs)** — organ-specific subsets + a **previously undescribed uterus/fallopian-tube shared subset** (uftLAM; Supp Table 3B).
- **Adventitial fibroblasts (AdvFib)** — a distinct pan-reproductive compartment (DPT/SFRP2/C3+; PI16hi → C7/COL15A1hi continuum) overlooked in prior atlases.
- **Ectopic endometrial-like epithelial cells** in a paediatric ovary (early-endometriosis-consistent).
- **PMOS GWAS link**: PolyendocrineMetabolic OS risk locus → *INHBB* in granulosa cells.

## Deliverables written

- `cell_type_annotations.json` — first-pass catalogue (250 entries = 239 fine types + unmatched CL-only labels), schema-conformant (`label`/`granularity`/`scope`) and enriched with L1–L4 hierarchy, positive/negative markers, descriptions, alternative labels, and manual CL term IDs. `scope`: `*_fetal`→fetal (49), else adult/postnatal (201).

## Still outstanding

- **h5ad files not yet provided** — may add author-provided obs columns / DEGs. Re-run the `anndata-zarr-summary` skill on them when available to cross-check labels and pull co-annotation stats.
- Reconcile the 12 label mismatches (a: auto; b: needs human).
- `media-1.docx` extended results not yet fully parsed (python-docx not installed; TOC extracted). Parse for per-population narrative when drafting reports.

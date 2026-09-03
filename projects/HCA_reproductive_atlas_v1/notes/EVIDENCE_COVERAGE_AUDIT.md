# Evidence coverage audit — subatlas reachability, open data, and fallbacks

**Written:** 2026-09-01 · Branch `HCA_reproductive_atlas_v1`
**Scope:** which subatlas papers the reporter can actually reach, which cell types
are exposed by the gaps, and what open data exists for downstream test fixtures.

All cell counts derive from the committed `h5ad_obs/obs.categoricals.parquet`
(2,235,448 cells × 56 categorical columns) — no network access needed to
reproduce them. Marker/description coverage comes from `inputs/media-4.xlsx`
sheet B (Supp Table 2B).

---

## 1. Subatlas paper count and DOI ↔ dataset reconciliation

`inputs/subatlas_pubs` lists **22 DOIs = 21 unique papers**
(`10.1016/j.devcel.2025.09.011` appears twice).

The h5ad `Dataset` column has **27 categories**. The two counts do not
reconcile cleanly:

| Discrepancy | Detail |
|---|---|
| **6 `Sanger_*` datasets have no DOI** | `Sanger_Endometrium` (258,989), `Sanger_PediatricOvary` (238,143), `Sanger_MenstrualFluid` (81,812), `Sanger_AdultOvary` (78,897), `Sanger_FallopianTube` (49,832), `Sanger_Uterus` (39,041) — **748,714 cells, 33.5% of the atlas**. This is the preprint's own newly generated data. |
| **`Liu 2025` has no DOI** | 71,818 cells. Not matched to any entry in `subatlas_pubs`. **Needs author query.** |
| **`10.1172/jci.insight.153921` has no dataset** | Pique-Regi 2022 (myometrium in parturition) is seeded but no `Dataset` value corresponds to it. Either dropped from the final integration or merged into a `Sanger_*` object. **Needs author query.** |

⚠️ **Correction to an earlier working assumption:** `10.1126/science.adx0659` is
**Gaylord et al. 2026** (Science; first author Eliza A. Gaylord — confirmed from
`local_index/papers/10.1126_science.adx0659/chunks/chunks.fulltext.txt`), which
maps to the `Gaylord 2025` dataset. It is *not* a missing DOI. Note also that
the `celltype_OvarySanger2026` author-label column is a **separate** annotation
spanning `Sanger_PediatricOvary`, `Sanger_AdultOvary` and `Garcia-Alonso 2022`
— do not conflate it with the Gaylord paper.

### Dataset → author-label column map

Derived by counting non-null author labels per dataset. Useful as the
name-resolution bridge back to original study nomenclature.

| Dataset | n cells | Author label column (n labelled) |
|---|---|---|
| Lorenzi 2025 | 286,893 | `Lorenzi2025` (279,195) |
| Garcia-Alonso 2022 | 221,740 | `GarciaAlonso2022` (185,264), `OvarySanger2026` (91,418), `Lorenzi2025` (22,332) |
| Weigert 2025 | 149,729 | `Weigert2025` (102,518) |
| Huang 2023 | 101,682 | `HECA` (64,193) |
| Garcia-Alonso 2021 | 88,226 | `GarciaAlonso2021` (38,488), `Ulrich2024` (41,366), `HECA` (31,025) |
| Sanger_PediatricOvary | 238,143 | `OvarySanger2026` (196,991) |
| Sanger_AdultOvary | 78,897 | `OvarySanger2026` (52,995) |
| Lardenois 2026 | 66,472 | `Lardenois2026` (62,201) |
| Wang 2020 | 63,098 | `HECA` (47,085), `GarciaAlonso2021` (40,903), `Ulrich2024` (32,230) |
| Ulrich 2022_FallopianTube | 54,043 | `Ulrich2022` (48,497) |
| Ulrich 2024_Uterus | 50,689 | `Ulrich2024` (42,386) |
| Mareckova 2024 | 77,850 | `HECA` (8,301) |
| *(13 others)* | — | no author label column |

⚠️ **Gotcha for anyone re-running this:** in this pandas version
`Series.astype(str)` on a categorical **preserves NaN as NaN** rather than
producing the string `'nan'`. Test missingness with `.notna()`; a
`.astype(str) != 'nan'` filter silently returns True for every row.

---

## 2. Subatlas papers ASTA cannot serve

Per the access audit recorded in `ANNOTATION_INSPECTION.md`:

| DOI | Study | Problem |
|---|---|---|
| `10.1126/science.adx0659` | Gaylord et al. 2026 (Science, ovarian aging) | Not indexed in Semantic Scholar — **no CorpusId at all** |
| `10.1093/cei/uxad029` | Huang 2023 (endometriosis immune microenv.) | Indexed but non-OA, no PMC — **no retrievable snippets** |
| `10.1016/j.devcel.2025.09.011` | Lardenois 2026 (gonadal sex determination) | Indexed, **title/abstract only** — body snippets thin |

⚠️ **Not independently re-verified on 2026-09-01.** No `snippet_search` tool was
loaded in that session, and the Semantic Scholar MCP endpoint returned empty
results for every query *including a control on a paper known to be indexed*
— so a negative result there proves nothing. The table above is the prior
audit carried forward. Re-verify before relying on it.

**All three are already covered by the local snippet index**
(`local_index/papers/`), so they are reachable via
`services.citation_traverser.traverse_local`:

| Local index paper | Snippets |
|---|---|
| `10.1126_science.adx0659` | 93 |
| `10.64898_2026.06.10.731198` (atlas preprint) | 90 |
| `10.1016_j.devcel.2025.09.011` | 58 |
| `10.1093_cei_uxad029` | 34 |

---

## 3. Cell-type exposure to unreachable sources

Per-cell-type dataset composition, keyed on `celltype_HCA_fine` (212 types).
Full table committed alongside this doc as **`asta_coverage.csv`** (columns:
`n_cells`, `pct_ASTAblind`, `pct_noDOI`, `pct_unreachable`,
`top_unreachable_src`, `top_src_pct`; sorted by `pct_unreachable`).

**Headline: 78 of 212 fine cell types (37%) draw a majority of their cells
from sources ASTA cannot reach.** Split into two very different problems.

### 3a. ASTA-blind *published* studies — 7 cell types ≥50%

Recoverable via the local index. Low priority.

| `celltype_HCA_fine` | n cells | % blind | Driver |
|---|---|---|---|
| `Epi_EndoGlandBas` | 748 | 96.1 | Huang 2023 |
| `Epi_OvarianInclSec` | 202 | 91.1 | Gaylord 2025 |
| `Germcell_PGC_Cyc` | 2,592 | 70.8 | Lardenois 2026 |
| `Epi_OvarianInclCil` | 20 | 60.0 | Gaylord 2025 |
| `Gonadal_SupportingUndiff` | 16,769 | 58.8 | Lardenois 2026 |
| `Mesen_OvarianFibs_AdvLike` | 507 | 58.0 | Gaylord 2025 |
| `Germcell_PGCs` | 6,862 | 54.9 | Lardenois 2026 |

⚠️ `Epi_OvarianInclCil` / `Epi_OvarianInclSec` are **headline report targets**
(the rare ovarian-inclusion epithelia of preprint Figure 5) and are ~90%
Gaylord cells — the one paper with no CorpusId whatsoever. They are also tiny
(20 and 202 cells). Doubly fragile; route explicitly through the local index.

### 3b. Sources with no publication at all — 48 cell types ≥50%

`Sanger_*` and `Liu 2025`. **Nothing to traverse — the primary atlas paper is
the only citable source.** Worst-affected blocks:

| Compartment | Examples (≥90% no-DOI) | Driver |
|---|---|---|
| Ovarian fibroblasts | `Mesen_OvarianFibs_InncorMedulla` (125,985 cells, 92.9%), `_Perifol` (44,411, 95.6%), `_Outcor` (21,434, 96.1%) | Sanger_PediatricOvary |
| Granulosa | `Granulosa_AMHneg_Squamous` (99.2%), `AMHpos_nonSteroidogenic` (95.7%), `AMHpos_Steroidogenic` (95.2%) | Sanger_PediatricOvary |
| Menstrual fluid | `Mesen_EndoStromalFib_MenstrualFluid` (27,092, 99.8%), `Immune_uMac_Inf` (23,069, 96.6%), `Epi_EndoGlandFun_Menstr` (98.7%) | Sanger_MenstrualFluid |
| Endometrial stroma | `Mesen_EndoStromalFib_nEMC` (48,007, 80.3%), `_nEMC_Cyc` (89.3%) | Sanger_Endometrium |

---

## 4. Is the atlas paper enough for the 48? Mostly yes

Coverage of those 48 cell types in the atlas's own evidence:

| Evidence available | Count |
|---|---|
| Present in Supp Table 2B | **44 / 48** |
| Has a positive marker list | **40 / 48** |
| Has a free-text `Celltype_description` | **10 / 48** |

Marker evidence — a legitimate, citable primary source — exists for the large
majority. The preprint itself is in the local index (90 snippets), so narrative
context is reachable for the headline populations
(`Mesen_Pericyte_EndoSpiralArt`, `Mesen_AdvFibsIntr`, `Immune_oLAM`,
`Mesen_Pericyte` are all discussed in main text).

### The 7 genuine dead ends

≥50% Sanger/Liu cells **and** no markers **and** no description:

| `celltype_HCA_fine` | n cells | % no-DOI | In Supp T2B? |
|---|---|---|---|
| `Granulosa_AMHpos_Steroidogenic` | 15,814 | 95.2 | ❌ |
| `Granulosa_AMHpos_Atretic` | 5,440 | 54.2 | ✓ (empty row) |
| `Mesen_EndoStromalFib_Menopause` | 2,855 | 85.3 | ✓ (empty row) |
| `Granulosa_AMHpos_nonSteroidogenic_early` | 1,267 | 94.4 | ❌ |
| `Neural_Schwann` | 781 | 79.6 | ✓ (empty row) |
| `Granulosa_AMHpos_nonSteroidogenic` | 694 | 95.7 | ❌ |
| `Germcell_PrimaryOocyte_ZP4pos` | 391 | 73.1 | ❌ |

The four marked ❌ are the **CL-mapping-only labels** already flagged as class
(b) granularity divergence in `ANNOTATION_INSPECTION.md` — present in
`cell_ontology_mapping.xlsx` but absent from sheet B. They have no data source
*and* no annotation row: nothing to synthesise from in either runtime. **These
need the author reconciliation resolved, not more traversal.**

### Unpulled lever

`inputs/media-1.docx` (Supplementary Notes 1–2) is still unparsed —
`python-docx` was unavailable, only the TOC was extracted. Note 2.1 is cited in
the preprint exactly where epithelial sublineage rationale lives. Per-population
annotation narrative is the content that would fill the description gap for the
**38 cell types that have markers but no description**. Highest-value remaining
extraction for the Sanger-only block.

⚠️ **Metric that did not work:** counting verbatim `celltype_HCA_fine` labels in
the preprint full text undercounts badly — the paper uses display names
(`Pericyte EndoSpiralArt`, `AdvFib PI16hi`) rather than underscore labels. Only
5/48 matched exactly. Do not use text-mention counts as a coverage signal;
Supp Table 2B presence is the reliable measure.

---

## 5. Open-data provenance (for the parallel FT multiciliated project)

**Requirement:** fallopian tube multiciliated cell profiles from an open source,
ideally paired with spatial transcriptomics confirming location.

⚠️ **The integrated h5ad is not a usable public source.** The recorded URL
`https://cellgeni-share.cog.sanger.ac.uk/REQ-69024/integrated_scvi_all_tissues_cellxgene_filtered.h5ad`
now returns **HTTP 404** (checked 2026-08-20). It is a REQ-scoped
Sanger-internal share, not cited in the preprint, and not citable.

### Provenance of the 14,392 `Epi_FallopianCil*` cells

| Source dataset | Cells | Accession | Open? |
|---|---|---|---|
| Weigert 2025 | 7,281 | `EGAS50000000628` | ❌ **EGA controlled access** |
| Sanger_FallopianTube | 3,348 | *none* | ❌ no accession yet |
| **Ulrich 2022** | **3,247** | **`GSE178101`** | ✅ **GEO, fully open** |
| Garcia-Alonso 2022 | 391 (fetal) | `E-MTAB-10551` | ✅ open |
| Lorenzi 2025 | 125 (fetal) | `E-MTAB-15475` | ✅ open |

The trap: the largest contributor (Weigert, 51%) is controlled-access, and the
second (`Sanger_FallopianTube` — precisely the CW21/CW6 donors carrying the
matched Visium HD / Xenium) has no public accession. **The spatially-paired
cells are exactly the ones that are not yet open.**

### Recommended fixture: Ulrich 2022 / GSE178101

Barcodes join directly — the integrated obs index is `{GSM}_{barcode}`
(e.g. `GSM5380100_ATCGATGAGTACTGGG-1`). GEO serves per-sample gzipped count
matrices individually (5–26 MB each; no need for the 223 MB RAW tar).

| GSM | Multiciliated cells | Region | Donor |
|---|---|---|---|
| GSM5380103 | 1,692 | Fimbria | FT2 |
| GSM5701416 | 415 | FT (unspec.) | FT4 |
| GSM5380104 | 336 | Ampulla | FT2 |
| GSM5380108 | 312 | Fimbria | FT3 |
| *(6 more)* | 60–105 each | mixed | FT1–FT3 |

For a 1,500-cell test: `GSM5380103` alone (one 23 MB file, single region), or
`GSM5380103` + `GSM5380104` + `GSM5380105` (donor FT2, all three regions,
2,118 cells, ~72 MB) subsampled to 1,500.

**Label agreement:** of Ulrich cells carrying an original author label,
**1,678/1,682 (99.8%)** are `ciliated epithelial cell` in Ulrich's own
annotation (4 are `secretory cell`). Caveat: only ~52% (1,682/3,247) carry a
populated `celltype_Ulrich2022` value; the rest rely on the integrated label alone.

### Note on row-subsetting the integrated h5ad

Technically viable had the URL been live: `X` in an h5ad is normally CSR, where
each cell is a **contiguous run** in `data`/`indices`. Read the small `indptr`,
then one range request per selected row — 1,500 rows ≈ 20–50 MB transferred,
not 92.8 GB. Same mechanism as `h5ad_obs/pull_obs.py`. Non-contiguity across
cells is not the blocker. Moot here: URL 404s, and it is VPN-gated and
non-citable regardless.

### Spatial gap

Ulrich 2022 is scRNA-seq only. Options for the spatial half:

1. **Split the requirement** — open scRNA-seq from GSE178101 for profiles, plus
   Hikmet et al. 2026 (`10.1038/s41467-026-71692-6`, CC-BY, HPA cilia protein
   map of FT) for location. Spatial *protein*, not transcriptomics.
2. **Fetal only, fully paired and open** — Lorenzi 2025 (`E-MTAB-15475`) has
   both modalities, all public, but only 125 multiciliated cells.
3. **Wait / ask** — the `Sanger_FallopianTube` data with matched Visium HD +
   Xenium gets an accession at journal publication. Vento-Tormo's group is
   in-house; asking about the planned accession is cheap.

Checked and rejected: **Weigert 2025** (scRNA + scATAC, no spatial) and
**Ulrich 2022** (scRNA only) — neither has spatial transcriptomics.

---

## 6. Actions

**Author queries (blocking for affected cell types)**
- [ ] What publication does `Liu 2025` (71,818 cells) correspond to?
- [ ] Why does Pique-Regi 2022 (`10.1172/jci.insight.153921`) have no dataset?
- [ ] Resolve the 4 CL-mapping-only granulosa/germ-cell labels (class (b)
      divergence) — they are unreportable as they stand.
- [ ] Planned public accession + timing for the `Sanger_*` datasets.

**Pipeline**
- [ ] Make local-index routing **explicit** for the 7 ASTA-blind cell types,
      especially `Epi_OvarianInclCil` / `Epi_OvarianInclSec`.
- [ ] Re-verify the three ASTA access failures once `snippet_search` is
      available and the Semantic Scholar endpoint is responding.
- [ ] For the 48 Sanger-only cell types, constrain synthesis to the atlas
      preprint + Supp Table 2B markers and have reports say so, rather than
      reaching into adjacent literature.

**Extraction**
- [ ] Parse `inputs/media-1.docx` Supplementary Note 2 for per-population
      narrative — fills the description gap for 38 cell types.

**Parallel FT project**
- [ ] Fetch + subsample GSE178101 (`GSM5380103`/`104`/`105`) to a 1,500-cell
      open fixture, joined to integrated labels by `{GSM}_{barcode}`.

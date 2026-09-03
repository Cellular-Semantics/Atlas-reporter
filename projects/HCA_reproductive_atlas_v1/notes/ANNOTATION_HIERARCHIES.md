# Annotation hierarchies — HCA Female Reproductive System Cell Atlas v1

**Atlas:** *An integrated multimodal pan-organ atlas of the female reproductive
system across the lifespan* (Cohen et al.; Garcia-Alonso & Vento-Tormo labs).
bioRxiv **10.64898/2026.06.10.731198**. 2,235,448 cells · 291 donors · 27 datasets.

**Purpose of this note:** map how the cell-type annotations are structured across
the three sources we hold — the integrated **h5ad** obs, the **`cell_ontology_mapping.xlsx`**
spreadsheet, and **`media-4.xlsx`** (Supp Table 2) — how they relate, whether the
hierarchies are clean subsumption trees, how they line up with the DEG tables, and
what that implies for representation. All numbers below are measured, not asserted.

Sources:
- h5ad obs (obs-only remote pull): `h5ad_obs/obs.categoricals.parquet` (see `h5ad_obs/OBS_SUMMARY.md`)
- `inputs/cell_ontology_mapping.xlsx` sheet `Final` (manual CL mapping, 238 rows)
- `inputs/media-4.xlsx` sheet B (Supp Table 2B annotation table, 239 rows) + sheet A (3-tier view)
- `inputs/media-5.xlsx` (Supp Table 3, DEGs)

---

## 1. There are TWO parallel hierarchies in the h5ad, not one

The obs carries **six** cell-type columns. They resolve into two distinct axes plus a cross-link.

### Axis A — computational cluster tree (the annotation levels)
```
celltype_HCA_lineage (8)  ⊃  celltype_HCA_broad (98)  ⊃  celltype_HCA (149)  ⊃  celltype_HCA_fine (212)
```
Nesting (measured "child → exactly one parent"):

| child → parent | result |
|---|---|
| celltype_HCA_fine → celltype_HCA | **212/212 ✓ strict tree** |
| celltype_HCA → celltype_HCA_broad | 147/149 (2 boundary exceptions) |
| celltype_HCA_fine → celltype_HCA_broad | 211/212 — only `Mesen_Pericyte` spans 2 broad classes |
| celltype_HCA_broad → celltype_HCA_lineage | **98/98 ✓ strict tree** |

`celltype_HCA` (149) is an **intermediate level between broad and fine** (fine nests
perfectly into it). It is the "main" published label; `fine` adds extra splits
(cycling states etc.). **`celltype_HCA_fine` (212) is the canonical leaf set** and the
one the reporter should key on — it matches the paper's ~210 fine types.

### Axis B — structured ontology nomenclature (human-readable naming)
```
ontology_level1 (8)  ⊃  level2 (24)  ⊃  level3 (57)  ⊃  level4 (117)
```
All levels nest cleanly (apart from `empty` placeholder fills). This is the
HCA-Reproductive-Network nomenclature, a *separate* axis from A.

### The cross-link
`celltype_HCA_fine → ontology_level4` is a clean **212/212** tree: every leaf maps to
exactly one level-4 nomenclature node. So B hangs off the leaves of A; the two axes
meet only at the leaf.

**Consequence for representation:** CAS `parent_cell_set_accession` encodes a *single*
parent chain. Use **Axis A as the CAS hierarchy** (lineage → broad → celltype_HCA → fine,
ranks 3→0) and attach **Axis B (ontology_level1–4 names) as a per-annotation nomenclature
block**, not as the parent chain.

---

## 2. The spreadsheet hierarchy (`cell_ontology_mapping.xlsx`) IS a clean subsumption tree — after one typo fix

The spreadsheet defines its **own** L1→L2→L3→L4 hierarchy over 238 cell-type rows,
carrying a CL term per row. This is *not* the same value set as the h5ad ontology levels
(it is richer: 9 / 34 / 101 / 160 distinct values vs the h5ad's 8 / 24 / 57 / 117, and only
partially overlapping). Tree test ("does each node have exactly one parent"):

| level | result |
|---|---|
| L2 → L1 | **34/34 ✓ clean** |
| L3 → L2 | 97/101 — 4 "violations" |
| L4 → L3 | **160/160 ✓ clean** |
| leaf labels | **0 duplicated** (each cell type appears once) |

**The 4 L3 violations are one typo, not a structural defect.** `Cervix stroma`,
`Fallopian tube stroma`, `Ovarian stroma`, `Vagina stroma` each appear under two L2
parents that are the same class spelled two ways: `Stromal-interstitial fibroblast`
vs `Stromal-interstitial fibroblast`**s** (singular/plural — the same `Fib`/`Fibs`
class of typo seen in the leaf labels). **Normalise that one string → the tree is
clean at every level.**

**It is a ragged tree** (legitimate, but the builder must handle it): leaves attach at
different depths, not all at L4 — attachment depth distribution **L1: 3, L2: 20, L3: 55,
L4: 160**. So "L4 = leaf's parent" is not uniform; read "deepest non-blank L-column" per row.

---

## 3. Three-way reconciliation: spreadsheet ≈ media-4, both a superset of the h5ad leaves

| set | size |
|---|---|
| media-4 sheet B (`celltype_HCA` col) | 239 |
| media-4 sheet A (fine col) | 209 |
| CL-mapping spreadsheet | 238 |
| **h5ad `celltype_HCA_fine`** | **212** |
| h5ad `celltype_HCA` | 149 |

- **The CL-mapping spreadsheet ≈ media-4 sheet B** — 227 of ~238 labels identical (the
  ~11 diffs are the `Fib`/`Fibs` typos + granularity splits). The spreadsheet was built
  *from* media-4 sheet B + a CL term + its own L1–L4. Not an independent source.
- **Both are a ~238-label superset of the 212 h5ad leaves.** CL-map ∩ `celltype_HCA_fine`
  = **211/212** (the single miss is `Endo_cap_APCDD1+` vs spreadsheet `Endo_cap_APCDD1` —
  a trailing-`+` formatting diff).
- media-4 sheet A (the light lineage/broad/fine export) aligns to the leaves at only 187/209.

### The 27 spreadsheet rows "coarser than the leaf"
The spreadsheet's flat label column is **mixed-granularity**: 211 leaves + **27 coarser/other**
rows that also receive a CL term. Triage:

- **13 = h5ad *broad*-level labels** (genuine internal/parent nodes, already CL-mapped — a
  bonus): `Endo_ven`, `Epi_EndoCil`, `Epi_EndoGland`, `Epi_EndoGlandFun`, `Epi_EndoGlandLum`,
  `Epi_FallopianCil`, `Epi_FallopianSec`, `Granulosa_AMHpos`, `Mesen_EndoStromalFib`,
  `Mesen_OvarianFibs`, `Mesen_Theca`, `Mesen_vSMCs`, `Neural_SympatheticNeurons`.
- **14 = not in any h5ad cell-type column**, two kinds:
  - **umbrella/ancestor terms** (shallow): `Endo`, `Germcell`, `Germcell_Oocyte`,
    `Mesothelial`, `Epi_Sec`, `Epi_Squamous`, `Epi_Mucinous`, `Mesen_StromalFibs`,
    `Mesen_InterstitialFibroblast` — likely duplicate L1/L2 nomenclature nodes.
  - **fetal / out-of-scope types** (flagged by `source_sheet`): `Mesen_SMCs_Fetal`,
    `Gonadal_rete_Fetal_Undiff`, `Epi_FallopianSec_EstrInd`, `Mesen_AdvFibs_PI16low_Vagina`
    — cells that live in a fuller/prenatal object (e.g. Lorenzi 2025), empty in this h5ad.

**Handling for tree-building:** keep the 13 broad-node rows as internal nodes (CL done ✓);
decide whether the ~9 umbrella rows attach to the L-level node or a label-row; drop or defer
the ~5 fetal rows for this (postnatal-filtered) object.

---

## 4. CL-subsumption consistency of the manual mapping (13 internal nodes vs their children)

Does the spreadsheet's own hierarchy respect CL subsumption — i.e. for each of the 13
broad-node CL terms, are the CL terms of its fine children actually `is_a` descendants
(via OLS4 `cl`)? Result: **11 of 13 consistent, 2 flagged.**

- **9 trivially consistent** — children carry the *same* CL term as the parent (CL is not
  granular enough to distinguish the fine subdivisions; e.g. `Epi_EndoGlandFun`'s 7 children
  all → CL:0009084). This is *why* new CL terms get requested.
- **2 confirmed consistent** (children are genuine CL descendants):
  - `Mesen_Theca` → CL:0000503 (theca cell); children → **CL:4052012, CL:4052013**, both `is_a` theca cell ✓ (new CL terms, likely minted for reproductive work).
  - `Neural_SympatheticNeurons` → CL:0011103 (sympathetic neuron); child → **CL:3000002** `is_a` sympathetic neuron ✓.
- **2 INCONSISTENT — flag for the authors:**
  - **`Endo_ven`** mapped to **CL:0002543** (*vein endothelial cell*), but its children map to
    **CL:0002652** (*endothelial cell of vein*) and **CL:1000414** (*endothelial cell of venule*),
    which sit under *endothelial cell of vascular tree* / *blood vessel endothelial cell* —
    **not** under CL:0002543. Driver: CL carries two near-synonymous "vein endothelial"
    terms that are not nested. **Fix:** align the parent to a term that is an ancestor of the
    children (e.g. CL:0002139) or switch the children to CL:0002543's subtree.
  - **`Mesen_OvarianFibs`** mapped to **CL:0000057** (*fibroblast*), but child **CL:0002132**
    (*stromal cell of ovary*) sits under *stromal cell* (CL:0000499), **not** fibroblast.
    This is a genuine semantic tension (are ovarian stromal cells fibroblasts?) — a real
    modelling decision, not a typo.

**Takeaway:** the manual CL mapping is largely subsumption-consistent; the two flagged
cases are worth resolving before adopting the spreadsheet hierarchy as canonical.

---

## 5. DEG tables (`media-5.xlsx`) attach only at the leaf — nothing at upper levels

The supplementary DEGs are **not** systematic per-cell-type DEGs at any level; they are three
targeted analyses:

| table | what it is | keyed on |
|---|---|---|
| **3A** DEGs_macrophages_OnevRest | one-vs-rest **within the macrophage compartment**, one gene-block per subset | `HCA_celltype_label` = **fine** (`Immune_uftLAM`, `Immune_Mac_LYVE1hi`, `Immune_oLAM`, …) |
| **3B** DEGs_uftLAM_vs_oLAM | a single **fine-vs-fine** pairwise contrast | `Immune_uftLAM_vs_Immune_oLAM` |
| **3C** ILC3_NCRhi_Repro_vs_nonRepro | a **tissue** contrast within one cell type (not a cell-type DE) | `ReproTract_vs_NonReproTract` |

Consequences:
- **Zero DEGs at `broad`, `celltype_HCA`(149), or `lineage`.** Even at leaf level only ~a dozen
  immune/macrophage types are covered, and 3A's "one-vs-rest" is within-compartment, not atlas-wide.
- Upper-level DEGs would require **roll-up** or **recomputation from the expression matrix**
  (the 92.8 GB h5ad `X`, not pulled).
- The **systematic, all-types marker evidence** the paper actually provides is the curated
  positive/negative marker lists in **media-4 sheet B** — those propagate up a subsumption tree;
  DE statistics do not.

---

## 6. Recommended representation (working proposal)

1. **One extended-CAS document** (Variant B; schema at
   `src/atlas_chat/atlas_chat/schemas/cas_annotation.schema.json`) as canonical — it subsumes
   the rollup CSVs: `transferred_annotations` = subatlas author-label co-annotation
   (cell_count/cell_ratio), `composition` = tissue/stage/disease distributions,
   `marker_gene_evidence` = media-4 markers, `cell_ontology_term_id` = manual CL mapping.
2. **Hierarchy = Axis A** (lineage → broad → celltype_HCA → fine) via `rank` +
   `parent_cell_set_accession`. **Axis B** (ontology_level1–4) and the spreadsheet's L1–L4 attach
   as a per-annotation **nomenclature block**, not the parent chain.
3. **Materialise at every labelset level** (per the decision on this project): each level gets its
   own annotations with **set-relative** composition + transferred distributions; add labelset-level
   `coverage_ratio` / `n_cells_labelled` so global %labelled survives.
4. **Composition key = verbatim obs column name** (e.g. `Organ_part`); ontology mapping deferred and
   kept in a separate classify-obs-fields artifact, never by mutating keys/values.
5. **Before adopting the spreadsheet hierarchy as canonical:** fix the `fibroblast`/`fibroblasts`
   L2 typo; resolve the 27 coarser rows (§3); resolve the 2 CL-subsumption inconsistencies (§4);
   confirm handling of the `Mesen_Pericyte` fine→broad multi-parent case (§1).

---

## Appendix — open items feeding back to the author discussion
- `celltype_OvarySanger2026` = newly-generated Sanger ovary data (no external DOI) — see `OBS_SUMMARY.md`.
- `celltype_HECA` DOI (Marečková 2024) is tentative.
- No CELLxGENE-Discover standard ontology columns present; metadata is HCA-schema free text (see `OBS_SUMMARY.md`).
- `Endo_cap_APCDD1` (spreadsheet) vs `Endo_cap_APCDD1+` (h5ad) — reconcile the trailing `+`.

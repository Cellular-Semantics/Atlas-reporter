# Annotation source reconciliation — for author updates

**Atlas:** Human Female Reproductive System Cell Atlas v1 (bioRxiv 10.64898/2026.06.10.731198).

**Purpose.** While assembling a unified, ontology-linked cell-type annotation
(a Cell Annotation Schema / CAS export) from the three annotation sources, we
found a small set of inconsistencies *between the sources*. This document lists
them precisely so they can be corrected — primarily in
**`cell_ontology_mapping.xlsx`**, and in several cases in **media-4.xlsx
(Supplementary Table 2)** for journal resubmission, plus one fix in the **h5ad
object** annotation.

**The three sources and how they relate**

| source | what it provides | role in the build |
|---|---|---|
| **h5ad object** (`integrated_scvi_all_tissues…filtered.h5ad`) `obs.celltype_HCA_fine` | the actual per-cell leaf labels (212 fine types) | **ground truth for cells** — the leaf identity |
| **`cell_ontology_mapping.xlsx`** (sheet `Final`) | per-leaf L1–L4 nomenclature + Cell Ontology (CL) term | **the master hierarchy** (L1–L4) + CL mapping |
| **media-4.xlsx** sheet B (Supp Table 2) | per-leaf markers (+/−), descriptions, synonyms, L1–L4 | **markers & evidence** |

**Key overall finding:** the **h5ad object and `cell_ontology_mapping.xlsx`
agree** on cell-type labels; **media-4 is the out-of-date source** in three
places (B1–B3 below). Importantly, the build **auto-normalises the trivial
spelling drift** (singular/plural `Fib`/`Fibs`, trailing `+`), so those markers
*do* attach and the CAS export is complete — the edits requested for **A, B1 and
C are for source hygiene / publication cleanliness, not to make the build work**.
The only divergences that genuinely block marker attachment are the **different
subtyping schemes** (B2 Granulosa, B3 oocyte), which are real relabellings, not
spelling variants, and so cannot be reconciled automatically. One further issue
is a duplicate label inside the **h5ad object** itself (C).

---

## Alignment strategy used in the build

**The join.** All three sources are keyed on the **fine leaf code**. Explicitly,
the build joins:

```
obs.celltype_HCA_fine
   ==  cell_ontology_mapping.xlsx[sheet "Final"].celltype_HCA
   ==  media-4.xlsx[sheet "B. HCA_femaleRepSys_v1_celltype"].celltype_HCA
```

⚠️ Both spreadsheet key columns are *labelled* `celltype_HCA`, but their **values
are the fine leaf codes** — they match the object's `celltype_HCA_fine` (212
types), **not** the coarser 149-way `obs.celltype_HCA`. (This mislabelling is
issue **D3**.) The object's `celltype_HCA_fine` is the single source of truth for
which cells exist; the spreadsheets only annotate those codes.

Step by step, each with a worked example:

1. **Leaf = `obs.celltype_HCA_fine`** — the labels actually applied to cells; the
   key everything else is looked up by.
   *Example:* the per-cell label `Mesen_AdvFibs_PI16hi` (3,032 cells) is a leaf;
   both spreadsheets are joined to it by this exact string.

2. **Hierarchy = L1→L2→L3→L4** from `cell_ontology_mapping.xlsx`, built up from
   the leaf. **Assumption: the deepest non-blank L-column of a row is the
   human-readable full name of that leaf code.** *(Sanity-checked: the deepest-L
   value is unique per leaf — 0 duplicated leaf names — and
   `celltype_HCA_fine → ontology_level4` is a clean 212/212 map, so a leaf never
   carries two full names.)*
   *Example:* `Mesen_UterusFibs_Fetal` → L1 `Mesenchymal` · L2 `Stromal-interstitial
   fibroblasts` · L3 `Uterine interstitial fibroblast` · L4 `Fetal uterine
   stromal fibroblast`; the L4 string is taken as its full name.

3. **Skip-level, ragged tree** — a leaf attaches at its deepest *defined* tier;
   blank deeper columns are not padded with synthetic nodes.
   *Example:* `Mesen_GonadalFibs_Undiff` has L4 blank, so it attaches at L3
   `Gonadal fibroblast` — no artificial L4 is invented.

4. **Markers** joined from media-4 by the same leaf code. For broad/supertype
   media-4 rows that match no leaf, markers attach to the matching internal
   nomenclature node by its L-path terminal string.
   *Example:* media-4 row `Mesen_AdvFibs_PI16hi` → `PI16;CD34;DPP4;SFRP2;C3;IL33;MFAP5;…`
   attach to that leaf; the broad row `Mesen_Theca` (no leaf of its own) → its
   markers attach to the internal node named `Theca`.

5. **CL terms** taken from `cell_ontology_mapping.xlsx` (one per row), attached at
   each code's terminal node.
   *Example:* `Mesen_AdvFibs_PI16hi` → CL:4052030 (*adventitial fibroblast*).

**Trivial spelling drift is normalised at join time — the source files do NOT
have to be fixed first for the build to succeed.** Three classes of cosmetic
mismatch are absorbed automatically so markers and CL terms still attach:

| drift | how the build absorbs it | issue |
|---|---|---|
| L2 `Stromal-interstitial fibroblast` (sing.) vs `fibroblasts` (plur.) | a canonicalisation map forces singular→plural **before** the tree is built | A |
| leaf code `…Fib…` (media-4) vs `…Fibs…` (object + CL map) | the join retries with `Fib`↔`Fibs` swapped — applied to **both** the leaf join and the media-4 marker join (all 5 fetal-fibroblast leaves receive their distinct markers) | B1 |
| trailing `+` (`Endo_cap_APCDD1+`) | the join strips a trailing `+`, merging it onto `Endo_cap_APCDD1` | C |

So **A, B1 and C do not block the build** — those markers attach and the CAS is
complete; the fixes requested for them below are to make the **source files
self-consistent for publication and downstream reuse**, not to repair the build.
What the build **cannot** absorb automatically is a genuinely *different label*
(not a spelling variant): the **B2 Granulosa** and **B3 oocyte** subtype schemes,
whose media-4 markers stay unattached until a human confirms the correspondence.

The inconsistencies below are the points where sources disagreed; the manual
fixes keep all three files in lockstep (and are required for B2/B3 before their
markers can attach).

---

## Summary of required edits (by priority)

| # | Issue | Fix in | Severity |
|---|---|---|---|
| A | L2 `Stromal-interstitial fibroblast` vs `fibroblasts` (singular/plural) forks fetal vs adult stroma | `cell_ontology_mapping.xlsx` (+ media-4) | Source hygiene — **would** corrupt the hierarchy, but the build canonicalises it; fix for a clean, reusable source |
| B1 | 5 fetal-fibroblast leaf codes spelled `…Fib…` in media-4 but `…Fibs…` in object + CL map | media-4 | Low — build auto-normalises; **markers do attach**; fix for source hygiene |
| B2 | Granulosa AMH+ subtypes named differently in media-4 vs object + CL map | media-4 | **High** — different subtyping scheme |
| B3 | Primary oocyte subtypes named differently in media-4 vs object + CL map | media-4 | Medium |
| C | Object carries duplicate leaf labels `Endo_cap_APCDD1` **and** `Endo_cap_APCDD1+` for one cell type | h5ad object | Medium — build merges via `+`-strip; fix in the object for cleanliness |
| D1 | media-4 L4 collides for two Granulosa leaves; CL map disambiguates | media-4 | Low |
| D2 | Two CL-term assignments break ontology subsumption | `cell_ontology_mapping.xlsx` | Medium |
| D3 | `cell_ontology_mapping.xlsx` key column mixes granularities (27 non-leaf rows) | `cell_ontology_mapping.xlsx` | Low (documentation) |
| E | Two literature citations in media-4 descriptions unverifiable | media-4 | Low — verify |

---

## A. L2 nomenclature typo forks the stromal lineage (High)

In `cell_ontology_mapping.xlsx`, the **fetal** rows use L2 = `Stromal-interstitial
fibroblast` (singular) while the **postnatal** rows use `Stromal-interstitial
fibroblasts` (plural). Built literally, this single-character difference splits
the mesenchymal stromal lineage into **two parallel L2 subtrees** — one entirely
fetal (247,700 cells), one adult (781,769 cells) — and **duplicates four L3
region labels**, each appearing once fetal and once adult:

| duplicated L3 label | adult branch (plural L2) | fetal branch (singular L2) |
|---|---|---|
| Ovarian stroma | 205,535 | 32,133 |
| Fallopian tube stroma | 64,649 | 41,092 |
| Cervix stroma | 452 | 11,916 |
| Vagina stroma | 1,463 | 8,570 |

Consequence: the adult ovarian/cervix stroma appears "missing" from the fetal
branch and vice-versa, when in fact both exist. (An audit of *all* L1–L4 labels
found this is the **only** such trivial-variant collision in the hierarchy.)

**Fix:** standardise the L2 label to one spelling — **`Stromal-interstitial
fibroblasts`** (plural) — across all rows in `cell_ontology_mapping.xlsx`
(the 19 fetal rows currently use the singular). Check media-4 sheet B for the
same L2 split and standardise identically. After this, fetal and adult stroma
correctly share one L2 and one L3 per region.

---

## B. media-4 (Supp Table 2) is out of sync with the object + CL map

In each case below, the **object and `cell_ontology_mapping.xlsx` agree**, and
**media-4 differs**. The consequence depends on the *kind* of difference:

- **B1 (spelling drift, `Fib`/`Fibs`)** — absorbed by the build's normalisation,
  so these markers **do** attach; the rename is for source cleanliness only.
- **B2 / B3 (different subtype schemes)** — genuine relabellings the build cannot
  normalise, so these media-4 markers **do not attach** until a human confirms
  the correspondence and updates media-4.

For journal resubmission, media-4 should be brought in line with the released
object in all three cases.

### B1. Fetal fibroblast leaf codes: `Fib` (media-4) → `Fibs` (object + CL map)

| media-4 `celltype_HCA` (current) | object + CL map (correct) |
|---|---|
| `Mesen_GonadalFib_Undiff` | `Mesen_GonadalFibs_Undiff` |
| `Mesen_MesonephricFib_Fetal` | `Mesen_MesonephricFibs_Fetal` |
| `Mesen_OvarianFib_Fetal` | `Mesen_OvarianFibs_Fetal` |
| `Mesen_UterusFib_Fetal` | `Mesen_UterusFibs_Fetal` |
| `Mesen_VaginaFib_Upper_Fetal` | `Mesen_VaginaFibs_Upper_Fetal` |

**Fix:** rename these 5 codes in media-4 to the plural (`…Fibs…`). *Cosmetic —
the build already swaps `Fib`↔`Fibs` when joining, so all 5 leaves receive their
(distinct) media-4 markers today; this rename simply removes the discrepancy from
the source file.*

### B2. Granulosa AMH+ subtyping scheme differs (High — not a typo, a different scheme)

| source | `Granulosa_AMHpos_*` subtypes |
|---|---|
| **object** | `Steroidogenic`, `nonSteroidogenic`, `nonSteroidogenic_early`, `Atretic`, `Cyc` |
| **CL map** | `Steroidogenic`, `nonSteroidogenic`, `nonSteroidogenic_early`, `Atretic`, `Cyc` (+ `Granulosa_AMHpos`) |
| **media-4** | `Antral`, `Cumulus`, `Prenatral`, `Primary`, `smallPrenatral`, `Atretic`, `Cyc` (+ `Granulosa_AMHpos`) |

media-4 uses a **follicle-stage** naming (Antral/Cumulus/Primary/…) that the
released object does **not** use — the object uses a **steroidogenic-status**
naming. These are different subclusterings, not renamings, so they cannot be
auto-mapped. **Action for authors:** decide the canonical scheme and update
media-4 (and provide a correspondence if the follicle-stage labels should be
retained as synonyms/alternative labels).

### B3. Primary oocyte subtypes named differently

| source | `Germcell_PrimaryOocyte_*` |
|---|---|
| **object** | `ZP4neg`, `ZP4pos` |
| **CL map** | `ZP4neg`, `ZP4pos` |
| **media-4** | `Fetal`, `ZP4` |

**Fix:** update media-4 to `ZP4neg` / `ZP4pos`. Likely correspondence
`ZP4`→`ZP4pos` and `Fetal`→`ZP4neg` — **please confirm** before applying.

---

## C. Duplicate leaf label inside the h5ad object (Medium)

The object's `celltype_HCA_fine` column carries **two labels for one cell type**:

| `celltype_HCA_fine` value | cells |
|---|---|
| `Endo_cap_APCDD1` | 4,691 |
| `Endo_cap_APCDD1+` | 2,567 |

media-4 and the CL map both have only `Endo_cap_APCDD1`. The trailing `+` looks
like an artifact (e.g. a residual marker-positive suffix). **Fix in the object /
annotation pipeline:** merge `Endo_cap_APCDD1+` into `Endo_cap_APCDD1` (or, if
they are genuinely distinct states, add the second to media-4 + CL map with its
own markers and CL term).

---

## D. Internal issues in `cell_ontology_mapping.xlsx`

### D1. media-4 L4 collides for two Granulosa leaves (CL map already disambiguates)

For the two leaves that share the L3 "Granulosa of primordial follicle":

| leaf | media-4 L4 | CL-map L4 |
|---|---|---|
| `Granulosa_AMHneg_Squamous` | Granulosa of primordial follicle quiescent | Granulosa of primordial follicle quiescent |
| `Granulosa_sq_Fetal` | Granulosa of primordial follicle quiescent | Granulosa of primordial follicle quiescent**, fetal** |

The CL map's disambiguation (adding ", fetal") is correct and keeps L4 unique
per leaf. **Fix media-4** to match (its L4 currently collides).

### D2. Two CL-term assignments break ontology subsumption (Medium)

Verified against the Cell Ontology (OLS4). In each, a supertype node's CL term is
**not** an ancestor of its children's CL terms:

- **`Endo_ven`** → mapped to **CL:0002543** (*vein endothelial cell*), but its
  children map to **CL:0002652** (*endothelial cell of vein*) and **CL:1000414**
  (*endothelial cell of venule*), which sit under *endothelial cell of vascular
  tree*, **not** under CL:0002543. (CL carries two near-synonymous "vein
  endothelial" terms that are not nested.) → **Re-map** the parent to a term that
  is a true ancestor (e.g. CL:0002139) or switch the children into CL:0002543's
  subtree.
- **`Mesen_OvarianFibs`** → mapped to **CL:0000057** (*fibroblast*), but child
  **CL:0002132** (*stromal cell of ovary*) sits under *stromal cell*
  (CL:0000499), **not** fibroblast. → A genuine modelling decision (are ovarian
  stromal cells fibroblasts?); reconcile parent/child CL choices.

(For reference: 11 of 13 checked supertype→children CL relations were consistent.)

### D3. The key column mixes granularities (Low — documentation)

The `celltype_HCA` column in `cell_ontology_mapping.xlsx` is *labelled*
`celltype_HCA` but its values are the **fine** leaf codes (matching the object's
`celltype_HCA_fine`, 211/212). It also contains **27 coarser rows** (e.g.
`Endo`, `Epi_EndoGland`, `Mesen_Theca`, plus a few fetal/out-of-scope codes) that
are internal-node or umbrella labels rather than leaves. This is fine for CL
mapping (it usefully provides CL terms at internal nodes too) but is worth a note
in the column header / legend so downstream users don't treat every row as a leaf.

---

## E. Verify: two literature citations could not be resolved (Low)

Author-year citations were mined from media-4 descriptions and resolved to DOIs.
Five resolved with high confidence; **two could not be verified** and should be
checked against the manuscript reference list:

| citation (in media-4 description) | cell type | status |
|---|---|---|
| "Wang et al., 2021" (Th17/TSCM) | `Immune_CD4_Th17_SCMlike` | no unique primary paper found — please supply the intended reference |
| "Masopust et al., 2026" (TEMRA) | `Immune_CD8_T_EM` | **no such paper found** in Semantic Scholar / EuropePMC — likely an erroneous or in-press citation; please verify |

Resolved (for completeness): Villani 2017 → 10.1126/science.aah4573; Maier 2020
→ 10.1038/s41586-020-2134-y; Vento-Tormo 2018 → 10.1038/s41586-018-0698-6;
Nguyen 2017 → 10.1093/humrep/dex289; Fu et al. → 10.1038/s41586-025-08982-4.

---

## Appendix — how to re-verify after edits

The unified annotation is rebuilt deterministically by `scripts/build_cas.py` from the
object obs (`h5ad_obs/obs.categoricals.parquet`) + the two spreadsheets. After
correcting the sources, re-running it should show: no duplicated (labelset,
label) pairs for stroma, all fetal-fibroblast leaves carrying markers, and the
still-unattached media-4 code list reduced to only genuinely out-of-object
(prenatal) codes. Companion internal analysis: `ANNOTATION_HIERARCHIES.md`.

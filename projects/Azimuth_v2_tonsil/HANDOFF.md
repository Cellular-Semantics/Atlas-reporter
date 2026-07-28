# Azimuth_v2_tonsil — Session Handoff

**Branch:** `azimuth_c2_tonsil_atlas` (forked from `revert-orchestration-contracts`,
which is `main` reverted to the pre-PR#8 / pre-"orchestration-contracts" state).
**Atlas:** Azimuth `human_tonsil_v2`
(https://azimuth.hubmapconsortium.org/references/human_tonsil_v2/).
**Source paper:** King HW et al. (2021) *Science Immunology*,
DOI `10.1126/sciimmunol.abh3768`, PMID `34623901`.

---

## What is already done (committed to disk, not git)

| File | Status |
|------|--------|
| `inputs/CL_Map_Jie.xlsx` | Original externally-curated input (77 rows). ⚠ May still be open in Excel (`~$` lock file present). |
| `inputs/cl_map_jie.json` | Faithful parse of all 77 rows. |
| `inputs/cl_map_cleaned.json` | Cleaned, non-destructive. QC status per row: **70 ok / 6 fixed / 1 error**. |
| `inputs/cl_map_QC.md` | Full QC narrative. |
| `cell_type_annotations.json` | Workflow config (step 1). Schema-valid vs `src/schemas/cell_type_annotation.schema.json`. 112 annotations = 42 l1 (broad) + 70 fine. scope=`adult`. |

---

## NEXT STEPS (resume here)

MCP servers are being enabled in a parallel session. Once `/mcp` shows
`ols4`, `Asta_semanticscholar`, `artl-mcp`, `paper-search` connected
(verify: `ToolSearch "select:..."` or check they surface as tools):

### Step A — Validate the 77 parent CL IDs against OLS4 ✅ DONE (2026-07-27)
Validated all 77 rows (33 unique parent IDs) via **ols4 MCP** `fetch`.
Result → `inputs/cl_map_ols4_validation.json`:
- **77/77 resolve**, **0 obsolete**, **0 label mismatches** (all `parent_cl_label`
  match OLS4 canonical labels exactly).
- Row [56] carries the known **plausibility error** flag in `notes` (CD8 follicular
  T cell → CD4-naive parent `CL:0000895`); parent-ID validity itself is fine.
  Fix still awaiting curator (see OPEN DECISION 1).

### Step B — Report workflow
Follow `CLAUDE.md` Workflow Sequence for chosen cell type(s). Config is ready
(`cell_type_annotations.json`). Suggested first targets = the fine-grained
subtypes that are the actual NTR candidates (see `cl_map_cleaned.json`).

**✅ First run complete (2026-07-27): `FCRL4/5+` (order 91) → "FCRL4-positive memory B cell".**
Output in `traversal_output/FCRL4_5_positive/` + `reports/FCRL4_5_positive.md`.
- Steps 2–9 done. Report **passed** validation (quotes + DOIs).
- Evidence corpus built entirely from **ASTA `snippet_search`** across the literature:
  ASTA indexes only the King et al. **abstract** (CorpusId 238530091); no PMC
  supplement (paper not fully OA) and `get_europepmc_full_text` returned empty;
  no local index. 9 papers catalogued (Ehrhardt 2005/2008, Karnell, Liu, Jourdan,
  Gjertsson, Yeo, Carrasco, King).
- **CL mapping**: broad match `CL:0000787` (memory B cell); `new_term_needed: true`.
- **NTR drafted** → `cl_term_request.json` (schema-valid). Parent = `CL:0000787`.
- ⚠ **Fixed after drafting**: the `cl-term-request` agent hallucinated all 7 PMIDs;
  corrected against verified metadata (DOIs were correct). If re-running the NTR
  agent for other cell types, **verify PMIDs**.
- PR term IDs (FCRL4=PR:000007443, FCRL5=PR:000001314, CD11c=PR:000001013) plus
  UBERON:0002373 and GO:0002385 **verified against OLS4 (2026-07-27)** — all valid.
  Protein-level (flow/mAb) surface evidence confirmed for FCRL4/FCRL5/CD11c;
  recorded in the NTR justification.

**✅ Batch run complete (2026-07-27): all "tonsil sub-location + marker" cell types.**
Criterion = defined by a *sub-tonsillar* location (follicle / germinal center /
epithelium) **and** a marker. 8 candidates found in `cl_map_cleaned.json`; all
processed end-to-end (report → validate → CL map → header → NTR). Reference/first
run FCRL4/5+ above makes 9 total. Every report **passes** `report_checker`
(quotes + DOIs); every `cl_mapping.json` and `cl_term_request.json` is schema-valid;
every NTR PMID is sourced from its `paper_catalogue.json` (verified, none stray);
every ontology ID (CL/PR/UBERON/GO) verified against OLS4.

| order | slug | proposed CL label | broad-match parent |
|---|---|---|---|
| 44 | FDC_CD14_CD55 | CD55-positive follicular dendritic cell of palatine tonsil | CL:0000442 |
| 67 | FDC_COL27A1 | COL27A1-positive follicular dendritic cell of palatine tonsil | CL:0000442 |
| 179 | GC_T_OX40 | OX40-positive germinal center T follicular helper cell of palatine tonsil | CL:0009062 |
| 211 | GC_T_SAP | SAP-high germinal center T follicular helper cell | CL:0009062 |
| 231 | epithelial_VEGFA | epithelial cell of palatine tonsil (VEGFA+ subset) | CL:0000066 |
| 51 | memory_Tfh_CD4 | memory T follicular helper cell | CL:0002038 (+CL:0000897) |
| 60 | central_memory_preTfh | precursor T follicular helper cell of palatine tonsil | CL:0000904 |
| 56 | follicular_CD8_T | follicular CD8-positive, alpha-beta T cell | CL:0000625 ✎ |

Notes:
- All 8 are **broad match, new_term_needed=true** (no existing CL subtype term).
- ✎ Row 56: NTR documents the **CL:0000895→CL:0000625 parent correction** (OPEN
  DECISION #1) for the curator.
- Honest evidence handling: transcript-only / secreted / intracellular markers
  (CD14, COL27A1, VEGFA, SAP, BCL6) are described in definition text and NOT
  asserted as `has plasma membrane part`; only protein-surface markers are
  axiomatised (verified PR IDs).
- ASTA still indexes only the atlas **abstract**; all evidence is from broader-
  literature snippet_search. Building a **local snippet index** (see
  `local-paper-index` skill) would let name-resolution use King et al. full text.

**✅ Tissue-specificity review (2026-07-28).** Broad ASTA searches showed most of
these are **general secondary-lymphoid / MALT populations, not palatine-tonsil-
specific** (tonsil is just the atlas-sampled tissue). NTRs de-anchored from
palatine tonsil — labels shortened + location axioms generalised:

| slug | final label | location axiom |
|---|---|---|
| GC_T_OX40 | OX40-positive germinal center T cell | germinal center (UBERON:0010754) |
| GC_T_SAP | SAP-high germinal center T follicular helper cell | germinal center |
| follicular_CD8_T | follicular CD8-positive, alpha-beta T cell | germinal center |
| FDC_CD14_CD55 | CD55-positive follicular dendritic cell | germinal center |
| FDC_COL27A1 | COL27A1-positive follicular dendritic cell | germinal center |
| central_memory_preTfh | precursor T follicular helper cell | lymphoid tissue (UBERON:0001744) |
| FCRL4_5_positive | FCRL4-positive memory B cell**, human** | mucosa-associated lymphoid tissue (UBERON:0001961) |
| memory_Tfh_CD4 | memory T follicular helper cell | left general (already not tonsil-anchored) |
| epithelial_VEGFA | epithelial cell of palatine tonsil | **kept palatine tonsil** — genuinely tonsil epithelial anatomy |

All 9 NTRs remain schema-valid; every PMID is catalogue-sourced; every PR/UBERON/GO
ID verified against OLS4 (incl. protein-vs-transcript axiom discipline).

**FCRL4/5 made HUMAN-SPECIFIC (2026-07-28, curator decision).** Rationale: FCRL4/FCRL5
lack clean 1:1 mouse orthologs, so generic ortholog-spanning PR semantics are wrong.
Changes: label → "FCRL4-positive memory B cell, human"; marker axioms switched to human
PR terms (FCRL4 PR:Q96PJ5, FCRL5 PR:Q96RD9, CD11c PR:P20702); added `only in taxon`
(RO:0002160) Homo sapiens (NCBITaxon:9606); parent CL:0000787 kept species-neutral.
All three surface markers re-confirmed at PROTEIN level (antibody/flow, not transcript-only):
FCRL4 (Ehrhardt 2005), CD11c (Yeo 2014), FCRL5 (Owczarczyk; Sullivan/Kim; Carrasco flow panel).
The other 8 NTRs stay species-neutral (conserved cell types; markers attributed to human in
definition text per CL guidelines) — their marker axioms could optionally be standardised to
generic PR classes for consistency.

**✅ Posted to GitHub (2026-07-28, Step 10 done).** All 9 NTRs filed as issues on
`obophenotype/cell-ontology` (label `new term request`), via `ATLAS_CHAT_GH_TOKEN`
(account `cellsemantic`, `public_repo` scope). Issue URLs recorded in each report's
`Cell Ontology:` header line and in `ntr_issue_urls.json`:

| # | slug | issue |
|---|------|-------|
| 1 | FCRL4_5_positive | obophenotype/cell-ontology#3667 |
| 2 | FDC_CD14_CD55 | #3668 |
| 3 | FDC_COL27A1 | #3669 |
| 4 | GC_T_OX40 | #3670 |
| 5 | GC_T_SAP | #3671 |
| 6 | central_memory_preTfh | #3672 |
| 7 | epithelial_VEGFA | #3673 |
| 8 | follicular_CD8_T | #3674 |
| 9 | memory_Tfh_CD4 | #3675 |

**✅ Second batch posted (2026-07-28) — DZ/LZ + γδ cell types (5).** Criterion: only
genuine cell types generated; transient cell-cycle/transition rows were **flagged
as states, not minted** (see below).

| slug | proposed label | parent | issue |
|------|----------------|--------|-------|
| gd_MAIT_TRDV2 | Vδ2-positive gamma-delta T cell | CL:0000800 | #3676 |
| gd_MAIT_CD161_TRDV2 | CD161-positive Vδ2-positive gamma-delta T cell | CL:0000800 | #3677 |
| gd_nonTRDV2 | non-Vδ2 gamma-delta T cell | CL:0000800 | #3678 |
| GC_B_dark_zone | tonsil centroblast | CL:0009112 + CL:2000006 | #3679 |
| LZ_Tfh | light zone germinal center T cell | CL:0009062 | #3680 |

- Modelled after existing `CL:0020001` (V1δ): γδ TCR usage textual, not axiomatised.
- MAIT terms (#3676/#3677) additionally **CC @addiehl** flagging the MAIT/γδ
  nomenclature conflation (atlas calls them MAIT but they carry γδ TCRs).
- `tonsil centroblast` = dual parent (centroblast + tonsil GC B cell); flags the
  missing general "germinal center dark zone" UBERON (only lymph-node one exists).
- `light zone GC T cell` flags the missing general "light zone" UBERON.
- non-Vδ2 requests `CL:0020001` (V1δ) be reclassified as its subtype.

**NOT minted — flagged as transient states (CL practice: no cell-cycle-phase terms):**
DZ/LZ rows 380/381/386/382/384/383/376/435/436/331 and vague [225] "TCRV+ γδ T cell".

**Post-hoc curation fixes applied to ALL 14 NTRs (2026-07-28):**
- Species-neutral terms standardised to **generic (cross-species) PR** marker classes;
  FCRL4/5 kept human-specific (human PR + `only in taxon` Homo sapiens).
- **Definitions de-referenced from the atlas** — provenance moved to justification /
  source line; MAIT caveat reworded generically. Posted issue bodies re-synced.

**All 14 NTRs live: #3667–#3680.** URLs in `ntr_issue_urls.json` + report headers.

Remaining fine-grained NTR candidates NOT yet done (future targets): the
germinal-center dark-zone/light-zone `tonsil germinal center B cell` states and
the `MAIT/TRDV2+` gamma-delta T subsets.
Test/reference cell type per CLAUDE.md is "Iron-recycling macrophage" (other project).

---

## OPEN DECISIONS (need the user / curator)

1. **Row [56] genuine mapping error** — "CD8-positive, alpha-beta follicular
   T cell" is mapped to CD4-naive parent `CL:0000895`. Proposed fix:
   `CL:0000625` (CD8-positive, alpha-beta T cell) or a follicular/GC CD8 subtype.
   **Not yet applied** — awaiting curator confirmation.

2. **Do NOT "correct" these** — faithful to Azimuth's own l2 labels:
   - "commited" (Azimuth: `Early GC-commited NBC`)
   - "preMature IgG/IgM PC" = *pre-mature* precursor, not "immature".

3. **CD27 contradiction in FCRL4/5+ parent mapping** (surfaced by the report run).
   `cl_map_cleaned.json` maps the fine `FCRL4/5+` rows (orders 90/91) to
   class-switched/unswitched memory B cell parents (`CL:0000972` / `CL:0000970`),
   but CL's definition of `CL:0000972` requires **CD27-positive**, whereas
   FCRL4/5+ atypical memory B cells are defining **CD27-negative**. The report's
   CL mapping therefore chose `CL:0000787` (memory B cell) as the honest broad
   parent and the NTR proposes `CL:0000787` as direct parent. Curator may want a
   new "CD27-negative class-switched memory B cell" intermediate in CL.

4. **Post NTR to GitHub? (CLAUDE.md Step 10)** — NOT done. Requires explicit
   user confirmation + a `public_repo` GH token; verify PR IDs first (see Step B).

---

## DATA GAPS

- Azimuth web page yielded only **partial** lists to WebFetch: 42/49 l1 labels
  captured; l2 list was collapsed (page claims 157+). `cell_type_annotations.json`
  therefore covers 42 l1 + the 70 fine descriptors from Jie's file — **not the
  full l2 set**.
- **Per-cell-type DEGs / marker genes** (the "DEGs" the user referenced) are NOT
  yet captured — the rendered page doesn't expose them to WebFetch. Get them via
  the Azimuth reference data download or the `playwright` MCP server, then
  optionally enrich `cell_type_annotations.json` / supplementary evidence.

---

## TOOL RULES REMINDERS (from CLAUDE.md)
- Never use `curl`/`WebFetch` for APIs that have MCP tools (Semantic Scholar,
  Europe PMC, PMC). Prefer `snippet_search` over full text.
- This branch is **pre-PR#8**: no curation guard, no orchestration-contract
  schemas/hooks. Writes are not hook-restricted.
- Do not modify `src/`, commit, or run the test suite unless asked.

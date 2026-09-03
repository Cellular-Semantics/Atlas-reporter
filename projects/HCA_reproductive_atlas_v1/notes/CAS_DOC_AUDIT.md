# CAS documentation audit — HCA Female Reproductive System Cell Atlas v1

**Date:** 2026-08-03 · **Scope:** read-only audit (no source edits). Re-derives
every measurable claim in the three CAS notes from the source files and checks
that `cas.json` reflects the documented mapping decisions.

**Audited docs**
- `ANNOTATION_INSPECTION.md` (input inventory)
- `ANNOTATION_HIERARCHIES.md` (internal hierarchy analysis)
- `SOURCE_RECONCILIATION_for_authors.md` (source-mismatch memo)

**Sources checked against**
- `h5ad_obs/obs.categoricals.parquet` (2,235,448 cells × 56 cols)
- `inputs/cell_ontology_mapping.xlsx` sheet `Final`
- `inputs/media-4.xlsx` sheet B (+ A), `inputs/media-5.xlsx`
- `cas.json` (312 annotations)
- live OLS4 `cl` (for the two subsumption flags)

Audit script: `/tmp/audit_cas.py` (re-runnable).

---

## Verdict

**The documentation is accurate.** Of ~60 checkable quantities, all but one
reproduce exactly from source, and the mapping decisions described in the notes
are the ones actually implemented in `cas.json`. The single count
discrepancy traces to a **previously-undocumented duplicate row in media-4**,
which is a real source defect (see Finding 1) — the docs are wrong only in that
they don't yet mention it.

| Severity | Finding |
|---|---|
| **Medium (new)** | media-4 sheet B has a **duplicate `Neural_Schwann` row** with conflicting L-path + markers; not flagged in the reconciliation memo, and markers for this leaf are lost in the CAS draft |
| Low (doc) | `ANNOTATION_INSPECTION.md` "239 fine rows" vs its own lineage table summing to 240; "219 marker rows" → actually 220 — both artefacts of Finding 1 |
| Low (doc) | `ANNOTATION_HIERARCHIES.md` §3 says "14 not in any column" but enumerates only 13 (`Epi_Cil` omitted) |
| Low (doc) | §2 "9/34/101/160 distinct" — the `34` is the **pre-typo-fix** L2 count; post-fix (and in the CAS draft) L2 = 33. Internally consistent but worth a footnote |
| Low (doc) | §D2 glosses `CL:0002652` as "endothelial cell of vein"; the spreadsheet's own label for that ID is "endothelial cell of high endothelial venule" |

Everything else below is **confirmed exact**.

---

## Finding 1 (Medium, new) — duplicate `Neural_Schwann` row in media-4 sheet B

media-4 sheet B has **240 physical data rows but 239 distinct `celltype_HCA`
codes**. The duplicate is `Neural_Schwann`, appearing on sheet rows **165 and
166** with **different content**:

| sheet row | L1 | L2 | L3 | Markers_positive |
|---|---|---|---|---|
| 165 | Neural crest-derived | Glials | *(blank)* | `S100B;PLP1;SOX10` |
| 166 | Neural crest-derived | Glials | Schwanns | `MBP;PRX;GJC3` |

This is not a harmless repeat — it is the **same leaf code annotated two ways**
(two L-paths, two disjoint marker sets). Downstream consequences:

- `scripts/build_cas.py` indexes media-4 into a dict keyed by code (`m4[code] = …`), so
  **row 166 silently overwrites row 165**; only one marker set could ever attach.
- In the current `cas.json` the `Neural_Schwann` leaf (node label
  `Glials`, CL:0000125) carries **`marker_gene_evidence: None`** — *neither*
  marker set attached. So this leaf's markers are lost entirely.
- `SOURCE_RECONCILIATION_for_authors.md` §C flags the object-side duplicate
  (`Endo_cap_APCDD1` / `Endo_cap_APCDD1+`) but **not** this media-4-side
  duplicate.

**Recommendation (for the authors' memo, not applied here):** add a media-4
item — dedupe `Neural_Schwann` into one row with an agreed L-path and a merged
marker list; confirm whether `Glials`/`Schwanns` are one type or two.

---

## Confirmed exact — obs object (Axes A & B)

| Claim (docs) | Source | Result |
|---|---|---|
| 2,235,448 cells · 291 donors · 27 datasets | parquet | ✅ all exact |
| Axis A: lineage 8 · broad 98 · celltype_HCA 149 · fine 212 | parquet | ✅ |
| Axis B: ontology_level 8 · 24 · 57 · 117 | parquet | ✅ |
| fine → celltype_HCA strict tree 212/212 | parquet | ✅ |
| celltype_HCA → broad 147/149 (2 boundary exceptions) | parquet | ✅ |
| fine → broad 211/212, only `Mesen_Pericyte` spans 2 | parquet | ✅ (exactly `Mesen_Pericyte`) |
| broad → lineage strict 98/98 | parquet | ✅ |
| fine → ontology_level4 clean 212/212 | parquet | ✅ |

---

## Confirmed exact — CL-mapping spreadsheet

| Claim (docs) | Result |
|---|---|
| 238 cell-type rows, 0 duplicated leaf labels | ✅ |
| header = `celltype_HCA, source_sheet, L1–L4, Perfect match, ID_perfect, Nearest match, ID_nearest, cell_type_ontology_term_id` | ✅ |
| 59 perfect matches; every row has a final CL term (238/238) | ✅ (59 perfect; 238/238 final filled) |
| distinct L1–L4 = 9 / 34 / 101 / 160 | ✅ (34 = raw, pre typo-fix; see below) |
| both `…fibroblast` (sing.) and `…fibroblasts` (plur.) present at L2 | ✅ (this is the documented typo) |
| pre-fix L3→L2 = 97/101 with 4 violations (`Cervix/Fallopian tube/Ovarian/Vagina stroma`) | ✅ exact |
| after typo canon: L2→L1, L3→L2, L4→L3 all clean | ✅ (33/33, 101/101, 160/160) |
| leaf attachment depth L1:3 · L2:20 · L3:55 · L4:160 | ✅ exact |
| CL-map ∩ celltype_HCA_fine = 211/212 (miss = `Endo_cap_APCDD1+`) | ✅ exact |
| 27 coarser rows = 13 broad-node + 14 not-in-any-column | ✅ (13 + 14 = 27) |

- The 13 broad-node rows enumerated in §3 match source **exactly**.
- The "14 not in any column" set is correct in count, but §3 lists only 13 —
  **`Epi_Cil` is the unlisted 14th.**

---

## Confirmed exact — media-4 / media-5

| Claim (docs) | Result |
|---|---|
| media-4 B header row 6; columns as documented | ✅ |
| "239 fine rows" | ⚠️ 239 **distinct**, 240 physical (Finding 1) |
| "219 rows with positive markers" | ⚠️ actually **220** (Finding 1) |
| "37 rows with descriptions" | ✅ 37 |
| L1 lineage breakdown (Mesen 75 · Immune 54 · Epi 53 · Support-Ovary 13 · Endo 13 · Neural-crest 12 · Germ 9 · Mesothelial 7 · Gonadal-somatic 4) | ✅ all counts match (sum = 240, i.e. counts the dup row) |
| media-5 = 3 sheets 3A/3B/3C (macrophage OnevRest; uftLAM vs oLAM; ILC3 repro vs non-repro) | ✅ |

---

## Confirmed exact — SOURCE_RECONCILIATION mapping claims

**Label divergences media-4 ↔ CL-map/object** — reproduced exactly:
- 12 media-4-only labels = 5 fetal `…Fib…` typos + 5 Granulosa follicle-stage
  names + 2 primary-oocyte names.
- 11 CL-map-only labels including `Epi_FallopianSec_OVGP1hi_EstrInd` (present
  only in the CL map), the 5 `…Fibs…` corrections, 3 Granulosa
  steroidogenic-status names, 2 `ZP4neg/ZP4pos`.

**Stromal typo cell counts (§A table)** — exact to the cell:

| L3 region | plural L2 (adult) | singular L2 (fetal) |
|---|---|---|
| Ovarian stroma | 205,535 | 32,133 |
| Fallopian tube stroma | 64,649 | 41,092 |
| Cervix stroma | 452 | 11,916 |
| Vagina stroma | 1,463 | 8,570 |

**`Endo_cap_APCDD1` duplicate (§C)** — `Endo_cap_APCDD1` = 4,691 cells,
`Endo_cap_APCDD1+` = 2,567 cells; both present in `celltype_HCA_fine`. ✅ exact.

**CL subsumption flags (§D2 / Hierarchies §4)** — spreadsheet CL IDs match the
docs exactly, and both flags verified against **live OLS4**:
- `Endo_ven` → CL:0002543; children `Endo_ven_*` → CL:1000414 / CL:0002652.
  OLS4: CL:1000414's ancestors are *endothelial cell of vascular tree*
  (CL:0002139) → blood vessel endothelial cell — **CL:0002543 is not an
  ancestor.** Flag valid; the doc's suggested re-map to CL:0002139 is indeed the
  shared ancestor. *(Note: the doc glosses CL:0002652 as "endothelial cell of
  vein"; the spreadsheet's own label for it is "endothelial cell of high
  endothelial venule".)*
- `Mesen_OvarianFibs` → CL:0000057 (fibroblast); child → CL:0002132 (stromal
  cell of ovary). OLS4: CL:0002132's ancestors are *stromal cell* (CL:0000499)
  → connective tissue cell — **CL:0000057 is not an ancestor.** Flag valid.

---

## `cas.json` reflects the documented decisions

| Documented decision | In the draft? |
|---|---|
| Labelsets = master L1–L4, materialise every tier | ✅ L1:9 · L2:33 · L3:103 · L4:167 (total 312) |
| Typo canon applied (singular→plural) so stroma unifies | ✅ L2 = **33**, not 34 |
| n_cells conserved (Σ L1 = object total) | ✅ 2,235,448 |
| CL term at terminal nodes | ✅ 223 nodes carry a CL term; **0 ambiguous** multi-CL terminals |
| Generic leaves minted for the 13 mixed broad nodes | ✅ 13 minted leaves |
| `Endo_cap_APCDD1+` normalised/merged | ✅ (only that label is absent from CL-map; handled by suffix-strip) |
| Transferred labels → 8 subatlas DOIs + Sanger (no DOI) | ✅ all 9 source_taxonomy values present & documented |
| Parent-accession integrity | ✅ 0 dangling parents |
| media-4 markers attached | ✅ 206 nodes with markers — **except `Neural_Schwann`** (Finding 1) |

---

## Suggested follow-ups (reports/edits deferred per instruction)

1. Add the `Neural_Schwann` media-4 duplicate to
   `SOURCE_RECONCILIATION_for_authors.md` (new item under §B/§C) and decide the
   canonical L-path + merged markers — currently this leaf loses all markers.
2. Trivial doc touch-ups: reconcile the 239/240 wording in
   `ANNOTATION_INSPECTION.md`; add `Epi_Cil` to the §3 "14" list; footnote that
   the L2 `34` is pre-typo-fix (draft uses 33).
3. Optional: correct the `CL:0002652` label gloss in the reconciliation memo.

*Nothing in this audit was applied to source files or `cas.json`.*

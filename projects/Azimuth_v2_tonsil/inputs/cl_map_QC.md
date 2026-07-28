# CL Map (Jie) — QC Log

**Source:** `CL_Map_Jie.xlsx` (externally curated) → parsed to `cl_map_jie.json` (77 rows).
**Cleaned output:** `cl_map_cleaned.json`.
**Atlas:** Azimuth `human_tonsil_v2`. **Paper:** King HW et al. (2021) *Science Immunology*, DOI 10.1126/sciimmunol.abh3768 (PMID:34623901).

## Summary

77 Azimuth tonsil annotation terms, each pre-mapped to a parent CL term + an OBO
design pattern (`cellHasPlasmaMembranePartX`, `cellPartOfAnatomicalEntity`,
`like`, and cell-cycle / GC-zonation groupings). The `new_term_request` labels
are auto-generated as roughly `descriptor + parent CL label`, which produces
awkward two-cell-type strings — but most are **faithful** to Azimuth's own l2
labels rather than curation errors.

QC status of cleaned rows: **70 ok · 6 auto-fixed · 1 genuine error**.

## Genuine error (needs a curator decision)

- **[56] "CD8-positive, alpha-beta follicular T cell"** mapped to parent
  `CL:0000895` *naive thymus-derived **CD4**-positive, alpha-beta T cell*.
  CD8 term under a CD4 **naive** parent — wrong on lineage (CD8 vs CD4) and
  state (naive vs follicular). Suggested parent: `CL:0000625`
  (CD8-positive, alpha-beta T cell), or a more specific follicular/GC CD8 subtype.

## Auto-fixed (biomarker re-derivation + one typo)

The `Biomarker?` column was mis-tokenized (comma-split of compound tokens).
Re-derived from the descriptor:

| Row | Raw | Cleaned |
|-----|-----|---------|
| 46  | `CD16,CD56`     | CD16-negative, CD56-dim |
| 51  | `CD4,alpha`     | CD4-positive |
| 56  | `CD8,alpha`     | CD8-positive |
| 60  | `CD4,alpha`     | CD4-positive |
| 91  | `FCRL4,FCRL5`   | FCRL4/5 |
| 92  | `FCRL4,FCRL5`   | FCRL4/5 |
| 447 | typo `SELNOP`   | **SELENOP** (Azimuth: `SELENOP Slan-like`) — Jie-origin typo, fixed |

(Row 90 biomarker `receptor,4,5,FCRL` remains messy — descriptor is
"Fc receptor-like (FCRL) 4/5+"; low priority.)

## Flagged-but-faithful (NOT errors — keep, do not "correct")

These looked dirty but match Azimuth's own l2 labels:

- **[332] "commited"** — Azimuth l2 label is literally `Early GC-commited NBC`
  (upstream typo).
- **[475]/[476] "premature IgG/IgM plasma cell"** — Azimuth `preMature IgG+/IgM+ PC`
  = **pre-Mature** (precursor of mature PC), *not* "immature".
- Concatenated two-cell-type labels ([115], [120], [330], [331], [383], [405],
  [467], [532], …) — faithful renderings of Azimuth descriptor + CL parent.

## Still outstanding

1. **Validate all 77 parent CL IDs against OLS4** — confirm each ID resolves,
   label matches, and is a plausible superclass. **Blocked:** the `ols4` MCP
   server is not connected in this session (OLS4 REST is reachable, but the repo
   tool rules say route through MCP). Enable via `/mcp` or authorize a REST
   fallback.
2. **Complete atlas label set + DEGs** — the Azimuth web page exposes only
   partial lists to fetch (42/49 l1 captured; l2 collapsed). Full l2 labels and
   per-cell-type marker genes need the Azimuth data download or the `playwright`
   MCP server.

# DPYSL2+ Basal Keratinocyte in Fetal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Source dataset: Gopee et al. (2024), prenatal skin, 7–17 PCW
Cell Ontology: [basal cell of epidermis](http://purl.obolibrary.org/obo/CL_0002187) (CL:0002187, broad match)

## New Term Request

A new CL term is needed for the DPYSL2-positive basal keratinocyte of fetal skin. This is a temporally and molecularly distinct basal keratinocyte state that emerges after 11 PCW, defined by expression of DPYSL2 and AGR2, and a specific trajectory position upstream of ORS and companion layer cells. CL:0002187 (basal cell of epidermis) is the closest existing term but does not capture the fetal-specific maturation state, the AGR2/DPYSL2 expression profile, or the trajectory relationship to hair follicle lineages.

**Proposed label:** DPYSL2-positive basal keratinocyte

**Proposed definition (CL-style):** A basal cell of the epidermis that is part of fetal skin, arising after 11 post-conception weeks and distinguished by expression of DPYSL2 and AGR2 (Gopee et al., 2024). This cell is positioned along the outer root sheath/companion layer (ORS/CL) differentiation trajectory downstream of POSTN-positive basal cells, giving rise to outer root sheath and companion layer cells during hair follicle morphogenesis. The upregulation of AGR2, which functions in the assembly of cysteine-rich receptors enriched in hair follicles, is a defining feature of the ORS/CL branch compared with the inner root sheath trajectory.

**Proposed logical axioms:**
- subClassOf: basal cell of epidermis (CL:0002187)
- part of: fetal skin
- expresses: DPYSL2
- expresses: AGR2

**Evidence:** Gopee et al. (2024), DOI: 10.1038/s41586-024-08002-x, Figure 2, Extended Data Figure 4, Supplementary Tables 6 and 7.

## Summary

The DPYSL2+ basal cluster represents the mature state of interfollicular basal keratinocytes in fetal skin that emerges after 11 post-conception weeks (PCW). Identified in the Gopee et al. (2024) prenatal skin atlas, this population is defined by upregulation of DPYSL2 and AGR2, and is positioned along the ORS/CL trajectory downstream of POSTN+ basal progenitors. Trajectory and pseudotime analysis predicted two differentiation paths from POSTN+ basal cells: the ORS/CL trajectory (through DPYSL2+ basal cells to ORS and companion layer) and the IRS trajectory (through placode and matrix cells). AGR2 is upregulated in the ORS/CL branch and downregulated in the IRS branch. This population is absent in early embryonic skin and increases after 11 PCW, marking the transition from embryonic to mature fetal epidermis.

## Markers

### Defining markers: DPYSL2 and AGR2

Gopee et al. (2024) identified this mature basal state and its trajectory-specific markers:

> "Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation"
>
> — Gopee et al. (2024)

> "Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)"
>
> — Gopee et al. (2024)

### Trajectory-specific marker contrasts: AGR2 vs matrix markers

AGR2 marks the ORS/CL branch whereas matrix markers (SHH, WNT10B) mark the IRS branch:

> "AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B...were upregulated"
>
> — Gopee et al. (2024)

## Location

### Basal layer of the fetal interfollicular epidermis, from 11 PCW

DPYSL2+ basal cells occupy the stratum basale of the interfollicular epidermis of fetal skin, appearing from 11 PCW as the skin transitions from an embryonic to a mature fetal state. In trajectory analyses they are classified as late epithelial cells (≥12 PCW) alongside POSTN+ basal cells, placode, matrix, ORS, CL, IRS, and cuticle/cortex.

## Function

### Intermediate on the ORS/companion layer hair follicle differentiation trajectory

DPYSL2+ basal cells are an intermediate along the ORS/CL differentiation trajectory during fetal hair follicle morphogenesis, positioned downstream of POSTN+ basal progenitors and upstream of ORS and companion layer cells:

> "Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS"
>
> — Gopee et al. (2024)

The migratory role proposed for POSTN+ progenitors may drive basal cell movement into the ORS during hair follicle invagination:

> "Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination"
>
> — Gopee et al. (2024)

## References

- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis". *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)

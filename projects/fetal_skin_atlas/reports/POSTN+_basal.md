# POSTN+ Basal Keratinocyte in Fetal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Source dataset: Gopee et al. (2024), prenatal skin, 7–17 PCW
Cell Ontology: [basal cell of epidermis](http://purl.obolibrary.org/obo/CL_0002187) (CL:0002187, broad match)

## New Term Request

A new CL term is needed for the POSTN-positive basal keratinocyte of fetal skin. This is a fetal-specific basal keratinocyte state defined by expression of periostin (POSTN), present throughout gestation (7–17 PCW), with dual progenitor capacity for both the ORS/CL and IRS hair follicle trajectories. CL:0002187 (basal cell of epidermis) is the closest existing term but does not capture the POSTN expression, the dual-trajectory progenitor capacity, or the proposed role in placode specification.

**Proposed label:** POSTN-positive basal keratinocyte

**Proposed definition (CL-style):** A basal cell of the epidermis that is part of fetal skin, present throughout gestation from 7 post-conception weeks onward and distinguished by expression of periostin (POSTN) (Gopee et al., 2024). This cell is positioned at the origin of dual hair follicle differentiation trajectories: the outer root sheath/companion layer (ORS/CL) trajectory, via DPYSL2-positive basal cells, and the inner root sheath (IRS) trajectory, via placode and matrix cells. Loss of AGR2, which is downregulated in POSTN-positive basal cells compared with the ORS/CL branch, may promote cellular migration involved in placode specification and dermal invagination during hair follicle morphogenesis.

**Proposed logical axioms:**
- subClassOf: basal cell of epidermis (CL:0002187)
- part of: fetal skin
- expresses: POSTN (human gene product)

**Evidence:** Gopee et al. (2024), DOI: 10.1038/s41586-024-08002-x, Figure 2, Extended Data Figure 4, Supplementary Tables 6 and 7.

## Summary

The POSTN+ basal cluster in the Gopee et al. (2024) prenatal skin atlas represents a basal keratinocyte state that is present throughout fetal skin development from 7 to 17 PCW, defined by expression of the extracellular matrix protein periostin (POSTN). In contrast to the mature DPYSL2+ basal state, which appears only after 11 PCW, POSTN+ basal cells are detected across the entire gestational window sampled. Trajectory and pseudotime analysis positioned POSTN+ basal cells at the root of two distinct hair follicle differentiation paths: the ORS/CL trajectory (through DPYSL2+ basal cells) and the IRS trajectory (through placode and matrix cells). Their migratory capacity — potentially linked to AGR2 regulation — has been proposed to contribute to placode specification and dermal invagination during hair follicle formation.

## Markers

### Defining marker: POSTN (periostin)

POSTN (periostin) is the marker that distinguishes this basal keratinocyte population. POSTN is an extracellular matrix protein involved in cell adhesion and migration. Its expression in the basal layer throughout gestation, in contrast to the later-appearing DPYSL2+ basal cells, suggests a role in the early and sustained stages of epidermal and hair follicle development:

> "Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation"
>
> — Gopee et al. (2024)

### Dual-trajectory progenitor position

POSTN+ basal cells sit at the origin of both major hair follicle epithelial trajectories:

> "Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS"
>
> — Gopee et al. (2024)

### ORS/CL branch: AGR2 upregulation

Along the ORS/CL branch, DPYSL2+ basal cells upregulate AGR2 and the transcription factors BARX2 and SOX9:

> "Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)"
>
> — Gopee et al. (2024)

In contrast, the IRS branch is characterised by AGR2 downregulation and matrix marker upregulation:

> "AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B...were upregulated"
>
> — Gopee et al. (2024)

## Location

### Basal layer of the fetal interfollicular epidermis and hair follicle epithelium, 7–17 PCW

POSTN+ basal cells are annotated as a fine-grained fetal cell type in Supplementary Table 6 of Gopee et al. (2024), present throughout gestation. They occupy the stratum basale of the interfollicular epidermis and are positioned at the origin of hair follicle epithelial differentiation trajectories.

## Function

### Dual progenitor of ORS/CL and IRS hair follicle lineages

The primary functional significance of POSTN+ basal cells is as a progenitor population giving rise to two distinct hair follicle lineages. Their migratory capacity may directly drive the cellular movements that initiate hair follicle formation:

> "Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination"
>
> — Gopee et al. (2024)

## References

- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis". *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)

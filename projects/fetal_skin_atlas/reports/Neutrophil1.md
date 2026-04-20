# Neutrophil1
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | neutrophil |
| CL ID | CL:0000775 |
| CL definition | Any of the immature or mature forms of a granular leukocyte that in its mature form has a nucleus with three to five lobes connected by slender threads of chromatin, and cytoplasm containing fine inconspicuous granules and stainable by neutral dyes. |
| Match type | skos:broadMatch |
| Confidence | medium |

**Justification:** The atlas identifies two transcriptionally distinct neutrophil subpopulations (Neutrophil1 and Neutrophil2) in fetal skin; CL:0000775 'neutrophil' is the closest available CL term. No CL term exists for transcriptionally defined neutrophil subtypes in fetal tissue. Neutrophil1 is a subtype of neutrophil, making broad match appropriate. No new term is required.

## Summary

Neutrophil1 is one of two transcriptionally distinct neutrophil subpopulations annotated in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. The atlas confirmed that multiple innate immune populations populate fetal skin from early gestation:

> "Innate immune cells, such as macrophages and innate lymphoid cells (ILCs), were present from early gestation, whereas B cells and T cells emerged later, accompanying thymus, bone marrow and spleen formation from around 10 PCW"
> — Gopee et al. (2024), *Nature*

The neutrophil-myeloid precursor lineage was identified in first-trimester skin by scRNA-seq:

> "plasmacytoid DCs, monocytes, monocyte-DCs (having both a monocyte and DC gene signature) and a neutrophil-myeloid precursor have also recently been identified in first-trimester human skin using single-cell RNA sequencing (scRNAseq)."
> — Botting and Haniffa (2020), *Immunology*

Neutrophil1 is distinguished from Neutrophil2 by differentially expressed genes in Supplementary Table 3 of the atlas, and likely represents a distinct maturation stage or activation state along the neutrophil continuum.

## Markers

Marker genes distinguishing Neutrophil1 from Neutrophil2 are defined in Supplementary Table 3 of Gopee et al. (2024). Based on cross-tissue studies of neutrophil heterogeneity, canonical neutrophil maturity markers include SELL (CD62L), CXCR1, CXCR2, FCGR3B (CD16b), and S100A8/S100A9:

> "Relative to TANs, matched NANs in our dataset showed high expression of established neutrophil maturity markers (SELL, PTSG2, CXCR2, CXCR1, FCGR3B, MME) as well as canonical neutrophil markers (S100A8, S100A9, S100A12)"
> — Salcher et al. (2022), *Nature Cancer*

## Location

Neutrophil1 cells are found within fetal skin (dermis/immune compartment) during prenatal development (7–17 PCW). They were isolated as CD45+ immune cells by FACS prior to scRNA-seq profiling.

## Function

Fetal neutrophils represent an early innate immune population with immature effector function compared to adult neutrophils:

> "Mature neutrophils are present at the end of the first trimester and steeply increase in number, stimulated by granulocyte-colony-stimulating factor, shortly before birth. Their number then returns to a stable level within days, but they show weak bactericidal functions, poor responses to inflammatory stimuli, reduced adhesion to endothelial cells and diminished chemotaxis"
> — Simon et al. (2015), *Proceedings of the Royal Society B*

The two-subpopulation structure (Neutrophil1 and Neutrophil2) in fetal skin likely reflects different maturation states or tissue-adaptation phenotypes. IL-8/CXCL8, a potent neutrophil chemoattractant, is expressed in prenatal skin and may contribute to neutrophil recruitment and positioning.

## Structure / Morphology

No specific structural data for fetal skin Neutrophil1 are reported in the atlas text. Mature neutrophils have a multi-lobed nucleus (3–5 lobes); immature forms have band or ring-shaped nuclei. Distinct transcriptional states likely map onto these morphological maturation stages.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting, R. and Haniffa, M. (2020). "The developing immune network in human prenatal skin." *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
- Simon, A.K. et al. (2015). "Evolution of the immune system in humans from infancy to old age." *Proceedings of the Royal Society B*. DOI: [10.1098/rspb.2014.3085](https://doi.org/10.1098/rspb.2014.3085)
- Salcher, S. et al. (2022). "High-resolution single-cell atlas reveals diversity and plasticity of tissue-resident neutrophils in non-small cell lung cancer." *Nature Cancer*. DOI: [10.1038/s43018-022-00459-x](https://doi.org/10.1038/s43018-022-00459-x)
- Grieshaber-Bouyer, R. et al. (2021). "The neutrotime transcriptional signature defines a single continuum of neutrophils across biological compartments." *Nature Communications*. DOI: [10.1038/s41467-021-22973-9](https://doi.org/10.1038/s41467-021-22973-9)

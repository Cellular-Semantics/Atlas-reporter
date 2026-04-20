# Eo/baso/mast cell progenitor
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | granulocyte monocyte progenitor cell |
| CL ID | CL:0000557 |
| CL definition | A hematopoietic progenitor cell that is committed to the granulocyte and monocyte lineages. |
| Match type | skos:broadMatch |
| Confidence | low |

**Justification:** The 'Eo/baso/mast cell progenitor' label indicates a multi-lineage progenitor with potential to give rise to eosinophils, basophils, and mast cells. In mouse haematopoiesis, the basophil/mast cell progenitor (BMCP) sits downstream of GMP; human equivalents are less clearly defined. CL:0000557 'granulocyte monocyte progenitor cell' (GMP) is the best broad match as the upstream progenitor of granulocytic lineages including eosinophil, basophil, and mast cell. No CL term exists for a human eosinophil-basophil-mast cell progenitor as a distinct cell type. A new CL term may be warranted if this cluster is validated as a distinct progenitor state.

## Summary

Eo/baso/mast cell progenitor is a multi-lineage myeloid progenitor cluster identified in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. This cluster corresponds to a progenitor population with transcriptional features of eosinophil, basophil, and mast cell commitment — collectively representing the granulocytic lineages downstream of the common myeloid programme.

The atlas uses 'MEMP' (megakaryocyte-erythroid-mast cell progenitor) as a distinct progenitor category in the immune compartment:

> "MEMP, megakaryocyte-erythroidmast cell progenitor"
> — Gopee et al. (2024), *Nature*

MEMP-related progenitors in fetal dermis contribute to the in situ mast cell differentiation programme:

> "The presence of megakaryocyte-erythrocyte-mast cell progenitors (MEMPs), lymphocyte precursors, B-cell progenitors, ILC precursors and their progeny 41 indicates differentiation of these lineages may be supported within developing dermis."
> — Botting and Haniffa (2020), *Immunology*

The eo/baso/mast cell progenitor cluster in the atlas is distinct from the MEMP and represents the granulocyte-biased fork of the mast cell lineage, potentially capturing cells at the junction between GMP and committed basophil/mast cell progenitor stages. Mast cells, which derive from these progenitors, are detectable in fetal skin from 8 PCW:

> "Mast cells have been detected in fetal skin as early as 8 PCW, 41 and continue to mature and expand throughout the second trimester."
> — Botting and Haniffa (2020), *Immunology*

## Markers

Eo/baso/mast cell progenitors in fetal skin are expected to express markers of GMP commitment with partial granulocyte lineage specification:

- **CD34** — retained haematopoietic progenitor marker
- **CD117 (KIT)** — expressed on GMP and downstream granulocyte progenitors
- **GATA1 / GATA2** — transcription factors bridging mast cell and eosinophil commitment
- **IL3RA (CD123)** — IL-3 receptor alpha; expressed on GMP and basophil/mast progenitors
- **FcεRI** — low or absent at progenitor stage; upregulated during mast cell commitment

Specific differentially expressed markers for this cluster are provided in Supplementary Table 3 of Gopee et al. (2024).

## Location

Eo/baso/mast cell progenitor cells are located in the dermal immune compartment of fetal skin during prenatal development (7–17 PCW). They were isolated as CD45+ immune cells by FACS prior to scRNA-seq. Their presence in skin alongside committed mast cell, macrophage, and DC populations indicates ongoing granulopoiesis within peripheral fetal tissues.

## Function

This progenitor population represents the multipotent granulocytic precursor stage that gives rise to eosinophils, basophils, and mast cells in skin. In the context of fetal skin:

- Mast cell progeny support immune surveillance and tissue homeostasis in the developing dermis
- The progenitor pool maintains the mast cell compartment throughout gestation
- Basophil and eosinophil derivatives may contribute to innate immune responses in fetal skin, though their specific roles during prenatal development are poorly characterised
- Stem cell factor (SCF) from the skin microenvironment acts as the primary survival and differentiation signal for mast cell-committed progeny

## Structure / Morphology

Eo/baso/mast cell progenitors are small haematopoietic cells with a round-to-oval nucleus, relatively high nuclear-to-cytoplasmic ratio, and few if any specific granules. At the transcriptional level, these cells express both granulocyte commitment genes and low-level lineage-specific markers. No specific morphological data for this fetal skin progenitor cluster are reported in the atlas text.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting, R. and Haniffa, M. (2020). "The developing immune network in human prenatal skin." *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
- Popescu, D.M. et al. (2019). "Decoding human fetal liver haematopoiesis." *Nature*. DOI: [10.1038/s41586-019-1652-y](https://doi.org/10.1038/s41586-019-1652-y)

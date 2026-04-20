# Monocyte precursor
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | promonocyte |
| CL ID | CL:0000559 |
| CL definition | A precursor in the monocytic series, being a cell intermediate in development between the monoblast and monocyte. This cell is CD11b-positive and has fine azurophil granules. |
| Match type | skos:broadMatch |
| Confidence | medium |

**Justification:** No CL term exists specifically for 'monocyte precursor' as a transcriptionally defined atlas cluster. CL:0000559 'promonocyte' is the most committed monocyte precursor stage in the CL, representing the intermediate between monoblast and mature monocyte. The atlas cluster may encompass both GMP-stage (CL:0000557) and promonocyte-stage cells; promonocyte is selected as the best broad match given the label implies monocyte commitment. GMP (CL:0000557) is an equally valid alternative.

## Summary

Monocyte precursor is a myeloid progenitor population identified in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. This cluster represents myeloid progenitor cells committed to the monocyte lineage that have seeded the skin from the fetal liver or bone marrow. Multi-organ single-cell profiling of the human prenatal immune system has demonstrated the widespread distribution of myeloid progenitors across peripheral fetal tissues:

> "we detected B cell progenitors in almost all prenatal organs, megakaryocyte/erythroid progenitors in developing spleen and skin, and myeloid progenitors in the thymus, spleen, skin, and kidney"
> — Suo et al. (2022), *Science*

The developmental origin of fetal skin monocyte precursors can be traced to fetal liver granulocyte-monocyte progenitors (GMPs):

> "These HSCs rapidly enter the circulation and seed the fetal liver (FL), which produces the first population of granulocyte-monocyte progenitors (GMPs) and blood monocytes at 4-5 PCW"
> — Miah et al. (2021), *Frontiers in Immunology*

The presence of monocyte precursors in prenatal skin indicates that myelopoiesis is not confined to canonical haematopoietic organs during fetal development.

## Markers

Based on GMP/promonocyte biology and the literature, monocyte precursors at this stage are expected to express:

- **CD34** — haematopoietic progenitor marker
- **CD117 (KIT)** — progenitor marker; retained in GMP/promonocyte
- **CD123 (IL3RA)** — expressed on GMPs and early myeloid progenitors
- **CD38** — upregulated during myeloid commitment
- **CD45RA** — present on GMPs (CL:0000557 definition)
- **CD11b** — expressed on promonocytes per CL:0000559 definition

Specific differentially expressed markers for the monocyte precursor cluster in fetal skin are listed in Supplementary Table 3 of Gopee et al. (2024).

## Location

Monocyte precursor cells are found in the dermis/immune compartment of fetal skin during prenatal development (7–17 PCW). Isolation was performed via FACS enrichment of CD45+ immune cells prior to scRNA-seq. The detection of myeloid progenitors in prenatal skin alongside committed immune cells (macrophages, DCs) indicates local seeding from circulating haematopoietic progenitors.

## Function

Monocyte precursors in prenatal skin represent an early myeloid progenitor population that gives rise to circulating monocytes and ultimately skin macrophages and dendritic cells. Fetal liver GMPs produce the first wave of blood monocytes from 4–5 PCW; these and subsequent bone marrow-derived progenitors seed peripheral fetal organs throughout gestation.

In peripheral organs, CCR2hi monocytes and their precursors undergo tissue adaptation, upregulating inflammatory signalling genes. The monocyte precursor cluster in fetal skin likely represents cells at an intermediate stage of this differentiation trajectory, between circulating GMP and tissue-committed monocyte fates.

## Structure / Morphology

Promonocytes have an oval or kidney-shaped nucleus with open chromatin and fine azurophil granules in the cytoplasm — intermediate between the monoblast (large, with prominent nucleoli) and the mature monocyte. No specific ultrastructural descriptions for fetal skin monocyte precursors are provided in the atlas text.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Suo, C. et al. (2022). "Mapping the developing human immune system across organs." *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Miah, M. et al. (2021). "Prenatal Development and Function of Human Mononuclear Phagocytes." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2021.607998](https://doi.org/10.3389/fimmu.2021.607998)
- Alsinet, C. et al. (2022). "Robust temporal map of human in vitro myelopoiesis using single-cell genomics." *Nature Communications*. DOI: [10.1038/s41467-022-30423-1](https://doi.org/10.1038/s41467-022-30423-1)

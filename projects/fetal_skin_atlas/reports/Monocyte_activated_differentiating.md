# Monocyte (activated/differentiating)
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | classical monocyte |
| CL ID | CL:0000860 |
| CL definition | A monocyte that responds rapidly to microbial stimuli by secreting cytokines and antimicrobial factors and which is characterized by high expression of CCR2 in both rodents and humans. |
| Match type | skos:broadMatch |
| Confidence | low |

**Justification:** No CL term exists for an 'activated/differentiating monocyte' as a distinct tissue-adapted cell state. The 'Monocyte (activated/differentiating)' cluster in the atlas represents CCR2hi monocytes that have undergone tissue adaptation in peripheral fetal organs, upregulating IL1B and TNF signalling genes. CL:0000860 'classical monocyte' is the closest available term as it captures the CCR2hi monocyte lineage identity, but does not represent the activated tissue-adapted phenotype. A new CL term may be warranted if this transitional state is reproducibly identified across datasets.

## Summary

Monocyte (activated/differentiating) is a transcriptionally distinct monocyte state identified in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. This cluster represents CCR2hi monocytes that have undergone tissue adaptation following egress from the bone marrow or fetal liver. Multi-organ single-cell profiling has characterised the transcriptional divergence between bone marrow and peripheral organ monocyte subsets:

> "Among CCR2 hi monocytes, we distinguished bone marrowand peripheral organ-specific subpopulations"
> — Suo et al. (2022), *Science*

The activated state is characterised by upregulation of inflammatory signalling programs:

> "Bone marrow CCR2 hi monocytes expressed proliferation genes, whereas peripheral organ CCR2 hi monocytes upregulated IL1B and other TNF-a signaling genes"
> — Suo et al. (2022), *Science*

Monocytes and macrophages are among the earliest innate immune populations to populate fetal skin:

> "Innate immune cells, such as macrophages and innate lymphoid cells (ILCs), were present from early gestation, whereas B cells and T cells emerged later, accompanying thymus, bone marrow and spleen formation from around 10 PCW"
> — Gopee et al. (2024), *Nature*

## Markers

Key markers for this activated/differentiating monocyte state include:

- **IL1B** — upregulated in peripheral organ monocytes; hallmark of tissue adaptation
- **CD14** — canonical monocyte surface marker; high in classical monocytes
- **CCR2** — CCR2hi defines this monocyte lineage; drives trafficking to peripheral tissues
- **S100A8 / S100A9** — calcium-binding proteins expressed in myeloid cells including monocytes
- **TNF** — upregulated as part of the peripheral tissue-adapted transcriptional programme

Differential expression data distinguishing this cluster from the Monocyte and Mono clusters in fetal skin are provided in Supplementary Table 3 of Gopee et al. (2024).

## Location

Monocyte (activated/differentiating) cells are found in the dermal immune compartment of fetal skin during prenatal development (7–17 PCW). These cells were isolated as CD45+ immune cells by FACS prior to scRNA-seq. The activated/differentiating phenotype is characteristic of monocytes in peripheral fetal organs, distinct from their bone marrow counterparts.

## Function

This monocyte population represents cells actively adapting to the tissue environment of fetal skin, transitioning from a circulating CCR2hi monocyte toward a tissue-resident macrophage or dendritic cell fate. Key functional characteristics:

- IL1B secretion contributes to local inflammatory signalling in the fetal dermis
- TNF-alpha pathway activation may regulate skin morphogenesis and immune surveillance
- These cells likely represent intermediates in the differentiation trajectory from circulating monocytes to Langerhans cells, MHCII+ macrophages, or other skin-resident myeloid lineages

The distinction from resting monocytes (Mono cluster) and the monocyte precursor cluster suggests a sequential differentiation axis within the fetal skin myeloid compartment.

## Structure / Morphology

Monocytes are large mononuclear phagocytes with a kidney- or horseshoe-shaped nucleus and granular cytoplasm containing lysosomes and vacuoles. Activated monocytes may exhibit increased cytoplasmic volume and organelle content. No specific morphological descriptions for this fetal skin subpopulation are provided in the atlas text; morphological differences from the resting monocyte state are expected to be transcriptionally rather than morphologically distinguishable at this resolution.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Suo, C. et al. (2022). "Mapping the developing human immune system across organs." *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Miah, M. et al. (2021). "Prenatal Development and Function of Human Mononuclear Phagocytes." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2021.607998](https://doi.org/10.3389/fimmu.2021.607998)
- Hoeffel, G. and Ginhoux, F. (2015). "Ontogeny of Tissue-Resident Macrophages." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2015.00486](https://doi.org/10.3389/fimmu.2015.00486)

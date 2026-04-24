# Inflammatory Dendritic Cells in Prenatal Human Skin
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: 10.1038/s41586-024-08002-x)  
Scope: fetal  
Cell Ontology: [CD1c-positive myeloid dendritic cell](http://purl.obolibrary.org/obo/CL_0002399) (CL:0002399, broad match — no exact CL term; new term needed)

## Summary

Inflammatory dendritic cells (Inflammatory DC), annotated as a fine-grained fetal immune cell state in the Gopee et al. (2024) prenatal skin atlas, correspond to type 3 dendritic cells (DC3), a recently recognized inflammatory subset within the conventional dendritic cell type 2 (cDC2) compartment. DC3 were originally identified in human blood by Villani et al. (2017) and subsequently characterized in detail by Dutertre et al. (2019) and Bourdely et al. (2020). They are distinguished from other cDC2 cells by a CD5-negative, CD163-positive, CD14-positive surface phenotype and elevated expression of inflammasome-related genes. Critically, Bourdely et al. (2020) demonstrated that DC3 develop via a GM-CSF-dependent pathway that is independent of both conventional DC-restricted progenitors (CDP) and monocyte-restricted progenitors (cMoP), establishing them as a distinct lineage rather than monocyte-derived cells.

In the prenatal skin atlas, Inflammatory DC are present in the fetal dermal immune compartment during the 7-17 post-conception weeks (PCW) window. The atlas paper does not discuss this cell type in the main narrative, but it is annotated as a distinct cell state based on differentially expressed genes in Supplementary Table 3. The presence of DC3 in prenatal skin is consistent with findings from the Suo et al. (2022) cross-organ developmental immune atlas, which showed that DC subsets are transcriptionally conserved between prenatal and adult compartments and that DCs increase in proportional abundance across multiple tissues during gestation.

## Markers

DC3/Inflammatory DC are defined by a combination of surface markers and transcriptional features that distinguish them from other dendritic cell subsets and from monocytes:

- **CD1c (BDCA-1)**: Expressed by DC3 as members of the cDC2 compartment, though at lower levels than DC2 cells. Villani et al. (2017) noted DC3 are CD1Clo compared to DC2 (DOI: 10.1126/science.aah4573).
- **CD14**: A key marker of the inflammatory DC3 subset. The most inflammatory DC3 subpopulation is CD163+CD14+ (Dutertre et al., 2019).

> "CD163+CD14+ DC3 expressed high levels of inflammasome-related genes"
>
> -- Dutertre et al. (2019)

- **CD163**: Expressed on DC3 but absent from DC2 cells, serving as a critical discriminating marker within the cDC2 compartment.

> "human cDC2 comprise CD5+ DC2 and CD5- DC3. Within the DC3 compartment, they described three clusters: CD163-, CD163-CD14+ and CD163+CD14+"
>
> -- Hill et al. (2022), summarizing Dutertre et al. (2019)

- **CD5**: Absent (negative) on DC3, distinguishing them from DC2 cells which are CD5-positive (Dutertre et al., 2019).
- **FcepsilonRIalpha**: Expressed on DC3, distinguishing them from monocytes alongside HLA-DQ. Bourdely et al. (2020) defined circulating DC3 precursors as CD88-CD1c+CD163+ and mature inflammatory DC3 as CD88-CD14+CD1c+CD163+FcepsilonRI+.
- **EREG**: The low-affinity EGFR ligand epiregulin is a key transcriptional marker of DC3, particularly in skin tissue.

> "DC3 in skin are marked by expression of EREG and can express pathogenic inflammatory cytokines characteristic of psoriasis"
>
> -- Odell (2024)

- **FCN1, VCAN, S100A8, S100A9, S100A12**: Inflammatory genes shared between DC3 and monocytes, though DC3 are additionally distinguished by Fc receptor gene expression (Odell, 2024).
- **TMEM176B**: Differentially expressed in DC3 versus cDC2 following TLR stimulation (Bourdely et al., 2020; Hill et al., 2022).
- **CD88 (C5aR1) and CD89 (FcalphaR)**: Negative on DC3; these markers are specific to monocytes and can be used to distinguish DC3 from monocytes (Dutertre et al., 2019).

## Location

### Prenatal Human Skin

In the Gopee et al. (2024) atlas, Inflammatory DC are annotated as a distinct cell state within the fetal immune compartment of prenatal skin spanning 7-17 PCW. DCs broadly (including DC1, DC2, ASDC, and pDC) are found in the dermal compartment of prenatal skin, where they co-locate with pre-dermal condensate cells and lymphoid cells based on spatial transcriptomics correlation analyses.

> "pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses"
>
> -- Gopee et al. (2024)

### Adult Human Skin

DC3 have been identified in adult human skin using single-cell approaches. Nakamizo et al. (2021) demonstrated that CD14+CD1c+ DC3 are present in healthy human dermis and are significantly enriched in psoriatic skin lesions compared to atopic dermatitis and healthy controls.

### Blood and Other Tissues

DC3 were originally identified as circulating cells in human peripheral blood (Villani et al., 2017; Dutertre et al., 2019). Bourdely et al. (2020) identified DC3 infiltrating luminal breast cancer primary tumors. DC3/inflammatory DC markers are also elevated in fibrotic lung, liver, and skin tissue (Odell, 2024).

## Function

### Naive T Cell Activation

Like classical DCs but unlike monocytes, DC3 are capable of activating naive T cells:

> "Like classical DCs but unlike monocytes, DC3s drove activation of naive T cells."
>
> -- Bourdely et al. (2020)

### CD8+CD103+ Tissue-Resident Memory T Cell Priming

DC3 display a distinctive functional capacity to prime CD8+ T cells expressing the tissue-homing integrin CD103 through TGF-beta signaling:

> "DC3s displayed a distinctive ability to prime CD8+ T cells expressing a tissue homing signature and the epithelial homing alpha-E integrin (CD103) through transforming growth factor beta (TGF-beta) signaling."
>
> -- Bourdely et al. (2020)

This function is relevant in the tumor microenvironment, where DC3 infiltration correlated positively with CD8+CD103+CD69+ tissue-resident memory T cells in breast cancer (Bourdely et al., 2020).

### Inflammatory Cytokine Production

In the context of inflammatory skin disease, DC3 are a major source of pathogenic cytokines:

> "DC3 were found to be enriched in psoriasis skin compared with eczema and healthy controls. DC3 in psoriatic skin expressed higher levels of EREG as well as cytokines characteristic of psoriasis, including IL1B and IL23A."
>
> -- Nakamizo et al. (2021)

Stimulated DC3 also secrete higher levels of TNF and IL-1beta compared to cDC2 (Bourdely et al., 2020).

### Potential Role in Prenatal Skin

While the atlas paper does not specifically discuss the functional role of Inflammatory DC in prenatal skin, the broader findings suggest that immune cells in early gestation may have non-immune functions in tissue morphogenesis. The atlas demonstrated that macrophages and DCs occupy defined microanatomical niches where they may contribute to morphogenesis rather than performing conventional immune surveillance (Gopee et al., 2024). Whether DC3/Inflammatory DC participate in these developmental processes, or instead represent the early establishment of an inflammatory DC niche, remains to be determined.

## References

- Gopee et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis". *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Dutertre et al. (2019). "Single-Cell Analysis of Human Mononuclear Phagocytes Reveals Subset-Defining Markers and Identifies Circulating Inflammatory Dendritic Cells". *Immunity*. DOI: [10.1016/j.immuni.2019.08.008](https://doi.org/10.1016/j.immuni.2019.08.008)
- Bourdely et al. (2020). "Transcriptional and Functional Analysis of CD1c+ Human Dendritic Cells Identifies a CD163+ Subset Priming CD8+CD103+ T Cells". *Immunity*. DOI: [10.1016/j.immuni.2020.06.002](https://doi.org/10.1016/j.immuni.2020.06.002)
- Villani et al. (2017). "Single-Cell RNA-Seq Reveals New Types of Human Blood Dendritic Cells, Monocytes, and Progenitors". *Science*. DOI: [10.1126/science.aah4573](https://doi.org/10.1126/science.aah4573)
- Nakamizo et al. (2021). "Single-cell analysis of human skin identifies CD14+ type 3 dendritic cells co-producing IL1B and IL23A in psoriasis". *Journal of Experimental Medicine*. DOI: [10.1084/jem.20202345](https://doi.org/10.1084/jem.20202345)
- Suo et al. (2022). "Mapping the developing human immune system across organs". *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Hill et al. (2022). "The intracellular cation channel TMEM176B as a dual immunoregulator". *Frontiers in Cell and Developmental Biology*. DOI: [10.3389/fcell.2022.1038429](https://doi.org/10.3389/fcell.2022.1038429)
- Odell (2024). "Cross-tissue organization of myeloid cells in scleroderma and related fibrotic diseases". *Current Opinion in Rheumatology*. DOI: [10.1097/BOR.0000000000001042](https://doi.org/10.1097/BOR.0000000000001042)

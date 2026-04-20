# CD4 T Cells in Prenatal Human Skin
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: 10.1038/s41586-024-08002-x)
Scope: fetal
CL Mapping: CL:0000492 (CD4-positive helper T cell) | Confidence: high | skos:exactMatch

## Summary

CD4+ T cells are among the adaptive immune cell populations that emerge in prenatal human skin from approximately 10 post-conception weeks (PCW), coinciding with thymus, bone marrow, and spleen formation. Unlike innate immune cells such as macrophages and innate lymphoid cells (ILCs), which populate the skin from early gestation, T cells appear later as part of the developing adaptive immune compartment. In fetal skin, CD4+ T cells are predominantly naive and proliferative, with a smaller subset (~30%) displaying memory-like features marked by CD45RO expression. They constitute the largest lymphocyte population in utero alongside CD8+ T cells. A notable feature of fetal skin CD4+ T cells is the progressive accumulation of FoxP3+ regulatory T cells (Tregs) during the second trimester, which coincides with and is spatially linked to hair follicle development. These cells arrive in the skin as recent thymic emigrants and expand through both continued thymic egress and local proliferation, establishing an early immunological niche that is biased toward tolerance.

## Markers

CD4+ T cells in prenatal skin are identifiable by canonical markers and exhibit a phenotypic profile distinct from adult counterparts:

- **CD4**: Defining surface marker for helper T cells; the majority of CD3+ T cells in fetal skin express CD4 (Schuster et al., 2012; Dhariwala et al., 2020).
- **CD3**: Pan-T cell marker used to identify T cell populations in the atlas via scRNA-seq and spatial transcriptomics (Gopee et al., 2024).
- **Ki-67**: Marker of recent cell cycling, highly expressed on fetal skin CD4+ Tconv cells, reflecting their proliferative status (Dhariwala et al., 2020).
- **CD27**: Expressed at high levels on fetal CD4+ Tconv cells, consistent with a naive phenotype (Dhariwala et al., 2020).
- **CD45RA / CD45RO**: Most fetal CD4+ T cells are CD45RA+ (naive), but up to 30% are CD45RO+ (memory-like) with evidence of TCR signaling (higher Nur77 levels) (Dhariwala et al., 2020).
- **CD31 (PECAM-1)**: Enriched on fetal skin T cells, marking recent thymic emigrants; up to 60% of fetal skin CD4+ Tconv cells are CD31+ compared to <10% in adult skin (Dhariwala et al., 2020).
- **FoxP3**: Expressed by ~20% of CD3+ T cells in fetal skin, marking regulatory T cells at a frequency comparable to adult skin (Schuster et al., 2012; Dhariwala et al., 2020).
- **CD25, CTLA4**: Expressed on fetal skin Tregs as part of the effector memory Treg phenotype (Dhariwala et al., 2020).
- **IL7R, LEF1, CCR7**: Differentially expressed in CD4+ T cell clusters in the atlas dataset (Supplementary Table 3; Gopee et al., 2024).

## Location

### Developmental Timing

> "Innate immune cells, such as macrophages and innate lymphoid cells (ILCs), were present from early gestation, whereas B cells and T cells emerged later, accompanying thymus, bone marrow and spleen formation from around 10 PCW"
>
> -- Gopee et al. (2024)

CD4+ T cells are absent from the earliest stages of prenatal skin development (7-9 PCW) and begin to appear from approximately 10 PCW onward. This timing aligns with the onset of thymic T cell output.

### Thymic Egress and Tissue Accumulation

> "CD31+ T cells were substantially enriched in fetal skin at both 17-18 and 23 weeks"
>
> -- Dhariwala et al. (2020)

> "the average percentage of Foxp3+ regulatory T cells (Tregs) among CD4+ cells increased significantly between 17 and 23 weeks gestation and was higher at this later fetal time point than in adult skin"
>
> -- Dhariwala et al. (2020)

CD4+ T cells accumulate progressively in fetal skin during the second trimester through both continued thymic emigration (marked by CD31 expression) and local proliferation (marked by Ki-67). The Treg fraction increases notably between 17 and 23 weeks of gestation.

### Association with Hair Follicles

> "prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells"
>
> -- Gopee et al. (2024)

> "Accumulation of Tregs in fetal skin occurs contemporaneously with hair follicle development, and preferentially at sites of higher hair follicle density within a given fetus, suggesting an early role for hair follicle biology in skin Treg residency."
>
> -- Dhariwala et al. (2020)

The spatial relationship between Tregs and hair follicles is a prominent feature of prenatal skin. CXCL14 produced by hair follicle matrix cells may serve as a chemoattractant for Treg recruitment. Treg density correlates with hair follicle density across different skin sites within individual fetuses.

### Dermal Localization

> "the majority of CD3+ cells expressed CD4, thus, confirming previous results described by Di Nuzzo et al. (2009)"
>
> -- Schuster et al. (2012)

In prenatal dermis, CD4+ T cells represent the dominant T cell subset, with the majority of CD3+ cells expressing CD4.

## Function

### Predominantly Naive, Tolerance-Biased Phenotype

> "the largest subsets of both CD4+ Tconv and CD8+ T cells in fetal skin demonstrated a largely naive, proliferative status, whereas those dominating in adult skin were enriched for markers of memory and activation"
>
> -- Dhariwala et al. (2020)

Fetal CD4+ T cells are functionally distinct from their adult counterparts. Their naive, proliferative phenotype reflects the developing immune system's bias toward tolerance rather than effector responses. This is consistent with the broader understanding that fetal CD4+ T cells have an enhanced propensity to differentiate into regulatory T cells when stimulated with alloantigens.

### Memory-Like Subset and Cytokine Potential

> "Strikingly, up to 30% of CD4+ Tconv and slightly fewer CD8+ T cells in fetal skin were CD45RO+"
>
> -- Dhariwala et al. (2020)

Despite the predominantly naive status, a subset of fetal skin CD4+ T cells expresses CD45RO with evidence of TCR signaling (elevated Nur77), suggesting antigen experience in utero. These cells show relatively enriched capacity for IFN-gamma production compared to IL-13, IL-17A, and IL-22, though overall cytokine production is substantially lower than in adult skin T cells.

### Regulatory T Cell Accumulation and Hair Follicle Protection

> "T reg cells are known to localize around the HF in late second trimester (around 21 PCW) and in postnatal skin"
>
> -- Gopee et al. (2024)

> "FoxP3 expression was found in 20.0% (SD 6.5%; n=5) of all T cells, a frequency comparable to what is found in the adult skin"
>
> -- Schuster et al. (2012)

The progressive accumulation of FoxP3+ Tregs in fetal skin, particularly around developing hair follicles, suggests a role in immune protection during the early stages of hair follicle morphogenesis. The atlas paper highlights that CXCL14-mediated Treg recruitment to the hair follicle niche may contribute to maintaining immune protection during matrix differentiation. The Treg fraction in fetal skin reaches and even exceeds adult levels by the late second trimester.

### T Cell Progenitor Restriction to Thymus

> "T cell progenitors were restricted to the thymus, potentially reflecting more stringent niche requirements for T cell development"
>
> -- Suo et al. (2022)

Unlike B cell progenitors, which were found in multiple prenatal organs, T cell progenitors remained restricted to the thymus across 7-17 PCW. This indicates that CD4+ T cells in fetal skin are thymus-derived emigrants rather than locally differentiating cells.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis". *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Suo, C. et al. (2022). "Mapping the developing human immune system across organs". *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Dhariwala, M. et al. (2020). "Developing Human Skin Contains Lymphocytes Demonstrating a Memory Signature". *Cell Reports Medicine*. DOI: [10.1016/j.xcrm.2020.100132](https://doi.org/10.1016/j.xcrm.2020.100132)
- Schuster, C. et al. (2012). "Phenotypic Characterization of Leukocytes in Prenatal Human Dermis". *Journal of Investigative Dermatology*. DOI: [10.1038/jid.2012.187](https://doi.org/10.1038/jid.2012.187)

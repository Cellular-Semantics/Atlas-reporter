# DC1 (cDC1) in Prenatal Human Skin
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: 10.1038/s41586-024-08002-x)  
Scope: fetal  
CL mapping: CL:0002394 (CD141-positive myeloid dendritic cell) -- exact match

## Summary

DC1, also known as conventional dendritic cell type 1 (cDC1), is a rare but well-characterised antigen-presenting cell subset identified in prenatal human skin from as early as the first trimester. In the fetal skin atlas (Gopee et al., 2024), DC1 is annotated as a fine-grained immune cell state in scRNA-seq data spanning 7-17 post-conception weeks (PCW). DC1 cells in developing skin closely resemble their adult counterparts (Botting & Haniffa, 2020), and DC subset transcriptional profiles are conserved between prenatal and adult tissues (Suo et al., 2022). In the prenatal skin microenvironment, Visium spatial transcriptomics predicted DC1 co-location with pre-dermal condensate cells, DC2, lymphoid tissue inducer (LTi) cells, and ILC3, placing DC1 in a niche associated with early hair follicle formation (Gopee et al., 2024). cDC1 are functionally specialised in cross-presenting exogenous antigens to CD8+ T cells and are defined by expression of CD141 (BDCA-3), XCR1, and CLEC9A (Lukowski et al., 2021; Schroth et al., 2020).

## Markers

DC1/cDC1 cells are defined by a conserved set of surface markers and transcription factors:

- **CD141 (BDCA-3, thrombomodulin)**: The canonical human cDC1 surface marker, used to distinguish cDC1 from cDC2 (CD1c-positive) subsets across tissues (Lukowski et al., 2021).

- **XCR1**: A chemokine receptor exclusively expressed on the cross-presenting DC lineage. XCR1 mediates interactions with CD8+ T cells and NK cells expressing its ligand XCL1/XCL2.
  > "the expression of XCR1 appears to be an exclusive cross-presentation feature"
  >
  > -- Bachem et al. (2012)

- **CLEC9A (DNGR-1)**: A C-type lectin receptor that recognises actin filaments exposed by necrotic cells and channels cell-associated antigens into the cross-presentation pathway.
  > "Both mouse and human cDC1s selectively express the chemokine receptor XCR1 and C-type lectin endocytic receptor CLEC9A"
  >
  > -- Qu et al. (2020)

- **Transcription factors (IRF8, BATF3, ID2)**: Required for cDC1 lineage commitment and maintenance.
  > "cDC1 development and maintenance depends on transcription factors IRF8, ID2, and Batf3."
  >
  > -- Lukowski et al. (2021)

- **Additional markers**: TLR3 (pattern recognition receptor), CADM1 (cell adhesion molecule), CD172a-negative (distinguishes from cDC2).

In the atlas, DC1 annotation was based on differentially expressed genes (Supplementary Table 3) consistent with this canonical cDC1 marker profile (Gopee et al., 2024).

## Location

### Prenatal Skin (Dermis)

DC1 cells reside in the dermis of prenatal human skin and are present from early gestation:

> "Mature adult skin contains the dendritic cell (DC) subsets DC1 and DC2, as well as macrophages, all of which have been identified in first-trimester human skin and closely resemble their adult counterparts."
>
> -- Botting & Haniffa (2020)

> "DC1 and DC2 have been identified in fetal skin prior to bone marrow production"
>
> -- Botting & Haniffa (2020)

This suggests DC1 cells initially derive from fetal liver haematopoiesis before bone marrow production begins.

### Spatial Co-location with Pre-Dermal Condensate

In the atlas Visium spatial transcriptomics analysis, DC1 was predicted to co-locate with pre-dermal condensate (pre-Dc) cells alongside DC2, LTi cells, and ILC3, based on positive Pearson correlation coefficients between per-spot normalised cell type abundances (Gopee et al., 2024, Extended Data Fig. 1f). This places DC1 within a microenvironment associated with the earliest stages of hair follicle formation.

> "pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses"
>
> -- Gopee et al. (2024)

### Temporal Dynamics

Innate immune cells, including dendritic cells, were present throughout the 7-17 PCW window studied. Macrophages initially outnumber DCs in the first trimester, but the ratio approaches adult levels by mid-gestation (Botting & Haniffa, 2020).

## Function

### Cross-Presentation and T Cell Priming

cDC1 are the principal cell type specialised in cross-presenting exogenous and cell-associated antigens to CD8+ T cells via MHC class I:

> "cDC1 cells are highly specialized in cross-presentation and activation of cytotoxic T cells, whereas cDC2 cells are primarily driving helper T responses"
>
> -- Lukowski et al. (2021)

> "Following the commitment to the cDC1 pathway, the heterogeneity of CLEC9A+ CADM1+ CD141+ lineage in the blood was also reported, splitting this population between XCR1- CXCR4hi and XCR1+ DCs"
>
> -- Calmeiro et al. (2020)

This suggests a two-staged differentiation process for cDC1: a pre-cross-presentation phase followed by acquisition of full cross-presenting capacity upon XCR1 expression.

### Potential Role in Fetal Skin Morphogenesis

While the functional role of DC1 in prenatal skin has not been directly tested, the atlas reveals that DC1 co-locates with pre-dermal condensate cells in a microenvironment linked to hair follicle initiation. The peer review of the atlas noted that adult fibroblasts interact with DC1/DC2, whereas prenatal fibroblasts do not show these interactions, suggesting that DC-fibroblast crosstalk emerges with developmental maturation (Gopee et al., 2024, Peer Review).

### Immunosuppressive Environment

Fetal skin maintains an immunosuppressive milieu. Fetal splenic DCs, which are transcriptionally similar to fetal skin DCs, demonstrate immunosuppressive properties:

> "fetal splenic DCs, which are transcriptionally similar to fetal skin DCs, are immunosuppressive in an arginase-2 dependent manner"
>
> -- Botting & Haniffa (2020)

This suggests fetal DC1 may contribute to immune tolerance rather than classical immune activation during prenatal development, consistent with the broader observation that immune effector functions are acquired between 10-12 PCW (Suo et al., 2022).

### Conservation Between Prenatal and Adult

DC subset transcriptional profiles are conserved between adult and prenatal counterparts (Suo et al., 2022), indicating that cDC1 identity is established early in development. However, functional maturation, including antigen presentation capacity (MHCII upregulation), occurs progressively during gestation (Gopee et al., 2024; Suo et al., 2022).

## References

- Gopee et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting & Haniffa (2020). "The developing immune network in human prenatal skin." *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
- Suo et al. (2022). "Mapping the developing human immune system across organs." *Science*. DOI: [10.1126/science.abo0510](https://doi.org/10.1126/science.abo0510)
- Lukowski et al. (2021). "Absence of Batf3 reveals a new dimension of cell state heterogeneity within conventional dendritic cells." *iScience*. DOI: [10.1016/j.isci.2021.102462](https://doi.org/10.1016/j.isci.2021.102462)
- Calmeiro et al. (2020). "Dendritic Cell Vaccines for Cancer Immunotherapy: The Role of Human Conventional Type 1 Dendritic Cells." *Pharmaceutics*. DOI: [10.3390/pharmaceutics12020158](https://doi.org/10.3390/pharmaceutics12020158)
- Schroth et al. (2020). "Innate Functions of Dendritic Cell Subsets in Cardiac Allograft Tolerance." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2020.00798](https://doi.org/10.3389/fimmu.2020.00798)
- Bachem et al. (2012). "Expression of XCR1 Characterizes the Batf3-Dependent Lineage of Dendritic Cells Capable of Antigen Cross-Presentation." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2012.00214](https://doi.org/10.3389/fimmu.2012.00214)
- Qu et al. (2020). "Conventional type 1 dendritic cells in protective antitumor immunity and its potential in hepatocellular carcinoma." *Hepatoma Research*. DOI: [10.20517/2394-5079.2020.12](https://doi.org/10.20517/2394-5079.2020.12)
- Reynolds et al. (2021). "Developmental cell programs are co-opted in inflammatory skin disease." *Science*. DOI: [10.1126/science.aba6500](https://doi.org/10.1126/science.aba6500)

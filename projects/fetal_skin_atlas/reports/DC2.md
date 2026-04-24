# Type 2 Conventional Dendritic Cell in Adult Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: adult
Source dataset: Reynolds et al. (2021), integrated into Gopee et al. (2024)
Cell Ontology: [conventional dendritic cell type 2](http://purl.obolibrary.org/obo/CL_0002400) (CL:0002400, exact match)

## Summary

DC2 cells in adult human skin correspond to type 2 conventional dendritic cells (cDC2), defined by expression of CD1c (BDCA-1), CLEC10A (CD301), and IRF4. Reynolds et al. (2021) identify DC2 alongside DC1 as the myeloid DC branch within the 14-state mononuclear phagocyte landscape of human skin, distinguished from Langerhans cells and monocyte-derived DCs. DC2 cells are present in embryonic skin from 7 post-conception weeks (PCW). In adult skin they are the more abundant of the two myeloid DC subtypes, specialised for MHC class II antigen presentation to CD4+ T helper cells and for promoting T helper cell polarisation. Note: this report describes the adult DC2 population; the fetal DC2 population is documented separately (DC2_fetal.md).

## Markers

Defining markers of DC2 (cDC2):

> "cDC2, also known as CD1c+ DC, express CD1c together with CD301 (CLEC10A) and FcεR1α and are the human equivalent to murine cDC2"
>
> — Heger et al. (2022)

> "DC2 cells express CD1c together with CLEC10A and IRF4; DC3 (CD163+CD14+) cells share transcriptional features with monocytes and are distinct from bona fide cDC2"
>
> — Brown et al. (2019)

Reynolds et al. (2021) confirm DC2 identity via gene signature enrichment:

> "enrichment of gene signatures for murine dermal CD11c+ (DC2) in each node"
>
> — Reynolds et al. (2021)

Key markers: **CD1C** (BDCA-1, defining surface marker), **CLEC10A** (CD301, defining C-type lectin), **CD11B** (ITGAM), **IRF4** (master transcription factor).

## Location

DC2 cells are found in the dermis of adult human skin and are detectable from early in fetal development:

> "We observe Dendritic Cells 1 and 2 (DC1, DC2) and Langerhans cells (LCs) in embryonic skin as early as 7 PCW, prior to bone marrow hematopoiesis, but macrophages are the dominant MP in first trimester skin"
>
> — Reynolds et al. (2021)

In PAGA analysis of the adult skin mononuclear phagocyte landscape, DC1 and DC2 form a single myeloid DC branch of differentiation distinct from the Langerhans cell and monocyte-derived DC branches:

> "Partition-based approximate graph abstraction (PAGA) analysis revealed three branches of differentiation: LCs, myeloid DCs (DC1 and DC2) and monocyte-derived DCs (mo-DCs)"
>
> — Reynolds et al. (2021)

## Function

### MHC class II antigen presentation

DC2 cells are the principal cDC subset specialised for MHC class II antigen presentation to CD4+ T helper cells. They can drive polarisation of naïve CD4+ T cells toward Th2 or Th17 helper cell subsets depending on the inflammatory context and cytokine milieu. The expression of FcεR1α enables DC2 to respond to IgE-opsonised allergens, linking them to allergic skin inflammation.

### Role in inflammatory skin disease

DC2 cells are enriched in lesional skin from atopic dermatitis and psoriasis patients relative to healthy control skin. Reynolds et al. (2021) show that developmental DC programmes are co-opted in inflammatory skin disease, with myeloid DCs including DC2 as key mediators of this process.

### Distinction from DC3

Human skin also contains a CD163+CD14+ population (sometimes termed DC3) that shares transcriptional features with monocytes. DC3 cells are distinct from bona fide cDC2 (DC2), which express CD1c, CLEC10A, and IRF4 without significant monocyte features (Brown et al., 2019). In Reynolds et al. (2021), such monocyte-like DCs may correspond to the monocyte-derived DC (mo-DC) population in the PAGA topology rather than DC2.

## References

- Reynolds G, Vegh P, Fletcher J et al. (2021). "Developmental cell programs are co-opted in inflammatory skin disease." *Science*. DOI: [10.1126/science.aba6500](https://doi.org/10.1126/science.aba6500)
- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Heger L et al. (2022). "Guidelines for the use of flow cytometry and cell sorting in immunological studies." *European Journal of Immunology*. DOI: [10.1002/eji.202249917](https://doi.org/10.1002/eji.202249917)
- Brown CC et al. (2019). "Human skin DC2 and DC3 are characterised by distinct transcriptional signatures." CorpusId:239818941

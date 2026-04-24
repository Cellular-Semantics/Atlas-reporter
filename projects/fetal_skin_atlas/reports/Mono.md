# Monocyte in Adult Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: adult
Source dataset: Reynolds et al. (2021), integrated into Gopee et al. (2024)
Cell Ontology: [monocyte](http://purl.obolibrary.org/obo/CL_0000576) (CL:0000576, broad match — no exact CL term for skin-resident monocyte)

## Summary

Monocytes (Mono) in adult human skin are one of 14 mononuclear phagocyte (MP) states identified by Reynolds et al. (2021). They are annotated by alignment to blood MP populations using TransferAnchors, and are distinguished from monocyte-derived macrophages (Mono mac) and monocyte-derived dendritic cells (MoDC) by their retention of monocyte-specific gene programmes. Skin monocytes express CD14 and can carry CD16 (FCGR3A) depending on their classical or non-classical state. They are capable of differentiating into macrophages or dendritic cells upon tissue entry.

## Markers

Reynolds et al. (2021) used CD14 and CCR7 among the panel for CyTOF protein validation of skin MPs:

> "CD8A, CD163, CD14 and CCR7 were chosen for CyTOF protein validation"
>
> — Reynolds et al. (2021)

Human blood monocytes are classified into three subsets based on CD14 and CD16 expression:

> "human monocytes were initially defined based on morphology and cytochemistry. The nomenclature committee of the International Union of Immunological Societies classified monocytes into three subsets-classical (CD14++ CD16-), intermediate (CD14++ CD16+), and non-classical (CD14+ CD16++)-each with distinct surface markers and immune functions"
>
> — Lin et al. (2025)

## Location

Monocytes appear as a distinct cluster in the adult skin MP UMAP. Reynolds et al. (2021) identified:

> "We observed 14 states of mononuclear phagocytes (MPs) in human skin (Figs. 3A-B and S5A) that we annotated by aligning skin and blood MPs using TransferAnchors function in Seurat (Fig. S5B) and expression of MP marker genes. We show the limitations of currently used surface markers and FACS-gates to adequately resolve skin MP heterogeneity"
>
> — Reynolds et al. (2021)

Skin monocytes are found in the dermis, where they can patrol blood vessels or extravasate into tissue. Monocyte-derived dermal CD14+ cells provide direct B cell help and support T cell differentiation (Reynolds and Haniffa, 2015).

## Function

### Inflammatory recruitment and differentiation

Classical monocytes are rapidly recruited from blood to sites of skin inflammation via CCR2-CCL2 signalling. Upon entry, they can differentiate into macrophages or dendritic cells:

> "Classical monocytes initiate the immune system's inflammatory response and facilitate tissue repair. They possess a strong capacity for phagocytosis, enabling them to engulf and eliminate pathogens"
>
> — Lin et al. (2025)

### Monocyte-derived cells in skin homeostasis

> "CD14+ human and Ly6Chi CX3CR1lo murine monocytes can exhibit considerable functional plasticity as demonstrated by their acquisition of DC-like and macrophage-like characteristics in vitro and in vivo"
>
> — Reynolds and Haniffa (2015)

Monocyte-derived dermal cells fulfil DC-associated functions including T cell activation and B cell help:

> "Monocyte-derived dermal CD14+ cells express IL-1α have been shown to induce differentiation of follicular helper T cells and provide direct B cell help"
>
> — Reynolds and Haniffa (2015)

### Relationship to inflammatory monocytes

In AD skin, inflammatory monocytes and monocyte-derived DCs (Mo-DCs) positively correlate with tissue-resident memory T cells and disease severity (EASI score), indicating their role in sustaining cutaneous inflammation (Mehta et al., 2024). Reynolds et al. (2021) distinguish the Mono population from the Inf. mono (inflammatory monocyte) state, which is specifically enriched in inflammatory conditions.

## References

- Reynolds G, Vegh P, Fletcher J et al. (2021). "Developmental cell programs are co-opted in inflammatory skin disease." *Science*. DOI: [10.1126/science.aba6500](https://doi.org/10.1126/science.aba6500)
- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Reynolds G, Haniffa M (2015). "Human and Mouse Mononuclear Phagocyte Networks: A Tale of Two Species?" *Frontiers in Immunology*. PMC: PMC4479794
- Lin Y, Makkar H, Zhang S et al. (2025). "Mechanical cues orchestrate monocyte behavior in immune regulation and disease." *PMC*: PMC12205964

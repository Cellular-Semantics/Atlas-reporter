# Plasmacytoid Dendritic Cells (pDC) in Prenatal Human Skin
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Cell Ontology: [plasmacytoid dendritic cell](http://purl.obolibrary.org/obo/CL_0000784) (CL:0000784, exact match)

## Summary

Plasmacytoid dendritic cells (pDCs) are a specialized subset of innate immune cells identified in the prenatal human skin atlas of Gopee et al. (2024). In the integrated UMAP visualization of prenatal skin, adult skin, and skin organoid datasets, pDCs are annotated as a distinct cell lineage among the immune compartment (Fig. 1e). pDCs are classically defined as the principal producers of type I interferons (IFN-alpha/beta) in response to viral nucleic acids, a function mediated through Toll-like receptors TLR7 and TLR9 (Reizis et al., 2011; Collin & Bigley, 2018). They are distinguished from conventional dendritic cells (cDCs) by their plasma cell-like morphology, lymphoid-associated transcriptional regulators, and a unique surface marker profile centred on CD123, CD303 (CLEC4C/BDCA-2), and CD304 (BDCA-4) (Collin & Bigley, 2018).

In the context of prenatal skin development, pDCs have been identified in first-trimester human skin by single-cell RNA sequencing, alongside other myeloid subsets including DC1, DC2, monocytes, and macrophages (Botting & Haniffa, 2020). However, very little is known about the specific function of pDCs in developing skin beyond their presence. In adult skin, pDCs are generally absent under homeostatic conditions but are rapidly recruited during injury, infection, or inflammation, where they contribute to wound healing and immune defence through type I interferon production (Gregorio et al., 2010; Chen et al., 2020). Their presence in prenatal skin suggests a potential role in immune surveillance or tissue homeostasis during early gestation, although direct functional studies in this context are currently lacking.

## Markers

pDCs are defined by a characteristic set of surface markers and transcription factors that distinguish them from conventional dendritic cells:

- **CD123 (IL3RA):** The alpha chain of the interleukin-3 receptor, universally expressed on pDCs and a key identifying marker. CD123 is retained from the granulocyte-monocyte-dendritic cell progenitor (GMDP) stage and is down-regulated when progenitors differentiate into myeloid cDCs (Collin & Bigley, 2018).
- **CLEC4C (CD303/BDCA-2):** A type II C-type lectin exclusively expressed on pDCs that mediates antigen capture and potently inhibits type I interferon production when cross-linked. First characterised by Dzionek et al. (2001) as a pDC-specific marker.
- **CD304 (Neuropilin/BDCA-4):** Another well-established pDC surface marker used in combination with CD303 for identification (Collin & Bigley, 2018).
- **LILRA4 (ILT7/CD85g):** An immunoglobulin-like receptor expressed on pDCs that regulates type I interferon production (Collin & Bigley, 2018).
- **TCF4 (E2-2):** The master transcription factor required for pDC development and lineage identity. TCF4 is part of a multiprotein complex with BCL11A that maintains pDC lineage commitment (Collin & Bigley, 2018; Araujo et al., 2024).
- **TLR7 and TLR9:** Intracellular Toll-like receptors that mediate recognition of single-stranded RNA and unmethylated CpG DNA, respectively. These are the primary sensors through which pDCs detect viral nucleic acids and trigger type I interferon production (Tsepkolenko et al., 2019).
- **IRF7:** Interferon regulatory factor 7, a key downstream transcription factor in the pDC interferon signalling pathway.

Additional transcriptomic markers identified in single-cell studies include RHEX, GZMB (granzyme B), FAM129C, and CUX2 (Collin & Bigley, 2018).

## Location

### Prenatal skin

In the Gopee et al. (2024) prenatal skin atlas, pDCs are annotated as a fetal-specific fine-grained cell type within the immune compartment, identified across 7-17 PCW prenatal skin samples. Their spatial distribution within prenatal skin (epidermal versus dermal) is not described in detail in the accessible atlas data.

Botting & Haniffa (2020) report that pDCs have been identified in first-trimester human skin by scRNA-seq, but note that "very little is known about dermal DCs in developing skin beyond their presence." Dzionek et al. (2001) documented immature pDCs in fetal tissues including fetal thymus, fetal liver, and fetal bone marrow, establishing that pDC precursors are present in multiple fetal haematopoietic compartments.

### Adult skin

In healthy adult skin, pDCs are generally absent under homeostatic conditions (Chen et al., 2020). However, they rapidly infiltrate the skin during:
- Viral infection (Gregorio et al., 2010)
- Inflammatory and autoimmune diseases such as lupus erythematosus
- Skin injury and wound healing (Gregorio et al., 2010)

> "Plasmacytoid dendritic cells (pDCs), a BDCA-2-expressing dendritic cell (DC) subset, are generally not found in healthy human skin."
>
> -- Chen et al. (2020)

### Other tissues

Outside the skin, pDCs are found in peripheral blood, lymph nodes, tonsils, bone marrow, and cord blood (Dzionek et al., 2001; Collin & Bigley, 2018).

## Function

### Type I interferon production

The hallmark function of pDCs is the rapid and massive production of type I interferons (IFN-alpha and IFN-beta) upon sensing viral nucleic acids through TLR7 (ssRNA) and TLR9 (CpG DNA). pDCs can produce 10,000-fold more type I interferon than other cell types during viral infection (Tsepkolenko et al., 2019).

> "Plasmacytoid dendritic cells (pDCs) were first described as interferon-producing cells."
>
> -- Reizis et al. (2011)

### Wound healing in skin

pDCs have been shown to sense skin injury and promote wound healing through type I interferons in a TLR7- and TLR9-dependent manner:

> "Cutaneous injury in mice drives transient TLR7- and TLR9-mediated production of type I interferon by plasmacytoid dendritic cells, which is required for re-epithelialization of the skin."
>
> -- Gregorio et al. (2010)

The mechanism involves cathelicidins (antimicrobial peptides) released by wounded keratinocytes forming complexes with self-DNA and self-RNA from dying cells, which then activate pDC TLR7 and TLR9 signalling (Chen et al., 2020). pDCs also secrete IL-6, an inflammatory cytokine involved in re-epithelialisation of skin wounds (Tsepkolenko et al., 2019).

### Potential role in prenatal skin

The function of pDCs in prenatal skin is not yet characterised. Their presence from the first trimester suggests potential roles in:
- Innate immune surveillance of the developing skin
- Contribution to the tolerogenic environment that prevents maternal-fetal immune rejection
- Possible non-immune functions in tissue morphogenesis, analogous to the non-immune roles of macrophages in prenatal skin demonstrated by Gopee et al. (2024)

Further investigation is needed to determine whether fetal skin pDCs are functionally mature or whether they remain in an immature, quiescent state during prenatal development.

## References

- Gopee N et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis". *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting RA, Haniffa M (2020). "The developing immune network in human prenatal skin". *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
- Gregorio J et al. (2010). "Plasmacytoid dendritic cells sense skin injury and promote wound healing through type I interferons". *Journal of Experimental Medicine*. DOI: [10.1084/jem.20101102](https://doi.org/10.1084/jem.20101102)
- Chen YL et al. (2020). "Re-evaluation of human BDCA-2+ DC during acute sterile skin inflammation". *Journal of Experimental Medicine*. DOI: [10.1084/jem.20190811](https://doi.org/10.1084/jem.20190811)
- Collin M, Bigley V (2018). "Human dendritic cell subsets: an update". *Immunology*. DOI: [10.1111/imm.12888](https://doi.org/10.1111/imm.12888)
- Reizis B et al. (2011). "Plasmacytoid dendritic cells: one-trick ponies or workhorses of the immune system?". *Nature Reviews Immunology*. DOI: [10.1038/nri3027](https://doi.org/10.1038/nri3027)
- Tsepkolenko A et al. (2019). "The regenerative potential of skin and the immune system". *Clinical, Cosmetic and Investigational Dermatology*. DOI: [10.2147/ccid.s196364](https://doi.org/10.2147/ccid.s196364)
- Dzionek A et al. (2001). "BDCA-2, a Novel Plasmacytoid Dendritic Cell-specific Type II C-type Lectin, Mediates Antigen Capture and Is a Potent Inhibitor of Interferon alpha/beta Induction". *Journal of Experimental Medicine*. DOI: [10.1084/jem.20011267](https://doi.org/10.1084/jem.20011267)

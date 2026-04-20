# ASDC (Axl+Siglec6+ Dendritic Cells) in Prenatal Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: fetal
Cell Ontology: [Axl+ dendritic cell, human](http://purl.obolibrary.org/obo/CL_0017009) (CL:0017009, exact match)

## Summary

ASDC (Axl+Siglec6+ dendritic cells) is a transitional dendritic cell population identified in the prenatal skin atlas of Gopee et al. (2024), where it is annotated as a distinct immune cell lineage within the integrated prenatal skin, adult skin, and skin organoid UMAP. Also known as AS-DC, DC5, pre-DC, or transitional DC (tDC) in various studies, ASDCs were first described in human blood through single-cell RNA-seq by Villani et al. (2017) and independently by See et al. (2017), who identified them as a population within the CD123+ DC gate that expresses AXL and SIGLEC6 and exhibits a mixed pDC-cDC transcriptomic profile. ASDCs occupy a unique position at the intersection of plasmacytoid DC (pDC) and type 2 conventional DC (cDC2) clusters, displaying a spectrum from pDC-like to cDC2-like features (Idoyaga et al., 2025). Functionally, ASDCs are closer to cDC2: they efficiently stimulate CD4 and CD8 T cells but produce minimal type I interferon (Segura, 2022; Roussel et al., 2022). They arise from the common dendritic cell progenitor (CDP) via an IRF8-high developmental pathway and require TCF4/E2-2 for their differentiation, similar to pDCs (Cytlak et al., 2020). In the prenatal skin context, their presence among the annotated immune populations suggests a role in the developing skin immune network, though the atlas does not provide detailed functional characterization specific to this population.

## Markers

ASDCs are defined by a distinctive combination of markers that reflect their transitional identity between pDCs and cDC2s:

- **AXL**: A receptor tyrosine kinase that serves as a primary defining marker for this subset. AXL binds apoptotic cells and is involved in phagocytosis and efferocytosis, suggesting functions beyond antigen presentation.
  > "a DC subset expressing AXL, SIGLEC1, and SIGLEC6 (AS DCs), was identified as a distinct DC population that arises from the CDP progenitor."
  > -- Pachocki et al. (2025)

- **SIGLEC6 (CD327)**: A sialic acid-binding immunoglobulin-like lectin co-expressed with AXL as the second defining marker of this population.
  > "AXL+SIGLEC6+ DC were identified in the blood by scRNA-seq analysis as a subpopulation of CD123+ DC."
  > -- Segura (2022)

- **SIGLEC1 (CD169)**: Co-expressed with AXL and SIGLEC6, particularly on CD123+ ASDCs.
  > "AS-DCs represent 2-3% of DCs in scRNAseq and cytometry analysis, are CD123 + CD11c −/low , co-express unique markers AXL, SIGLEC1/6 and SIGLEC2/CD22, and exhibit a continuum of pDCs and cDC markers and signatures"
  > -- Roussel et al. (2022)

- **CD123 (IL3RA)**: Shared with pDCs; ASDCs are identified within the CD123+ DC gate but subdivide into CD123+ and CD11c+ subsets.
  > "AXL+ Siglec-6+ dendritic cells (ASDC) are novel myeloid DCs which can be subdivided into CD11c+ and CD123+ expressing subsets."
  > -- Warner van Dijk et al. (2024)

- **CD11c (ITGAX)**: Marks the more cDC2-like subset of ASDCs; CD11c+ ASDCs express higher levels of co-stimulatory markers.

- **CD86 and HLA-DR**: Costimulatory molecules enabling T cell activation.
  > "AS-DCs also express the costimulatory molecule CD86 and HLA-DR and are able to induce CD4 + and CD8 + T-cell proliferation, while IFN-I secretion remains marginal"
  > -- Roussel et al. (2022)

- **CD2, CX3CR1, CD33 (SIGLEC3), CD5**: cDC-associated markers co-expressed in ASDCs at both protein and mRNA levels.

- **BDCA-2 (CD303)**: Expressed at lower levels than on canonical pDCs but contributes to their historical misclassification within pDC gates.

- **Transcription factors**: BCL11A, RUNX2, SPIB (pDC-associated); TCF4/E2-2 (required for development); ID2 (cDC-associated).
  > "AXL+SIGLEC6+ DC also highly express the transcription factors BCL11A, RUNX2, and SPIB, which are involved in pDC development."
  > -- Segura (2022)

## Location

### Prenatal Skin

ASDCs are annotated as a distinct immune cell lineage in the prenatal skin atlas (Gopee et al., 2024), identified in the integrated scRNA-seq dataset of prenatal skin (7-17 PCW) alongside DC1, DC2, Langerhans cells, pDCs, macrophage subsets, and lymphoid populations.

### Blood and Lymphoid Organs

ASDCs were originally identified in human peripheral blood and represent 2-3% of DCs in scRNA-seq and cytometry analyses (Villani et al., 2017; See et al., 2017; Roussel et al., 2022). They have been detected in lymphoid organs including tonsil and spleen.
> "They have also been evidenced in lymphoid organs but not in steady-state peripheral tissues, and are recruited to inflamed skin and lungs."
> -- Segura (2022)

### Inflamed Tissues

ASDCs are absent from steady-state peripheral tissues but are recruited to sites of inflammation, including skin, lungs, and anogenital tissues:
> "The ASDCs detected herein from skin blisters were highly activated, expressing CCL22 and CD83, and may be recruited into skin in response to inflammatory cues."
> -- Chen et al. (2019)

> "We showed for the first time that these two ASDC subsets are present in inflamed human anogenital tissues where HIV transmission occurs."
> -- Warner van Dijk et al. (2024)

ASDCs have also been found in the circulation and tumors of cancer patients, including pancreatic cancer and melanoma (Sosa Cuevas et al., 2022; Pachocki et al., 2025).

## Function

### T Cell Stimulation and Polarization

ASDCs are efficient antigen-presenting cells that stimulate both CD4+ and CD8+ T cell proliferation, despite their inability to produce type I IFN:
> "They are efficient for stimulating CD4 T cells ex vivo, and do not secrete type I IFN."
> -- Segura (2022)

CD11c+ ASDCs are more potent than CD123+ ASDCs in co-stimulatory marker expression and T cell activation:
> "both subsets of blood ASDCs but not pDCs expressed co-stimulatory and maturation markers which were more prevalent on CD11c + ASDCs, thus inducing more T cell proliferation and activation than their CD123 + counterparts."
> -- Warner van Dijk et al. (2024)

ASDCs polarize naive T cells toward multiple T helper subsets:
> "There was also a significant polarisation of naive T cells by both ASDC subsets toward Th2, Th9, Th22, Th17 and Treg but less toward a Th1 phenotype."
> -- Warner van Dijk et al. (2024)

### Inflammatory Recruitment and Effector Function

During inflammation, ASDCs are actively recruited from the circulation and acquire an effector phenotype with a distinct IFN signature:
> "local inflammation recruits cDC to the site of inflammation, where Axl Siglec-6 DC (ASDC) acquires an effector phenotype."
> -- Lubin et al. (2024)

> "Blister ASDC preserved their expression of Siglec-6 and AXL, two receptors involved in phagocytosis, that may aid the clearance of the pathogen or required for efferocytosis during the resolution phase of inflammation."
> -- Lubin et al. (2024)

### Regulatory Potential

ASDCs can adopt a regulatory phenotype under certain conditions:
> "ASDC cultured with recombinant IFNbeta adopted a more regulatory phenotype."
> -- Lubin et al. (2024)

### Precursor/Transitional Identity

Whether ASDCs represent a bona fide DC subset or a precursor population remains debated. They can differentiate into cDC2 in culture systems, mapping exclusively to the DC2 developmental pathway:
> "AXL+SIGLEC6+ pre-DCs mapped exclusively to the DC2 pathway."
> -- Cytlak et al. (2020)

> "As AS DCs (also called AXL + DCs) are also able to prime T cells but do not proliferate, it is hypothesized that instead of a precursor, they represent a distinct functional DC subset that can transition to cDC2."
> -- Pachocki et al. (2025)

## References

- Gopee et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Villani et al. (2017). "Single-cell RNA-seq reveals new types of human blood dendritic cells, monocytes, and progenitors." *Science*. DOI: [10.1126/science.aah4573](https://doi.org/10.1126/science.aah4573)
- See et al. (2017). "Mapping the human DC lineage through the integration of high-dimensional techniques." *Science*. DOI: [10.1126/science.aag3009](https://doi.org/10.1126/science.aag3009)
- Segura (2022). "Human dendritic cell subsets: An updated view of their ontogeny and functional specialization." *European Journal of Immunology*. DOI: [10.1002/eji.202249950](https://doi.org/10.1002/eji.202249950)
- Chen et al. (2019). "Re-evaluation of human BDCA-2+ DC during acute sterile skin inflammation." *Journal of Experimental Medicine*. DOI: [10.1084/jem.20190811](https://doi.org/10.1084/jem.20190811)
- Warner van Dijk et al. (2024). "Characterising plasmacytoid and myeloid AXL+ SIGLEC-6+ dendritic cell functions and their interactions with HIV." *PLoS Pathogens*. DOI: [10.1371/journal.ppat.1012232](https://doi.org/10.1371/journal.ppat.1012232)
- Roussel et al. (2022). "Plasmacytoid Dendritic Cells, a Novel Target in Myeloid Neoplasms." *Cancers*. DOI: [10.3390/cancers14143621](https://doi.org/10.3390/cancers14143621)
- Lubin et al. (2024). "The lifespan and kinetics of human dendritic cell subsets and their precursors in health and inflammation." *Science Immunology*. DOI: [10.1126/sciimmunol.adk4092](https://doi.org/10.1126/sciimmunol.adk4092)
- Cytlak et al. (2020). "Differential IRF8 Transcription Factor Requirement Defines Two Pathways of Dendritic Cell Development in Humans." *Immunity*. DOI: [10.1016/j.immuni.2020.07.003](https://doi.org/10.1016/j.immuni.2020.07.003)
- Pachocki et al. (2025). "Comparing DC subsets in solid tumors: what about DC3s?" *Frontiers in Immunology*. DOI: [10.3389/fimmu.2025.1573437](https://doi.org/10.3389/fimmu.2025.1573437)
- Collin & Bigley (2018). "Human dendritic cell subsets: an update." *Immunology*. DOI: [10.1111/imm.12888](https://doi.org/10.1111/imm.12888)
- Leylek et al. (2019). "Integrated Cross-Species Analysis Identifies a Conserved Transitional Dendritic Cell Population." *Cell Reports*. DOI: [10.1016/j.celrep.2019.11.042](https://doi.org/10.1016/j.celrep.2019.11.042)
- Idoyaga et al. (2025). "Bridging pDCs and cDCs: The Identity of Transitional Dendritic Cells." *Cells*. DOI: [10.3390/cells14131009](https://doi.org/10.3390/cells14131009)
- Sosa Cuevas et al. (2022). "Diversification of circulating and tumor-infiltrating plasmacytoid DCs towards the P3 (CD80+ PDL1-)-pDC subset negatively correlated with clinical outcomes in melanoma patients." *Clinical & Translational Immunology*. DOI: [10.1002/cti2.1389](https://doi.org/10.1002/cti2.1389)
- Rhodes et al. (2019). "Human Dendritic Cell Subsets, Ontogeny, and Impact on HIV Infection." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2019.01088](https://doi.org/10.3389/fimmu.2019.01088)

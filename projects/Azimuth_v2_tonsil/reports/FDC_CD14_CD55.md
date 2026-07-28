# CD14+CD55+ Follicular Dendritic Cells in the Human Tonsil Germinal Center

Atlas: An atlas of cells in the human tonsil (Massoni-Badosa et al., 2024) — Azimuth human_tonsil_v2 reference (DOI: 10.1016/j.immuni.2024.01.006). Upstream starting annotation: King et al. (2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (B-cell follicle / germinal center)
Cell Ontology: [follicular dendritic cell](http://purl.obolibrary.org/obo/CL_0000442) (CL:0000442, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3668

## Summary

"CD14+CD55+" is a fine-grained annotation in the Azimuth human_tonsil_v2 reference, derived from the King et al. (2021) integrated single-cell atlas of the human palatine tonsil. The label names two defining surface markers — CD14 and CD55 (decay-accelerating factor, DAF) — carried by a stromal, antigen-retaining subset of the B-cell follicle. On the basis of its complement-regulatory (CD55/DAF) phenotype, its residence in the germinal center, and its dendritic-morphology, antigen-trapping behaviour, this population is assigned to the follicular dendritic cell (FDC) lineage (proposed Cell Ontology parent CL:0000442). FDCs are non-hematopoietic stromal fibroblasts of the lymphoid follicle that capture and display native antigen as immune complexes to germinal-center B cells, support B-cell survival, and organise follicular architecture (Rezk et al., 2013; Doan et al., 2022). The CD55 (DAF) mark reflects the complement-regulatory environment of the germinal center (Dernstedt et al., 2020), while CD14 distinguishes this particular FDC subset within the atlas.

## Markers

The Azimuth label itself supplies the two subset-defining markers, **CD14** and **CD55** (paraphrased from the atlas annotation; King et al., 2021). No atlas supplementary marker table was retrievable, so the marker biology below is grounded in the broader FDC literature.

**CD55 / DAF (decay-accelerating factor)** is a complement-regulatory protein. Its functional role in the germinal center — restraining complement deposition on host cells — is protein-level (surface DAF measured by flow cytometry):

> "The complement regulatory protein Decay Accelerating Factor (DAF) blocks complement deposition host cells and therefore also phagocytosis of cells."
>
> — Dernstedt et al. (2020)

Expression of CD55/DAF on cells of the follicle is consistent with the FDC lineage's role in creating a protected niche where complement-opsonised antigen is retained rather than destroyed.

**Complement receptors CR1 (CD35) and CR2 (CD21)** are the canonical FDC surface markers and are protein-level (antibody/imaging based). They mediate the immune-complex capture that defines FDC function:

> "FDCs within primary follicles express high amounts of complement receptors-1 and -2 (CR1 or CD35 and CR2 or CD21) and can be induced to express Fc"
>
> — Wang et al. (2011)

Human FDCs additionally express CR3, again a protein-level surface marker:

> "CR1 and CR2 are also expressed by human FDCs, along with CR3"
>
> — Doan et al. (2022)

**CD14** is the second subset-defining marker in the Azimuth label. It is not a classical FDC marker in the reviewed literature; within this atlas it distinguishes the CD14+CD55+ subset from other follicular stromal/FDC states. No independent protein-level evidence for CD14 on FDCs was found in the traversed literature (marker asserted at the annotation/transcript level by the atlas label only).

## Location

FDCs are confined to the lymphoid follicle. In the tonsil, this places the CD14+CD55+ subset within the B-cell follicle and germinal center:

> "Follicular dendritic cells (FDCs) are a specialized type of antigen-presenting dendritic cells that are largely restricted to lymphoid follicles. They form dense three-dimensional meshwork patterns within benign follicles, which maintain the follicular architecture."
>
> — Rezk et al. (2013)

Within the germinal center, FDCs are especially prominent in the light zone, where they express additional markers such as MFG-E8 (FDC-M1) and VCAM-1 and help establish follicle identity and B-cell retention (Wang et al., 2011).

## Function

The core function of the FDC lineage is capture, long-term retention, and periodic re-display of native antigen as immune complexes to germinal-center B cells. This is achieved through complement receptors CR1/CR2:

> "Here we found that FDC acquired complement-coated immune complexes (IC) from non-cognate B cells via complement receptors 1 and 2 (CD35 and CD21 respectively) and rapidly internalized them by an actin-dependent pathway."
>
> — Heesters et al. (2013)

> "IC were retained intact within a non-degradative cycling compartment and were displayed periodically on the cell surface where they were accessible to antigen-specific B cells."
>
> — Heesters et al. (2013)

Through this antigen display and accompanying survival signals, FDCs rescue germinal-center B cells from apoptosis and drive their onward differentiation:

> "FDCs aid in the rescue of bound B cells from apoptosis, and induce the differentiation of B cells into long-term memory B cell clones or plasma cells."
>
> — Rezk et al. (2013)

Single-cell RNA sequencing of human FDCs has refined this functional picture, implicating FDCs in regulating B-cell antigen availability and in T-cell interactions:

> "Single-cell RNA sequencing of human follicular dendritic cells (FDCs) provides insights in germinal center biology and enhances our understanding of these enigmatic cells. Data suggest regulation of B cell antigen availability by FDCs and T cell interactions with FDCs."
>
> — Heesters et al. (2021)

The CD55/DAF component of this subset's phenotype ties directly to complement regulation in the follicle. DAF shapes complement-dependent clearance of germinal-center cells:

> "Collectively, our results reveal a novel role of DAF to pre-prime activated human B cells for phagocytosis prior to apoptosis."
>
> — Dernstedt et al. (2020)

## Structure / Morphology

FDCs are non-hematopoietic stromal cells with a fibroblastic origin and an elaborate dendritic morphology that forms a three-dimensional network throughout the follicle:

> "Follicular dendritic cells (FDCs) are a radio-resistant stromal fibroblast subset that can capture and harbor antigen over extended periods of time"
>
> — Doan et al. (2022)

This meshwork is the structural scaffold of the germinal center, maintaining follicular architecture as described above (Rezk et al., 2013).

## References
- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Heesters B et al. (2021). "Characterization of human FDCs reveals regulation of T cells and antigen presentation to B cells". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.20210790](https://doi.org/10.1084/jem.20210790)
- Rezk S et al. (2013). "Follicular dendritic cells: origin, function, and different disease-associated patterns". *Human Pathology*. DOI: [10.1016/j.humpath.2012.10.005](https://doi.org/10.1016/j.humpath.2012.10.005)
- Heesters B et al. (2013). "Endocytosis and recycling of immune complexes by follicular dendritic cells enhances B cell antigen binding and activation". *Immunity*. DOI: [10.1016/j.immuni.2013.02.023](https://doi.org/10.1016/j.immuni.2013.02.023)
- Doan TA et al. (2022). "Trafficking and retention of protein antigens across systems and immune cell types". *Cellular and Molecular Life Sciences*. DOI: [10.1007/s00018-022-04303-4](https://doi.org/10.1007/s00018-022-04303-4)
- Dernstedt A et al. (2020). "Regulation of Decay Accelerating Factor Primes Human Germinal Center B Cells for Phagocytosis". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2020.599647](https://doi.org/10.3389/fimmu.2020.599647)
- Wang X et al. (2011). "Follicular dendritic cells help establish follicle identity and promote B cell retention in germinal centers". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.20111449](https://doi.org/10.1084/jem.20111449)

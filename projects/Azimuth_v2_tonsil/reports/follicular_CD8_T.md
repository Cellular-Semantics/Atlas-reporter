# Follicular CD8-positive, alpha-beta T cells in the human tonsil

Atlas: Single-cell analysis of human B cell maturation (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (B-cell follicle / germinal center)
Cell Ontology: [CD8-positive, alpha-beta T cell](http://purl.obolibrary.org/obo/CL_0000625) (CL:0000625, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3674

## Summary

The Azimuth human_tonsil_v2 fine label "CD8-positive, alpha-beta follicular T cell" denotes a CD8+ alpha-beta T cell that expresses the follicle-homing chemokine receptor CXCR5 and localises to the B-cell follicle and germinal center — a population referred to in the literature as the follicular CD8 T cell, CXCR5+ CD8 T cell, or follicular cytotoxic CD8 T cell (Tfc). Unlike the bulk of CD8 T cells, which reside in the T-cell zone, this subset gains CXCR5 and thereby enters the CXCL13-rich B-cell follicle (Schaerli et al., 2000; Perdomo-Celis et al., 2017). In human tonsil it has been directly identified within germinal centers by flow cytometry and imaging (Chu et al., 2015; Shen et al., 2018). Functionally it combines cytolytic potential (perforin, granzyme B) with the capacity to regulate the germinal-center reaction, including suppression of T follicular helper (Tfh)-driven B cell differentiation (Chu et al., 2019; Petrovas et al., 2017).

> "Yet, a distinct CXCR5+ CD8 T cell subset identified within the B cell follicle and germinal center in situations of chronic antigen has recently been defined."
>
> — Valentine & Hoyer (2019)

## Markers

The defining marker of this subset is **CXCR5** (the B-cell-follicle homing receptor) co-expressed on a **CD8+** alpha-beta T cell background. In the primary human studies these are measured as **cell-surface proteins by flow cytometry and immunostaining** — CXCR5, CD8, CD45RA, CD3, CD4(negative). The Azimuth atlas label instead derives from **single-cell transcriptomes**, so the atlas assignment reflects transcript-level surrogates of the same surface phenotype; CXCR5 and CD8 (CD8A/CD8B) transcript detection underpins the atlas annotation, whereas the classical subset definition below is protein-based.

- **CXCR5 (protein / surface)** — the follicle-homing receptor whose expression permits entry into the B-cell zone. Its ligand is CXCL13 (BCA-1):

  > "Memory but not naive T cells from tonsils are CXCR5+ and migrate in response to the B cell–attracting chemokine 1 (BCA-1), which is selectively expressed by reticular cells and blood vessels within B cell follicles."
  >
  > — Schaerli et al. (2000)

  > "Importantly, these cells express high levels of the C-X-C chemokine receptor type 5 (CXCR5), critical for entering the B cell zones in secondary lymphoid organs (13), and do not express the C-C chemokine receptor type 7 (CCR7), which directs them to the T cell zones (14)."
  >
  > — Perdomo-Celis et al. (2017)

- **CCR7 (protein, negative)** — loss of CCR7 releases the cell from the T-cell zone, complementing CXCR5-driven follicular homing (Perdomo-Celis et al., 2017).

- **Perforin and granzyme B (protein)** — cytolytic effector molecules carried by follicular CD8 T cells despite reduced cytokine polyfunctionality:

  > "Follicular CD8 (fCD8) T cells, despite compromised cytokine polyfunctionality, showed good cytolytic potential characterized by high ex vivo expression of granzyme B and perforin."
  >
  > — Petrovas et al. (2017)

- **Transcriptomic signature** — RNA-seq (transcript level) resolves this population as distinct from CXCR5- CD8 T cells:

  > "Furthermore, RNA-Seq-based transcriptional profiling revealed 77 differentially expressed genes unique to CXCR5+CD8+ T cells."
  >
  > — Chu et al. (2019)

## Location

This subset is defined by its position inside the B-cell follicle and germinal center of secondary lymphoid organs, including the palatine tonsil that is the atlas tissue. It was first characterised in human tonsil follicles and has been repeatedly imaged in tonsillar germinal centers.

> "Quigley et al. first characterized a population of CD8 + T cells infiltrating human tonsil follicles and provided the insights into the phenotype and function of follicular CD8 + T cells (5)."
>
> — Perdomo-Celis et al. (2017)

> "We found that CXCR5+CD8+ T cells were present in high numbers and localized to GCs and T cell zones in the tonsillar tissues and FL, but present in low numbers in the peripheral blood."
>
> — Chu et al. (2015)

The germinal-center localisation in human tonsil and lymph node is further supported by Shen et al. (2018):

> "A Subset of CXCR5+CD8+ T Cells in the Germinal Centers From Human Tonsils and Lymph Nodes Help B Cells Produce Immunoglobulins"
>
> — Shen et al. (2018)

Follicular infiltration by CD8 T cells has also been documented directly in human lymph nodes and tonsils:

> "Petrovas et al. examined human lymph nodes and tonsils and somewhat surprisingly found that CD8 T cells did infiltrate follicles in HIV-infected individuals."
>
> — Petrovas et al. (2017)

## Function

Follicular CD8 T cells are functionally bimodal, combining germinal-center immune surveillance with regulation of the humoral response.

### Cytolytic surveillance of the germinal center

Within germinal centers these cells retain cytotoxic effector capacity and are positioned to survey follicle-resident targets such as infected or malignant B cells and Tfh cells:

> "Follicular CD8+ T cells (fCD8) mediate surveillance in lymph node (LN) germinal centers against lymphotropic infections and cancers, but the precise mechanisms by which these cells mediate immune control remain incompletely resolved."
>
> — Collins et al. (2023)

> "In HIV controllers, the cytotoxic effectors perforin and granzyme B were elevated among virus-specific CXCR5+ fCD8s proximate to foci of HIV RNA within germinal centers."
>
> — Collins et al. (2023)

### Regulation of the germinal-center / Tfh–B cell axis

Beyond killing, tonsillar CXCR5+CD8+ T cells modulate the germinal-center reaction by dampening Tfh-driven B cell maturation:

> "These experiments indicated that CXCR5+CD8+ T cells suppressed Tfh function, as demonstrated by reduced differentiation of naive and/or memory B cells into plasmablasts cells (CD19intCD38+)."
>
> — Chu et al. (2015)

> "In summary, our study identified CXCR5+CD8+ T cells as a distinct T cell subset with ability to suppress TFH-mediated B cell differentiation, exert strong antitumor activity, and confer favorable prognosis in follicular lymphoma patients."
>
> — Chu et al. (2019)

This positions the subset alongside CD4 Tfh cells as a follicle-resident regulator of humoral immunity:

> "CD8 T cell localization to the B cell follicle suggests a functional profile similar to CD4 T follicular helper cells that are licensed to promote B cell responses."
>
> — Valentine & Hoyer (2019)

The subset also secretes effector cytokines more strongly than its extrafollicular counterpart, and in disease contexts contributes to viral control:

> "Further analysis using intracellular cytokine staining showed that CXCR5+CD8+ T cells produced higher levels of IFN-γ and TNF-α compared to CXCR5-CD8+ subset."
>
> — Chu et al. (2015)

> "CXCR5+ CD8 T cells control viral load during infection, and also promote antibody-mediated autoimmune disease progression."
>
> — Valentine & Hoyer (2019)

## Structure / Morphology

No dedicated ultrastructural or morphological description of this subset was found in the traversed literature beyond its immunophenotype and anatomical positioning. Migratory behaviour toward the follicle is chemokine-driven: purified human CXCR5+CD8+ T cells migrate to the CXCR5 ligand CXCL13, consistent with their follicular localisation.

> "In agreement with the expression of CXCR5, purified human CXCR5 + CD8 + T cells migrate in response to its ligand, the C-X-C motif ligand 13 (CXCL13) chemokine."
>
> — Perdomo-Celis et al. (2017)

## Cell Ontology note

The curated Azimuth-to-CL map assigned parent CL:0000895 (a CD4-naive term), which is incorrect for a CD8+ population. The correct parent is **CL:0000625 (CD8-positive, alpha-beta T cell)**. The follicular/CXCR5+ specialisation described above is not captured by an existing exact CL term; a new-term request downstream will formalise this correction.

## References
- Massoni-Badosa R et al. (2024). "An atlas of cells in the human tonsil". *Immunity*. DOI: [10.1016/j.immuni.2024.01.006](https://doi.org/10.1016/j.immuni.2024.01.006) — Azimuth human_tonsil_v2 reference atlas

- King HW et al. (2021). "Single-cell analysis of human B cell maturation predicts how antibody class switching shapes selection dynamics". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Valentine KM & Hoyer K (2019). "CXCR5+ CD8 T Cells: Protective or Pathogenic?". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2019.01322](https://doi.org/10.3389/fimmu.2019.01322)
- Chu F & Neelapu S (2015). "CXCR5+CD8+ T cells are localized in B cell follicles and germinal centers and exhibit regulatory and anti-tumor function". *Journal for Immunotherapy of Cancer*. DOI: [10.1186/2051-1426-3-S2-P321](https://doi.org/10.1186/2051-1426-3-S2-P321)
- Shen J et al. (2018). "A Subset of CXCR5+CD8+ T Cells in the Germinal Centers From Human Tonsils and Lymph Nodes Help B Cells Produce Immunoglobulins". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2018.02287](https://doi.org/10.3389/fimmu.2018.02287)
- Perdomo-Celis F et al. (2017). "Follicular CD8+ T Cells: Origin, Function and Importance during HIV Infection". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2017.01241](https://doi.org/10.3389/fimmu.2017.01241)
- Petrovas C et al. (2017). "Follicular CD8 T cells accumulate in HIV infection and can kill infected cells in vitro via bispecific antibodies". *Science Translational Medicine*. DOI: [10.1126/scitranslmed.aag2285](https://doi.org/10.1126/scitranslmed.aag2285)
- Chu F et al. (2019). "CXCR5+CD8+ T cells are a distinct functional subset with antitumor activity". *Leukemia*. DOI: [10.1038/s41375-019-0464-2](https://doi.org/10.1038/s41375-019-0464-2)
- Collins D et al. (2023). "Cytolytic CD8+ T cells infiltrate germinal centers to limit ongoing HIV replication in spontaneous controller lymph nodes". *Science Immunology*. DOI: [10.1126/sciimmunol.ade5872](https://doi.org/10.1126/sciimmunol.ade5872)
- Schaerli P et al. (2000). "Cxc Chemokine Receptor 5 Expression Defines Follicular Homing T Cells with B Cell Helper Function". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.192.11.1553](https://doi.org/10.1084/jem.192.11.1553)

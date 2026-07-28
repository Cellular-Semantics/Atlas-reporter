# Non-Vδ2 (TRDV2-negative) γδ T Cells in the Human Palatine Tonsil

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil
Cell Ontology: [V1delta gamma-delta T cell](http://purl.obolibrary.org/obo/CL_0020001) (CL:0020001, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3678

## Summary

The Azimuth `human_tonsil_v2` fine label "non-TRDV2+" identifies a gamma-delta (γδ) T cell defined by the **absence of TRDV2**, the transcript encoding the Vδ2 TCR chain. It is therefore a non-Vδ2 γδ T cell — the transcriptional counterpart of the protein-defined subset that, unlike the blood-dominant innate-like Vγ9Vδ2 population, lacks the Vδ2 element and is dominated by Vδ1 (TRDV1) cells (Kabelitz et al., 2013; Pérez et al., 2020; Fisher et al., 2026). Non-Vδ2 γδ T cells are rare in peripheral blood but enriched in mucosal, epithelial and organized lymphoid tissues, including the tonsil (Kabelitz et al., 2013; Groh et al., 1989). Rather than a positive lineage marker, the defining feature of this annotation is a **negative marker** — loss of the Vδ2 (TRDV2) chain — with Vδ1 (TRDV1) as its usual positive correlate. Functionally, these cells recognise stress-associated and non-classical MHC ligands and can adopt tissue-resident phenotypes (Khairallah et al., 2018; Negash et al., 2018; Wu et al., 2022).

## Markers

**A note on how this cell type is defined.** The atlas label is transcript-based: it flags cells that do *not* express TRDV2 (Vδ2). This is fundamentally a marker of **absence**. In most of the cited literature the same subset is instead defined at the protein / surface level, using anti-Vδ2 and anti-Vδ1 antibodies against the TCR δ chains, so protein-level "non-Vδ2 / Vδ1" and transcript-level "TRDV2-negative / TRDV1-positive" describe the same biological population by different assays.

The strongest bridge between the transcript and protein levels comes from a study that measured both TRDV1/TRDV2 mRNA and Vδ1/Vδ2 protein in the same human tissue (Wu et al., 2022):

> "Furthermore, expression of TRDV1 (Vδ1 T cells) was higher than TRDV2 (Vδ2 T cells) within lung tissue (Extended Data Fig. 2b,c), consistent with our own data."
>
> — Wu et al. (2022)

- **TRDV2 (Vδ2) — negative (defining marker).** The annotation is TRDV2-low/absent. Cells lacking Vδ2 are collectively grouped as "non-Vδ2" γδ T cells, a grouping with broadly shared biology (Fisher et al., 2026):

  > "From a functional perspective, separation of human γδ T cells into Vδ2 and non-Vδ2 subsets allows grouping of cells with broadly similar biological properties, although the differences between Vδ1 + and Vδ3 + cells should not be ignored"
  >
  > — Fisher et al. (2026)

- **TRDV1 (Vδ1) — positive correlate.** The non-Vδ2 compartment is dominated by Vδ1, with a smaller contribution from Vδ3 (and rarer Vδ5) (Khairallah et al., 2018; Pérez et al., 2020):

  > "Non-Vδ2 γδ-TCR T cells consist of Vδ1 and Vδ3 γδ-TCR T cells, and are mostly tissue-resident T cells present in barrier epithelium, though some of these cells are also circulating in blood (127). Between these two subsets, Vδ1 are the most abundant."
  >
  > — Pérez et al. (2020)

  > "In contrast to Vγ9Vδ2 + T cells, the Vδ2 − γδ T cell subset is heterogenous (106) and preferentially resides in epithelial tissues such as the skin (118) and intestines (119) and appears to form resident populations in the liver (120) (Table 1). Vδ2 − γδ T cells mainly consist of Vδ1 + T cells, with fewer Vδ3 + and Vδ5 + T cells."
  >
  > — Khairallah et al. (2018)

- **TRDC (pan-γδ constant region).** Shared by all γδ T cells; it confirms γδ lineage but does *not* discriminate the non-Vδ2 subset. No subset-specific evidence from traversed literature is quoted for TRDC in the tonsil beyond its general use as a γδ marker.

## Location

### In the tonsil and organized lymphoid tissue

γδ T cells, of which the non-Vδ2 / Vδ1 subset is a major tissue component, are directly documented in the human tonsil (Groh et al., 1989):

> "Human TCR-gamma/delta+ cells populate both organized lymphoid tissues (thymus, tonsil, lymphnode, and spleen) as well as the gut- and skin-associated lymphoid systems at similar frequencies without obvious tropism for epithelial microenvironments."
>
> — Groh et al. (1989)

> "TCR-gamma/delta+ lymphocytes tend to be located within a given organ wherever TCR-alpha/beta+ lymphocytes are found."
>
> — Groh et al. (1989)

### Blood-vs-tissue partitioning

The defining biological contrast of the non-Vδ2 subset is its tissue tropism relative to the blood-dominant Vγ9Vδ2 population (Kabelitz et al., 2013; Fisher et al., 2026):

> "Human γδ T cells come in two major flavors: Vδ2 T cells account for the majority (50-95%) of circulating γδ T cells (in turn constituting only 5% of T cells in the peripheral blood), whereas γδ T cells expressing other Vδ elements ('non-Vδ2') are rare in the blood but appear at increased frequencies in mucosal tissues and in the skin."
>
> — Kabelitz et al. (2013)

> "Tissue residency, for example, is predominantly segregated by γδ T subset: Vγ9Vδ2 predominate in the blood, whereas non-Vδ2 γδT reside in barrier tissues from which most solid cancers arise"
>
> — Fisher et al. (2026)

γδ T cells overall are enriched in mucosal lymphoid tissue, and the Vδ1 subset in particular is concentrated at mucosal sites (Negash et al., 2018):

> "γδ T cells are minor subset, 1-5%, among circulating T cells, but are present in abundance within mucosal lymphoid tissue, therein comprising as much as 50% of T cells."
>
> — Negash et al. (2018)

## Function

### Recognition of stress-associated and non-classical MHC ligands

Unlike the phosphoantigen-reactive Vγ9Vδ2 subset, non-Vδ2 / Vδ1 cells are geared toward sensing cellular stress and lipid/metabolite antigens presented on non-classical MHC-like molecules (Kabelitz et al., 2013; Negash et al., 2018; Pérez et al., 2020):

> "While the T-cell receptor of Vδ2 T cells primarily recognizes tumor cell-derived pyrophosphates, non-Vδ2 γδ T cells preferentially recognize stress-associated surface antigens."
>
> — Kabelitz et al. (2013)

> "The Vδ1 + γδ T cells are mainly situated at mucosal sites and respond to non-classical major histocompatibility complex molecules such as MICA and/or MICB expressed on stressed cells [2]. The Vγ9Vδ2 T cell subset on the other hand are dominant in the peripheral circulation and respond to phospholigands (non-peptide molecules) derived from potentially diverse microbes, including mycobacteria [3]."
>
> — Negash et al. (2018)

> "Even though the antigens recognized by Vδ1 γδ-TCR T cells are mostly unknown, they were shown to recognize ligands presented by CD1a, CD1c, CD1d, and MR1 molecules as well as various stress-induced ligands (133,151,152)."
>
> — Pérez et al. (2020)

### Tissue immunosurveillance and antitumor activity

Both major γδ subsets exert antitumor effector functions, but through distinct homing and ligand programs (Kabelitz et al., 2013; Khairallah et al., 2018):

> "The Vδ2 and non-Vδ2 (mainly Vδ1) subsets of human γδ T cells have distinct homing patterns and recognize different types of ligands, yet both exert potent antitumor effects."
>
> — Kabelitz et al. (2013)

> "Vδ2 − γδ T cells can recognize stress antigens"
>
> — Khairallah et al. (2018)

## Structure / Morphology

The non-Vδ2 / Vδ1 subset frequently acquires a tissue-resident memory (T_RM) program in tissues, distinguishing it from its Vδ2 counterpart (Wu et al., 2022):

> "Similar to the CD8 + T cell compartment, we found that many, albeit not all, Vδ1 T cells in NT lung tissues displayed a CD103 + T RM phenotype, particularly in some patients"
>
> — Wu et al. (2022)

> "In contrast, most CD4 + and Vδ2 T cells in NT lung tissues were CD103 − as were their counterparts in peripheral blood (Fig. 2a,b)."
>
> — Wu et al. (2022)

No tonsil-specific ultrastructural or morphological description of this subset was found in the traversed literature.

## References

- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Kabelitz D et al. (2013). "Human Vδ2 versus non-Vδ2 γδ T cells in antitumor immunity". *Oncoimmunology*. DOI: [10.4161/onci.23304](https://doi.org/10.4161/onci.23304)
- Khairallah C et al. (2018). "Tissue Adaptations of Memory and Tissue-Resident Gamma Delta T Cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2018.02636](https://doi.org/10.3389/fimmu.2018.02636)
- Wu Y et al. (2022). "A local human Vδ1 T cell population is associated with survival in nonsmall-cell lung cancer". *Nature Cancer*. DOI: [10.1038/s43018-022-00376-z](https://doi.org/10.1038/s43018-022-00376-z)
- Groh V et al. (1989). "Human lymphocytes bearing T cell receptor gamma/delta are phenotypically diverse and evenly distributed throughout the lymphoid system". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.169.4.1277](https://doi.org/10.1084/jem.169.4.1277)
- Pérez C et al. (2020). "Off-the-Shelf Allogeneic T Cell Therapies for Cancer: Opportunities and Challenges Using Naturally Occurring 'Universal' Donor T Cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2020.583716](https://doi.org/10.3389/fimmu.2020.583716)
- Fisher J et al. (2026). "Harnessing the potential of γδ T cells through engineering and combination treatment for cancer therapies". *Nature Communications*. DOI: [10.1038/s41467-026-73451-z](https://doi.org/10.1038/s41467-026-73451-z)
- Negash M et al. (2018). "Phenotypic and functional heterogeneity of peripheral γδ T cells in pulmonary TB and HIV patients in Addis Ababa, Ethiopia". *BMC Infectious Diseases*. DOI: [10.1186/s12879-018-3361-9](https://doi.org/10.1186/s12879-018-3361-9)

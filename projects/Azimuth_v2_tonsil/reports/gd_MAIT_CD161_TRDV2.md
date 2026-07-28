# CD161+ TRDV2+ (Vδ2) Gamma-Delta T Cell ("MAIT/CD161+TRDV2+")

Atlas: An atlas of cells in the human tonsil (Massoni-Badosa et al., 2024) — Azimuth human_tonsil_v2 reference (DOI: 10.1016/j.immuni.2024.01.006). Upstream starting annotation: King et al. (2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil
Cell Ontology: [mature gamma-delta T cell](http://purl.obolibrary.org/obo/CL_0000800) (CL:0000800, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3677

## Summary

The Azimuth human_tonsil_v2 fine label "MAIT/CD161+TRDV2+" (King et al., 2021) denotes an unconventional, innate-like T cell defined at the transcript level by **TRDV2** (encoding the Vδ2 T-cell receptor delta chain) together with **KLRB1/CD161**. TRDV2 is a defining marker of the gamma-delta (γδ) T-cell lineage — specifically the Vδ2 subset, which most often pairs with TRGV9 to form the innate-like Vγ9Vδ2 receptor (Shepherd & McLaren, 2020). CD161 (KLRB1) is a C-type lectin-like receptor shared by NK cells and multiple unconventional T-cell subsets, including γδ T cells and MAIT cells (Rajoriya et al., 2014). In human palatine tonsil, γδ T cells are a rare population localised mainly to the crypt epithelium and interfollicular zone (Kawaguchi, 1993; Germain et al., 2015), and Vδ2+ γδ T cells display cytotoxic, pro-inflammatory effector functions in tonsil tissue (Press et al., 2025).

**Nomenclature caveat (important).** The label "MAIT/CD161+TRDV2+" conflates two distinct lineages. Canonical MAIT (mucosal-associated invariant T) cells are **alpha-beta** T cells that use the semi-invariant TRAV1-2 (Vα7.2) TCR and are restricted by the MHC class-Ib molecule MR1 (Gherardin et al., 2018; Koay et al., 2019). A cell expressing **TRDV2** carries a γδ TCR delta chain and therefore cannot be a genuine αβ MAIT cell. High CD161 is a widely used but non-specific MAIT surrogate that is shared across γδ, iNKT, and MAIT cells (van der Geest et al., 2018). This population is therefore best understood as a **CD161+ Vδ2+ γδ T cell with MAIT-like innate features**, with the correct Cell Ontology lineage being gamma-delta T cell (CL:0000798); the "MAIT" component of the atlas label reflects transcriptional overlap in CD161/KLRB1-associated innate-like programmes rather than true MAIT identity.

## Markers

**TRDV2 (Vδ2 TCR delta chain) — transcript-level lineage marker.** TRDV2 is the atlas's driving marker and unambiguously assigns the cell to the γδ lineage. Human γδ T cells are partitioned by δ-chain gene usage, and TRDV2 defines the Vδ2 subset (Shepherd & McLaren, 2020):

> "In humans, γδ T cells can be classified into two main populations, based on their expression of TCR δ-chains encoded by two TRDV genes-TRDV1 + γδ T cells (or Vδ1 + T cells) and TRDV2 + γδ T cells (or Vδ2 + T cells)."
>
> — Shepherd & McLaren (2020)

Vδ2+ cells are the dominant circulating γδ subset (and almost invariably pair TRDV2 with TRGV9 to form the semi-invariant Vγ9Vδ2 receptor; Shepherd & McLaren, 2020), whereas Vδ1+ cells predominate at mucosal and epithelial sites:

> "Vδ1 + T cells are abundant in the skin, intestine, and uterus, whereas Vδ2 + T cells constitute the majority of peripheral blood γδ T cells [24,173,174]."
>
> — Shepherd & McLaren (2020)

**CD161 / KLRB1 — protein-and-transcript marker.** CD161 is the second defining marker in the atlas label. As a gene, KLRB1 is a transcript in single-cell data; in the flow-cytometry literature it is a surface protein. It is expressed across NK cells and both αβ and γδ T cells (Rajoriya et al., 2014):

> "CD161 [also known as killer lectin receptor subfamily B member 1 (KLRB1)] is a C-type lectin membrane glycoprotein that is expressed on the majority of NK cells, and approximately 24% of peripheral T-cells (65)."
>
> — Rajoriya et al. (2014)

> "It is composed of a disulfide-linked homodimer of 40 kDa subunits, and has been shown to be expressed on both αβ and γδ T-cells (66)."
>
> — Rajoriya et al. (2014)

On γδ T cells, CD161 (surface protein, measured by flow cytometry) marks a memory phenotype and is examined alongside CD27 and CD28 on the TRDV2+ subset (Mata Forsberg et al., 2021):

> "We therefore investigated whether SEinduced responses in TRDV2 + T cells associated with a particular phenotype. We specifically investigated the memory-associated markers CD27, CD28, and CD161, commonly associated with pro-inflammatory responses in memory T cells."
>
> — Mata Forsberg et al. (2021)

Because CD161 is a memory/innate marker shared across lineages rather than a MAIT-specific one, its presence together with TRDV2 does not indicate a MAIT cell (see Function and the caveat below).

## Location

### In palatine tonsil (atlas tissue)

γδ T cells are a rare population in human palatine tonsil, first quantified by Kawaguchi (1993), who found they make up ~1.5% of tonsillar T cells:

> "Flowcytometric analysis showed that 1.56% of T cells in palatine tonsils obtained from patients with recurrent tonsillitis (n=17) expressed the γδT cell receptor."
>
> — Kawaguchi (1993)

Within the tonsil, γδ T cells are concentrated in the crypt epithelium, with progressively fewer in the surface epithelium and the interfollicular space:

> "It was demonstrated that T cells in the crypt epithelium contained more γδT cell receptor bearing cells than did T cells infiltrating the tonsillar epithelium on the free surface. T cells in the interfollicular space included even fewer γδT cells."
>
> — Kawaguchi (1993)

CD161-expressing T cells in tonsil — a compartment that includes small numbers of TCRγδ+ cells alongside CD161-high MAIT cells — localise mainly to the interfollicular zone surrounding germinal centers (Germain et al., 2015):

> "CD161 C cells were mostly found in the IFZ surrounding GC (Fig. 2A)."
>
> — Germain et al. (2015)

*(Note: the "C" in the Germain et al. quotes is an OCR rendering of a superscript "+".)*

## Function

### Effector / cytotoxic programme

Vδ2+ (TRDV2+) γδ T cells are innate-like effectors. In human tonsil and spleen organoids they expand in response to pathogen (malaria) challenge, unlike the Vδ1+ subset (Press et al., 2025):

> "In this study, we found that Vδ2 + γδ T cells increase in abundance in tonsil and spleen organoids in response to malaria parasites, similarly to what has been observed in blood in malaria-naïve individuals."
>
> — Press et al. (2025)

Their functional repertoire spans cytotoxicity, cytokine production, and help for adaptive immunity:

> "They can play diverse roles, including production of pro-inflammatory cytokines, cytotoxic killing, antigen presentation, promotion of dendritic cell maturation, B cell help, recruitment of other immune cells, and secretion of growth factors [29]."
>
> — Press et al. (2025)

In secondary lymphoid organs such as the tonsil, γδ T cells may also influence humoral responses:

> "γδ + T cells may also play a role in direct or indirect modulation of antibody production in secondary lymphoid organs [30][31][32][33][34])."
>
> — Press et al. (2025)

### MAIT-like features versus true MAIT identity

The atlas "MAIT" designation reflects the CD161/KLRB1-driven innate-like transcriptional programme this γδ subset shares with MAIT cells, not a shared lineage. CD161 is expressed by several innate-like T-cell types, and MAIT cells must be resolved by an additional, lineage-specific marker:

> "Previous studies have reported that gamma-delta T cells, invariant natural killer T (iNKT) cells, and MAIT cells may express CD161 (33,37,38)."
>
> — van der Geest et al. (2018)

> "To delineate MAIT cells, additional staining was performed for the TCR-Vα7.2 receptor (Figure 2E)."
>
> — van der Geest et al. (2018)

Canonical MAIT cells are defined by the TRAV1-2 alpha-beta TCR and MR1 restriction, with CD161 serving only as an imperfect surrogate (Gherardin et al., 2018):

> "MAIT cells exhibit a unique cell surface phenotype, including expression of high levels of the C-type lectin CD161, 3 the IL-18Ra chain CD218 4 as well as the ectopeptidase CD26."
>
> — Gherardin et al. (2018)

> "Taken together, while the CD161 HI TRAV1-2 + phenotype is a reasonably accurate indicator of CD8aa + and DN MAIT cells, for other MAIT cell populations (CD4 + , DP and CD8ab + ) this approach is not very reliable."
>
> — Gherardin et al. (2018)

MR1-restricted cells that lie outside the TRAV1-2 compartment but share high CD161 are described as "MAIT-like" rather than MAIT (Koay et al., 2019):

> "For TRAV1-2 − MR1-5-OP-RU tetramer + cells, two distinct populations emerged: some had high CD218a and CD161 expression, akin to MAIT cells (MAIT-like cells), and some had low expression of these markers (non-MAIT-like cells) (Fig. 6a, third panels)."
>
> — Koay et al. (2019)

Because the present population carries a γδ (TRDV2/Vδ2) TCR — not the αβ TRAV1-2 chain and not MR1 restriction — it is a MAIT-*like* γδ T cell, and its correct lineage is gamma-delta T cell (CL:0000798).

## Structure / Morphology

No evidence found in traversed literature.

## References

- Shepherd F, McLaren J (2020). "T Cell Immunity to Bacterial Pathogens: Mechanisms of Immune Control and Bacterial Evasion". *International Journal of Molecular Sciences*. DOI: [10.3390/ijms21176144](https://doi.org/10.3390/ijms21176144)
- Rajoriya N et al. (2014). "Gamma Delta T-lymphocytes in Hepatitis C and Chronic Liver Disease". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2014.00400](https://doi.org/10.3389/fimmu.2014.00400)
- Mata Forsberg M et al. (2021). "Activation of human γδ T cells and NK cells by Staphylococcal enterotoxins requires both monocytes and conventional T cells". *Journal of Leukocyte Biology*. DOI: [10.1002/JLB.3A1020-630RR](https://doi.org/10.1002/JLB.3A1020-630RR)
- Germain C et al. (2015). "Lectin-like transcript 1 is a marker of germinal center-derived B-cell non-Hodgkin's lymphomas dampening natural killer cell functions". *OncoImmunology*. DOI: [10.1080/2162402X.2015.1026503](https://doi.org/10.1080/2162402X.2015.1026503)
- Kawaguchi T (1993). "γδT CELLS IN THE PALATINE TONSIL". *Nippon Jibiinkoka Gakkai Kaiho*. DOI: [10.3950/JIBIINKOKA.96.810](https://doi.org/10.3950/JIBIINKOKA.96.810)
- Press K et al. (2025). "Cytotoxic Vδ2+ T cell subsets expand in response to malaria in human tonsil and spleen organoids". *PLOS Pathogens*. DOI: [10.1101/2025.09.24.678447](https://doi.org/10.1101/2025.09.24.678447)
- van der Geest KV et al. (2018). "Impact of Aging on the Frequency, Phenotype, and Function of CD161-Expressing T Cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2018.00752](https://doi.org/10.3389/fimmu.2018.00752)
- Gherardin N et al. (2018). "Human blood MAIT cell subsets defined using MR1 tetramers". *Immunology and Cell Biology*. DOI: [10.1111/imcb.12021](https://doi.org/10.1111/imcb.12021)
- Koay H et al. (2019). "Diverse MR1-restricted T cells in mice and humans". *Nature Communications*. DOI: [10.1038/s41467-019-10198-w](https://doi.org/10.1038/s41467-019-10198-w)
- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)

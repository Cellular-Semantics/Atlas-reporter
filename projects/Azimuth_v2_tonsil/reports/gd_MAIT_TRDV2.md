# TRDV2+ (Vδ2) Gamma-Delta T Cell with MAIT-like Features ("MAIT/TRDV2+")

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil
Cell Ontology: [gamma-delta T cell](http://purl.obolibrary.org/obo/CL_0000798) (CL:0000798, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3676

## Summary

The Azimuth `human_tonsil_v2` fine annotation "MAIT/TRDV2+" (fine, order 143;
related labels "MAIT/TRDV2+ gdT" and "MAIT/CD161+TRDV2+") denotes an
innate-like T-cell state defined by expression of *TRDV2*, the gene segment
encoding the Vδ2 T-cell receptor (TCR) chain. Cells expressing *TRDV2* (Vδ2)
almost always pair it with Vγ9 (*TRGV9*) to form Vγ9Vδ2 T cells, the dominant
gamma-delta subset of adult human blood (Ma et al., 2021; Herrmann et al.,
2020; Li et al., 2026). These cells are activated by non-peptidic
phosphoantigens through the butyrophilin BTN3A1/BTN2A1 machinery rather than
by peptide-MHC, and they display a cytotoxic, cytokine-secreting effector
program (Herrmann et al., 2020; Oh et al., 2026; Li et al., 2026).
Gamma-delta T cells including canonical Vγ9Vδ2 clonotypes are present and
enriched in human tonsil and respond to local antigen challenge (Guo et al.,
2024). **Naming caveat:** the atlas label conflates two lineages — canonical
MAIT cells are alpha-beta, TRAV1-2/MR1-restricted innate T cells, whereas
*TRDV2* marks gamma-delta cells; this state is best represented as a Vδ2
gamma-delta T cell carrying MAIT-like innate markers (e.g. CD161/KLRB1), not
as a bona fide MR1-restricted MAIT cell.

## Markers

The defining marker of this cluster is **TRDV2** (encoding the Vδ2 TCR delta
chain), essentially always co-expressed with **TRGV9** (Vγ9). This TCR pairing
is the molecular definition of the Vγ9Vδ2 subset (Ma et al., 2021):

> "A major γδ T cell population in human adult blood are the Vγ9Vδ2 T cells that are defined by the expression of a TCR containing the γ chain variable region 9 (Vγ9, TRGV9) and the δ chain V region 2 (Vδ2, TRDV2)."
>
> — Ma et al. (2021)

At the transcript level, *TRDV2* and *TRGV9* are V-gene-segment identities
detected as RNA in single-cell data; the corresponding Vγ9 and Vδ2 TCR chains
are the protein products detected by antibody/flow cytometry. Notably, the Vγ9
side of the repertoire is genetically constrained while the *TRDV2*-containing
delta repertoire is diverse (Oh et al., 2026):

> "Previous TCR repertoire analyses have shown that the Vγ9 TCR gamma (TRG) repertoire is relatively constrained, whereas the Vδ2 TCR delta repertoire is highly diverse."
>
> — Oh et al. (2026)

Consistent with the "MAIT-like" portion of the label, these cells co-express
innate-lymphocyte markers such as CD161 (KLRB1), reflected in the sibling atlas
label "MAIT/CD161+TRDV2+" (King et al., 2021). Beyond the TCR, the Vδ2 subset
carries a cytotoxic effector marker set (perforin, granzymes, FasL) and rapidly
produces IFN-γ and TNF-α on activation (Li et al., 2026; see Function).

## Location

This state is annotated in **adult palatine tonsil** by the King et al. (2021)
atlas. Independent work confirms that gamma-delta T cells — including canonical
Vγ9Vδ2 clonotypes — are resident in human tonsil and are actually enriched
there relative to matched blood (Guo et al., 2024):

> "Cy3 + HA + γδ T cells were present with variable frequencies in the tonsils (SI Appendix, Fig. S6B) but showed higher frequencies among tonsillar γδ T cells compared to paired peripheral blood γδ T cells (Fig. 4E)."
>
> — Guo et al. (2024)

The canonical Vγ9Vδ2 TCR configuration is represented within this tonsillar
gamma-delta compartment (Guo et al., 2024):

> "They also contained Vγ9Vδ2 TCRs with the canonical CDR3γ sequence CALWEVQELGKKIKV, generated from the Vγ9 and JγP gene segments without N-nucleotide addition, or with limited VJ junctional variations."
>
> — Guo et al. (2024)

More broadly, Vγ9Vδ2 cells are the predominant circulating gamma-delta
population, so the tonsillar pool represents a tissue-associated fraction of a
subset most abundant in blood (Li et al., 2026):

> "The Vδ2 subset, pairing predominantly with the Vγ9 chain to form Vγ9Vδ2 T cells, constitutes the most abundant circulating γδ T cell population in adult peripheral blood"
>
> — Li et al. (2026)

## Function

### Phosphoantigen-driven activation via butyrophilins

Unlike alpha-beta T cells (and unlike MR1-restricted MAIT cells), Vγ9Vδ2 cells
are activated in a TCR-dependent but MHC-independent manner by small
phosphorylated metabolites ("phosphoantigens") presented through the
butyrophilin complex (Ma et al., 2021; Herrmann et al., 2020; Oh et al.,
2026):

> "They express a potent cytotoxic effector phenotype and are activated and expanded in a TCR-dependent manner by microbe-and host-derived phosphorylated prenyl metabolites (phosphorylated Ags, or phosphoantigens), derived from the isoprenoid metabolic pathway"
>
> — Ma et al. (2021)

> "These TCRs respond to phosphoantigens (PAg) such as (E)-4-hydroxy-3-methyl-but-2-enyl pyrophosphate (HMBPP), which is found in many pathogens, and isopentenyl pyrophosphate (IPP), which accumulates in certain tumors or cells treated with aminobisphosphonates such as zoledronate."
>
> — Herrmann et al. (2020)

The molecular sensing mechanism is butyrophilin-dependent (Oh et al., 2026):

> "Phosphoantigen sensing is mediated by the BTN3A1/BTN3A2/BTN2A1 complex: phosphoantigens bind to the intracellular B30.2 domain of BTN3A1, inducing conformational changes that are transmitted to the extracellular domains, where engagement with the Vγ9Vδ2 TCR occurs."
>
> — Oh et al. (2026)

> "Human Vγ9Vδ2 γδ T cells, the predominant γδ T cells in peripheral blood, are innate-like lymphocytes that recognize non-peptidic phosphorylated metabolites ("phosphoantigens") through a butyrophilin-dependent manner, positioning them as key mediators of tumor immunosurveillance"
>
> — Oh et al. (2026)

### Cytotoxicity and cytokine production

Once activated, the Vδ2 subset mounts a rapid effector response combining
direct killing with pro-inflammatory cytokine secretion (Li et al., 2026):

> "Vγ9Vδ2 T cells exert direct cytotoxicity against target cells (e.g., tumor cells) via cytotoxic granule release (Perforin, Granzymes) or the Fas/Fas ligand (FasL) pathway."
>
> — Li et al. (2026)

> "Upon activation, they rapidly secrete key pro-inflammatory cytokines like Interferon-gamma (IFN-γ) and Tumor Necrosis Factor-alpha (TNF-α), bolstering host defense."
>
> — Li et al. (2026)

### Response to antigen challenge in tonsil

In tonsil organoid cultures, gamma-delta T cells expand upon vaccine
stimulation, demonstrating functional antigen responsiveness in this tissue
(Guo et al., 2024):

> "Stimulating tonsil organoid cultures with live-attenuated influenza vaccine (LAIV) induced Cy3 + HA + γδ T cell expansion when compared with unstimulated cultures."
>
> — Guo et al. (2024)

### Relationship to MAIT cells (naming caveat)

The atlas label pairs "MAIT" with "TRDV2+", but these mark different lineages.
Vγ9Vδ2 selection on a monomorphic non-peptide ligand is conceptually analogous
to — but mechanistically distinct from — the selection of alpha-beta innate T
cells such as MAIT cells (Pauza et al., 2015):

> "While selection on a monomorphic presenting molecule may seem unusual, similar mechanisms shape the alpha beta T cell repertoire including the extreme examples of NKT or mucosal-associated invariant T cells (MAIT)"
>
> — Pauza et al. (2015)

Vγ9Vδ2 cells are a numerically minor thymic output that is amplified
extrathymically (Pauza et al., 2015):

> "Lymphocytes expressing a T cell receptor (TCR) composed of Vgamma9 and Vdelta2 chains represent a minor fraction of human thymocytes."
>
> — Pauza et al. (2015)

The practical implication for downstream ontology mapping is that this state
should be classified as a gamma-delta T cell (CL:0000798), with the "MAIT"
component of the label understood as MAIT-*like* innate marker expression
(e.g. CD161) rather than true MR1-restricted MAIT identity.

## Structure / Morphology

No evidence found in traversed literature.

## References

- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Ma L et al. (2021). "Effector Vγ9Vδ2 T cell response to congenital Toxoplasma gondii infection". *JCI Insight*. DOI: [10.1172/jci.insight.138066](https://doi.org/10.1172/jci.insight.138066)
- Herrmann T et al. (2020). "An Update on the Molecular Basis of Phosphoantigen Recognition by Vγ9Vδ2 T Cells". *Cells*. DOI: [10.3390/cells9061433](https://doi.org/10.3390/cells9061433)
- Oh WJ et al. (2026). "Selective Enrichment of Non-Canonical Vγ9-Jγ2 TRG Clonotypes in Clear Cell Renal Cell Carcinoma With Shorter CDR3 Loops". *Immune Network*. DOI: [10.4110/in.2026.26.e25](https://doi.org/10.4110/in.2026.26.e25)
- Li H et al. (2026). "Impaired function of Vγ9Vδ2 T cells in frail elderly". *Immunity & Ageing*. DOI: [10.1186/s12979-026-00558-8](https://doi.org/10.1186/s12979-026-00558-8)
- Guo J et al. (2024). "γδ T cell antigen receptor polyspecificity enables T cell responses to a broad range of immune challenges". *Proceedings of the National Academy of Sciences*. DOI: [10.1073/pnas.2315592121](https://doi.org/10.1073/pnas.2315592121)
- Pauza CD, Cairo C (2015). "Evolution and Function of the TCR Vgamma9 Chain Repertoire: It's Good to be Public". *Cellular Immunology*. DOI: [10.1016/j.cellimm.2015.02.010](https://doi.org/10.1016/j.cellimm.2015.02.010)

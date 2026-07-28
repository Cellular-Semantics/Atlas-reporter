# Central-Memory-Phenotype Precursor T Follicular Helper (pre-Tfh) Cell in Human Tonsil

Atlas: An atlas of cells in the human tonsil (Massoni-Badosa et al., 2024) — Azimuth human_tonsil_v2 reference (DOI: 10.1016/j.immuni.2024.01.006). Upstream starting annotation: King et al. (2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (T:B border / B-cell follicle)
Cell Ontology: [central memory CD4-positive, alpha-beta T cell](http://purl.obolibrary.org/obo/CL_0000904) (CL:0000904, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3672

## Summary

This cell type — annotated in the Azimuth human tonsil v2 reference (King et al., 2021) as a "central memory CD4-positive, alpha-beta preT follicular helper cell" — corresponds to the well-described **precursor T follicular helper (pre-Tfh)** intermediate: a CD4+ alpha-beta T cell that has begun the Tfh program but has not completed germinal-center commitment. Tfh fate is primed at the T:B border of secondary lymphoid organs, where newly committed pre-Tfh cells upregulate the follicle-homing receptor CXCR5 while downregulating the T-zone receptor CCR7, positioning them to migrate into the B-cell follicle (Shen & Fu, 2025). The "central memory" qualifier reflects the fact that pre-Tfh (PD-1+CXCR5+) cells stand at a documented fate bifurcation, with one branch retaining CCR7/IL-7Rα and adopting a CXCR5+ memory CD4+ T-cell state rather than proceeding to the germinal-center Tfh (GC-Tfh) fate (Zhu et al., 2023). In human tonsil specifically, the great majority of CD4+ memory T cells are CXCR5+ and express activation markers, consistent with this being the resident compartment from which pre-Tfh cells arise (Schaerli et al., 2000). Key markers are CXCR5 (intermediate), CCR7 (retained), PD-1 and ICOS, together with the transcription-factor program (BCL6, ASCL2, c-Maf) that enforces commitment.

## Markers

The defining feature of the pre-Tfh state is intermediate CXCR5 expression combined with retained CCR7, distinguishing it from both naive T-zone cells and mature GC-Tfh. As Tfh precursors form, they begin expressing CXCR5:

> "it is still not fully understood how a subset of activated CD4+ T cells begin to express CXCR5 during the early stage of the response and, shortly after, how some CXCR5+ precursor Tfh (pre-Tfh) cells enter B cell follicles and differentiate further into germinal center Tfh (GC-Tfh) cells while others have a different fate"
>
> — Schroeder et al. (2021)

- **CXCR5** (protein/receptor and transcript) — the canonical follicular-homing chemokine receptor. In the human tonsil, CXCR5 is expressed at the cell surface by essentially all CD4+ memory T cells (Schaerli et al., 2000), and its transcriptional induction is a founding event of the Tfh program (Mastelic-Gavillet et al., 2019).
- **CCR7** (protein/receptor and transcript) — retained in the pre-Tfh/central-memory state and progressively downregulated on follicular commitment. Its retention is functionally significant:

> "CCR7 expression retains activated CD4 + T cells in T cell zone and thus inhibits their differentiation towards Tfh fate, despite co-expression of CXCR5"
>
> — Liu et al. (2025)

- **PD-1 and ICOS** (surface protein) — maturation markers that increase along the pre-Tfh → GC-Tfh axis; the full PD-1hi ICOShi phenotype is a hallmark of follicle-resident GC-Tfh rather than the precursor (Kerfoot et al., 2011). In the pre-Tfh fate-choice model, cells are staged as PD-1+CXCR5+ (Zhu et al., 2023).
- **Transcription-factor / program genes** (transcript) — CXCR5, IL-21, Bcl6, Ascl2 and c-Maf constitute the multi-signal pre-Tfh program:

> "T fh cells differentiation involves a multisignal process that includes expression of CXCR5, IL-21, Bcl6, TBK1, STAT4, Ascl2, and c-maf"
>
> — Mastelic-Gavillet et al. (2019)

ASCL2 links the transcriptional program to the receptor phenotype:

> "Ascl2 directly regulates the localization of T fh cells via CXCR5 expression and suppression of CCR7 and PSGL1"
>
> — Mastelic-Gavillet et al. (2019)

CD4 itself is a lineage coreceptor rather than a state-specific marker and is retained across the entire trajectory.

## Location

### T:B border and inter-follicular zone

The pre-Tfh cell is defined in part by where it is: its fate is primed at the boundary between the T-cell zone and the B-cell follicle.

> "Tfh cell fate is primed at the T-B border of secondary lymphoid organs."
>
> — Shen & Fu (2025)

Development initiates in the inter-follicular/T:B border region, where responding T cells first acquire Tfh markers before follicle entry:

> "T cells also acquired the Tfh cell markers CXCR5, PD-1 and GL7."
>
> — Kerfoot et al. (2011)

### Migration into the follicle

The switch in chemokine-receptor expression drives directed migration into the follicle:

> "Upon upregulating CXCR5 and downregulating the T-zone homing receptor CCR7, newly committed pre-Tfh cells migrate towards the CXCL13 chemokine gradient into the follicle and mature into GC-Tfh (14-16). The initial positioning of pre-Tfh within GC is regulated by a balance of CXCR5, CCR7, and EBI2 signaling (17)."
>
> — Shen & Fu (2025)

CXCR5 is what enables this positioning and follicle entry:

> "Expression of CXCR5, which facilitates positioning of pre-Tfh cells at T:B border and entry into follicle to appropriately interact with B cells, is essential for further GC-Tfh and Tfh memory cell differentiation"
>
> — Liu et al. (2025)

### Human tonsil context

In the adult palatine tonsil, the CXCR5+ CD4+ memory compartment that contains these precursors is abundant and shows a recently-entered, activated phenotype:

> "Practically all (Ͼ95%) CD4 ϩ memory T cells in tonsils are CXCR5 ϩ and the majority express activation markers (CD69, HLA-DR, ICOS) suggesting their engagement in B cell activation. Drastic reduction in cell surface CCR7 and CD62L indicates that the majority of local CXCR5 ϩ T cells have recently entered the tonsillar tissue"
>
> — Schaerli et al. (2000)

Donor-matched repertoire analysis further shows clonal continuity between tonsillar and circulating Tfh compartments, consistent with a shared precursor pool:

> "our analysis of donormatched tissues directly demonstrates that the same Tfh clones are present in both tonsil and the blood CXCR5 + PD-1 + cTfh compartment"
>
> — Brenna et al. (2019)

## Function

### Committing toward the Tfh program while retaining a memory fate option

Functionally, the pre-Tfh cell is a decision point. PD-1+CXCR5+ precursors either continue toward GC-Tfh or divert to a CXCR5+ memory CD4+ T-cell fate — the biological basis for the atlas "central memory ... preT follicular helper" label:

> "the sustained Tigit expression in PD-1+CXCR5+CD4+ T cells marks the precursor Tfh (pre-Tfh) to GC-Tfh transition, whereas Tigit–PD-1+CXCR5+CD4+ T cells upregulate IL-7Rα to become CXCR5+CD4+ T memory cells with or without CCR7"
>
> — Zhu et al. (2023)

> "our work identifies an important marker and regulatory mechanism of PD-1+CXCR5+CD4+ T cells during their developmental choice between memory T cell fate and GC-Tfh cell differentiation"
>
> — Zhu et al. (2023)

### B-cell help requires follicle entry and cognate interaction

The precursor's ultimate effector function — helping B cells in the germinal center — depends on completing the migration and on cognate B-cell contact, which stabilises the mature effector phenotype:

> "Ag-specific B cells are required for the maintenance of the PD-1hi ICOShi GL7hi Tfh cell phenotype within the follicle, but not for their initial differentiation in the IF zone."
>
> — Kerfoot et al. (2011)

### Central-memory-like resting state

The "central memory" component is supported by the observation that resting CXCR5+ CD4+ T cells lacking activation markers behave as memory Tfh, distinct from the activated tissue-resident population:

> "unlike the activated tonsillar CXCR5+ CD4 T cells that were CD69+HLA-DR+ICOS+, circulating CXCR5+ cells in human blood are CD69−HLA-DR− ICOS−, and hypothesized that these blood CXCR5+ cells represent memory Tfh cells"
>
> — Hale & Ahmed (2015)

## Structure / Morphology

No specific structural or morphological evidence for this cell type was found in the traversed literature beyond its lymphocyte identity and spatial positioning at the T:B border / follicle described in the Location section.

## References

- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Schroeder AR et al. (2021). "Stepwise Tfh cell differentiation revisited: new advances and long-standing questions". *Faculty Reviews*. DOI: [10.12703/r/10-3](https://doi.org/10.12703/r/10-3)
- Shen C, Fu Q (2025). "Follicular helper T cells (Tfh): heterogeneity in spatial distribution and phenotypic characteristics". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2025.1686687](https://doi.org/10.3389/fimmu.2025.1686687)
- Liu J et al. (2025). "Advances and challenges in identifying precursors of memory CD4+ T cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2025.1540045](https://doi.org/10.3389/fimmu.2025.1540045)
- Zhu F et al. (2023). "Spatiotemporal resolution of germinal center Tfh cell differentiation and divergence from central memory CD4+ T cell fate". *Nature Communications*. DOI: [10.1038/s41467-023-39299-3](https://doi.org/10.1038/s41467-023-39299-3)
- Mastelic-Gavillet B et al. (2019). "Neonatal T Follicular Helper Cells Are Lodged in a Pre-T Follicular Helper Stage Favoring Innate Over Adaptive Germinal Center Responses". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2019.01845](https://doi.org/10.3389/fimmu.2019.01845)
- Schaerli P et al. (2000). "Cxc Chemokine Receptor 5 Expression Defines Follicular Homing T Cells with B Cell Helper Function". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.192.11.1553](https://doi.org/10.1084/jem.192.11.1553)
- Hale JS, Ahmed R (2015). "Memory T Follicular Helper CD4 T Cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2015.00016](https://doi.org/10.3389/fimmu.2015.00016)
- Kerfoot SM et al. (2011). "Germinal center B cell and T follicular helper cell development initiates in the inter-follicular zone". *Immunity*. DOI: [10.1016/j.immuni.2011.03.024](https://doi.org/10.1016/j.immuni.2011.03.024)
- Brenna E et al. (2019). "CD4+ T follicular helper (Tfh) cells in human tonsil and blood are clonally convergent, but divergent from non-Tfh CD4+ cells". *bioRxiv*. DOI: [10.1101/743187](https://doi.org/10.1101/743187)

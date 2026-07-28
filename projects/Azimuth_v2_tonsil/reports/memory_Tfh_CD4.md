# Memory T Follicular Helper Cells (CD4+ alpha-beta) in the Human Tonsil

Atlas: An atlas of cells in the human tonsil (Massoni-Badosa et al., 2024) — Azimuth human_tonsil_v2 reference (DOI: 10.1016/j.immuni.2024.01.006). Upstream starting annotation: King et al. (2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (B-cell follicle)
Cell Ontology: [T follicular helper cell](http://purl.obolibrary.org/obo/CL_0002038) (CL:0002038, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3675

## Summary

This cell type corresponds to a memory-phenotype CD4+ alpha-beta T follicular helper (Tfh) cell resolved within the human palatine tonsil by the Azimuth `human_tonsil_v2` reference, which is built on the integrated single-cell atlas of King et al. (2021). T follicular helper cells are the CD4+ helper subset specialised to support B-cell responses in the germinal centre, and they are defined by expression of the follicle-homing chemokine receptor CXCR5 together with PD-1, ICOS and the lineage-defining transcription factor BCL6 (Hale & Ahmed, 2015; Heit et al., 2017). The "memory" qualifier denotes antigen-experienced (CD45RA-negative / CD45RO-positive) Tfh that persist after a germinal-centre response and retain the capacity to recall Tfh effector functions on antigen re-encounter (Hale & Ahmed, 2015; Asrir et al., 2017). In the tonsil these cells localise to B-cell follicles and provide help that drives immunoglobulin class-switching and production (Schaerli et al., 2000; Breitfeld et al., 2000). Note that in the King et al. atlas the marker evidence is transcriptomic (e.g. *CXCR5*, *BCL6*, *PDCD1* transcripts), whereas most defining literature markers below were established as surface proteins or transcription factors by flow cytometry.

## Markers

The canonical Tfh marker programme combines a follicle-homing chemokine receptor, co-stimulatory/co-inhibitory surface receptors, and a lineage transcription factor:

> "Tfh cells are characterized by their expression of the chemokine receptor CXCR5, expression of the transcriptional repressor Bcl6, and their capacity to migrate to the follicle and promote germinal center B cell responses."
>
> — Hale & Ahmed (2015)

- **CXCR5** — the B-cell-follicle-homing chemokine receptor and the single most reliable surface marker of the Tfh lineage. In human tonsil, CXCR5 marks the memory (not naive) CD4 T-cell compartment (Schaerli et al., 2000). *Protein/flow-cytometry level in the source literature; transcript-level (CXCR5) in the King et al. atlas.*
- **BCL6** — the lineage-defining transcriptional repressor of Tfh differentiation (Hale & Ahmed, 2015; Kim et al., 2018). *Transcription-factor level; transcript-level (BCL6) in the atlas.*
- **PD-1 (PDCD1)** — a co-inhibitory receptor highly expressed by tonsillar Tfh, alongside CXCR5 (Kim et al., 2018; Heit et al., 2017). *Protein/flow-cytometry level; transcript-level (PDCD1) in the atlas.*
- **ICOS** — a co-stimulatory receptor characterising activated follicular tonsillar Tfh (Schaerli et al., 2000; Heit et al., 2017). *Protein/flow-cytometry level; transcript-level (ICOS) in the atlas.*
- **CD4** — the alpha-beta T-cell lineage co-receptor defining this as a CD4+ helper cell rather than a Tfh-specific marker (Hale & Ahmed, 2015). *Protein/flow-cytometry level; transcript-level (CD4) in the atlas.*
- **IL-21** — the signature Tfh effector cytokine secreted to help B cells (Kim et al., 2018). *Protein/secretion level.*

The Tfh phenotype in human tonsil is confined to antigen-experienced memory cells:

> "Memory but not naive T cells from tonsils are CXCR5+ and migrate in response to the B cell–attracting chemokine 1 (BCA-1), which is selectively expressed by reticular cells and blood vessels within B cell follicles."
>
> — Schaerli et al. (2000)

## Location

### In the tonsil B-cell follicle

Human tonsillar Tfh are follicle-resident CD4 T cells. Their defining CXCR5 expression directs migration toward the follicular chemokine CXCL13/BCA-1 produced within B-cell follicles, and they downregulate the T-zone homing receptors CCR7 and CD62L (Schaerli et al., 2000). The extrafollicular/follicular distinction is explicit in the tonsil literature: classical Tfh reside within the B-cell follicle and germinal centre, in contrast to related extrafollicular helper cells (Kim et al., 2018).

> "These cells are similar to Tfh cells in terms of expression of the chemokine receptor CXCR5 and the inhibitory receptor PD-1, IL-21 secretion, and expression of the transcription factor BCL6; however, unlike Tfh cells that are located within the B cell follicle and germinal center, they resi"
>
> — Kim et al. (2018)

### Memory Tfh: local and circulating compartments

Beyond the tonsil follicle, memory Tfh are distributed between lymphoid-organ-resident (local) and blood-circulating compartments (Asrir et al., 2017).

> "Memory follicular helper T cells can be local in draining lymphoid organs and circulate in the blood, but the underlying mechanisms of this subdivision are unresolved."
>
> — Asrir et al. (2017)

In the matched human tonsil-and-blood analysis of Brenna et al. (2020), tonsillar Tfh were characterised within the CD4+ CD45RA-negative memory compartment, confirming the memory identity of this population:

> "We refer to all antigen-experienced (CD4 + CD45RA − ) cells as memory cells, although this definition encompasses central memory and effector memory/effector T cells, which we did not distinguish in this study."
>
> — Brenna et al. (2020)

## Function

### Help for B cells and immunoglobulin production

The core function of tonsillar CXCR5+ memory CD4 T cells is to provide help that drives B-cell immunoglobulin production. Breitfeld et al. (2000) showed that co-culture of tonsillar B cells with the CXCR5+ CD45RO+ (memory) CD4 fraction, but not the CXCR5-negative fraction, markedly increased IgA and IgG output:

> "B cells produced comparable low amounts of both IgA and IgG when cultured for 11 d without T cells or with the CXCR5"
>
> — Breitfeld et al. (2000)

This help underpins the germinal-centre reaction and the generation of long-lived humoral immunity (Hale & Ahmed, 2015).

> "T follicular helper (Tfh) cells are the subset of CD4 T helper cells that are required for generation and maintenance of germinal center reactions and the generation of long-lived humoral immunity."
>
> — Hale & Ahmed (2015)

### Memory persistence and reactivation

The distinguishing functional feature of memory Tfh is their persistence after a germinal-centre response and their ability to be re-mobilised on antigen re-encounter (Hale & Ahmed, 2015; Asrir et al., 2017).

> "The implication of these findings is that memory Tfh cells retain their capacity to recall their Tfh-specific effector functions upon reactivation to provide help for B cell responses and play an important role in prime and boost vaccination or during recall responses to infection."
>
> — Hale & Ahmed (2015)

Local and circulating memory Tfh subsets both re-provide B-cell help but with distinct effector outcomes:

> "Here we show that both memory follicular helper T subsets sustain B-cell responses after reactivation. Local cells promote more plasma cell differentiation, whereas circulating cells promote more secondary germinal centers."
>
> — Asrir et al. (2017)

## Structure / Morphology

No evidence found in traversed literature.

## References

- Breitfeld D et al. (2000). "Follicular B Helper T Cells Express Cxc Chemokine Receptor 5, Localize to B Cell Follicles, and Support Immunoglobulin Production". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.192.11.1545](https://doi.org/10.1084/jem.192.11.1545)
- Brenna E et al. (2020). "CD4+ T Follicular Helper Cells in Human Tonsils and Blood Are Clonally Convergent but Divergent from Non-Tfh CD4+ Cells". *Cell Reports*. DOI: [10.1016/j.celrep.2019.12.016](https://doi.org/10.1016/j.celrep.2019.12.016)
- Asrir A et al. (2017). "Interconnected subsets of memory follicular helper T cells have different effector functions". *Nature Communications*. DOI: [10.1038/s41467-017-00843-7](https://doi.org/10.1038/s41467-017-00843-7)
- Hale JS & Ahmed R (2015). "Memory T Follicular Helper CD4 T Cells". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2015.00016](https://doi.org/10.3389/fimmu.2015.00016)
- Heit A et al. (2017). "Vaccination establishes clonal relatives of germinal center T cells in the blood of humans". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.20161794](https://doi.org/10.1084/jem.20161794)
- Kim ST et al. (2018). "Human Extrafollicular CD4+ T Helper Cells Help Memory B Cells Produce Immunoglobulins". *Journal of Immunology*. DOI: [10.4049/jimmunol.1701217](https://doi.org/10.4049/jimmunol.1701217)
- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Schaerli P et al. (2000). "Cxc Chemokine Receptor 5 Expression Defines Follicular Homing T Cells with B Cell Helper Function". *The Journal of Experimental Medicine*. DOI: [10.1084/jem.192.11.1553](https://doi.org/10.1084/jem.192.11.1553)

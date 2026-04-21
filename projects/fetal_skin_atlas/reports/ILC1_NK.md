# ILC1/NK Hybrid Innate Lymphoid Cell (ILC1_NK) in Adult Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: adult
Source dataset: Reynolds et al. (2021), integrated into Gopee et al. (2024)
Cell Ontology: [group 1 innate lymphoid cell](http://purl.obolibrary.org/obo/CL_0001067) (CL:0001067, broad match — ILC1_NK is a hybrid population with overlapping ILC1 and NK cell features; no single CL term captures this intermediate state)

## Summary

ILC1_NK corresponds to the ILC1/Natural Killer (NK) cluster identified by Reynolds et al. (2021) in adult human skin. This cluster is explicitly annotated as a hybrid or transitional population, sharing transcriptional features of both ILC1 and NK cells. It is part of the four CD161(KLRB1)+CD3(CD3D/CD3G)- innate lymphocyte clusters identified in adult dermis. ILC1_NK expresses KLRB1 (CD161) and IL7R alongside cytotoxic NK markers (KLRD1/CD94, GNLY, PRF1, GZMB), reflecting the biological continuum between group 1 ILCs and NK cells. Reynolds et al. (2021) note that ILC1 and NK cells share overlapping features at the transcriptional level, and ILC1_NK represents the intermediate state capturing this continuum. Johnson and Lee (2025) confirm that tissue-resident NK cells in the dermis are phenotypically distinct from circulating NK cells, with adaptations that blur the boundary between NK cells and ILC1.

## Markers

> "ILC1/NK have
> overlapping features of ILC1 and NKs, as described"
>
> — Reynolds et al. (2021)

> "We identified 4 clusters of innate lymphocytes that were CD161(KLRB1)+
> CD3(CD3D/CD3G)-, consisting of ILC1/3, ILC2, ILC1/Natural Killer (NK) and NK
> (KLRD1+, GNLY+, PRF1+, GZMB+ and FCGR3A+) cells"
>
> — Reynolds et al. (2021)

Shared ILC markers:
- **KLRB1 (CD161)** — pan-innate lymphocyte marker; distinguishes ILCs and NK cells from T cells
- **IL7R (CD127)** — ILC marker; differentiates ILCs from canonical NK cells (which lack IL7R)

NK cytotoxic markers (partially expressed in ILC1_NK):
- **KLRD1 (CD94)** — NK-associated C-type lectin receptor
- **GNLY (granulysin)** — cytotoxic NK/ILC effector molecule
- **PRF1 (perforin)** — pore-forming cytotoxic effector
- **GZMB (granzyme B)** — serine protease cytotoxic effector

Johnson and Lee (2025) confirm the four-cluster ILC structure and the distinct tissue-resident NK phenotype in dermis:

> "scRNA-seq of lesional vs non-lesional skin identified four unique clusters of innate lymphocytes in skin that were CD161(KLRB1)+/CD3(CD3D/CD3G)neg. These subgroups included ILC1/3, ILC2, ILC1/NK cells, and NK (KLRD1+, GNLY+, PRF1+, GZMB+, and FCGR3A+) cells"
>
> — Johnson and Lee (2025)

> "Healthy human dermis contains NK cells that are CD56+ and uniformly CD16a neg CCR7 neg, in contrast to circulating NK cells"
>
> — Johnson and Lee (2025)

## Location

ILC1_NK cells are resident in the adult dermis. They are CD3-negative, distinguishing them from cytotoxic T cells with similar effector profiles. Their tissue-resident phenotype is consistent with the CD56+CD16a-CCR7- NK cell phenotype described in healthy human dermis — distinct from circulating NK cells and adapted for tissue residency.

## Function

### 1. Cytotoxicity against infected and transformed cells

The partial expression of NK cytotoxic machinery (GNLY, PRF1, GZMB, KLRD1) equips ILC1_NK cells to kill virally infected keratinocytes, transformed cells, and stressed cells within the dermis. This cytotoxic capability is intermediate between the full NK programme (FCGR3A+) and the ILC1 programme.

### 2. IFN-γ production

Consistent with group 1 ILC identity, ILC1_NK cells produce IFN-γ in response to cytokine stimulation (IL-12, IL-18), contributing to type 1 immune surveillance in the dermis.

### 3. Representation of the ILC1-NK continuum

Reynolds et al. (2021) explicitly acknowledge this population as reflecting the biological continuum between ILC1 and NK cells, consistent with the known developmental relationship between these lineages:

> "ILC1/NK have
> overlapping features of ILC1 and NKs, as described"
>
> — Reynolds et al. (2021)

This intermediate state captures the transcriptional plasticity at the ILC1-NK boundary and is consistent with tissue-adapted NK cells that downregulate canonical NK markers while retaining partial cytotoxic capacity.

## Disease relevance

ILC1_NK cells are part of the broader skin innate lymphoid compartment that is dysregulated in inflammatory skin disease. Johnson and Lee (2025) note that all three ILC subsets are present in healthy human skin and are differentially regulated in disease. The ILC1/NK hybrid population may contribute to disease-associated cytotoxicity and IFN-γ-driven inflammation, though its specific disease roles remain less characterised than ILC2 (atopic dermatitis) or ILC3 (psoriasis).

## References

- Reynolds G, Vegh P, Fletcher J et al. (2021). "Developmental cell programs are co-opted in inflammatory skin disease." *Science*. DOI: [10.1126/science.aba6500](https://doi.org/10.1126/science.aba6500)
- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Johnson RL and Lee SH (2025). "Natural killer cells in skin: a unique opportunity to better characterize the many facets of an overlooked secondary lymphoid organ." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2025.1509635](https://doi.org/10.3389/fimmu.2025.1509635)

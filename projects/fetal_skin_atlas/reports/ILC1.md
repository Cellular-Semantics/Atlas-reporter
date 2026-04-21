# Innate Lymphoid Cell 1 (ILC1) in Adult Human Skin

Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis (DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x))
Scope: adult
Source dataset: Reynolds et al. (2021), integrated into Gopee et al. (2024)
Cell Ontology: [ILC1, human](http://purl.obolibrary.org/obo/CL_0001077) (CL:0001077, broad match — ILC1 in Gopee 2024 corresponds to ILC1/3 in Reynolds 2021, reflecting ILC1-ILC3 plasticity)

## Summary

ILC1 in Gopee et al. (2024) corresponds to the ILC1/3 cluster annotated by Reynolds et al. (2021) in adult human skin. Reynolds et al. identify this population as part of four CD161(KLRB1)+CD3(CD3D/CD3G)- innate lymphocyte clusters, and explicitly annotate it as ILC1/3 to reflect documented plasticity between ILC1 and ILC3 subsets in adult human skin. The cluster expresses KLRB1 (CD161) and IL7R as shared ILC markers, and co-expresses the ILC3-associated transcription factor RORC alongside ILC1-associated features. Fetal skin ILCs (IL7R+RORC+KIT+) resemble adult skin ILC3, and the ILC1/3 cluster captures the biologically relevant continuum between these two group 1/group 3 innate lymphoid states in the dermis. ILC3 (including ILC1/3) increases in psoriasis lesional skin.

## Markers

> "We identified 4 clusters of innate lymphocytes that were CD161(KLRB1)+
> CD3(CD3D/CD3G)-, consisting of ILC1/3, ILC2, ILC1/Natural Killer (NK) and NK
> (KLRD1+, GNLY+, PRF1+, GZMB+ and FCGR3A+) cells"
>
> — Reynolds et al. (2021)

> "Plasticity within ILC1
> and ILC3 is also recognized, as reflected in our annotation of ILC1/3"
>
> — Reynolds et al. (2021)

Defining markers of ILC1/ILC1_3:
- **KLRB1 (CD161)** — pan-innate lymphocyte marker; used to distinguish ILCs from T cells (CD3-)
- **IL7R (CD127)** — IL-7 receptor; ILC marker distinguishing ILCs from NK cells
- **RORC** — RAR-related orphan receptor C; ILC3 master transcription factor
- **KIT (CD117)** — ILC3 surface marker; stem cell factor receptor

Johnson and Lee (2025) confirm the four-cluster ILC annotation from Reynolds et al. in adult skin, and note that ILC1 cells may continuously traffic via CCR7/CD62L-dependent migration:

> "scRNA-seq of lesional vs non-lesional skin identified four unique clusters of innate lymphocytes in skin that were CD161(KLRB1)+/CD3(CD3D/CD3G)neg. These subgroups included ILC1/3, ILC2, ILC1/NK cells, and NK (KLRD1+, GNLY+, PRF1+, GZMB+, and FCGR3A+) cells"
>
> — Johnson and Lee (2025)

## Location

ILC1/ILC1_3 cells are resident in the adult dermis. They are distinguished from T cells by CD3 negativity and from NK cells by IL7R expression. Reynolds et al. demonstrate that fetal skin ILCs resemble adult ILC3, establishing that this innate lymphoid compartment has deep developmental roots in skin:

> "Fetal skin ILCs (IL7R+, RORC+ and KIT+)
> resemble adult skin ILC3"
>
> — Reynolds et al. (2021)

ILC1 cells may also exhibit greater tissue trafficking than ILC2/ILC3, circulating between dermis and lymph nodes via CCR7/CD62L-dependent mechanisms (Johnson and Lee, 2025).

## Function

### 1. IFN-γ production and type 1 immune responses

ILC1 cells are the innate counterpart of Th1 cells. They produce IFN-γ in response to IL-12 and IL-18 from activated macrophages and DCs, contributing to anti-microbial and anti-tumour responses in the dermis.

### 2. ILC1-ILC3 plasticity

The ILC1/3 annotation explicitly captures the known plasticity between ILC1 and ILC3 subsets. ILC3 cells can downregulate RORC and upregulate T-bet to adopt ILC1-like phenotypes in response to inflammatory signals, and this transition is reversible. Reynolds et al. reflect this biological reality in the ILC1/3 cluster name:

> "Plasticity within ILC1
> and ILC3 is also recognized, as reflected in our annotation of ILC1/3"
>
> — Reynolds et al. (2021)

Villanova et al. (2014) provide early characterisation of ILCs in human skin, confirming their presence in the dermis:

> "Characterization of innate lymphoid cells (ILC) in human skin and blood demonstrates increase of NKp44+ ILC3 in psoriasis"
>
> — Villanova et al. (2014)

### 3. Tissue homeostasis and neuro-immune interactions

Dermal ILC1/ILC3 cells respond to signals from keratinocytes (IL-33, TSLP) and stromal cells, contributing to steady-state tissue homeostasis and barrier immunity.

## Disease relevance

ILC3 (and ILC1/3 plastic cells) are increased in psoriasis lesional skin. Johnson and Lee (2025) note that ILCs are differentially expressed in disease-specific states:

> "Some propose that ILC2 and ILC3 cells are predominantly tissue resident in healthy homeostatic states, whereas ILC1 cells continuously traffic between circulation and lymph nodes in a CD62L-and CCR7-dependent manner"
>
> — Johnson and Lee (2025)

Villanova et al. (2014) were among the first to document ILC3 expansion in psoriasis, and Reynolds et al. (2021) capture the ILC1/3 plasticity that underlies this disease-associated shift.

## References

- Reynolds G, Vegh P, Fletcher J et al. (2021). "Developmental cell programs are co-opted in inflammatory skin disease." *Science*. DOI: [10.1126/science.aba6500](https://doi.org/10.1126/science.aba6500)
- Gopee NH et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Johnson RL and Lee SH (2025). "Natural killer cells in skin: a unique opportunity to better characterize the many facets of an overlooked secondary lymphoid organ." *Frontiers in Immunology*. DOI: [10.3389/fimmu.2025.1509635](https://doi.org/10.3389/fimmu.2025.1509635)
- Villanova F et al. (2014). "Characterization of innate lymphoid cells (ILC) in human skin and blood demonstrates increase of NKp44+ ILC3 in psoriasis." *Journal of Investigative Dermatology*. DOI: [10.1038/jid.2013.477](https://doi.org/10.1038/jid.2013.477)

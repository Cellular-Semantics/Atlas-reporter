# RETINAL_GANGLION_CELL — Retinal ganglion cell

Cell Ontology: [retinal ganglion cell](http://purl.obolibrary.org/obo/CL_0000740) (CL:0000740, **exact match** — CL definition matches the HDCA POU4F1+/ISL1+/PAX6+/NEFL+ RGC cluster precisely.)

## Summary

Retinal ganglion cells (RGCs) are the projection neurons of the retina, sending axons via the optic nerve to the brain. HDCA's RGC cluster shows the canonical RGC signature: POU4F1 / BRN3A (in T1_RGC), ISL1, GAP43, SNCG, NEFL, NRN1, STMN2, PRPH and PAX6. The HDCA paper explicitly attributes RGC identity in its data to ATOH7 expression, citing Ghiasvand et al. (2011) as the canonical reference for ATOH7 as the RGC competence factor.

## HDCA atlas evidence

**Cell count:** 2,633 cells. HDCA classifies this cluster as `broad_celltype = AUDIOVISUAL_NEURONAL`, `systems = AUDIOVISUAL_SYSTEM`.

### HDCA paper text


HDCA's main retina paragraph explicitly attributes RGC identity to ATOH7:

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"
>
> — Webb et al. (2026), HDCA

HDCA cites Ghiasvand et al. (2011) — ref [71] — as the source paper for ATOH7's role:

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."
>
> — Ghiasvand et al. (2011)


## Markers (HDCA Supplementary Table 9 signature)

> "GAP43,PAX6,SNCG,NEFL,NRN1,STMN2,ISL1,INA,MAPT,PRPH,SNCA,NEFM,SNAP25,OLFM1,RTN1,CRABP1,SCG5,SYT4,TSPAN7,GNG3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **RTN1** | 36.2 | 5.86 | 9.6e-283 |
| **CALM2** | 35.0 | 3.31 | 3.1e-264 |
| **TUBB2B** | 34.7 | 4.42 | 1.4e-259 |
| **STMN2** | 34.7 | 5.75 | 1.4e-259 |
| **PCSK1N** | 34.6 | 5.18 | 1.5e-258 |
| **TUBB2A** | 32.6 | 4.15 | 4.0e-230 |
| **CCNI** | 31.5 | 2.53 | 1.7e-214 |
| **CRABP1** | 31.4 | 5.57 | 5.3e-213 |
| **TUBA1A** | 31.4 | 3.58 | 7.6e-213 |
| **SNCG** | 31.3 | 5.94 | 3.7e-212 |
| **NSG1** | 31.0 | 4.48 | 8.5e-208 |
| **MLLT11** | 30.8 | 3.93 | 6.2e-205 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Ghiasvand NM et al. (2011). "Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease" *Nat Neurosci 14*. DOI: [10.1038/nn.2776](https://doi.org/10.1038/nn.2776)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (AUDIOVISUAL_NEURONAL compartment, AUDIOVISUAL_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

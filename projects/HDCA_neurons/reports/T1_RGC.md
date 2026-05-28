# T1_RGC — T1 retinal ganglion cell (POU4F1+/CNTN2+ early-born RGC subtype)

Cell Ontology: [retinal ganglion cell](http://purl.obolibrary.org/obo/CL_0000740) (CL:0000740, **narrow match** — HDCA assigned CL:0002672 (retinal progenitor cell) — but T1_RGC is a POU4F1+/CNTN2+/PRPH+ early-born RGC subtype, NOT a progenitor. Correct parent term is CL:0000740 (retinal ganglion cell). NTR candi...)

## Summary

T1_RGC is HDCA's annotation for an early-born RGC subtype distinguished from the bulk RGC pool by stronger expression of POU4F1 (BRN3A), CNTN2 (contactin-2 — axon-guidance molecule essential for RGC axon fasciculation), GAP43 and PRPH. The signature (PAX6+, SIX3+, ISL1+, POU4F1+, CNTN2+) matches the canonical 'early-wave' RGC profile in the mouse retina, consistent with the ATOH7-driven first wave of retinal neurogenesis described in Ghiasvand et al. (HDCA ref 71).

## HDCA atlas evidence

**Cell count:** 651 cells. HDCA classifies this cluster as `broad_celltype = AUDIOVISUAL_NEURONAL`, `systems = AUDIOVISUAL_SYSTEM`.

### HDCA paper text


HDCA characterises ATOH7-driven early RGC neurogenesis:

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"
>
> — Webb et al. (2026), HDCA

Ghiasvand et al. 2011 (HDCA ref 71) — the reference for ATOH7-driven RGC competence:

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."
>
> — Ghiasvand et al. (2011)


## Markers (HDCA Supplementary Table 9 signature)

> "PAX6,SIX3,ISL1,GAP43,PRPH,MAB21L1,CNTN2,STMN2,CRABP1,SNCG,INA,RTN1,DCX,MIAT,ELAVL4,RORB,CHRNA3,GNG3,NEFM,SLC18A2"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **MLLT11** | 36.9 | 4.77 | 5.3e-294 |
| **GAP43** | 36.5 | 5.87 | 9.7e-288 |
| **STMN2** | 36.1 | 6.03 | 5.1e-282 |
| **TUBB2B** | 35.9 | 4.57 | 5.6e-279 |
| **CALM2** | 35.8 | 3.28 | 2.5e-277 |
| **CCNI** | 35.5 | 2.67 | 5.3e-273 |
| **CRABP1** | 35.2 | 6.22 | 8.5e-268 |
| **NSG1** | 33.6 | 4.66 | 1.6e-243 |
| **PCSK1N** | 33.5 | 4.73 | 2.0e-243 |
| **PRPH** | 33.2 | 7.11 | 8.0e-238 |
| **RTN4** | 33.1 | 2.72 | 1.7e-236 |
| **YBX1** | 33.0 | 2.06 | 1.1e-235 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Ghiasvand NM et al. (2011). "Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease" *Nat Neurosci 14*. DOI: [10.1038/nn.2776](https://doi.org/10.1038/nn.2776)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (AUDIOVISUAL_NEURONAL compartment, AUDIOVISUAL_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

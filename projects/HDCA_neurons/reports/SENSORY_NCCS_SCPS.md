# SENSORY_NCCS_SCPS — Sensory NCC/SCP (sensory-committed neural crest / Schwann-cell precursor state)

Cell Ontology: [Schwann cell precursor](http://purl.obolibrary.org/obo/CL_0002375) (CL:0002375, **broad match** — HDCA-assigned. The sensory-committed SCP state (PAX3+, SOX2+, GFRA3+) sits as a transcriptionally biased subset of SCP — no CL term distinguishes lineage-biased SCP subsets.)

## Summary

Sensory NCC/SCPs in HDCA are a SOX10+/SOX2+ neural-crest-like state biased toward the sensory lineage, characterised by co-expression of glial markers (PLP1, MPZ, ERBB3, SPP1) with lineage-priming markers (PAX3, TFAP2A, TFAP2B, EDNRB, GFRA3). In Soldatov et al.'s spatiotemporal model of murine NCC fate decisions — which the HDCA paper cites as its developmental framework — sensory specification is the earliest branch from multipotent neural crest.

## HDCA atlas evidence

**Cell count:** 11,683 cells. HDCA classifies this cluster as `broad_celltype = PNS_NCC`, `systems = NERVOUS_SYSTEM`.

### HDCA paper text


HDCA describes the broader NCC compartment from which sensory NCC/SCPs emerge:

> "broad NCC (SOX10, FOXD3) compartment we observed sensory (PRDM12), autonomic (PHOX2B), and mesenchymal (PDGFRA) populations co-existing at 6PCW"
>
> — Webb et al. (2026), HDCA

Soldatov et al. (2019), HDCA's cited basis for this lineage hierarchy:

> "differentiation tree suggested by single cell sequencing implies a series of binary cell fate decisions, with an early split into sensory neurons versus other potential neural crest fates, followed by the splitting of autonomic neuronal and mesenchymal lineages"
>
> — Soldatov et al. (2019)


## Markers (HDCA Supplementary Table 9 signature)

> "SOX10,SOX2,MPZ,SPP1,PLP1,PAX3,ERBB3,CNP,TFAP2A,EDNRB,TFAP2B,INSC,GFRA3,NPR3,NRP2,TTYH1,POSTN,COL18A1,SCRG1,FOXD3"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **MPZ** | 37.6 | 7.50 | 1.7e-304 |
| **CUEDC2** | 35.5 | 3.45 | 7.3e-272 |
| **PLP1** | 35.3 | 5.20 | 3.3e-269 |
| **MOXD1** | 35.2 | 5.14 | 3.3e-268 |
| **SPP1** | 34.7 | 5.49 | 4.0e-260 |
| **NPR3** | 33.8 | 5.17 | 1.0e-246 |
| **ISYNA1** | 33.4 | 3.49 | 6.3e-241 |
| **SOX10** | 33.4 | 5.94 | 6.3e-241 |
| **LINC01198** | 32.7 | 7.28 | 1.0e-230 |
| **EGFL8** | 32.5 | 5.37 | 2.2e-228 |
| **TTYH1** | 32.0 | 3.99 | 3.5e-221 |
| **ERBB3** | 31.9 | 4.48 | 1.4e-220 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Soldatov R et al. (2019). "Spatiotemporal structure of cell fate decisions in murine neural crest" *Science 364*. DOI: [10.1126/science.aas9536](https://doi.org/10.1126/science.aas9536)
- Kastriti ME et al. (2022). "Schwann cell precursors represent a neural crest-like state with biased multipotency" *EMBO J 41*. DOI: [10.15252/embj.2021108780](https://doi.org/10.15252/embj.2021108780)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (PNS_NCC compartment, NERVOUS_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

# SCPS — Schwann cell precursors

Cell Ontology: [Schwann cell precursor](http://purl.obolibrary.org/obo/CL_0002375) (CL:0002375, **exact match** — CL definition ("multipotent progenitor cell that develops from a migratory neural crest cell ... lacks a basal lamina") matches HDCA SOX10+/PLP1+/ERBB3+/MPZ+ cluster precisely.)

## Summary

Schwann cell precursors (SCPs) are nerve-associated, multipotent neural-crest-derived progenitors that travel along outgrowing peripheral axons throughout the embryo. In the HDCA whole-embryo data they form a SOX10+/PLP1+/ERBB3+/MPZ+/S100B+ cluster of 5,092 cells at Carnegie stages 13–14, representing the 'multipotent hub' state from which Schwann lineage, melanocyte, parasympathetic, enteric and chromaffin fates diverge.

## HDCA atlas evidence

**Cell count:** 5,092 cells. HDCA classifies this cluster as `broad_celltype = PNS_NCC`, `systems = NERVOUS_SYSTEM`.

### HDCA paper text


In the HDCA spatial+transcriptomic atlas, SCPs sit at the trunk of the PNS lineage tree:

> "broad NCC (SOX10, FOXD3) compartment we observed sensory (PRDM12), autonomic (PHOX2B), and mesenchymal (PDGFRA) populations co-existing at 6PCW"
>
> — Webb et al. (2026), HDCA

The Kastriti et al. (2022) paper that HDCA cites as the canonical source on SCP identity defines them as:

> "SCPs are nerve-associated progenitors that can generate myelinating and non-myelinating Schwann cells but also are multipotent like the neural crest cells from which they originate ... early SCPs and late migratory crest cells have similar transcriptional profiles characterised by a multipotent "hub" state"
>
> — Kastriti et al. (2022)


## Markers (HDCA Supplementary Table 9 signature)

> "SOX10,PLP1,ERBB3,S100B,EDNRB,MPZ,CNP,SPP1,POSTN,NGFR,INSC,CDH6,COL18A1,FOXD3,MEGF10,L1CAM,PTPRZ1,ITGA4,PLAT,SCRG1"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **MOXD1** | 35.4 | 5.82 | 1.0e-270 |
| **MPZ** | 35.4 | 7.25 | 1.0e-270 |
| **PLP1** | 34.5 | 5.40 | 1.2e-256 |
| **ERBB3** | 34.1 | 5.18 | 6.9e-252 |
| **ISYNA1** | 34.0 | 3.59 | 9.7e-250 |
| **POSTN** | 33.5 | 5.25 | 1.6e-242 |
| **CDH6** | 33.3 | 5.39 | 6.7e-240 |
| **EGFL8** | 33.3 | 6.15 | 1.3e-239 |
| **PLS3** | 33.2 | 4.46 | 9.7e-239 |
| **S100B** | 33.2 | 5.65 | 1.8e-238 |
| **SOX10** | 32.3 | 6.22 | 3.0e-226 |
| **COL18A1** | 32.0 | 3.87 | 1.1e-221 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Kastriti ME et al. (2022). "Schwann cell precursors represent a neural crest-like state with biased multipotency" *EMBO J 41*. DOI: [10.15252/embj.2021108780](https://doi.org/10.15252/embj.2021108780)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (PNS_NCC compartment, NERVOUS_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

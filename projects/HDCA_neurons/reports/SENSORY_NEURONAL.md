# SENSORY_NEURONAL — Sensory neuron (post-mitotic, DRG/trigeminal-type)

Cell Ontology: [sensory neuron](http://purl.obolibrary.org/obo/CL_0000101) (CL:0000101, **exact match** — HDCA-assigned. Generic "sensory neuron" definition matches the post-mitotic ISL1+/POU4F1+/PRPH+ pan-sensory population well.)

## Summary

Sensory neurons in HDCA are the post-mitotic terminal product of the NCC sensory branch, carrying the canonical DRG/trigeminal molecular fingerprint: ISL1+, POU4F1+ (BRN3A), PRPH+, with mature ion channel (SCN9A, PIEZO2), neurotrophic receptor (NTRK family) and axonal cytoskeleton (GAP43, MAPT, STMN2) signatures. The HDCA paper cites Soldatov et al. (ref 149) for the early-fate framework and Murtazina & Adameyko (ref 160) and Kupari et al. (ref 161) for the molecular taxonomy this state represents.

## HDCA atlas evidence

**Cell count:** 4,815 cells. HDCA classifies this cluster as `broad_celltype = PNS_NEURONAL`, `systems = NERVOUS_SYSTEM`.

### HDCA paper text


HDCA describes the PNS neuronal output of the NCC programme:

> "Multipotent sensory NCCs were predicted to progress through sensory neuronal progenitor states to form sensory neurons (CNTN2), while autonomic NCCs were predicted to develop into autonomic neuronal progenitor states (PHOX2B, ASCL1) and diverse autonomic neuronal derivatives"
>
> — Webb et al. (2026), HDCA

Soldatov et al. (2019), HDCA ref [149]:

> "differentiation tree suggested by single cell sequencing implies a series of binary cell fate decisions, with an early split into sensory neurons versus other potential neural crest fates, followed by the splitting of autonomic neuronal and mesenchymal lineages"
>
> — Soldatov et al. (2019)


## Markers (HDCA Supplementary Table 9 signature)

> "GAP43,ISL1,SCN9A,PRPH,MAPT,CNTN2,PIEZO2,STMN2,ELAVL4,EBF1,NRXN1,GNAO1,RTN1,DCX,PLXNA4,FGF13,ELAVL3,KIF5A,PRKG1,SCN7A"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **PRPH** | 37.0 | 8.03 | 5.0e-295 |
| **GAP43** | 35.1 | 5.15 | 7.7e-266 |
| **MAP1B** | 34.8 | 4.15 | 2.8e-262 |
| **GNAO1** | 34.5 | 4.81 | 1.4e-256 |
| **STMN2** | 34.4 | 5.60 | 1.6e-255 |
| **ISL1** | 34.2 | 5.64 | 6.7e-253 |
| **MAPT** | 34.0 | 4.89 | 1.4e-250 |
| **SCN9A** | 33.7 | 5.56 | 8.9e-246 |
| **PPP1R1C** | 33.7 | 7.18 | 2.0e-245 |
| **DPYSL3** | 33.5 | 3.95 | 8.1e-243 |
| **ELAVL4** | 33.4 | 4.41 | 1.5e-241 |
| **EBF1** | 33.3 | 5.08 | 1.4e-239 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Soldatov R et al. (2019). "Spatiotemporal structure of cell fate decisions in murine neural crest" *Science 364*. DOI: [10.1126/science.aas9536](https://doi.org/10.1126/science.aas9536)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (PNS_NEURONAL compartment, NERVOUS_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

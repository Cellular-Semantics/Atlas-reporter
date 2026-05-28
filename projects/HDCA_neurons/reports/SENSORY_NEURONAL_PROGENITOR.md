# SENSORY_NEURONAL_PROGENITOR — Sensory neuronal progenitor (DRG / spinal sensory neurogenic precursor)

Cell Ontology: [sensory neuron of dorsal root ganglion](http://purl.obolibrary.org/obo/CL_1001451) (CL:1001451, **broad match** — HDCA-assigned. CL:1001451 is DRG-specific and describes the mature neuron, not a progenitor state. The HDCA cluster spans multiple ganglia and is a SIX1+/POU4F1+/TLX3+ pre-neuronal state. NTR needed f...)

## Summary

Sensory neuronal progenitors are the post-mitotic-onset state between NCC commitment and mature sensory neurons. The HDCA signature (SIX1+, ISL1+, POU4F1+, TLX3+, NHLH1+, DLL3+, INSM1+) maps directly to the canonical sensory specification programme described in Soldatov et al. — Neurogenin1/2 activation → ISL1/POU4F1 (BRN3A) → TLX3 in the early differentiating sensory neuron lineage.

## HDCA atlas evidence

**Cell count:** 3,349 cells. HDCA classifies this cluster as `broad_celltype = PNS_NEURONAL`, `systems = NERVOUS_SYSTEM`.

### HDCA paper text


HDCA's PNS lineage reconstruction places sensory neuronal progenitors as the obligate transition state:

> "Multipotent sensory NCCs were predicted to progress through sensory neuronal progenitor states to form sensory neurons (CNTN2), while autonomic NCCs were predicted to develop into autonomic neuronal progenitor states (PHOX2B, ASCL1) and diverse autonomic neuronal derivatives"
>
> — Webb et al. (2026), HDCA

Soldatov et al. (2019), HDCA ref [149], establishes the sensory binary fate decision:

> "differentiation tree suggested by single cell sequencing implies a series of binary cell fate decisions, with an early split into sensory neurons versus other potential neural crest fates, followed by the splitting of autonomic neuronal and mesenchymal lineages"
>
> — Soldatov et al. (2019)


## Markers (HDCA Supplementary Table 9 signature)

> "SIX1,ISL1,POU4F1,DCX,ELAVL4,TLX3,GFRA1,EYA2,NHLH1,CNTN2,DLL3,SRRM4,SSTR2,PTPRF,INSM1,TRHDE,EBF1,ELAVL2,PPP1R14A,CACNA1A"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **ISL1** | 33.0 | 5.70 | 1.3e-234 |
| **ENC1** | 32.2 | 3.84 | 3.8e-223 |
| **SIX1** | 32.0 | 5.11 | 1.1e-220 |
| **CADM1** | 31.2 | 3.93 | 2.0e-209 |
| **BASP1** | 30.8 | 3.31 | 4.4e-205 |
| **ELAVL4** | 30.6 | 3.83 | 8.3e-202 |
| **THSD7B** | 30.6 | 6.38 | 8.3e-202 |
| **PCBP4** | 30.1 | 3.70 | 5.1e-196 |
| **NHLH1** | 29.3 | 4.90 | 5.3e-185 |
| **C14orf132** | 27.9 | 3.78 | 7.6e-168 |
| **TAGLN3** | 27.4 | 3.48 | 2.4e-162 |
| **SRRM4** | 27.3 | 3.49 | 5.8e-161 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Soldatov R et al. (2019). "Spatiotemporal structure of cell fate decisions in murine neural crest" *Science 364*. DOI: [10.1126/science.aas9536](https://doi.org/10.1126/science.aas9536)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (PNS_NEURONAL compartment, NERVOUS_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

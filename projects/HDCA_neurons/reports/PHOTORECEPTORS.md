# PHOTORECEPTORS — Photoreceptor (rod / cone, embryonic stage)

Cell Ontology: [photoreceptor cell](http://purl.obolibrary.org/obo/CL_0000210) (CL:0000210, **exact match** — At CS13-22 most cells in HDCA cluster are not yet committed rod vs cone; CL:0000210 is the appropriate ancestor term.)

## Summary

HDCA's embryonic photoreceptor cluster expresses RCVRN (recoverin, pan-photoreceptor marker), NRL (the master rod-determining transcription factor), GNB3 (cone transducin subunit), AIPL1 (photoreceptor aryl-hydrocarbon-interacting protein-like 1) and FABP7. At this stage (Carnegie 13–22-equivalent), cones predominate; HDCA explicitly invokes the thyroid-hormone / TRH axis from Eldred et al. (cited ref 74) for cone subtype specification.

## HDCA atlas evidence

**Cell count:** 7,760 cells. HDCA classifies this cluster as `broad_celltype = AUDIOVISUAL_NEURONAL`, `systems = AUDIOVISUAL_SYSTEM`.

### HDCA paper text


HDCA links photoreceptor development to thyroid-hormone signalling:

> "TRH signalling has been reported to specify cone subtypes in human retinal organoids74, and thus we provide further evidence in support of a role for TRH in the retina"
>
> — Webb et al. (2026), HDCA

HDCA cites Eldred et al. 2018 (ref 74), which showed:

> "S cones are specified first, followed by L/M cones, and thyroid hormone signaling controls this temporal switch."
>
> — Eldred et al. (2018)


## Markers (HDCA Supplementary Table 9 signature)

> "RCVRN,NRL,GNB3,AIPL1,FABP7"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | Score | logFC | padj |
|---|--:|--:|--:|
| **RCVRN** | 36.0 | 11.05 | 8.6e-279 |
| **CKB** | 29.2 | 3.63 | 4.2e-183 |
| **MALAT1** | 27.7 | 1.57 | 8.8e-165 |
| **YBX1** | 27.6 | 1.85 | 8.8e-164 |
| **NRL** | 26.1 | 8.37 | 4.6e-147 |
| **CIRBP** | 24.2 | 1.97 | 7.2e-126 |
| **EEF1A1** | 23.6 | 1.94 | 5.0e-120 |
| **EIF1** | 22.0 | 1.14 | 8.1e-105 |
| **RPL13** | 21.4 | 1.18 | 3.1e-99 |
| **AIPL1** | 20.9 | 8.60 | 1.6e-94 |
| **PDC** | 19.5 | 8.82 | 1.5e-82 |
| **GNB3** | 18.8 | 6.81 | 3.7e-77 |

## References (HDCA paper + atlas-cited literature)

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development" *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Eldred KC et al. (2018). "Thyroid hormone signaling specifies cone subtypes in human retinal organoids" *Science 362*. DOI: [10.1126/science.aau6348](https://doi.org/10.1126/science.aau6348)


## Source-of-label note

This cell type was annotated within HDCA's whole-embryo data (AUDIOVISUAL_NEURONAL compartment, AUDIOVISUAL_SYSTEM). All evidence quoted above is sourced either from the HDCA paper itself (Webb et al., 2026) or from the specific reference HDCA cites at that passage, retrieved via citation-traversal snippet search.

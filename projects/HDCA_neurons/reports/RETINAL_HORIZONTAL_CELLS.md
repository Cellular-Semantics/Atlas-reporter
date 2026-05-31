# Retinal Horizontal Cells (RETINAL_HORIZONTAL_CELLS)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=68 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retina horizontal cell](http://purl.obolibrary.org/obo/CL_0000745) (CL:0000745, exact match)

## Summary

The RETINAL_HORIZONTAL_CELLS population in HDCA v2 comprises 68 fetal retinal
cells classified within the broader AUDIOVISUAL_NEURONAL compartment. Horizontal
cells (HCs) are GABAergic/glycinergic interneurons of the inner nuclear layer
(INL) that modulate photoreceptor-to-bipolar signalling and mediate lateral
inhibition. In HDCA, this cluster is defined by a transcription factor (TF)
signature characteristic of early retinal interneurons including PAX6, SIX3,
ONECUT2, MAB21L1 and RORB, together with pan-neuronal markers (STMN2, RTN1).
The annotation derives entirely from kNN label propagation seeded from
Sridhar et al. 2020 (Sridhar et al., 2020), in which post-neurogenic HCs and
RGCs were observed to be transcriptionally separated from ongoing transition
populations of the central retina.

## Annotation provenance

100% of cells in RETINAL_HORIZONTAL_CELLS were contributed by Sridhar et al.
2020 (DOI: 10.1016/j.celrep.2020.01.007). HDCA audiovisual-system labels were
harmonised by kNN propagation of Sridhar's published cell-type labels onto
HDCA retinal cells. The Sridhar crosswalk indicates 85.3% concordance with
the "HC" label — some impurity is expected given the small n and the
overlapping transition states. In Sridhar 2020 the HC cluster was
characterised by ONECUT2 and TFAP2A expression in the INL, where mature HCs
co-stain with CALBINDIN and TFAP2A:

> A single layer of PRs (ONL, OTX2+/RCVRN+), BCs (INL, OTX2+/VSX2+), and HCs and ACs (CALBINDIN+/TFAP2A+)

(paraphrased structure of Sridhar Fig. 4A; Sridhar et al., 2020).

Sridhar additionally noted that by mid-gestation, HCs and RGCs have largely
exited the neurogenic programme:

> the UMAP plot also shows that the RGCs and HCs (gray, Figure 2D) are separate from the other cell transition populations, presumably because they are no longer being generated in the central retina

(Sridhar et al., 2020).

## Markers

Top differentially expressed genes for RETINAL_HORIZONTAL_CELLS in HDCA
(Supp Table 16) include retinal-interneuron TFs and pan-neuronal cytoskeletal
markers:

- TF / fate markers: **PAX6** (logFC 4.25), **SIX3** (5.60), **ONECUT2**
  (5.06), **MAB21L1** (4.53), **RORB** (5.55).
- Pan-neuronal / cytoskeletal: **STMN2** (3.98), **RTN1** (3.34),
  **TUBB2B** (3.21), **TUBA1A** (2.49), **MLLT11** (2.85), **CALM2** (2.15),
  **PCSK1N** (3.00), **MARCKSL1** (1.38).
- Metabolic / RNA-binding: **CKB** (3.37), **CIRBP** (2.48), **CCNI** (2.20),
  **YBX1** (1.94), **HNRNPA1** (1.64), **HNRNPDL** (1.01), **EIF1** (1.12).

HDCA Supp Table 9 reports the curated gene signature for this cell type:

> PAX6,SIX3,RORB,ONECUT2,MAB21L1,STMN2,RTN1,CRABP1

(Webb et al., 2026). ONECUT2 is a canonical horizontal-cell TF (also active in
early RGCs and amacrine cells), and PAX6 together with SIX3 mark the broader
retinal progenitor / interneuron programme. In Sridhar et al. 2020, mature
HCs of the FD125 INL co-expressed CALBINDIN and TFAP2A by
immunofluorescence; CALBINDIN/TFAP2A protein markers are not in the HDCA top
scRNA DEGs for this small cluster but are consistent with the assigned
identity.

## Location and function in fetal retina

In Sridhar et al. 2020, horizontal cells reside in the inner nuclear layer
of the fetal retina alongside amacrine cells and bipolar cells. By FD125
near the fovea, the laminar architecture is established:

> IF of FD125 near the fovea shows that neurogenesis is complete: a single layer of PRs (ONL, OTX2+/RCVRN+), BCs (INL, OTX2+/VSX2+), and HCs and ACs (CALBINDIN+/TFAP2A+)

(Sridhar et al., 2020). Functionally, HCs provide horizontal (lateral)
inhibitory feedback at the outer plexiform layer synapse between
photoreceptors and bipolar cells, shaping centre-surround receptive fields
and contrast sensitivity.

## Developmental specification

HCs are among the earliest-born retinal cell types and share an early
neurogenic window with retinal ganglion cells (RGCs). Sridhar et al. 2020
show that by FD125, RGCs and HCs are no longer being produced in central
retina, while bipolar and photoreceptor generation continues through
later transition states (T2/T3, marked by PRDM13 and FABP7 respectively):

> RGCs are more highly represented at FD59 ... In contrast, PRs predominate at FD125C

(Sridhar et al., 2020). HDCA notes that the embryonic retina is broadly
characterised by ATOH7 (RGC fate), PRDM13 (amacrine fate in mouse) and
GADD45A:

> embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73

(Webb et al., 2026). ATOH7 itself is RGC-restricted (Ghiasvand et al., 2011)
and PRDM13 marks the amacrine lineage (Watanabe et al., 2015) — horizontal
cells in HDCA are therefore distinguished from these neighbouring early
fates by their ONECUT2 / PAX6 / SIX3 / MAB21L1 / RORB TF combination rather
than by ATOH7 or PRDM13 expression. Thyroid-hormone signalling, implicated
in cone subtype switching (Eldred et al., 2018), is not a feature of the HC
cluster.

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas
  of human prenatal development. bioRxiv. DOI:
  [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Sridhar A et al. (2020). Single-Cell Transcriptomic Comparison of Human
  Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal
  Cultures. Cell Reports 30:1644-1659.e4. DOI:
  [10.1016/j.celrep.2020.01.007](https://doi.org/10.1016/j.celrep.2020.01.007)
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7
  disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14.
  DOI: [10.1038/nn.2776](https://doi.org/10.1038/nn.2776)
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of
  Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J
  Neurosci 35. DOI:
  [10.1523/JNEUROSCI.0089-15.2015](https://doi.org/10.1523/JNEUROSCI.0089-15.2015)
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone
  subtypes in human retinal organoids. Science 362. DOI:
  [10.1126/science.aau6348](https://doi.org/10.1126/science.aau6348)

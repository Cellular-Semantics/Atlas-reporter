# Bipolar Cells (BIPOLARS)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=1334 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal bipolar neuron](http://purl.obolibrary.org/obo/CL_0000748) (CL:0000748, exact match)

## Summary

The BIPOLARS cluster in HDCA v2 comprises 1,334 fetal retinal bipolar neurons within the broader AUDIOVISUAL_NEURONAL compartment. These are second-order interneurons of the inner nuclear layer (INL) that relay photoreceptor signals to retinal ganglion cells. Cells are characterised by an HDCA gene signature including RORB, RCVRN, NEUROD4, GNB3, UNC119, CA10, SYT1, SNAP25, SYP, MAB21L1, CPE and FABP7 (HDCA Supp Table 9; Webb et al., 2026), consistent with late-born retinal interneurons emerging from progenitors via a FABP7+/DLL3+ T3 transition state (Sridhar et al., 2020).

## Annotation provenance

All 1,334 BIPOLARS cells were annotated by harmonisation with Sridhar et al. (2020), whose scRNA-seq of fetal human retina at FD59, FD82 and FD125 first identified a distinct bipolar cluster in the developing INL. Sridhar et al. (2020) describe the appearance of this population at FD82 as:

> "a distinct population of bipolar cells (BCs) can now be identified"

and at FD125 confirm bipolars by co-expression of OTX2/VSX2/RCVRN in the INL:

> "BCs (OTX2/ VSX2/RCVRN) in the INL"

HDCA v2 propagated this Sridhar label to whole-embryo cells in matching audiovisual clusters via kNN classifier (Webb et al., 2026).

## Markers

The HDCA bipolar gene signature (Webb et al., 2026; HDCA Supp Table 9) is:

> "RORB,RCVRN,NEUROD4,GNB3,UNC119,CA10,SYT1,SNAP25,SYP,TUBB2B,MLLT11,MAB21L1,FSTL5,CPE,FABP7"

Top differentially expressed genes from HDCA Supp Table 16 include the canonical bipolar/photoreceptor marker RCVRN (logFC=6.20, padj=1.3e-41), the T3-transition marker FABP7 (logFC=3.45, padj=9.0e-44), CKB (logFC=3.66), PCBP4 (logFC=3.58), CPE (logFC=2.43), CA10 (logFC=4.95), and the neuronal microtubule gene STMN1. The Sridhar et al. (2020) bipolar identification was anchored on co-expression of OTX2 and RCVRN in the INL:

> "cells that express markers of bipolar cells (OTX2/RCVRN in the inner nuclear layer [INL])"

VSX2 — a pan-retinal progenitor/bipolar marker — is added by Sridhar at FD125 to disambiguate mature bipolars from photoreceptors (which share OTX2/RCVRN but reside in the ONL).

## Location and function in fetal retina

Bipolar cells reside in the inner nuclear layer of the neural retina. Their appearance lags that of RGCs, amacrines and horizontal cells: Sridhar et al. (2020) found no bipolars at FD59 and only a rudimentary photoreceptor layer with no defined INL at peripheral FD78:

> "Peripheral retina shows a rudimentary PR layer (OTX2+/ RCVRN+) but no BCs and no defined INL or plexiform layers."

By FD82 central retina they form a distinct cluster, and by FD125 central retina bipolars are abundant alongside photoreceptors:

> "all major retinal cell types are present: PRs (OTX2/RCVRN) in the ONL, BCs (OTX2/ VSX2/RCVRN) in the INL, and HCs and ACs (AP2A/CALB1"

Bipolars function as glutamatergic relay interneurons between photoreceptors and retinal ganglion cells; the HDCA signature genes SYT1, SNAP25 and SYP confirm a mature synaptic-vesicle machinery is being deployed at fetal stages.

## Developmental specification

Sridhar et al. (2020) describe a stereotyped sequence in which retinal progenitors transit through an ATOH7+ T1 state and then bifurcate, with bipolars and photoreceptors emerging via a shared T3 transition characterised by high FABP7, OTX2 and DLL3:

> "T3 cells lie between T1 cells and PR cells or BCs; T3 cells express high levels of FABP7"

and

> "T3 cells express high levels of FABP7, OTX2, and DLL3"

This T3 → BC/PR fate split is mirrored in the HDCA BIPOLARS DEGs, where FABP7 (logFC=3.45) and RCVRN (logFC=6.20) co-rank highly, suggesting the HDCA cluster captures cells across late-T3 and committed-bipolar states rather than only fully mature bipolars. Consistent with this, Sridhar shows the late-born bipolar fate emerges only after the early-born RGC/amacrine/horizontal waves driven by ATOH7 and PRDM13, the latter being a T2/amacrine determinant rather than a bipolar gene (Watanabe et al., 2015; Sridhar et al., 2020). The HDCA atlas reiterates the ATOH7/PRDM13 axis for early retinal neurogenesis (Webb et al., 2026):

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

placing BIPOLARS downstream of these earlier-born populations.

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015

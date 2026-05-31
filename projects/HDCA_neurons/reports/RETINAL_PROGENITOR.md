# Retinal Progenitors (RETINAL_PROGENITOR)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=6609 cells (broad: AUDIOVISUAL_NEUROEPITHELIUM)
Cell Ontology: [retinal progenitor cell](http://purl.obolibrary.org/obo/CL_0002672) (CL:0002672, exact match)

## Summary

The HDCA RETINAL_PROGENITOR cluster captures the proliferative, multipotent neuroepithelial population of the fetal human neural retina, expressing canonical progenitor markers (SOX2, FABP7, CCND1, HES6) alongside the HDCA-defined signature SOX2/SPP1/RORB/FABP7/MAB21L1/CRABP1/TTYH1 (Webb et al., 2026). Cells in this state give rise sequentially to all retinal neurons and Müller glia, and the cluster captures both uncommitted progenitors and early-committed neurogenic transition states (Sridhar et al., 2020).

**Impurity flag.** This is not a pure progenitor cluster. Annotation provenance traces 100% of cells to Sridhar et al. (2020); the Sridhar crosswalk shows the HDCA RETINAL_PROGENITOR label is a composite of three Sridhar populations: "Progenitors" (58.0%), "Photo/Progen" (37.2%, progenitors biased toward photoreceptor specification), and "Early Glia/imGlia" (~5%). The cluster therefore conflates uncommitted retinal progenitors with photoreceptor-biased transition cells (analogous to the T3/FABP7+ state) and a small fraction of early/immature glia. Downstream marker interpretation should treat photoreceptor-priming signatures (e.g. FABP7, RORB, OTX2 derivatives) as contributed by the Photo/Progen sub-fraction rather than by uncommitted progenitors.

## Annotation provenance

Labels for the HDCA audiovisual system were harmonised by kNN propagation of the Sridhar et al. (2020) reference annotations onto the HDCA single-cell data; 100% of cells carrying the RETINAL_PROGENITOR label trace back to Sridhar. The Sridhar reference populations contributing to this cluster are: Progenitors (58.0%), Photo/Progen (37.2%), and Early Glia/imGlia (~5%). Sridhar et al. (2020) defined the principal progenitor pool by SOX2/PAX6 expression in the neuroblast layer:

> "The two predominant cell types in the retina at this stage are retinal progenitors in the neuroblast layer (NBL; SOX2+/PAX6+) and retinal ganglion cells(RGCs;HUC/D+)"

## Markers

HDCA top DEGs for RETINAL_PROGENITOR (Supp Table 16) include the progenitor TFs **SOX2** (logFC=4.39) and cell-cycle/proliferation genes **CCND1** (logFC=3.07), **HMGB2**, **H2AFZ**, **TUBA1B**, alongside the secreted matricellular gene **SPP1** (logFC=5.34), the retinal-progenitor TF **RORB** (logFC=5.30), the developmental gene **MAB21L1** (logFC=4.87), the retinoic-acid-binding protein **CRABP1** (logFC=3.90), the glial/neural-stem marker **GPM6B** (logFC=3.27), **CKB** (logFC=4.60), and the proneural/Notch-target **HES6** (logFC=3.33). HDCA Supp Table 9 records the consensus progenitor signature:

> "SOX2,SPP1,RORB,FABP7,MAB21L1,CRABP1,TTYH1"

FABP7 is notable as a marker of the photoreceptor-biased T3 transition state in Sridhar et al. (2020), consistent with the 37% Photo/Progen contribution flagged above. HES6 is co-expressed with ATOH7 in the neurogenic T1 transition (Sridhar et al., 2020).

## Location and function in fetal retina

Retinal progenitors reside in the neuroblast layer of the developing neural retina, where they undergo proliferative and neurogenic divisions to generate the full diversity of retinal neurons and Müller glia. At early stages (~FD59) progenitors dominate the tissue; by mid-gestation they persist in the periphery while differentiated layers form centrally (Sridhar et al., 2020):

> "Progenitors and RGCs still make up the largest clusters, but now amacrine cells (ACs) and horizontal cells (HCs) form distinct clusters"

> "the peripheral retina is still dominated by progenitors (SOX2) and RGC, amacrine, or horizontal cells (AP2A/HUC/D)"

By late fetal stages neurogenesis is restricted to the far peripheral retina:

> "there are still substantial numbers of ATOH7 T1 cells in the periphery"

## Developmental specification

Sridhar et al. (2020) resolved the progenitor pool into a root proliferative state plus three neurogenic transition states (T1/T2/T3) that emerge from it, with the HDCA RETINAL_PROGENITOR cluster overlapping the progenitor root and the FABP7+ T3 photoreceptor-biased state:

> "T1 cells seem to form a root for two additional transition states, T2 and T3, as shown by UMAP clustering. The T2 cells lead to ACs; the cells in this cluster express PRDM13, a gene that promotes AC identity"

> "T3 cells lie between T1 cells and PR cells or BCs; T3 cells express high levels of FABP7"

> "in addition to ATOH7, T1 cells express HES6, whereas PRDM13+ cells express PTF1A and HSPB1, and T3 cells express high levels of FABP7, OTX2, and DLL3"

ATOH7 marks the early post-mitotic neurogenic T1 state that gives rise primarily to RGCs (Ghiasvand et al., 2011):

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."

PRDM13 in the T2 branch specifies amacrine identity (Watanabe et al., 2015):

> "the Prdm13 transcriptional regulator is specifically expressed in developing and mature amacrine cells in the mouse retina. Most Prdm13-positive amacrine cells are Calbindin- and Calretinin-positive GABAergic or glycinergic neurons."

The HDCA paper recapitulates this neurogenic signature in the embryonic retina and additionally implicates TRH in cone specification (Webb et al., 2026; Eldred et al., 2018):

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

> "S cones are specified first, followed by L/M cones, and thyroid hormone signaling controls this temporal switch."

## References

- Webb S et al. (2026) An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020) Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644–1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Ghiasvand NM et al. (2011) Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776
- Watanabe S et al. (2015) Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Eldred KC et al. (2018) Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348

# Amacrine Cell (AMACRINE_CELL)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=78 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [amacrine cell](http://purl.obolibrary.org/obo/CL_0000561) (CL:0000561, exact match)

## Summary

Amacrine cells are GABAergic and glycinergic interneurons of the inner nuclear layer (INL) of the retina that shape retinal ganglion cell output through lateral and vertical modulation of bipolar–RGC signalling. In HDCA v2 (Webb et al., 2026), the AMACRINE_CELL cluster comprises 78 fetal-retina cells assigned to CL:0000561 with an exact ontology match. The HDCA marker signature for this cluster includes pan-neuronal genes (STMN2, GAP43, RTN1, SNCG) together with retinal interneuron transcription factors PAX6 and ISL1, plus CRABP1 and SIX3 — consistent with an immature amacrine identity (HDCA Supp Table 9; see also top DEGs CALM2, MLLT11, STMN2, CRABP1, GAP43, PAX6, SNCG in HDCA Supp Table 16).

The HDCA atlas paper anchors the molecular definition of fetal retinal neurogenesis around a small set of factors, noting that

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

(Webb et al., 2026).

## Annotation provenance

The AMACRINE_CELL label is not an HDCA de novo call: 100% of the 78 cells originate from Sridhar et al. (2020), and 98.7% retained the original author label "AC" after harmonisation. HDCA's audiovisual subatlas was built by propagating Sridhar's published labels onto matching whole-embryo clusters via a kNN classifier; for amacrine cells, no HDCA whole-embryo cells contribute, so the cluster is effectively a verbatim re-publication of Sridhar's AC population embedded in the integrated HDCA latent space (Sridhar et al., 2020; Webb et al., 2026). The provenance summary captured during traversal records this directly:

> "AMACRINE_CELL (n=78 cells): 100% from Sridhar_et_al_2020_CellPress; 98.7% of cells carried the original author label "AC" (amacrine cell). No HDCA whole-embryo cells contribute to this cluster."

## Markers

HDCA reports an amacrine/neuronal signature dominated by neurite-outgrowth and synaptic-vesicle machinery, layered onto retinal-interneuron transcription factors:

> "PAX6,ISL1,RORB,GAP43,SIX3,PRPH,ELAVL4,MAB21L1,STMN2,CRABP1,RTN1,SNCG,SNCA,INA,MTRNR2L1,SYT4,SCG5,NHLH2,MIAT,STMN4"

(Webb et al., 2026; HDCA Supp Table 9). Supplementary DEG analysis (HDCA Supp Table 16) reinforces this with top markers including CRABP1 (logFC=5.90), STMN2 (logFC=5.65), PAX6 (logFC=5.44), GAP43 (logFC=5.07), SNCG (logFC=4.77), RTN1 (logFC=4.70), MLLT11 (logFC=4.59), TUBB2B (logFC=4.38) and PCSK1N (logFC=4.39). PAX6 and ISL1 are the canonical TFs that distinguish amacrine identity within the broader retinal interneuron compartment, while STMN2/GAP43/SNCG mark active neuritogenesis in fetal post-mitotic neurons.

## Location and function in fetal retina

Amacrine cells reside in the inner portion of the INL and provide inhibitory (GABA/glycine) lateral input that sculpts RGC receptive fields. In mouse, Prdm13-defined amacrine subsets co-express Calbindin and Calretinin and adopt GABAergic or glycinergic neurotransmitter phenotypes:

> "the Prdm13 transcriptional regulator is specifically expressed in developing and mature amacrine cells in the mouse retina. Most Prdm13-positive amacrine cells are Calbindin- and Calretinin-positive GABAergic or glycinergic neurons."

(Watanabe et al., 2015). The HDCA AMACRINE_CELL signature (PAX6+, ISL1+, STMN2+, GAP43+, SNCG+) is consistent with immature post-mitotic interneurons that have exited the cell cycle but are still elaborating neurites, in agreement with the Sridhar et al. (2020) fetal AC cluster from which it is derived.

## Developmental specification

Fetal retinal neurogenesis is organised around a small set of fate-instructing transcription factors. HDCA explicitly highlights PRDM13 as the amacrine-specifying factor and ATOH7 as the RGC-specifying factor in the same retinal neurogenic window (Webb et al., 2026):

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

The PRDM13 mechanism was established in mouse, where Prdm13 not only marks but regulates amacrine subtype specification (Watanabe et al., 2015). ATOH7 acts in the parallel RGC lineage and is required for optic nerve formation:

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."

(Ghiasvand et al., 2011; quoted as represented in HDCA evidence). The presence of PAX6+/ISL1+/STMN2+ amacrine cells alongside ATOH7-driven RGCs in the HDCA fetal retina cohort places this cluster within the early neurogenic wave of human retinal development described by Sridhar et al. (2020).

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776

# T1 to Retinal Ganglion Cell Transition (T1_RGC)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=651 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal ganglion cell](http://purl.obolibrary.org/obo/CL_0000740) (CL:0000740, narrow match — no exact CL term; T1_RGC is an early-born transitional RGC subtype, not a generic mature RGC)

## Summary

T1_RGC is a transitional state spanning the commitment of bipotent ATOH7+ "T1" postmitotic cells to a retinal ganglion cell (RGC) fate in the human fetal retina. In the source dataset (Sridhar et al., 2020), label crosswalk to the HDCA harmonised cluster is 59.8% "T1/RGC" plus 36.1% "RGC", indicating cells captured mid-trajectory between the T1 transition population and committed RGCs. In Sridhar's data the T1 cluster

> "form a root for all retinal lineages at the early ages of retinal development"

and represents

> "an intermediate developmental state"

(Sridhar et al., 2020). The HDCA cluster (n=651) carries a pan-neuronal/RGC signature consistent with this transitional position.

## Annotation provenance

Annotations were propagated 100% from Sridhar et al. (2020) onto HDCA via kNN harmonisation across the audiovisual compartment. The composition (≈60% T1/RGC + 36% RGC) reflects cells transitioning out of the ATOH7+ "T1" postmitotic state into committed RGCs, rather than mature ganglion cells of the GCL (Sridhar et al., 2020). The HDCA Supp Table 9 assigns this cluster to AUDIOVISUAL_NEURONAL within AUDIOVISUAL_SYSTEM.

## Markers

HDCA Supp Table 16 top DEGs for this cluster are dominated by a pan-RGC / early neuronal program: PRPH (logFC=7.11), CRABP1 (6.22), STMN2 (6.03), ISL1 (5.90), GAP43 (5.87), SNCG (5.52), PAX6 (5.48), MLLT11 (4.77), PCSK1N (4.73), RTN1 (4.68), NSG1 (4.66), TUBB2B (4.57), TAGLN3 (4.06), TUBA1A (3.76), RBP1 (3.56), CD24 (3.51), MAP1B (3.40), CALM2 (3.28). The HDCA Supp Table 9 signature for this state is

> "PAX6,SIX3,ISL1,GAP43,PRPH,MAB21L1,CNTN2,STMN2,CRABP1,SNCG,INA,RTN1,DCX,MIAT,ELAVL4,RORB,CHRNA3,GNG3,NEFM,SLC18A2"

(Webb et al., 2026), with SNCG and ISL1 specifically marking committed RGCs and GAP43/STMN2/TUBB2B reflecting active axonogenesis. The defining T1 transition marker ATOH7 is required for the upstream commitment step:

> "ATOH7 (Math5), a bHLH transcription factor gene that is required for retinal ganglion cell (RGC) and optic nerve development. In humans, the absence of RGCs stimulates massive neovascular growth of fetal blood vessels in the vitreous and early retinal detachment."

(Ghiasvand et al., 2011). In Sridhar's data:

> "The T1 cell population is characterized by expression of ATOH7; this gene is known in the mouse to be primarily expressed in newly generated postmitotic cells that can differentiate into diverse retinal cell types"

and HDCA confirms the broader retinal context:

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

(Webb et al., 2026).

## Location and developmental position

In the fetal retina, T1 cells reside in the neuroblast layer above the nascent GCL, while differentiated RGCs occupy the GCL:

> "ATOH7-expressing cells are located in the NBL but not the ganglion cell layer"

(Sridhar et al., 2020). The T1 population is sharply enriched at early ages (FD59) and depleted later:

> "the T1 population predominates at FD59, with only a relatively small number of T3 cells. However, by FD125, ATOH7+ cells are not detected in the central retina"

and

> "RGCs are more highly represented at FD59; the many yellow dots in Figure 3D show that FD59 cells overlap well with RGCs"

(Sridhar et al., 2020). T1_RGC therefore captures the early-fetal window of RGC genesis from ATOH7+ neurogenic precursors, with retention of some progenitor-proximal features alongside expression of mature RGC markers such as SNCG.

## Lineage relationships

The T1 → RGC trajectory is supported by Sridhar et al.'s pseudotime analysis, in which ATOH7+ cells sit at the root of all neuronal lineages and feed an RGC branch defined by SNCG. ATOH7 is genetically required for this commitment (Ghiasvand et al., 2011). The HDCA atlas applies Cell2fate to reconstruct such fate transitions:

> "applied Cell2fate153 as it outperforms existing RNA velocity models in reconstructing known cell fate trajectories"

(Webb et al., 2026; Aivazidis et al., 2025). Parallel transition populations (T2 → amacrine, marked by PRDM13; T3 → photoreceptors/Müller glia, marked by FABP7) emerge from the same ATOH7+ pool, consistent with PRDM13's amacrine-specifying role (Watanabe et al., 2015) and with thyroid-hormone-regulated photoreceptor specification observed in the same retinal system (Eldred et al., 2018).

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348
- Aivazidis A et al. (2025). Cell2fate infers RNA velocity modules to improve cell fate prediction. Nat Methods 22. DOI: 10.1038/s41587-022-01624-4

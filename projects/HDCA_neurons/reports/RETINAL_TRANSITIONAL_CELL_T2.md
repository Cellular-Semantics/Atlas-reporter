# Retinal Transitional Cell T2 (RETINAL_TRANSITIONAL_CELL_T2)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=1018 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal progenitor cell](http://purl.obolibrary.org/obo/CL_0002672) (CL:0002672, broad match — no exact CL term; T2 is a Sridhar 2020 amacrine-committed transitional state not yet represented in CL)

## Summary

RETINAL_TRANSITIONAL_CELL_T2 represents a fetal retinal transitional state defined by Sridhar et al. (2020), corresponding to a PRDM13+ amacrine-committed intermediate positioned between multipotent retinal progenitors and differentiating amacrine cells (ACs). In the HDCA v2 atlas (Webb et al., 2026) this cluster comprises 1018 cells annotated 87.7% as "T2" and 12.3% as a mixed "T2/T3" label, indicating partial admixture with the photoreceptor-biased T3 state. The HDCA gene signature `RORB,CRABP1` is consistent with a neurogenic, retinoid-responsive intermediate, while the top-ranked differential expression of PRDM13 (logFC=7.42) anchors the T2 identity established by Sridhar et al. (2020).

## Annotation provenance

Cell-type labels were inherited 100% from Sridhar et al. (2020), the single source of the T1/T2/T3 transitional-state nomenclature, via crosswalk to the HDCA cluster labels (87.7% "T2", 12.3% "T2/T3"). T2 is a Sridhar 2020 innovation — an amacrine-committed transitional state defined by PRDM13 expression — and is not yet represented as a distinct CL term, so the HDCA atlas maps it to the broader parent CL:0002672 (retinal progenitor cell). The HDCA classification is `broad_celltype=AUDIOVISUAL_NEURONAL, systems=AUDIOVISUAL_SYSTEM` (HDCA Supp Table 9).

## Markers

Top differentially expressed genes (HDCA Supp Table 16) include **PRDM13** (logFC=7.42, padj=1.4e-62), **RORB** (logFC=5.89), **CRABP1** (logFC=4.19), **RBP1** (logFC=3.52), **CIRBP** (logFC=2.69), **MLLT11** (logFC=2.69), **CKB** (logFC=2.56), **HNRNPA1** (logFC=2.21), **RBM3** (logFC=2.15), and **MARCKSL1** (logFC=1.93). The HDCA marker signature for the cluster is summarised as:

> RORB,CRABP1

PRDM13 is the defining marker of the T2 state. Sridhar et al. (2020) report:

> For example, in addition to ATOH7, T1 cells express HES6, whereas PRDM13+ cells express PTF1A and HSPB1, and T3 cells express high levels of FABP7, OTX2, and DLL3

and explicitly tie PRDM13 to the amacrine lineage:

> Slingshot analysis plotting T2-specific PRDM13 expression along the amacrine lineage and T3-specific FABP7 and DLL3 along the PR lineage.

The functional role of PRDM13 in amacrine specification is supported by mouse work from Watanabe et al. (2015):

> the Prdm13 transcriptional regulator is specifically expressed in developing and mature amacrine cells in the mouse retina. Most Prdm13-positive amacrine cells are Calbindin- and Calretinin-positive GABAergic or glycinergic neurons.

The HDCA atlas paper (Webb et al., 2026) likewise places PRDM13 within the embryonic retinal marker repertoire:

> embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone

## Location and developmental position

T2 cells occupy an intermediate developmental position within the fetal neuroblastic layer (NBL) of the central retina. Sridhar et al. (2020) place T2 between progenitors and differentiated neurons in pseudotime:

> Figures 2D and 2D[0] show that the transition cell clusters are located between the progenitors and the differentiated neurons in their pseudotime values, with T1 cells having slightly earlier pseudotime values than T2 and T3 cells.

The T2 population is detected across multiple fetal ages and persists into later stages alongside T3:

> Heatmap showing genes characteristic of transition clusters in FD59, FD82, and FD125 retinas; T2 and T3 genes are still expressed at later ages.

At FD125, T2 cells are identifiable by PRDM13 expression after ATOH7+ T1 cells have disappeared from central retina (Sridhar et al., 2020):

> PRDM13 marks T2 cells, and FABP7 marks the T3 population.

## Lineage relationships

T2 is the amacrine-committed branch of a tripartite transitional model (T1 → T2/T3 → mature neurons) introduced by Sridhar et al. (2020). The authors explicitly assign T2 to the amacrine trajectory and note that ACs may transit through both T1 and T2 states:

> ACs appear to go through both a T1 and T2 transition state; however, PR cells appear to go through both the T1 and T3 states.

The combined Monocle/Slingshot analyses summarised in Sridhar et al. (2020) Figure 2 position T2 between multipotent progenitors and differentiated amacrine cells, with PRDM13/PTF1A as the molecular signature of commitment. The 12.3% "T2/T3" admixture observed in this HDCA cluster is consistent with the shared neurogenic origin of both branches and the partial overlap of their transcriptional programs at later fetal ages (Sridhar et al., 2020). Velocity inference in the HDCA atlas was performed with Cell2fate (Aivazidis et al., 2025):

> applied Cell2fate153 as it outperforms existing RNA velocity models in reconstructing known cell fate trajectories

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348
- Aivazidis A et al. (2025). Cell2fate infers RNA velocity modules to improve cell fate prediction. Nat Methods 22. DOI: 10.1038/s41587-022-01624-4

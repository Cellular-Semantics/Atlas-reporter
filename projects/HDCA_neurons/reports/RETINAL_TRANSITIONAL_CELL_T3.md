# Retinal Transitional Cell T3 (RETINAL_TRANSITIONAL_CELL_T3)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina — n=1873 cells (broad: AUDIOVISUAL_NEURONAL)
Cell Ontology: [retinal progenitor cell](http://purl.obolibrary.org/obo/CL_0002672) (CL:0002672, broad match — no exact CL term; T3 is a Sridhar 2020 photoreceptor/bipolar-committed transitional state)

## Summary

T3 cells are a fetal retinal transitional state, originally defined by Sridhar et al. (2020), that lie developmentally between multipotent retinal progenitors and differentiated photoreceptor (PR) / bipolar cell (BC) neurons. They are marked by high expression of FABP7, DLL3, and OTX2, and Sridhar's pseudotime/Slingshot analyses position them on the lineage from progenitors toward photoreceptors:

> "T3 cells express high levels of FABP7, OTX2, and DLL3"

(Sridhar et al., 2020). The cluster's HDCA gene signature `FABP7,RORB` (HDCA Supp Table 9) is consistent with this PR-committed identity, with NRL and RCVRN among top DEGs indicating active photoreceptor specification (HDCA Supp Table 16).

## Annotation provenance

Cell-type label and biology are inherited 100% from Sridhar et al. (2020) (DOI: 10.1016/j.celrep.2020.01.007), with crosswalk confidence "T3" 99.4%. T3 is a Sridhar 2020 innovation — a photoreceptor/bipolar-committed transitional state arising from the earlier ATOH7+ T1 state — and is not yet represented by an exact term in the Cell Ontology; CL:0002672 (retinal progenitor cell) is used as a broad parent.

## Markers

HDCA top DEGs for this cluster (Supp Table 16) include the canonical T3 marker **FABP7** (logFC=6.90, padj=3.0e-232) and photoreceptor-committed factors **NRL** (logFC=6.31), **RCVRN** (logFC=6.56), **NEUROD4** (logFC=5.51), and **RORB** (logFC=5.02), plus **RBP1**, **GPM6A**, **CKB**, **PCBP4**, and **TMX1**. The HDCA short signature is `FABP7,RORB` (HDCA Supp Table 9).

These align with Sridhar et al.'s defining T3 markers:

> "T3 cells express high levels of FABP7, OTX2, and DLL3 (Figure S2A)"

(Sridhar et al., 2020). Sridhar also used FABP7 and DLL3 as the canonical T3-lineage markers in their PR-lineage Slingshot analysis:

> "Slingshot analysis plotting T2-specific PRDM13 expression along the amacrine lineage and T3-specific FABP7 and DLL3 along the PR lineage"

(Sridhar et al., 2020). The presence of NRL, RCVRN, and NEUROD4 among the top HDCA DEGs is consistent with T3 cells already initiating photoreceptor differentiation programs.

## Location and developmental position

T3 cells are positioned between progenitors and differentiated retinal neurons in pseudotime, and become the dominant transition population at later fetal ages:

> "the transition cell clusters are located between the progenitors and the differentiated neurons in their pseudotime values, with T1 cells having slightly earlier pseudotime values than T2 and T3 cells"

(Sridhar et al., 2020). By mid-fetal ages T3 cells dominate the transition compartment of the central retina:

> "the T1 population predominates at FD59, with only a relatively small number of T3 cells. However, by FD125, ATOH7+ cells are not detected in the central retina (Figure 3E; Figure S3D), whereas FABP7-expressing T3 cells now account for the majority of the"

transitional pool (Sridhar et al., 2020). This timing matches the broader HDCA observation that the embryonic retina expresses neurogenic regulators including ATOH7, PRDM13, and GADD45A:

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"

(Webb et al., 2026).

## Lineage relationships

Sridhar et al. (2020) place T3 on the PR-committed branch downstream of T1 (ATOH7+) progenitor-derived cells; T1 contributes to multiple lineages while T3 is restricted toward photoreceptors (and bipolar cells):

> "ACs appear to go through both a T1 and T2 transition state; however, PR cells appear to go through both the T1 and T3 states"

(Sridhar et al., 2020). Consistent with active PR commitment, NRL — the master regulator of rod fate — and RCVRN are among the top HDCA DEGs (Supp Table 16). The HDCA atlas applies Cell2fate-based velocity modelling to reconstruct such fate trajectories across organs:

> "applied Cell2fate153 as it outperforms existing RNA velocity models in reconstructing known cell fate trajectories"

(Webb et al., 2026). Thyroid-hormone signalling (TRH) acts later on cone subtype choice in the photoreceptor lineage T3 feeds into:

> "S cones are specified first, followed by L/M cones, and thyroid hormone signaling controls this temporal switch."

(Eldred et al., 2018).

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Ghiasvand NM et al. (2011). Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease. Nat Neurosci 14. DOI: 10.1038/nn.2776
- Watanabe S et al. (2015). Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity. J Neurosci 35. DOI: 10.1523/JNEUROSCI.0089-15.2015
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348
- Aivazidis A et al. (2025). Cell2fate infers RNA velocity modules to improve cell fate prediction. Nat Methods 22. DOI: 10.1038/s41587-022-01624-4

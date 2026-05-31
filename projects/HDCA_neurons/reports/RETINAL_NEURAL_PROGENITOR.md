# Retinal Neural Progenitor (RETINAL_NEURAL_PROGENITOR)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (HDCA v2) (DOI: 10.64898/2026.03.30.714220)
Scope: fetal — Retina (eye field / early neurogenic) — n=767 cells (broad: AUDIOVISUAL_NEUROEPITHELIUM)
Cell Ontology: [retinal progenitor cell](http://purl.obolibrary.org/obo/CL_0002672) (CL:0002672, narrow match — no exact CL term; HDCA RNP is a PAX6+/LHX2+/SOX2+ neurogenic-committed subset, narrower than the generic CL term).

## Summary

RETINAL_NEURAL_PROGENITOR is an HDCA fetal retinal cluster (n=767) defined by a PAX6/SOX2/LHX2/SIX3/SFRP2 progenitor signature consistent with eye-field / early neurogenic retina at first-trimester stages (Webb et al., 2026). **Critically, and unlike every other retinal label in this subatlas, RETINAL_NEURAL_PROGENITOR is not derived from Sridhar et al. (2020).** It contains 100% HDCA whole-embryo de novo cells and the kNN-to-Sridhar harmonisation that produced the other retinal labels did not apply here — there were no community-data cells in the cluster for that mechanism to act on. The annotation is therefore a HDCA-internal manual call, supported by the Supp Table 9 / Supp Table 16 marker signature and by the spatial/molecular context of the embryonic retina at ~6 PCW described in the HDCA paper.

## Annotation provenance

This label is **HDCA de novo (whole-embryo) — manually curated**. The cluster comprises only HDCA-generated cells; no Sridhar 2020 cells were assigned to it during integration, so the Sridhar-driven label-transfer step that produced the other retinal labels (RGC, photoreceptor, amacrine, horizontal, bipolar, Müller, generic "Progenitors") had no effect here. RETINAL_NEURAL_PROGENITOR therefore reflects HDCA's own annotation of an early-neurogenic retinal compartment captured in their first-trimester whole-embryo sampling, with marker calls drawn from HDCA Supp Table 9 (gene signature) and Supp Table 16 (top DEGs). Sridhar 2020 is used in this report only as comparative literature context for what a "retinal progenitor" looks like in later fetal retina — it is **not** the source of this label.

## Markers

Top differentially expressed genes for the cluster (HDCA Supp Table 16) include canonical eye-field / retinal progenitor transcription factors and supporting genes: **PAX6** (logFC=5.62, padj=3.2e-272), **SOX2** (logFC=3.66, padj=7.9e-151), **LHX2** (logFC=3.78, padj=3.9e-159), **SIX3** (logFC=4.74, padj=1.0e-181), **SFRP2** (logFC=7.15, padj=3.3e-305), **DAPL1** (logFC=7.44, padj=2.3e-261), **MAB21L1** (logFC=4.38, padj=3.8e-214), **CRABP1**, **MDK**, **CCL2**, **CLDN1**, **GJA1**, **COL2A1**, **HMGA1**, **ID3**, **SPHK1**.

The published HDCA Supp Table 9 marker signature for this cluster is exactly:

> PAX6,SOX2,SIX3,LHX2,SFRP2,FGF19,GJA1,CCL2,CYP1B1,DIO3,CLDN1,TRPM3,MYCN,MAB21L1,COL9A1,COL2A1,HMX1,ZIC2,LRP2,OTX1

This is the prototypical eye-field / early neuroretinal-progenitor signature (PAX6/SOX2/LHX2/SIX3 with SFRP2, MAB21L1, ZIC2). Note the HDCA-assigned CL term in Supp Table 9 is CL:0002259 (neural retina progenitor cell); we re-map to CL:0002672 (retinal progenitor cell) here as a narrow match because the HDCA cluster is restricted to a PAX6+/LHX2+ neurogenic-committed eye-field state rather than the generic CL definition.

## Location and developmental position

HDCA spatial and molecular profiling places this population in the **early embryonic retina at first-trimester stages**, prior to the elaboration of differentiated retinal cell types. The HDCA paper describes the embryonic retina at this stage as already expressing early neurogenic and fate-specifying genes:

> embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone

(Webb et al., 2026). RETINAL_NEURAL_PROGENITOR sits transcriptionally upstream of these ATOH7+/PRDM13+ neurogenic transition states — i.e. it is the PAX6/SOX2/LHX2/SIX3 multipotent retinal-progenitor pool from which the ATOH7+ T1 neurogenic transition (and downstream RGC, amacrine, horizontal, photoreceptor lineages) emerges.

## Relationship to Sridhar 2020 progenitor populations

Sridhar et al. (2020) characterised human fetal retina at FD59, FD82 and FD125 and consistently identify a SOX2+/PAX6+ progenitor pool in the neuroblast layer:

> The two predominant cell types in the retina at this stage are retinal progenitors in the neuroblast layer (NBL; SOX2+/PAX6+) and retinal ganglion cells

(Sridhar et al., 2020, FD59). By FD82 their central-retinal progenitors are already producing later-born types:

> the progenitor cells in the central retina have started to 1646 Cell Reports 30, 1644–1659, February 4, 2020 generate later-born retinal cell types, including cells that express markers of bipolar cells

(Sridhar et al., 2020). The HDCA RETINAL_NEURAL_PROGENITOR cluster broadly aligns with this generic SOX2+/PAX6+ NBL progenitor pool, but it is captured at an **earlier, eye-field-flavoured stage** (strong SIX3, LHX2, ZIC2, MAB21L1, SFRP2 — markers more characteristic of the early optic vesicle / early neuroretina than of late peripheral progenitors). It is therefore not interchangeable with Sridhar's late-fetal "Progenitors" or with their ATOH7+ T1 neurogenic-transition state — the latter is captured by separate HDCA labels covering ATOH7+ neurogenic and lineage-committed intermediates. Sridhar 2020 is used here only as comparative context; the HDCA label itself was assigned independently of Sridhar's cells.

The HDCA paper also notes the relevance of TRH and thyroid-hormone signalling to downstream cone specification (Eldred et al., 2018):

> TRH signalling has been reported to specify cone subtypes in human retinal organoids74, and thus we provide further evidence in support of a role for TRH in the retina

(Webb et al., 2026), placing RETINAL_NEURAL_PROGENITOR as the upstream proliferative pool feeding such temporally regulated fate decisions.

## References

- Webb S et al. (2026). An integrated single cell and spatial omics atlas of human prenatal development. bioRxiv. DOI: 10.64898/2026.03.30.714220
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures. Cell Reports 30:1644-1659.e4. DOI: 10.1016/j.celrep.2020.01.007
- Eldred KC et al. (2018). Thyroid hormone signaling specifies cone subtypes in human retinal organoids. Science 362. DOI: 10.1126/science.aau6348

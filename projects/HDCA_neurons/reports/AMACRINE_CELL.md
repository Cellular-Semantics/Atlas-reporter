# AMACRINE_CELL — Retinal amacrine cell

Cell Ontology: [amacrine cell](http://purl.obolibrary.org/obo/CL_0000561) (CL:0000561, **exact match** — PAX6+/ISL1+/SIX3+ amacrine signature — CL exact match.)

Atlas: An integrated single cell and spatial omics atlas of human prenatal development (DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220))
Scope: embryonic/fetal (6-22 PCW)

## Summary

Amacrine cells are inner-retinal interneurons that modulate signal transfer between bipolar and retinal ganglion cells, and in most subtypes they are GABAergic or glycinergic. The HDCA AMACRINE_CELL cluster (n=78) expresses the canonical amacrine signature PAX6, ISL1, RORB, GAP43, SIX3, PRPH, ELAVL4 and MAB21L1 (HDCA Supp Table 9), consistent with committed post-mitotic amacrine identity. HDCA's main retinal paragraph attributes amacrine fate specification to PRDM13, citing Watanabe et al. (2015) for the mouse evidence that PRDM13 marks developing GABAergic / glycinergic amacrine neurons. As a data-provenance note, the cells in this cluster were contributed entirely by Sridhar et al. (2020), whose original author annotation "AC" (amacrine cell) was retained for 98.7% of cells when integrated into the HDCA v2 atlas.

## HDCA atlas evidence

**Cell count:** 78 cells. HDCA classifies this cluster as `broad_celltype = AUDIOVISUAL_NEURONAL`, `systems = AUDIOVISUAL_SYSTEM`.

### HDCA paper text

HDCA's main retina paragraph specifies the amacrine cell determinant:

> "embryonic retina was characterised by expression of ATOH7, required for retinal ganglion cell (RGC) development71; PRDM13, which specifies amacrine cell fate in mouse72; GADD45A, which characterises early neurogenic cells in mouse retina73; and TRH, which encodes thyrotropin releasing hormone"
>
> — Webb et al. (2026), HDCA

HDCA cites Watanabe et al. (2015) — ref [72] — for PRDM13 in amacrine subtype specification:

> "the Prdm13 transcriptional regulator is specifically expressed in developing and mature amacrine cells in the mouse retina. Most Prdm13-positive amacrine cells are Calbindin- and Calretinin-positive GABAergic or glycinergic neurons."
>
> — Watanabe et al. (2015)

## Markers

### HDCA Supplementary Table 9 signature

> "PAX6,ISL1,RORB,GAP43,SIX3,PRPH,ELAVL4,MAB21L1,STMN2,CRABP1,RTN1,SNCG,SNCA,INA,MTRNR2L1,SYT4,SCG5,NHLH2,MIAT,STMN4"
>
> — Webb et al. (2026), HDCA Supplementary Table 9

Of the signature genes, PAX6 and SIX3 are pan-retinal/eye-field transcription factors required for retinal patterning; ISL1 is a LIM-homeodomain factor active in committed amacrine and ganglion-cell lineages; GAP43, STMN2, RTN1, SNCG and INA mark neurite-extending post-mitotic neurons; and PRPH (peripherin) is a neuronal intermediate filament. The same combination of early post-mitotic neuronal markers (NEFM, GAP43, STMN2, ISL1, PRPH, ELAVL3/4) recurs across developing peripheral neurons, as noted by Kameneva et al. (2021) in the sympathoblast context:

> "Jansky et al. used NEFM,GAP43,STMN2,ISL1, and ALK at early stages to identify sympathoblasts ... Kameneva et al. also added PRPH, ELAVL3, ELAVL4, PHOX2B, and HAND2"
>
> — Kameneva et al. (2021)

### Top differentially expressed genes (HDCA Supp Table 16)

| Gene | logFC | padj |
|---|--:|--:|
| **CALM2** | 3.34 | 2.0e-42 |
| **MLLT11** | 4.59 | 2.0e-42 |
| **STMN2** | 5.65 | 4.4e-39 |
| **CCNI** | 2.57 | 1.0e-37 |
| **TUBB2B** | 4.38 | 1.4e-37 |
| **CRABP1** | 5.90 | 6.7e-36 |
| **MARCKSL1** | 2.45 | 9.7e-34 |
| **GAP43** | 5.07 | 6.0e-33 |
| **RTN1** | 4.70 | 6.5e-33 |
| **PCSK1N** | 4.39 | 8.0e-32 |
| **PAX6** | 5.44 | 1.3e-31 |
| **NSG1** | 4.31 | 1.4e-31 |
| **SNCG** | 4.77 | 3.1e-24 |

CRABP1, STMN2, GAP43 and TUBB2B are all consistent with an actively differentiating, neurite-extending post-mitotic neuron. PAX6 appearing as a top DEG matches the canonical PAX6+ amacrine identity.

## Location

Embryonic / fetal human retina, 6–22 post-conceptional weeks. HDCA places amacrine cells within the broader `AUDIOVISUAL_NEURONAL` compartment of the `AUDIOVISUAL_SYSTEM`, alongside other retinal cell types (photoreceptors, bipolars, retinal ganglion cells, horizontal cells and transitional T1/T2/T3 progenitor states). Within HDCA v2 the AMACRINE_CELL cluster (n=78) is contributed entirely by Sridhar et al. (2020):

> "AMACRINE_CELL (n=78 cells): 100% from Sridhar_et_al_2020_CellPress; 98.7% of cells carried the original author label "AC" (amacrine cell). No HDCA whole-embryo cells contribute to this cluster."
>
> — HDCA v2 label provenance cross-tab (Sridhar et al., 2020 source data)

This is a neutral data-provenance statement: the underlying tissue is human fetal retina sampled by Sridhar et al. (2020), and HDCA's harmonised label "AMACRINE_CELL" maps directly onto Sridhar's original "AC" annotation.

## Function

Amacrine cells are inner-retinal interneurons that shape retinal output via GABAergic and glycinergic inhibition of bipolar and ganglion cells. The functional identity in HDCA's cluster is established transcriptionally (via the PAX6/ISL1/SIX3/PRPH signature) rather than morphologically, so the inferences below are anchored to the cited literature:

- **Amacrine fate specification.** PRDM13 is the canonical amacrine fate determinant in mouse retina and marks the inhibitory (GABAergic / glycinergic) subset (Watanabe et al., 2015) — see quote above. HDCA endorses this assignment in its main retina paragraph (Webb et al., 2026).
- **Co-developmental context.** HDCA's retinal section places amacrine specification within the same window as ATOH7-dependent retinal ganglion cell birth (Ghiasvand et al., 2011) and GADD45A-marked early neurogenic states; this is part of the broader retinal neurogenic sequence described in the HDCA paper.

## Structure / Morphology

No morphological evidence is reported in the traversed literature for this HDCA cluster — identity is established transcriptionally only.

## References

- Webb S et al. (2026). "An integrated single cell and spatial omics atlas of human prenatal development". *bioRxiv*. DOI: [10.64898/2026.03.30.714220](https://doi.org/10.64898/2026.03.30.714220)
- Watanabe S et al. (2015). "Prdm13 Regulates Subtype Specification of Retinal Amacrine Interneurons and Modulates Visual Sensitivity". *J Neurosci 35*. DOI: [10.1523/JNEUROSCI.0089-15.2015](https://doi.org/10.1523/JNEUROSCI.0089-15.2015)
- Sridhar A, Hoshino A, Finkbeiner CR, et al. (2020). "Single-Cell Transcriptomic Comparison of Human Fetal Retina, hPSC-Derived Retinal Organoids, and Long-Term Retinal Cultures". *Cell Reports 30:1644-1659.e4*. DOI: [10.1016/j.celrep.2020.01.007](https://doi.org/10.1016/j.celrep.2020.01.007)
- Ghiasvand NM et al. (2011). "Deletion of a remote enhancer near ATOH7 disrupts retinal neurogenesis, causing NCRNA disease". *Nat Neurosci 14*. DOI: [10.1038/nn.2776](https://doi.org/10.1038/nn.2776)
- Kameneva P et al. (2021). "Single-cell transcriptomics of human embryos identifies multiple sympathoblast lineages with potential implications for neuroblastoma origin". *Nat Genet 53*. DOI: [10.1038/s41588-021-00818-x](https://doi.org/10.1038/s41588-021-00818-x)

## Source-of-label note

The AMACRINE_CELL cluster as it appears in HDCA v2 is contributed in its entirety (n=78, 100%) by Sridhar et al. (2020), with HDCA retaining Sridhar's original "AC" author annotation for 98.7% of cells. The HDCA paper text and HDCA Supplementary Tables 9 and 16 provide the harmonised marker signature and per-cluster DEGs used here; the inhibitory-amacrine biology is anchored to the literature HDCA cites (Watanabe et al., 2015) plus the Sridhar et al. (2020) primary source.

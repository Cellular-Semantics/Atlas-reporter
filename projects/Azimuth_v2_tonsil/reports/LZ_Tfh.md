# Germinal Center Light Zone T Follicular Helper Cell

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (germinal center light zone)
Cell Ontology: [germinal center T cell](http://purl.obolibrary.org/obo/CL_0009062) (CL:0009062, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3680

## Summary

The Azimuth human_tonsil_v2 fine label "light zone, germinal center" corresponds
to a T follicular helper (Tfh) cell positioned in the germinal center (GC) light
zone of the adult palatine tonsil (King et al., 2021). GC-Tfh cells are CD4 T
cells defined by high surface expression of CXCR5 and PD-1 together with the
transcription factor BCL6, and they reside in the germinal center where they
deliver survival and selection signals to GC B cells (Chu & Neelapu, 2015). Their
defining role is executed in the light zone, where centrocytes present
FDC-captured antigen and are selected through recognition by Tfh cells (Jing et
al., 2022; Kennedy et al., 2020). In human tonsil, the CXCR5-high, PD-1-high
protein phenotype specifically marks the mature GC-Tfh population (Bracey et al.,
2026; Ribeiro et al., 2025).

## Markers

The canonical Tfh phenotype combines surface receptors with an intracellular
transcription factor. Chu & Neelapu (2015) summarise this composite identity:

> "Follicular helper T cells (Tfh, CXCR5hiPDhiBcl-6+CD4+) that reside in GC serve as specialized B helper T cells and provide survival and selection signals to GC B cells."
>
> — Chu & Neelapu (2015)

- **CXCR5** — a cell-surface chemokine receptor (protein marker). It is one of
  the two established markers of Tfh maturation in human tonsil and, together
  with PD-1, distinguishes GC-Tfh from non-Tfh and pre-Tfh states (Bracey et
  al., 2026). CXCR5 directs follicular positioning by responding to CXCL13.
- **PD-1 (PDCD1)** — a cell-surface receptor (protein marker). High PD-1 surface
  expression specifically identifies the mature GC-Tfh population. Bracey et al.
  (2026) show marker expression measured at the protein level by intracellular
  cytokine staining / flow cytometry:

  > "using CXCR5 and PD-1 as previously established markers of Tfh cell maturation (Figure S3f). 7,35 CXCL13 expression was restricted to the CXCR5 + PD-1 hi GC-Tfh population and was absent from non-Tfh (CXCR5 -), pre-Tfh (CXCR5 + PD-1 lo ), and CXCR5 + PD-1 mid Tfh subsets (Figure 3h)."
  >
  > — Bracey et al. (2026)

- **BCL6 (Bcl-6)** — the master transcription factor of the Tfh lineage,
  detected as intracellular protein / transcript rather than as a surface
  marker. It is part of the canonical CXCR5hi PD-1hi Bcl-6+ CD4+ definition (Chu
  & Neelapu, 2015).
- **ICOS** — a surface co-stimulatory receptor. In human tonsil, ICOS and PD-1
  are activation markers characteristic of the most mature Tfh cells within the
  germinal center (Ribeiro et al., 2025):

  > "Within the cell subsets defined as T FH and T FR , we explored the presence of the activation markers ICOS and PD-1 known to be characteristic of the most mature cells within the GC (17) (Fig. 1A)."
  >
  > — Ribeiro et al. (2025)

Protein-vs-transcript note: CXCR5, PD-1 and ICOS are reported here as
cell-surface **proteins** (flow cytometry / immunostaining), whereas BCL6 is an
intracellular **transcription factor** typically read out as transcript or
intracellular protein. In the atlas single-cell data these correspond to the
transcripts *CXCR5*, *PDCD1*, *ICOS* and *BCL6*.

## Location

This cell type is defined by its position in the germinal center light zone. The
germinal center is spatially partitioned, and the light zone is the compartment
where selection occurs (Jing et al., 2022):

> "GCs are divided micro-anatomically into the dark zone where antigen-activated B cells proliferate and mutate their BCR genes, and the light zone (LZ) where they bind antigens that are captured and presented by follicular dendritic cells (FDC) followed by selection by T follicular helper (TFH) cell recognition of cognate peptide-loaded major histocompatibility complex class II (pMHCII) (De Silva and Klein, 2015)."
>
> — Jing et al. (2022)

Kennedy et al. (2020) localise the Tfh help interaction to the light-zone
compartment, where centrocytes contact FDCs and Tfh cells:

> "The LZ contains more sparse populations of CD83 + B cells that capture antigen from follicular dendritic cells (FDCs) and receive help from cognate T follicular helper (T FH ) cells 4 ."
>
> — Kennedy et al. (2020)

In this atlas the cells are sampled from adult human palatine tonsil, a highly
active secondary lymphoid organ (King et al., 2021).

## Function

The core function of the light-zone GC-Tfh cell is to select and help
centrocytes during affinity maturation. Selection is based on the B cell's
competency to present captured antigen back to the Tfh cell (Kennedy et al.,
2020):

> "B cells in the LZ are selected based on their competency to present antigen to TFH cells 5,6 more so than B cell antigen receptor (BCR) signal strength 7 ."
>
> — Kennedy et al. (2020)

Mechanistically, affinity selection in the light zone reflects a competition
between B-cell engagement of Tfh cells for costimulation and loss of B cells from
the compartment (Krishna & Bachman, 2016):

> "affinity selection of antigen bound B cells in the light zone is due to a competition between the binding of B cells to Tfh cells and loss of B cells from the GC light zone, either due to apoptosis, or due to a return of B cells to the GC dark zone."
>
> — Krishna & Bachman (2016)

Through these selection and help signals, GC-Tfh cells provide the survival and
selection cues that sustain the germinal center reaction (Chu & Neelapu, 2015),
driving high-affinity antibody output and B-cell memory.

## Structure / Morphology

No evidence found in traversed literature.

## References

- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Chu F, Neelapu S (2015). "CXCR5+CD8+ T cells are localized in B cell follicles and germinal centers and exhibit regulatory and anti-tumor function". *Journal for Immunotherapy of Cancer*. DOI: [10.1186/2051-1426-3-S2-P321](https://doi.org/10.1186/2051-1426-3-S2-P321)
- Jing Z et al. (2022). "Germinal center expansion but not plasmablast differentiation is proportional to peptide-MHCII density via CD40-CD40L signaling strength". *Cell Reports*. DOI: [10.1016/j.celrep.2022.110763](https://doi.org/10.1016/j.celrep.2022.110763)
- Kennedy DE et al. (2020). "Novel specialized cell state and spatial compartments within the germinal center". *Nature Immunology*. DOI: [10.1038/s41590-020-0660-2](https://doi.org/10.1038/s41590-020-0660-2)
- Bracey NA et al. (2026). "Aging restricts maturation of CXCL13+ T follicular helper cells in human immunity". *bioRxiv*. DOI: [10.64898/2026.04.03.715992](https://doi.org/10.64898/2026.04.03.715992)
- Ribeiro F et al. (2025). "PD-1 and ICOS are coexpressed in T follicular helper cells but define three stages of maturation of T follicular regulatory cells". *Science Advances*. DOI: [10.1126/sciadv.adt8901](https://doi.org/10.1126/sciadv.adt8901)
- Krishna V, Bachman K (2016). "A mechanism of T cell dependent selection of antigen engaged Germinal Center B cells". *PLoS ONE*. DOI: [10.1371/journal.pone.0200241](https://doi.org/10.1371/journal.pone.0200241)

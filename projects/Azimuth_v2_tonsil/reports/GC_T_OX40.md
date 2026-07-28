# OX40+ Germinal Center T Cell (GC-Tfh) in Human Tonsil

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (germinal center)
Cell Ontology: [germinal center T cell](http://purl.obolibrary.org/obo/CL_0009062) (CL:0009062, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3670

## Summary

The Azimuth `human_tonsil_v2` fine label "OX40+" denotes a germinal-center T
cell defined by expression of OX40 — the protein product of *TNFRSF4* (CD134),
a costimulatory member of the TNF-receptor superfamily. In tonsil, OX40 is
expressed on germinal-center-localised T follicular helper (GC-Tfh) cells,
the CD4+ subset that coordinates the germinal center (GC) reaction and provides
help to GC B cells (Fu et al., 2021; Dubensky et al., 2025). These cells are
fundamental for B cell selection and antibody maturation in germinal centers
(Brenna et al., 2020), and OX40/OX40L costimulation both drives their
differentiation and amplifies their capacity to help B cells (Fu et al., 2021;
Tahiliani et al., 2016). OX40 itself is detected principally as a cell-surface
protein by flow cytometry and imaging, whereas the broader GC-Tfh transcriptional
programme (e.g. *BCL6*, *GNG4*) is defined at the transcript level with protein
confirmation for selected markers.

## Markers

**OX40 / TNFRSF4 (CD134) — the defining marker (protein).** OX40 is a
costimulatory TNF-receptor that is detected at the cell-surface protein level.
In vivo work shows OX40 protein is expressed on Tfh cells positioned in and
around the germinal center:

> "In this study, with vaccinia virus infection in mice, we show that OX40 was expressed on Tfh cells that accumulated at the T/B borders in the white pulp of the spleen and that OX40-dependent signals directly shaped the magnitude and quality of the their response to viral Ags."
>
> — Tahiliani et al. (2016)

OX40 is co-expressed with the inducible costimulator ICOS on GC-associated Tfh:

> "Interestingly, OX40 was coexpressed with ICOS on Tfh cells in and around the GC, and ICOS–ICOSL interactions were similarly crucial at late times for maintenance of the Tfh and GC B cells."
>
> — Tahiliani et al. (2016)

**Canonical GC-Tfh surface markers (protein).** Beyond OX40, the tonsillar
GC-Tfh subset is conventionally gated by the chemokine receptor CXCR5 and the
inhibitory receptor PD-1 (both surface proteins), which distinguish GC-Tfh from
non-Tfh CD4+ cells. Yamashita et al. (2016) define GC-Tfh by the surface
phenotype and contrast them with the non-Tfh gate:

> "As assessed by quantitative RT-PCR analysis, the transcription levels of Bob1 were significantly higher in GC-Tfh cells than in non-Tfh cells (CD3 + CD4 + CXCR5 − PD-1 − ) and thymic CD4 + T cells in contrast to B-cell subsets including naïve, GC, and memory B cells of the tonsils (Fig. 1C and Supporting Information Fig. 2)."
>
> — Yamashita et al. (2016)

**Transcription factor BCL6 (transcript/protein).** The Tfh master transcription
factor BCL6 marks GC-resident CD4+ T cells; Yamashita et al. (2016) confirmed its
protein co-expression in situ:

> "Immunohistochemistry of tonsillar tissues also demonstrated that Bcl-6 + Bob1 + CD4 + cells were mainly present within GCs, and they were probably GC-Tfh cells (Fig. 1F)."
>
> — Yamashita et al. (2016)

**CD57 (protein) — GC-Th subset marker.** In human tonsil, the surface protein
CD57 marks CD4+ T cells localised to germinal centers:

> "As reported previously [12,19,28,29], most CD57 + CD4 + T cells are located in germinal centers surrounded by IgD + naïve B cells (Fig. 1)."
>
> — Kim et al. (2005)

**GNG4 (transcript + protein) — GC-positioning marker.** More recent multimodal
work identifies GNG4 as a marker of activated, GC-positioned Tfh, with evidence
at both mRNA and protein level:

> "Tfh with a GC-like phenotype exhibited markedly increased chromatin accessibility and both mRNA and protein expression of G protein subunit gamma 4 (GNG4)."
>
> — Dubensky et al. (2025)

Marker evidence status summary: OX40/TNFRSF4, CXCR5, PD-1 and CD57 are
established as surface-protein markers (flow cytometry / immunohistology); BCL6
is a transcription factor confirmed at the protein level in situ; GNG4 is
supported at both transcript and protein level.

## Location

OX40+ GC-Tfh cells reside within the germinal center of the palatine tonsil.
In human tonsil, the CD4+ GC-T helper population is found inside the B-cell
follicle / germinal center rather than the interfollicular T-cell zone:

> "Therefore, CD57, CD69 and CD4 are useful markers to identify CD57 + GC-Th cells and other T cell subsets differentially localized in tonsils: CD4 + CD57 + cells (mainly in GC), CD4 + CD57 -CD69 + cells (mainly in GC and a minor proportion in IFA), and CD4 + CD57 -CD69 -cells (mainly in IFA)."
>
> — Kim et al. (2005)

OX40-expressing Tfh specifically accumulate at the T/B border and within the GC
niche (Tahiliani et al., 2016, quoted above). Spatial single-cell analysis of
human tonsil further confirms that activated, GC-positioned Tfh states occupy
spatially demarcated germinal-center compartments:

> "In tonsil, single-cell spatial transcriptomics defined GNG4 expression as a distinguishing feature of activated Tfh states within spatially demarcated GC compartments, with greater specificity than conventionally GC-associated features such as BCL6, TOX2, and S1PR2."
>
> — Dubensky et al. (2025)

Tonsillar Tfh location is not merely descriptive: gene expression is tied to
position, with some bona fide follicular subsets restricted to the tonsil GC
environment:

> "Most subsets of CD4+ T-follicular helper cells occur in blood and tonsils, but location enforces specific gene expression."
>
> — Liang et al. (2024)

## Function

The core function of the OX40+ GC-Tfh cell is to provide cognate help to
germinal-center B cells, driving affinity maturation and antibody responses:

> "T follicular helper (Tfh) cells are fundamental for B cell selection and antibody maturation in germinal centers."
>
> — Brenna et al. (2020)

> "CD4 T follicular helper (Tfh) cells coordinate humoral immune responses within germinal centers (GC) of lymphoid tissue."
>
> — Dubensky et al. (2025)

**Role of OX40 costimulation.** OX40 (TNFRSF4) signalling is not just a passive
marker but an active driver of the Tfh programme. OX40/OX40L engagement promotes
Tfh differentiation, sustains survival, and enhances B-cell helper capacity:

> "Recent data have shown that OX40/OX40L signaling can not only promote Tfh cell differentiation and maintain cell survival, but also enhance the helper function of Tfh for B cells."
>
> — Fu et al. (2021)

> "Given that OX40 signaling is critical for costimulating T cell activation and function, its roles in regulating Tfh cells have attracted widespread attention."
>
> — Fu et al. (2021)

Functionally, loss of OX40 signalling degrades the downstream GC output —
impairing GC B-cell differentiation, plasma-cell generation and antibody
production — and OX40 works cooperatively with ICOS to sustain the response:

> "OX40 deficiency in Tfh cells profoundly impaired the acquisition of germinal center (GC) B cell phenotype, plasma cell generation, and virus-specific Ab responses."
>
> — Tahiliani et al. (2016)

> "Thus, OX40 and ICOS act in a cooperative, nonredundant manner to maximize and prolong the Tfh response that is generated after acute virus infection."
>
> — Tahiliani et al. (2016)

The subset also sits within a heterogeneous tonsillar Tfh landscape, with
several follicular gene-expression programmes seen only in the tonsil:

> "Three further subsets of TFH cells, however, with bona fide T-follicular gene expression patterns, are exclusively found in tonsils."
>
> — Liang et al. (2024)

## Structure / Morphology

No evidence found in traversed literature.

## References

- King HW et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Fu N et al. (2021). "The OX40/OX40L Axis Regulates T Follicular Helper Cell Differentiation: Implications for Autoimmune Diseases". *Frontiers in Immunology*. DOI: [10.3389/fimmu.2021.670637](https://doi.org/10.3389/fimmu.2021.670637)
- Tahiliani V et al. (2016). "OX40 Co-operates with ICOS to Amplify Follicular T Helper Cell Development and Germinal Center Reactions During Infection". *Journal of Immunology*. DOI: [10.4049/jimmunol.1601356](https://doi.org/10.4049/jimmunol.1601356)
- Kim JR et al. (2005). "Human CD57+ germinal center-T cells are the major helpers for GC-B cells and induce class switch recombination". *BMC Immunology*. DOI: [10.1186/1471-2172-6-3](https://doi.org/10.1186/1471-2172-6-3)
- Dubensky SB et al. (2025). "Multimodal analysis defines GNG4 as a distinguishing feature of germinal center-positioned CD4 T follicular helper cells in humans". *bioRxiv*. DOI: [10.64898/2025.12.10.693235](https://doi.org/10.64898/2025.12.10.693235)
- Brenna E et al. (2020). "CD4+ T Follicular Helper Cells in Human Tonsils and Blood Are Clonally Convergent but Divergent from Non-Tfh CD4+ Cells". *Cell Reports*. DOI: [10.1016/j.celrep.2019.12.016](https://doi.org/10.1016/j.celrep.2019.12.016)
- Yamashita K et al. (2016). "Bob1 limits cellular frequency of T-follicular helper cells". *European Journal of Immunology*. DOI: [10.1002/eji.201545499](https://doi.org/10.1002/eji.201545499)
- Liang C et al. (2024). "Oligoclonal CD4+CXCR5+ T cells with a cytotoxic phenotype appear in tonsils and blood". *Communications Biology*. DOI: [10.1038/s42003-024-06563-1](https://doi.org/10.1038/s42003-024-06563-1)

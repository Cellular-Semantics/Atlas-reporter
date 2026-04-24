# Lymphoid progenitor
Atlas: A prenatal skin atlas reveals immune regulation of human skin morphogenesis
Scope: fetal
Cell Ontology: [common lymphoid progenitor](http://purl.obolibrary.org/obo/CL_0000051) (CL:0000051, broad match — no exact CL term)

## CL Mapping

| Field | Value |
|-------|-------|
| CL term | common lymphoid progenitor |
| CL ID | CL:0000051 |
| CL definition | A lymphoid committed progenitor cell that has the potential to give rise to T cells, B cells, natural killer cells, and innate lymphoid cells. |
| Match type | skos:broadMatch |
| Confidence | medium |

**Justification:** The 'Lymphoid progenitor' cluster in the fetal skin atlas represents a broadly annotated lymphoid precursor population identified by scRNA-seq. CL:0000051 'common lymphoid progenitor' is the broadest available CL term for lymphoid-committed precursors, encompassing the potential to give rise to T cells, B cells, NK cells, and ILCs. The atlas label does not distinguish between CLP, ILC precursor (ILCP), and early lymphoid progenitor stages, so a broad match to the common lymphoid progenitor is most appropriate. No new term is required.

## Summary

Lymphoid progenitor is a lymphoid precursor population identified in fetal human skin (7–17 PCW) by the Gopee et al. (2024) prenatal skin atlas. Lymphocyte precursors were detected in first-trimester skin by scRNA-seq and were found to be more abundant in embryonic than fetal skin:

> "s well as ILC precursors, lymphocyte precursors were also identified in first-trimester skin by scRNAseq, where they were found to be more abundant in embryonic than fetal skin."
> — Botting and Haniffa (2020), *Immunology*

ILC precursors — a subset of lymphoid progenitors — were among the earliest lymphoid cells detected in fetal skin:

> "While T-cells were only detected in fetal skin after thymic production, natural killer (NK) cells and innate lymphoid cell (ILC) precursors have been identified in skin as early as 8 PCW."
> — Botting and Haniffa (2020), *Immunology*

The fetal dermis appears to support in situ lymphoid differentiation, with multiple progenitor lineages co-detected alongside their progeny:

> "The presence of megakaryocyte-erythrocyte-mast cell progenitors (MEMPs), lymphocyte precursors, B-cell progenitors, ILC precursors and their progeny 41 indicates differentiation of these lineages may be supported within developing dermis."
> — Botting and Haniffa (2020), *Immunology*

The temporal pattern of lymphoid development in fetal skin mirrors the broader programme of prenatal immune system assembly:

> "Innate immune cells, such as macrophages and innate lymphoid cells (ILCs), were present from early gestation, whereas B cells and T cells emerged later, accompanying thymus, bone marrow and spleen formation from around 10 PCW"
> — Gopee et al. (2024), *Nature*

## Markers

Lymphoid progenitors in fetal skin are expected to express canonical lymphoid commitment markers including:

- **IL7R (CD127)** — interleukin-7 receptor; marks lymphoid-committed progenitors including CLPs and ILC precursors
- **FLT3 (CD135)** — expressed on multipotent and lymphoid progenitors
- **RAG1/RAG2** — recombinase genes active in lymphoid progenitors committing to B or T cell fates
- **ID2** — transcription factor expressed in ILC precursors
- **GATA3** — expressed in early ILC and T cell precursors

Specific differentially expressed marker genes for the lymphoid progenitor cluster in fetal skin are provided in Supplementary Table 3 of Gopee et al. (2024).

## Location

Lymphoid progenitor cells are located in the dermal immune compartment of fetal skin during prenatal development (7–17 PCW), with greatest abundance in embryonic (first-trimester) compared to later fetal skin. They were isolated as CD45+ immune cells by FACS prior to scRNA-seq. Their presence without the earliest multipotent progenitors (HSC/MPPs) suggests they represent committed lymphoid precursors seeded from the circulation rather than local de novo haematopoiesis.

## Function

Lymphoid progenitors in fetal skin are poised to generate ILCs, NK cells, and B lymphocytes within the developing dermis. Their greater abundance in embryonic compared to fetal skin suggests an early window of lymphoid seeding and in situ differentiation. The detection of ILC precursors and mature ILC1/NK cells alongside lymphoid progenitors indicates that at least part of the fetal skin innate lymphoid compartment arises through local differentiation.

ILC precursors in first-trimester skin may give rise to the ILC1, ILC2, and ILC3 subsets found in later fetal and adult skin. The lymphoid progenitor cluster may therefore represent a mixed population of CLPs and committed ILC precursors captured at different points along this differentiation trajectory.

## Structure / Morphology

Lymphoid progenitors are small lymphoid cells with a large nucleus and scant cytoplasm. No specific ultrastructural data for fetal skin lymphoid progenitors are reported in the atlas text. At the scRNA-seq level, the lymphoid progenitor cluster is defined by transcriptional profiles rather than by morphological features.

## References

- Gopee, N. et al. (2024). "A prenatal skin atlas reveals immune regulation of human skin morphogenesis." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Botting, R. and Haniffa, M. (2020). "The developing immune network in human prenatal skin." *Immunology*. DOI: [10.1111/imm.13192](https://doi.org/10.1111/imm.13192)
- Popescu, D.M. et al. (2019). "Decoding human fetal liver haematopoiesis." *Nature*. DOI: [10.1038/s41586-019-1652-y](https://doi.org/10.1038/s41586-019-1652-y)

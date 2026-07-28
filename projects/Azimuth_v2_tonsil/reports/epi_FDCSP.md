# FDCSP Epithelium of the Human Palatine Tonsil

Atlas: An atlas of cells in the human tonsil (Massoni-Badosa et al., 2024) — Azimuth human_tonsil_v2 reference (DOI: 10.1016/j.immuni.2024.01.006)
Scope: adult
Tissue context: palatine tonsil crypt epithelium (FDCSP-expressing subpopulation)
Cell Ontology: [keratinocyte](http://purl.obolibrary.org/obo/CL_0000312) (CL:0000312, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3683

> **Curator note (label correction):** In the working cl_map this cluster (order 231) is recorded as "VEGFA+". This is a misnomer — VEGFA is *not* an atlas-defined marker of this cluster. The Massoni-Badosa et al. (2024) atlas defines the cluster by **FDCSP** expression and names it "FDCSP epithelium", with **KRTDAP** consistent with its oral-mucosa/keratinocyte identity. "VEGFA+" should be treated as an alias/mislabel for the FDCSP epithelium cluster and corrected.

## Summary

FDCSP epithelium is a specialised epithelial subpopulation of the adult human palatine tonsil, defined in the tonsil cell atlas of Massoni-Badosa et al. (2024) — the Azimuth `human_tonsil_v2` reference. Within the epithelial compartment the authors resolved three clusters overlapping the keratinocyte populations of the oral mucosa, one of which was distinguished by expression of *FDCSP* (follicular dendritic cell secreted protein) and annotated "FDCSP epithelium" (Massoni-Badosa et al., 2024). The cluster is a keratinocyte-type epithelial population, consistent with expression of the keratinocyte-differentiation marker *KRTDAP* (Su et al., 2021). Biologically it links the tonsillar epithelium to the leukocyte-infiltrated crypts, where *FDCSP* — a secreted immune-modulatory protein originally identified in follicular dendritic cells of human tonsils (Marshall et al., 2002; Lorenzi et al., 2017) — had previously been described but not assigned to a defined cell population.

## Markers

The two atlas markers for this population are reported at the **transcript level** (scRNA-seq / multiome), not protein level.

- **FDCSP** (follicular dendritic cell secreted protein; c4orf7) — the cluster-defining marker. The atlas identified one epithelial cluster expressing FDCSP and named it accordingly:

  > "One of these clusters expressed FDCSP (FDCSP epithelium)."
  >
  > — Massoni-Badosa et al. (2024)

  FDCSP is a small secreted immune protein. Across normal human tissues it is most abundant in tonsil and gingival epithelium (Wu et al., 2022):

  > "FDCSP showed the highest expression levels in tonsil tissue and gingival epithelium, with expression levels larger than 5 (raw data were downloaded from BioGPS)."
  >
  > — Wu et al. (2022)

  In epithelial tissue elsewhere, FDCSP marks a basal rather than luminal epithelial subpopulation, reinforcing its use here as a marker of a *specific* epithelial subpopulation (Lu et al., 2025):

  > "Single-cell transcriptome analysis demonstrated that FDCSP was predominantly highly expressed in basal cells but exhibited low expression in luminal epithelial cells."
  >
  > — Lu et al. (2025)

- **KRTDAP** (keratinocyte differentiation-associated protein) — consistent with the oral-mucosa / keratinocyte identity of the compartment. KRTDAP is a soluble regulator of keratinocyte differentiation (Su et al., 2021):

  > "KRTDAP acts as a soluble regulator of keratinocyte differentiation and serves a key role in embryonic skin morphogenesis (44)."
  >
  > — Su et al. (2021)

## Location

FDCSP epithelium is part of the tonsillar epithelial compartment, which in the atlas overlaps the keratinocyte populations of the oral mucosa:

> "In the epithelial compartment, we identified three clusters overlapping with the keratinocyte populations of the oral mucosa (Figures S6A-S6C)."
>
> — Massoni-Badosa et al. (2024)

The palatine tonsils are secondary lymphoid organs at the mucosal front line (Massoni-Badosa et al., 2024):

> "Palatine tonsils are secondary lymphoid organs representing the first line of immunological defense against inhaled or ingested pathogens."
>
> — Massoni-Badosa et al. (2024)

The FDCSP-expressing population is specifically associated with the tonsillar crypts. FDCSP had originally been reported in leukocyte-infiltrated crypts without a defined cellular source, a gap the atlas resolves by showing the signal comes from an epithelial subpopulation:

> "FDCSP was first described in FDC and in ''leukocyte-infiltrated tonsillar crypts,'' although the specific population within the crypts remained unknown."
>
> — Massoni-Badosa et al. (2024)

> "Here, we provide evidence that FDSCP-expressing cells represent a specific subpopulation of the tonsillar epithelium."
>
> — Massoni-Badosa et al. (2024)

## Function

The atlas does not assign a dedicated effector function to this epithelial cluster beyond its identity as a distinct FDCSP-expressing crypt-associated subpopulation. Functional context comes from the biology of its markers.

FDCSP itself is a secreted immune-modulatory protein. It was first isolated from human reactive tonsils and is expressed by B-cell-activating follicular dendritic cells (Lorenzi et al., 2017):

> "FDCSP, isolated in 2002 from human reactive tonsils, is specifically expressed by B-cell-activating-FDC [26]."
>
> — Lorenzi et al. (2017)

> "The few studies performed to understand the functions of this protein suggest that it can modulate B-cell immune response [26][27] and may have a role in autoimmune diseases [28][29]."
>
> — Lorenzi et al. (2017)

FDCSP is a secreted peptide that binds activated B cells and regulates antibody responses (Wu et al., 2022; Lu et al., 2025):

> "FDCSP specifically binds to activated B cells and functions as a regulator of antibody responses."
>
> — Wu et al. (2022)

> "FDCSP is a unique secreted peptide with a distinct expression pattern in the immune system and exhibits specific binding affinity to activated B cells."
>
> — Lu et al. (2025)

Its restriction largely to activated FDC-type cells underscores that its appearance in an epithelial compartment marks a specialised, immunologically engaged crypt epithelial niche (Wu et al., 2022):

> "FDCSP is expressed mostly by activated FDCs and TNF-alpha-activated FDC-like cell lines."
>
> — Wu et al. (2022)

The second marker, KRTDAP, points to a keratinocyte-differentiation programme, consistent with the population being a differentiated oral-mucosa-type epithelium rather than a mesenchymal or immune cell (Su et al., 2021).

## Structure / Morphology

No dedicated morphological description of the FDCSP epithelium cluster was found in the traversed literature. Its assignment to the tonsillar epithelial compartment overlapping oral-mucosa keratinocytes (Massoni-Badosa et al., 2024) and its keratinocyte-differentiation marker KRTDAP (Su et al., 2021) indicate a stratified squamous / keratinocyte-type epithelial morphology, but direct morphological evidence is not reported.

## References

- Massoni-Badosa R et al. (2024). "An atlas of cells in the human tonsil". *Immunity*. DOI: [10.1016/j.immuni.2024.01.006](https://doi.org/10.1016/j.immuni.2024.01.006)
- Marshall AJ et al. (2002). "FDC-SP, a Novel Secreted Protein Expressed by Follicular Dendritic Cells". *Journal of Immunology*. DOI: [10.4049/jimmunol.169.5.2381](https://doi.org/10.4049/jimmunol.169.5.2381)
- Wu Q et al. (2022). "FDCSP Is an Immune-Associated Prognostic Biomarker in HPV-Positive Head and Neck Squamous Carcinoma". *Biomolecules*. DOI: [10.3390/biom12101458](https://doi.org/10.3390/biom12101458)
- Lu X et al. (2025). "Multi-omics analysis identifies the unique high-FDCSP basal cells in triple-negative breast cancer". *Experimental Biology and Medicine*. DOI: [10.3389/ebm.2025.10632](https://doi.org/10.3389/ebm.2025.10632)
- Lorenzi L et al. (2017). "Identification of novel follicular dendritic cell sarcoma markers, FDCSP and SRGN, by whole transcriptome sequencing". *Oncotarget*. DOI: [10.18632/oncotarget.14864](https://doi.org/10.18632/oncotarget.14864)
- Su Y et al. (2021). "PSMC2, ORC5 and KRTDAP are specific biomarkers for HPV-negative head and neck squamous cell carcinoma". *Oncology Letters*. DOI: [10.3892/ol.2021.12550](https://doi.org/10.3892/ol.2021.12550)

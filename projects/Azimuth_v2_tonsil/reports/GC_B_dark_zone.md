# Dark Zone Germinal Center B Cell (Centroblast) of the Human Tonsil

Atlas: Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci (King et al., 2021) (DOI: 10.1126/sciimmunol.abh3768)
Scope: adult
Tissue context: palatine tonsil (germinal center dark zone)
Cell Ontology: [centroblast](http://purl.obolibrary.org/obo/CL_0009112) (CL:0009112, broad match — no exact CL term) — NTR: obophenotype/cell-ontology#3679

## Summary

The "dark zone" fine annotation in the Azimuth human_tonsil_v2 reference (King et al., 2021) corresponds to the germinal centre (GC) dark zone B cell, classically known as the **centroblast**. This is the proliferating, somatically-hypermutating compartment of the germinal centre reaction. In the canonical two-zone model of the germinal centre, GC B cells alternate between a dark zone state and a light zone state (Di et al., 2021; Kennedy et al., 2020). Dark zone cells are large, rapidly dividing blast cells that undergo immunoglobulin somatic hypermutation, and are distinguished at the protein level by a CXCR4-high, CD83-low, CD86-low surface phenotype together with high proliferative activity (Di et al., 2021; Stengel et al., 2019; Vora et al., 1998). Their progeny cease dividing, re-express surface immunoglobulin, and transition into the smaller light zone centrocytes that undergo antigen-based selection (Vora et al., 1998; Bannard et al., 2013).

**Centroblast equivalence:** Throughout the germinal-centre literature the terms "dark zone GC B cell" and "centroblast" are used interchangeably — the dark zone is the anatomical compartment and the centroblast is the cell it contains. Downstream Cell Ontology mapping should therefore treat "centroblast" as the equivalent concept for this label.

## Markers

The dark zone centroblast is defined by a well-established combination of surface (protein) and functional markers. Marker modality (protein vs transcript) is noted for each.

- **CXCR4 (protein, chemokine receptor — high).** CXCR4 is the canonical dark-zone surface marker. Di et al. (2021) describe the surface-phenotyping scheme that separates the two GC compartments:

  > "By surface phenotyping, cells in the two compartments can be distinguished based on CXCR4, CD83 and CD86 markers [20][21][22] , with light-zone cells being CXCR4 lo CD83 + CD86 + while dark-zone cells are CXCR4 + CD83 lo CD86 lo . GC cells cycle between the dark zone state and the light zone state. Dark zone cells are highly proliferative and undergo somatic hypermutation, which generates a range of affinities against antigens."
  >
  > — Di et al. (2021)

  Functionally, CXCR4 retains centroblasts in the dark zone through its ligand CXCL12 produced by dark-zone reticular/stromal cells (Stengel et al., 2019; Laidlaw & Cyster, 2020):

  > "CXCR4 not only marks dark zone centroblasts, but also facilitates the interaction with CXCL12 on reticular cells resulting in their localization in the dark zone (71,72)."
  >
  > — Stengel et al. (2019)

  Down-regulation of surface CXCR4 accompanies the exit of cells from the dark zone toward the light zone (Stewart et al., 2018), and CXCR4 signalling supports dark-zone proliferative capacity (Biajoux et al., 2016):

  > "dark zone centroblasts divide more rapidly than centrocytes (Gitlin et al., 2014;Victora et al., 2010), and proliferation is partly impaired in Cxcr4-deficient GC B cells (Bannard et al., 2013)."
  >
  > — Biajoux et al. (2016)

- **CD83 (protein — low).** CD83 is a light-zone marker; its low expression is diagnostic of dark zone identity. In human tonsil, CD83 is predominantly expressed on light-zone GC B cells (Ruffin et al., 2021):

  > "CD83 is also used to distinguish DZ and LZ in human and mice with expression being predominantly on LZ GC B cells 32,33 ."
  >
  > — Ruffin et al. (2021)

- **CD86 (protein — low).** CD86 low expression is part of the dark-zone surface signature, in contrast to CD86-high light-zone centrocytes (Di et al., 2021, quoted above).

- **AID / AICDA (AID protein; AICDA transcript — high).** The activation-induced cytidine deaminase that drives somatic hypermutation defines the dark-zone functional program. In human palatine tonsil, AID-positive centroblasts fill the dark zone (Steiniger et al., 2020), and this is the AID-dependent SHM compartment distinguished from the proliferation-focused "gray zone" (Kennedy et al., 2020):

  > "AID + cells filled the dark zone and tended to superficially extend around the light zone."
  >
  > — Steiniger et al. (2020)

  > "Clark and colleagues identify ‘gray zone’ cyclin B1+ B cell clusters as sites of ongoing cell proliferation, and these cells are distinct from dark zone B cells that undergo AID-dependent somatic hypermutation."
  >
  > — Kennedy et al. (2020)

- **Ki-67 / MKI67 (Ki-67 protein — positive).** Proliferation is a hallmark of the dark zone. In human tonsil, dark-zone AID+ centroblasts are overwhelmingly Ki-67 positive (Steiniger et al., 2020):

  > "The vast majority of these cells were also positive for CD20 and nearly all of them exhibited Ki-67 + nuclei."
  >
  > — Steiniger et al. (2020)

- **CD27 (protein — higher on DZ).** In human tonsil, CD27 surface expression is higher on dark-zone than light-zone GC B cells (Ruffin et al., 2021):

  > "CD27 expression was previously shown to be higher on DZ GC B cells in human tonsil 32 ."
  >
  > — Ruffin et al. (2021)

- **Surface immunoglobulin (protein — low).** Centroblasts express low levels of surface Ig while cycling in the dark zone (Vora et al., 1998):

  > "Mutations appear to be introduced in a stepwise manner into the V regions of the dark-zone centro- blast, which are in rapid cell cycle but express low levels of surface Ig (Liu et al., 1991)."
  >
  > — Vora et al. (1998)

## Location

The dark zone is one of the two histologically distinct compartments of the germinal centre, situated within B cell follicles of secondary lymphoid tissue — here, the palatine tonsil. It is anatomically and functionally polarised against the light zone (Kennedy et al., 2020):

> "In contrast to this complexity, GC B cells are canonically divided into two principal populations, dark zone (DZ) and light zone (LZ) cells."
>
> — Kennedy et al. (2020)

Localisation to the dark zone is enforced by the CXCR4–CXCL12 chemokine axis, with dark-zone stroma producing CXCL12 that retains CXCR4-high centroblasts (Laidlaw & Cyster, 2020; Stengel et al., 2019):

> "The compartment of the germinal centre in which B cells proliferate and undergo somatic hypermutation, which contains a network of stromal cells producing the CxCr4 ligand CxCL12."
>
> — Laidlaw & Cyster (2020)

In human palatine tonsil specifically, in situ imaging shows AID+ centroblasts filling the dark zone and extending around the light zone (Steiniger et al., 2020, quoted above).

## Function

### Somatic hypermutation

The defining function of the dark zone centroblast is immunoglobulin somatic hypermutation, which diversifies the antibody repertoire and generates the raw variation on which subsequent light-zone selection acts (Stengel et al., 2019; Stewart et al., 2018):

> "The germinal center can be divided into dark zone centroblasts, which are undergoing somatic hypermutation, and light zone centrocytes that are undergoing selection through association with antigen presenting cells and T FH cells."
>
> — Stengel et al. (2019)

> "Adaptive immunity involves the development of bespoke antibodies in germinal centers (GCs) through immunoglobulin somatic hypermutation (SHM) in GC dark zones (DZs) and clonal selection in light zones (LZs)."
>
> — Stewart et al. (2018)

### Proliferation and clonal expansion

The dark zone is the principal site of germinal-centre proliferation, sustaining the clonal expansion of selected B cells (Stengel et al., 2019; Vora et al., 1998):

> "Given that most germinal center proliferation occurs in the dark zone it may seem surprising that we did not observe reductions in germinal center B cell proliferation in the absence of Hdac3"
>
> — Stengel et al. (2019)

> "The dark zone consists of rapidly dividing blast cells called centroblasts."
>
> — Vora et al. (1998)

### Dark-zone quality control and cell-cycle checkpoint

Beyond mutation and division, the dark zone imposes a checkpoint: cells acquiring damaging BCR mutations are eliminated before light-zone entry, with apoptosis biased to a specific cell-cycle stage (Stewart et al., 2018):

> "Apoptosis of GC B cells in DZ occurs preferentially in the late G1 stage of cell cycle"
>
> — Stewart et al. (2018)

### Transition to the centrocyte / light-zone state

Dark-zone centroblasts are the upstream state in a dynamic, bidirectional cycle: their progeny exit the cell cycle and mature into light-zone centrocytes, which may recycle back to the dark zone (Bannard et al., 2013; Ci et al., 2008):

> "Germinal Center Centroblasts Transition to a Centrocyte Phenotype According to a Timed Program and Depend on the Dark Zone for Effective Selection"
>
> — Bannard et al. (2013)

> "The germinal center compartment is highly dynamic, and centroblasts eventually migrate to the more heterogeneous germinal center light zone region, which contains T cells, macrophages and follicular dendritic cells (FDCs)."
>
> — Ci et al. (2008)

## Structure / Morphology

Centroblasts are large, rapidly dividing blast cells; their differentiated light-zone progeny (centrocytes) are morphologically smaller and more dispersed within the dense follicular dendritic cell network (Vora et al., 1998):

> "The dark zone consists of rapidly dividing blast cells called centroblasts."
>
> — Vora et al. (1998)

> "The centrocytes are smaller and less densely packed than centroblasts, as they are separated by a dense FDC network."
>
> — Vora et al. (1998)

## References

- King HW, Wells KL, Shipony Z, et al. (2021). "Integrated single-cell transcriptomics and epigenomics reveals strong germinal center-associated etiology of autoimmune risk loci". *Science Immunology*. DOI: [10.1126/sciimmunol.abh3768](https://doi.org/10.1126/sciimmunol.abh3768)
- Di L, Liu B, Lyu Y, et al. (2021). "SHERRY2: A method for rapid and sensitive single cell RNA-seq". *bioRxiv (preprint)*. DOI: [10.1101/2021.12.25.474161](https://doi.org/10.1101/2021.12.25.474161)
- Stengel K, Bhaskara S, Wang J, et al. (2019). "Histone deacetylase 3 controls a transcriptional network required for B cell maturation". *Nucleic Acids Research*. DOI: [10.1093/nar/gkz816](https://doi.org/10.1093/nar/gkz816)
- Vora K, Ravetch J, Manser T. (1998). "Insights into the Mechanisms of Antibody-Affinity Maturation and the Generation of the Memory B-Cell Compartment Using Genetically Altered Mice". *Developmental Immunology*. DOI: [10.1155/1998/42595](https://doi.org/10.1155/1998/42595)
- Stewart I, Radtke D, Phillips B, McGowan S, Bannard O. (2018). "Germinal Center B Cells Replace Their Antigen Receptors in Dark Zones and Fail Light Zone Entry when Immunoglobulin Gene Mutations are Damaging". *Immunity*. DOI: [10.1016/j.immuni.2018.08.025](https://doi.org/10.1016/j.immuni.2018.08.025)
- Bannard O, Horton R, Allen CDC, An J, Nagasawa T, Cyster J. (2013). "Germinal Center Centroblasts Transition to a Centrocyte Phenotype According to a Timed Program and Depend on the Dark Zone for Effective Selection". *Immunity*. DOI: [10.1016/j.immuni.2013.08.038](https://doi.org/10.1016/j.immuni.2013.08.038)
- Kennedy DE, Okoreeh MK, Maienschein-Cline M, et al. (2020). "Novel specialized cell state and spatial compartments within the germinal center". *Nature Immunology*. DOI: [10.1038/s41590-020-0660-2](https://doi.org/10.1038/s41590-020-0660-2)
- Steiniger B, Raimer L, Ecke A, Stuck B, Cetin Y. (2020). "Plasma cells, plasmablasts, and AID+/CD30+ B lymphoblasts inside and outside germinal centres: details of the basal light zone and the outer zone in human palatine tonsils". *Histochemistry and Cell Biology*. DOI: [10.1007/s00418-020-01861-1](https://doi.org/10.1007/s00418-020-01861-1)
- Ruffin A, Cillo A, Tabib T, et al. (2021). "B cell signatures and tertiary lymphoid structures contribute to outcome in head and neck squamous cell carcinoma". *Nature Communications*. DOI: [10.1038/s41467-021-23355-x](https://doi.org/10.1038/s41467-021-23355-x)
- Laidlaw B, Cyster J. (2020). "Transcriptional regulation of memory B cell differentiation". *Nature Reviews Immunology*. DOI: [10.1038/s41577-020-00446-2](https://doi.org/10.1038/s41577-020-00446-2)
- Biajoux V, Natt J, Freitas C, et al. (2016). "Efficient Plasma Cell Differentiation and Trafficking Require Cxcr4 Desensitization". *Cell Reports*. DOI: [10.1016/j.celrep.2016.08.068](https://doi.org/10.1016/j.celrep.2016.08.068)
- Ci W, Polo J, Melnick A. (2008). "B-cell lymphoma 6 and the molecular pathogenesis of diffuse large B-cell lymphoma". *Current Opinion in Hematology*. DOI: [10.1097/MOH.0b013e328302c7df](https://doi.org/10.1097/MOH.0b013e328302c7df)

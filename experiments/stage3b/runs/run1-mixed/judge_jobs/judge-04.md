You are adjudicating answers to questions about cell types in one research
paper. For each case you are given: the question, the INTENDED answer (written
by a curator who read the paper), the READER's answer, and the quotes the reader
gave. **The quotes have already been verified as verbatim text from the context
the reader saw** — you do not need to check that.

Decide one verdict per case.

For cases marked `kind: present`:
  - `correct`     — the reader's answer conveys the intended answer. Wording,
                    ordering and level of detail may differ freely. A reader
                    using a different name for the same cell type is NOT wrong.
                    A partial answer that is accurate as far as it goes and
                    names the main point is correct.
  - `substituted` — the quote is real but does not support what the reader
                    claimed, OR the reader answered with a different claim than
                    the paper's. This is the important category: grounded but
                    not right.
  - `wrong`       — contradicts the intended answer.

For cases marked `kind: absent`:
  The paper says nothing about this cell type's structure or morphology. The
  reader was expected to decline but instead answered.
  - `correct`     — on reading it, the reader effectively declined: it says the
                    paper does not describe morphology, or its answer is about
                    location/function rather than morphology and it says so.
  - `overreach`   — it presented something as a structural or morphological
                    description when the paper offers none.

Where a case carries a `hazard` note, follow it. It records a distinction that
is easy to get backwards.

Return a JSON array, nothing else:

[{"arm": "...", "id": "...", "verdict": "correct", "why": "one short sentence"}]


# Cases (batch 4)


## arm: asta-sep | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The dermal condensate signals to the overlying epithelium during hair follicle formation - its formation accompanies placode invagination and it expresses FAM3C and EFNB1 predicted to engage LAMP1/CXADR and EPHB6 on the placode, molecules reported to promote cell migration and invasion; it subsequently becomes the dermal papilla.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp”


## arm: asta-sep | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** The matrix population is annotated as SHH+; relative to adult hair follicles, prenatal matrix cells also show increased CXCL14 and CD24 expression.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”


## arm: asta-sep | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells are a hair follicle cell state of prenatal skin, arising from the epidermal placode and detected in the scRNA-seq data from 14 PCW; they are prenatal-specific and absent from established adult hair follicles.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).”

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-sep | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Prenatal hair matrix cells are attributed a chemotactic/immune-recruiting role: they upregulate chemotaxis genes such as CXCL14 (which recruits regulatory T cells) and CD24, suggesting they promote Treg accumulation and immune protection during early matrix differentiation.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”

**Reader's quote:** “This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”


## arm: asta-sep | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The supplied context gives no marker gene list for this subset beyond the defining LYVE1 label; the only gene it explicitly states is expressed by LYVE1+ macrophages is GAS6.

**Reader's quote:** “Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts”


## arm: asta-sep | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages sit close to endothelial cells in prenatal skin - macrophages co-locate with endothelial cells in the early and late neurovascular microenvironments (ME1 and ME5), and staining showed LYVE1+ macrophages in close proximity to endothelial cells.

**Reader's quote:** “Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).”

**Reader's quote:** “Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).”


## arm: asta-sep | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are attributed pro-angiogenic roles (promoting sprouting angiogenesis and blood vessel morphogenesis, in close proximity to endothelial cells) and a part in maintaining prenatal skin dermal fibroblasts through growth factor interactions.

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).”

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”


## arm: asta-sep | id: G23-fibroblast-markers | kind: present

**Question:** Which genes mark fibroblast?

**Intended answer:** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Hazard:** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Reader's answer:** The context does not give a general fibroblast marker panel; it reports PDGFRalpha and PDGFRbeta receptors expressed on fibroblasts, and subset-level genes such as COL1A1, SFRP1, CDKN1A, IL1R1 and POSTN in WNT2+ and PEAR1+ prenatal fibroblasts.

**Reader's quote:** “Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b)”


## arm: asta-sep | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts sit in the dermis of prenatal skin; HOXC5+ early fibroblasts are specifically located in the upper dermis, and other subsets are described as dermal fibroblast subsets.

**Reader's quote:** “HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”

**Reader's quote:** “To identify the cellular and molecular mechanisms that may endow early prenatal skin with scarless healing properties, we investigated the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets (Extended Data Figs. 3c and 7a).”


## arm: asta-sep | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Fibroblasts are attributed extracellular matrix and collagen deposition (in late gestation WNT2 + fibroblasts) versus cellular growth and differentiation programmes in early gestation, and fibroblast features are proposed to underlie the capacity of prenatal skin to heal without scarring.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.”


## arm: asta-sep | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm belongs to the immature interfollicular epidermis, forming the outermost layer of the epidermis overlying the dermal stroma; it is present from 7 PCW and is seen sloughing from 11 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: asta-sep | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm is described as constituting the first skin permeability barrier, and it is enriched in early gestation.

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier 2 , were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: asta-sep | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** Histologically, the periderm is an outermost layer of the early epidermis that is seen sloughing from 11 PCW, and it is classed among the immature interfollicular epidermal cells present from 7 PCW.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: asta-sep | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths”

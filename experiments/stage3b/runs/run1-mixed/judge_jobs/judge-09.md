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


# Cases (batch 9)


## arm: local-comb | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate is found in the dermal compartment of prenatal skin, as an aggregate of dermal fibroblasts, observed from 12 PCW.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”


## arm: local-comb | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** Dermal condensates initiate prenatal hair follicle formation through their interactions with epidermal placodes.

**Reader's quote:** “Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.”


## arm: local-comb | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells are part of the hair follicle: they arise from the epidermal placode and are identified among the hair follicle cell states present from 14 PCW.

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells”

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs”


## arm: local-comb | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** Prenatal hair matrix cells show increased expression of chemotaxis genes (e.g. CXCL14, which recruits Treg cells) and autoimmunity-control genes (CD24), suggesting a role in Treg cell accumulation and immune protection during early matrix differentiation.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”


## arm: local-comb | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages are predicted to co-locate with WNT2+ fibroblasts in prenatal skin, within distinct tissue microenvironments in early gestation.

**Reader's quote:** “Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).”


## arm: local-comb | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are suggested to maintain prenatal skin dermal fibroblasts through growth factor interactions, to contribute via GAS6-AXL signalling to immunosuppression and tissue repair, and to promote angiogenesis, specifically sprouting angiogenesis and blood vessel morphogenesis.

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages”


## arm: local-comb | id: G23-fibroblast-markers | kind: present

**Question:** Which genes mark fibroblast?

**Intended answer:** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Hazard:** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Reader's answer:** The context gives no single pan-fibroblast marker, but prenatal skin fibroblast subsets are distinguished by marker genes: FRZB (FRZB+ fibroblasts), HOXC5 (HOXC5+ early fibroblasts), and WNT2 and PEAR1 (WNT2+ and PEAR1+ fibroblasts).

**Reader's quote:** “We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW)”

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”


## arm: local-comb | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts are found in the dermis of prenatal skin; HOXC5+ early fibroblasts are located in the upper dermis, and dermal fibroblasts produce the collagen of the dermal stroma.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”


## arm: local-comb | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Dermal fibroblasts produce collagen, whose aggregation causes scarring; early prenatal fibroblasts downregulate extracellular matrix, collagen and inflammation genes, which may favour scarless tissue regeneration, and later-gestation WNT2+ fibroblasts upregulate extracellular matrix and collagen deposition genes.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”

**Reader's quote:** “Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.”


## arm: local-comb | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** The periderm is an immature interfollicular epidermal cell state that constitutes the first skin permeability barrier; it overlies the epidermis and was seen sloughing from the skin surface from 11 PCW.

**Reader's quote:** “neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW”

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”


## arm: local-comb | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm constitutes the first skin permeability barrier and is enriched in early gestation.

**Reader's quote:** “Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).”


## arm: local-comb | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** Histologically the periderm is described as being seen sloughing from 11 PCW, overlying the layer of epidermal cells of early prenatal skin, and it is counted among the immature interfollicular epidermal cells.

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”


## arm: local-comb | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”


## arm: local-comb | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as the common fibroblast progenitor in prenatal skin, differentiating along a hair fibroblast trajectory into hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and along a dermal fibroblast trajectory into WNT2+ and PEAR1+ fibroblasts.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”

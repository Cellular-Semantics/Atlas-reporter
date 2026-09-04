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


# Cases (batch 5)


## arm: asta-sep | id: G18-matrix-location | kind: present

**Question:** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Reader's answer:** Hair matrix cells arise from the epidermal placode and are described as a prenatal-specific cell state absent in established adult hair follicles.

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs”


## arm: asta-sep | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** The paper reports that prenatal skin matrix cells have increased expression of chemotaxis genes such as CXCL14 (a chemokine that recruits regulatory T cells) and CD24 (involved in control of autoimmunity), suggesting a role in Treg cell recruitment and immune protection during matrix differentiation.

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”

**Reader's quote:** “This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).”


## arm: asta-sep | id: G20-lyve1-markers | kind: present

**Question:** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** LYVE1; also expresses GAS6.

**Hazard:** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Reader's answer:** The paper identifies LYVE1+ macrophages by LYVE1 protein expression, using anti-LYVE1 immunofluorescence/RNAscope staining alongside other markers such as CD45 and CD31 to detect these cells.

**Reader's quote:** “n = 1 biological replicate with n = 2 technical replicates for immunofluorescence slides with anti-LYVE1, anti-CD45 and anti-VIM (Fig. 3e)”

**Reader's quote:** “n = 3 biological replicates for prenatal skin whole-mount immunofluorescence with anti-CD31 and anti-LYVE1 (Fig. 4a)”


## arm: asta-sep | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages were shown by multiplex RNAscope and immunofluorescence staining to be in close proximity to endothelial cells in prenatal skin.

**Reader's quote:** “LYVE1 + and TML macrophages in close proximity to endothelial cells”


## arm: asta-sep | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are attributed roles in blood vessel morphogenesis and in the maintenance of prenatal skin dermal fibroblasts.

**Reader's quote:** “blood vessel morphogenesis by LYVE1 + macrophages”

**Reader's quote:** “LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts”


## arm: asta-sep | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** Fibroblasts in prenatal human skin are found in the dermal compartment, producing collagen there, with subsets such as HOXC5+ early fibroblasts located in the upper dermis.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate 51 .”

**Reader's quote:** “HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f)”


## arm: asta-sep | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** Periderm is one of the immature interfollicular epidermal (IFE) cell types, present in the epidermal layer overlying the dermal stroma from 7 PCW, and it sloughs from 11 PCW.

**Reader's quote:** “with the periderm seen sloughing from 11 PCW”

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW”


## arm: asta-sep | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm is described as constituting the first skin permeability barrier.

**Reader's quote:** “the periderm, which constitutes the first skin permeability barrier”


## arm: asta-sep | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The periderm is described as a layer that is seen sloughing from 11 PCW.

**Reader's quote:** “with the periderm seen sloughing from 11 PCW”


## arm: asta-sep | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: asta-sep | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts function as a common fibroblast progenitor, giving rise to pre-Dc cells, the dermal condensate, dermal papilla and other dermal fibroblasts.

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast)”


## arm: asta-sep | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** DPYSL2 is the marker gene used to identify the mature basal cell population (DPYSL2+ basal cells).

**Reader's quote:** “Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW”


## arm: asta-sep | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arteriole cells show sprouting angiogenesis potential (assessed by the 'tip' cell state score) in both prenatal skin and SkO, though in SkO these cells appear unable to guide stalk cells for new blood vessel formation despite this signature.

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h)”

**Reader's quote:** “SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation”


## arm: asta-sep | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** The supplied context does not give a specific marker gene panel identifying PEAR1+ fibroblasts beyond the PEAR1 name itself, but it notes that a pro-inflammatory gene set (APOE, IGFBP7, ITM2A) was upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A)”


## arm: asta-sep | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts express genes involved in cellular senescence, cytokine pathways and collagen deposition that are highly expressed in pathogenic fibroblasts of fibrotic skin disorders, linking them to progressive acquisition of scar-promoting properties in later gestation.

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-sep | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** The paper suggests that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.”


## arm: asta-sep | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene for the arteriolar pathway (which includes arterioles).

**Reader's quote:** “GJA5 for arteriolar and PLVAP for venular”


## arm: asta-sep | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells are described as part of the inner layers of the hair follicle, identified in the scRNA-seq data from 14 PCW.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-sep | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The dermal condensate is described structurally as abutting the epithelial hair placode, and after HF invagination it becomes encapsulated at its base to form the dermal papilla.

**Reader's quote:** “which abuts the epithelial hair placode”

**Reader's quote:** “the Dc becomes encapsulated at its base as the Dp”


## arm: asta-sep | id: G55-cuticle-cortex-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-comb | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The paper describes the placode as arising from budding of basal cells at 14-15 PCW, alongside germ cells, with elongation into hair pegs.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”


## arm: asta-comb | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** Hair placode was observed at 14-15 PCW as budding of basal cells, elongating into hair follicles.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

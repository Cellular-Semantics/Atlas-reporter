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


# Cases (batch 8)


## arm: local-comb | id: G21-lyve1-location | kind: present

**Question:** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Reader's answer:** LYVE1+ macrophages co-locate with WNT2+ fibroblasts in prenatal skin.

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”


## arm: local-comb | id: G22-lyve1-function | kind: present

**Question:** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer:** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Reader's answer:** LYVE1+ macrophages are proposed to help maintain dermal fibroblasts via growth-factor signalling (PDGF, IGF1, GRN) and to drive blood vessel morphogenesis and sprouting angiogenesis.

**Reader's quote:** “suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “blood vessel morphogenesis by LYVE1+ macrophages”


## arm: local-comb | id: G24-fibroblast-location | kind: present

**Question:** Where in prenatal human skin is fibroblast found?

**Intended answer:** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Reader's answer:** HOXC5+ early fibroblasts, a fibroblast progenitor population, are located in the upper dermis.

**Reader's quote:** “Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).”


## arm: local-comb | id: G25-fibroblast-function | kind: present

**Question:** What function does the paper attribute to fibroblast?

**Intended answer:** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Reader's answer:** Dermal fibroblasts produce the collagen that aggregates to form scars when the overlying epidermis fails to regenerate.

**Reader's quote:** “Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.”


## arm: local-comb | id: G26-periderm-location | kind: present

**Question:** Where in prenatal human skin is periderm found?

**Intended answer:** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Reader's answer:** The periderm is an immature interfollicular epidermal (IFE) cell type forming the outer epidermal layer overlying the dermal stroma in early prenatal skin, and it sloughs off from 11 PCW.

**Reader's quote:** “Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).”

**Reader's quote:** “Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).”


## arm: local-comb | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm constitutes the first permeability barrier of the skin.

**Reader's quote:** “the periderm, which constitutes the first skin permeability barrier”


## arm: local-comb | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))”


## arm: local-comb | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as the common fibroblast progenitor that gives rise to pre-Dc, Dc, Dp and other dermal fibroblast subsets.

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”


## arm: local-comb | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** DPYSL2+ basal cells are defined by DPYSL2 expression and upregulate AGR2, as well as the ORS-differentiation genes BARX2 and SOX9.

**Reader's quote:** “Mature basal (DPYSL2+)”

**Reader's quote:** “we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)”


## arm: local-comb | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** In prenatal skin, capillary arteriole cells are able to further differentiate into arterioles (unlike in the SkO model), and they show increased sprouting angiogenesis potential as assessed by a 'tip' cell state score.

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).”

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: local-comb | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** PEAR1+ fibroblasts upregulate a pro-inflammatory phenotype including APOE, IGFBP7 and ITM2A during their transition from HOXC5+ fibroblasts, and (together with WNT2+ fibroblasts) express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts”

**Reader's quote:** “WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: local-comb | id: G37-postn-location | kind: present

**Question:** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Reader's answer:** POSTN+ basal cells are one of the basal-cell populations of the interfollicular epidermis (IFE), and they are present throughout gestation.

**Reader's quote:** “In addition, we observed immature and mature interfollicular epidermal (IFE) cells.”

**Reader's quote:** “whereas POSTN+ basal cells were present throughout gestation”


## arm: local-comb | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** The paper suggests that increased cell migration in POSTN+ basal cells contributes to hair placode specification and dermal invagination.

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”


## arm: local-comb | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene marking the arteriolar lineage (as opposed to PLVAP for venular).

**Reader's quote:** “expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: local-comb | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle/cortex cells are part of the inner layers of the hair follicle (HF).

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: local-comb | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The dermal condensate is described structurally as an aggregate of dermal fibroblasts.

**Reader's quote:** “dermal condensates (aggregates of dermal fibroblasts)”

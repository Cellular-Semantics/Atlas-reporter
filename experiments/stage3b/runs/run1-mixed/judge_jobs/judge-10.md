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


# Cases (batch 10)


## arm: local-comb | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** Mature basal cells are marked by DPYSL2, and DPYSL2+ basal cells also upregulate newly identified genes such as AGR2 along the ORS/CL trajectory.

**Reader's quote:** “Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW”

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2”


## arm: local-comb | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ (mature) basal cells lie on the ORS/CL differentiation trajectory, where they upregulate new genes such as AGR2 and genes related to outer root sheath differentiation (BARX2 and SOX9), indicating a role in differentiating towards the outer root sheath and companion layer.

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7).”


## arm: local-comb | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Prenatal skin capillary arteriole cells can differentiate further into arterioles, and they show increased sprouting angiogenesis potential as assessed by 'tip' cell state scoring.

**Reader's quote:** “Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).”

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: local-comb | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts, abundant in later gestation, acquire an adult pro-inflammatory, scar-promoting profile, expressing genes involved in cellular senescence, cytokine pathways and collagen deposition that are characteristic of pathogenic fibroblasts in fibrotic skin disorders.

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b).”


## arm: local-comb | id: G37-postn-location | kind: present

**Question:** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Reader's answer:** POSTN+ basal cells are part of the interfollicular epidermis, where they were present throughout gestation; trajectory analysis places them as the starting basal population of the epidermal differentiation paths.

**Reader's quote:** “In addition, we observed immature and mature interfollicular epidermal (IFE) cells.”

**Reader's quote:** “Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW, whereas POSTN+ basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).”

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths”


## arm: local-comb | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells are proposed to give rise to two epidermal differentiation paths (ORS/CL and IRS trajectories), and their increased cellular migration may contribute to placode specification and dermal invagination.

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”

**Reader's quote:** “Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).”


## arm: local-comb | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as a characteristic gene of the arteriolar pathway, which comprises capillaries, capillary arterioles and arterioles.

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: local-comb | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** The paper attributes sprouting angiogenesis potential to prenatal skin arteriole cells: they showed an increased 'tip' cell state score, indicating capacity for new blood vessel growth.

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: local-comb | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells are part of the inner layers of the hair follicle, identified among hair follicle cells from 14 PCW.

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: local-comb | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The paper describes dermal condensates structurally as aggregates of dermal fibroblasts.

**Reader's quote:** “Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.”

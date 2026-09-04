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


# Cases (batch 7)


## arm: asta-comb | id: G32-dpysl2-function | kind: present

**Question:** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Reader's answer:** DPYSL2+ basal cells lie along the ORS/CL differentiation trajectory and upregulate genes such as AGR2, along with previously reported ORS differentiation genes BARX2 and SOX9.

**Reader's quote:** “Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26”


## arm: asta-comb | id: G33-caparteriole-markers | kind: present

**Question:** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Reader's answer:** The paper reports GJA5 as a characteristic gene of the arteriolar pathway, which includes capillary arterioles (as opposed to PLVAP marking the venular pathway).

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: asta-comb | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** Capillary arteriole cells in prenatal skin can further differentiate into arterioles, whereas the equivalent SkO cells cannot; SkO capillary arteriole cells also fail to guide stalk cells for new blood vessel formation despite expressing sprouting angiogenesis genes.

**Reader's quote:** “prenatal skin capillary arteriole cells could further differentiate into arterioles”

**Reader's quote:** “SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation”


## arm: asta-comb | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** PEAR1+ fibroblasts are marked by upregulation of APOE, IGFBP7 and ITM2A (pro-inflammatory phenotype genes), and express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: asta-comb | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts, together with WNT2+ fibroblasts, express genes involved in cellular senescence, cytokine pathways and collagen deposition that are highly expressed in pathogenic fibroblasts of fibrotic skin disorders, linking them to a scar-promoting phenotype.

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-comb | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** The paper suggests that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.”


## arm: asta-comb | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene marking the arteriolar pathway.

**Reader's quote:** “with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: asta-comb | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** Prenatal skin arteriole cells (along with capillary arteriole and capillary cells) showed increased sprouting angiogenesis potential, as assessed by scoring the 'tip' cell state.

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: asta-comb | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle/cortex cells form part of the inner layers of the hair follicle.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6)”


## arm: local-comb | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The hair (epidermal) placode is described structurally as a focal site of epidermal layer thickening.

**Reader's quote:** “epidermal placodes (focal sites of epidermal layer thickening)”


## arm: local-comb | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** Hair placode arises from budding basal cells of the epidermis and appears at 14-15 PCW, prior to elongation into hair pegs (hair follicles), and is abutted by the dermal condensate below.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”


## arm: local-comb | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The epidermal (hair) placode interacts with the dermal condensate to initiate hair follicle formation.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”


## arm: local-comb | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophage subsets are predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation.

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).”


## arm: local-comb | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** The paper attributes to macrophages roles in scarless skin repair, fibroblast homeostasis, and neurovascular development, including validated contributions to vascular network formation.

**Reader's quote:** “Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.”

**Reader's quote:** “We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.”


## arm: local-comb | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** WNT2+ fibroblasts are marked by COL1A1 (late gestation, ECM/collagen deposition), SFRP1 (early gestation, growth/differentiation), and, shared with PEAR1+ fibroblasts, CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: local-comb | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** The context does not give a discrete anatomical location for WNT2+ fibroblasts, but notes that they co-locate with LYVE1+ macrophages and, in early gestation, with TML macrophages.

**Reader's quote:** “LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e)”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW)”


## arm: local-comb | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** WNT2+ fibroblasts show gestation-stage-dependent gene programmes: in late gestation they upregulate extracellular matrix and collagen deposition genes, while earlier they express genes tied to cellular growth and differentiation.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”


## arm: local-comb | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages share an expression profile of P2RY12, CX3CR1 and OLFML3, and co-express immunomodulatory genes including CX3CR1 and SYT11.

**Reader's quote:** “share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs”

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: local-comb | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1) of prenatal skin.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin.”


## arm: local-comb | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are predicted to interact with Schwann cells to support synapse formation and axon guidance, and to promote sprouting angiogenesis.

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)”

**Reader's quote:** “sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages”


## arm: local-comb | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The dermal condensate, described as an aggregate of dermal fibroblasts, interacts with the epidermal placode to initiate hair follicle formation.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”


## arm: local-comb | id: G19-matrix-function | kind: present

**Question:** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Reader's answer:** The paper suggests hair matrix cells have a potential role in accumulating regulatory T cells and providing immune protection during early hair follicle differentiation, linked to their expression of chemotaxis and autoimmunity-control genes.

**Reader's quote:** “This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation”

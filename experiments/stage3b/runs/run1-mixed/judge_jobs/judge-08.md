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


## arm: asta-comb | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles), in contrast to PLVAP for the venular pathway; no arteriole-specific marker list beyond this is provided.

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: asta-comb | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** The only function the context attributes to arterioles is a sprouting-angiogenesis (new blood vessel growth) potential: prenatal skin arterioles, along with capillary arterioles and capillaries, showed increased 'tip' cell state scoring. Arterioles are also described as the endpoint of the arteriolar differentiation pathway from early endothelial cells.

**Reader's quote:** “However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”

**Reader's quote:** “Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: asta-comb | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle and cortex cells are hair follicle cells forming part of the inner layers of the follicle, identified in the scRNA-seq data from 14 PCW; they lie on the inner root sheath differentiation trajectory.

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”

**Reader's quote:** “IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7)”


## arm: local-comb | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** Epidermal placodes are focal sites of thickening of the epidermal layer, seen histologically as budding of basal cells at 14–15 PCW.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”


## arm: local-comb | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The hair placode is located in the epidermis, as a focal site of epidermal layer thickening, positioned adjacent to (abutting) the dermal condensate.

**Reader's quote:** “initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode”


## arm: local-comb | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The epidermal placode initiates hair follicle formation through interactions with dermal condensates, and it gives rise to hair matrix cells.

**Reader's quote:** “Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)”

**Reader's quote:** “We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs”


## arm: local-comb | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages seed prenatal skin from as early as 6 PCW and are predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments; LYVE1+ macrophages co-locate with WNT2+ fibroblasts, and TML macrophages co-locate with Schwann cells in an early neurovascular microenvironment.

**Reader's quote:** “immune cells such as macrophages seed the skin as early as 6 PCW”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)”


## arm: local-comb | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** The paper attributes to prenatal skin macrophages contributions to scarless skin repair, fibroblast homeostasis and neurovascular development, including a role in vascular network formation and support for establishing the skin peripheral nervous system.

**Reader's quote:** “Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.”

**Reader's quote:** “We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.”

**Reader's quote:** “These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.”


## arm: local-comb | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** Beyond the defining WNT2 in the subset name, the context does not give a marker list, but it reports genes expressed by WNT2+ fibroblasts: CDKN1A, IL1R1 and POSTN (shared with PEAR1+ fibroblasts), with COL1A1 upregulated in late gestation and SFRP1 among DEGs of early WNT2+ fibroblasts.

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”


## arm: local-comb | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** WNT2+ fibroblasts are dermal fibroblasts, formed along the dermal fibroblast trajectory, and they co-locate with LYVE1+ and TML macrophages in early prenatal skin.

**Reader's quote:** “the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”


## arm: local-comb | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** Early WNT2+ fibroblasts express genes involved in cellular growth and differentiation, whereas late gestation WNT2+ fibroblasts upregulate extracellular matrix and collagen deposition genes; together with PEAR1+ fibroblasts they express senescence, cytokine and collagen deposition genes, reflecting progressive acquisition of scar-promoting features.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: local-comb | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share a microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

**Reader's quote:** “We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs”

**Reader's quote:** “co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: local-comb | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment of prenatal skin.

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: local-comb | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages express immunomodulatory genes and are inferred to contribute to scarless healing, to support establishment of the skin peripheral nervous system through predicted interactions with Schwann cells in synapse formation and axon guidance, and to promote sprouting angiogenesis.

**Reader's quote:** “Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages”

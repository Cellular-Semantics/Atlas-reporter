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


# Cases (batch 3)


## arm: asta-sep | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The placode is described as a bud of basal cells seen at 14-15 PCW, and its formation involves invagination of the placode as the dermal condensate forms.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode”


## arm: asta-sep | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The hair placode is found in the epidermis as a bud of basal cells, observed histologically at 14-15 PCW, and placode cells were captured in the hair follicle scRNA-seq data from 14 PCW.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

**Reader's quote:** “Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-sep | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The context describes the placode only as the epithelial partner in the mesenchymal-epithelial interactions that instruct early hair follicle formation, bearing receptors (LAMP1 or CXADR and EPHB6) for Dc-derived ligands reported to promote cell migration and invasion.

**Reader's quote:** “We explored the mesenchymal-epithelial interactions that instruct early HF formation.”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: asta-sep | id: G05-macrophage-markers | kind: present

**Question:** Which genes mark macrophage?

**Intended answer:** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Hazard:** broad label; four subsets each have their own markers

**Reader's answer:** The context gives no pan-macrophage marker list; it names the genes that define subsets - TREM2 with a P2RY12, CX3CR1 and OLFML3 microglia-like profile, and LYVE1, MHCII and iron-recycling subsets.

**Reader's quote:** “We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).”

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”


## arm: asta-sep | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages are described by co-location: TREM2 + microglia-like macrophages co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in an early neurovascular microenvironment (ME1).

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: asta-sep | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages are attributed non-immune morphogenetic roles: contributing to prenatal skin angiogenesis, maintaining dermal fibroblasts via growth factor interactions, and supporting establishment of the skin peripheral nervous system in early gestation.

**Reader's quote:** “Our data suggested that macrophages contribute to prenatal skin angiogenesis.”

**Reader's quote:** “Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.”

**Reader's quote:** “These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .”


## arm: asta-sep | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** Beyond WNT2 in the subset name, the context reports COL1A1 upregulated in late gestation and SFRP1 in early gestation WNT2+ fibroblasts, and expression of CDKN1A, IL1R1 and POSTN by WNT2+ and PEAR1+ prenatal fibroblasts.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b)”


## arm: asta-sep | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** The context gives no anatomical compartment beyond co-location: WNT2+ fibroblasts are predicted to co-locate with LYVE1+ macrophages (and are abundant in later gestation) in prenatal skin.

**Reader's quote:** “Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2 + and PEAR1 + prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b).”


## arm: asta-sep | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** WNT2+ fibroblasts are linked to extracellular matrix and collagen deposition in late gestation versus cellular growth and differentiation in early gestation, and they express senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibroblasts, supporting progressive acquisition of scar-promoting programmes.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”

**Reader's quote:** “Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .”


## arm: asta-sep | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are TREM2+ and share the microglia-like profile P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11, and express GAS6.

**Reader's quote:** “We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).”

**Reader's quote:** “Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”


## arm: asta-sep | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to sit alongside WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and to co-locate with Schwann cells in the 'early neurovascular microenvironment' (ME1).

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”


## arm: asta-sep | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are attributed immunomodulatory functions (potentially contributing to scarless healing via IL-6 regulation and GAS6-AXL signalling to WNT2+ fibroblasts), support of the developing skin peripheral nervous system through Schwann cell interactions, and promotion of sprouting angiogenesis.

**Reader's quote:** “Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)”

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)”

**Reader's quote:** “Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages”


## arm: asta-sep | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is defined by FOXD1 and SOX2 expression (annotated in human using orthologous marker genes from mouse), and the Dc is also reported to express FAM3C and EFNB1.

**Reader's quote:** “In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 .”

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1”


## arm: asta-sep | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate lies in the dermal compartment of prenatal skin from 12 PCW, adjacent to (abutting) the epithelial hair placode, and after hair follicle invagination it becomes encapsulated at the follicle base as the dermal papilla.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp”

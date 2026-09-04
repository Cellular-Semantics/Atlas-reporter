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


## arm: local | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts express genes associated with an adult, pro-inflammatory phenotype, cellular senescence, cytokine signalling and collagen deposition — a gene programme the paper links to pathogenic, scar-promoting fibroblast states seen in fibrotic skin disorders and in later-gestation scarring.

**Reader's quote:** “The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: local | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells show increased cellular migration that may be involved in placode specification and dermal invagination.

**Reader's quote:** “Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.”


## arm: local | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene for the arteriolar pathway.

**Reader's quote:** “with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: local | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** The paper reports that arteriole cells (along with capillary arteriole and capillary cells) showed increased sprouting angiogenesis potential, based on scoring of a 'tip' cell state.

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: local | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle/cortex cells are part of the inner layers of the hair follicle, identified alongside other HF cell types from 14 PCW.

**Reader's quote:** “we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”


## arm: local | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The paper states that following HF invagination, the dermal condensate becomes encapsulated at its base as it forms the dermal papilla.

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)”


## arm: local | id: G55-cuticle-cortex-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: asta-sep | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The hair placode is described as arising via budding of basal cells, alongside germ cells, with subsequent elongation of hair follicles into hair pegs.

**Reader's quote:** “budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”


## arm: asta-sep | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The hair placode arises from budding of basal cells in the epidermis at 14-15 PCW, and it is abutted by the dermal condensate.

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).”

**Reader's quote:** “which abuts the epithelial hair placode 26,28”


## arm: asta-sep | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The placode is a site of ligand-receptor signalling (via EPHB6, among others) that is reported to promote cell migration and invasion.

**Reader's quote:** “EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: asta-sep | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Within this context, the only macrophage subset given an explicit skin location is the TML macrophage, which was predicted to co-locate with Schwann cells in an early neurovascular microenvironment.

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)”


## arm: asta-sep | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** The paper attributes several functions to macrophages in prenatal skin, including promoting angiogenesis and vascular network formation, interacting with fibroblasts to maintain tissue homeostasis, and supporting neural development alongside Schwann cells.

**Reader's quote:** “Macrophages have been implicated in angiogenesis during prenatal organ development and in the postnatal setting such as cancerrelated angiogenesis 67,68 .”

**Reader's quote:** “Our data suggested that macrophages contribute to prenatal skin angiogenesis.”


## arm: asta-sep | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** WNT2+ fibroblasts are marked by differentially expressed genes that vary with gestational age: COL1A1 in late gestation and SFRP1 in early gestation.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)”


## arm: asta-sep | id: G09-wnt2fib-location | kind: present

**Question:** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer:** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Reader's answer:** WNT2+ fibroblasts are found co-located with LYVE1+ macrophages in distinct tissue microenvironments in prenatal skin.

**Reader's quote:** “Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).”


## arm: asta-sep | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** Late gestation WNT2+ fibroblasts are attributed a function in extracellular matrix and collagen deposition.

**Reader's quote:** “Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1)”


## arm: asta-sep | id: G11-tml-markers | kind: present

**Question:** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Reader's answer:** TML macrophages are marked by TREM2, and share an expression profile of P2RY12, CX3CR1 and OLFML3 with microglia-like macrophages from other developing organs.

**Reader's quote:** “We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs”


## arm: asta-sep | id: G12-tml-location | kind: present

**Question:** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Reader's answer:** TML macrophages are predicted to co-locate with Schwann cells in the 'early neurovascular microenvironment' (ME1) and with WNT2+ fibroblasts in early prenatal skin (6-8 PCW).

**Reader's quote:** “TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)”

**Reader's quote:** “TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)”


## arm: asta-sep | id: G13-tml-function | kind: present

**Question:** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer:** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Reader's answer:** TML macrophages are attributed roles including anti-fibrogenic/scarless-healing contributions, sprouting angiogenesis, and interacting with Schwann cells to contribute to synapse formation and axon guidance.

**Reader's quote:** “TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance”


## arm: asta-sep | id: G14-dc-markers | kind: present

**Question:** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Reader's answer:** The dermal condensate is marked by FOXD1 and SOX2.

**Reader's quote:** “the Dc (FOXD1 + SOX2 + )”


## arm: asta-sep | id: G15-dc-location | kind: present

**Question:** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer:** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Reader's answer:** The dermal condensate is found within the dermal compartment of prenatal skin, from 12 PCW, and abuts the epithelial hair placode.

**Reader's quote:** “Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).”

**Reader's quote:** “which abuts the epithelial hair placode 26,28”


## arm: asta-sep | id: G16-dc-function | kind: present

**Question:** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Reader's answer:** The paper attributes a migration/invasion-promoting function to the dermal condensate: it expresses FAM3C and EFNB1, predicted to signal to the overlying placode via LAMP1/CXADR and EPHB6, and these interactions have been reported to promote cell migration and invasion.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: asta-sep | id: G17-matrix-markers | kind: present

**Question:** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer:** SHH, and WNT10B; both described as known matrix markers.

**Hazard:** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Reader's answer:** Hair matrix cells are marked by SHH, and matrix-specific genes include CXCL14 and CD24, which are increased compared with adult hair follicles.

**Reader's quote:** “which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).”

**Reader's quote:** “Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .”

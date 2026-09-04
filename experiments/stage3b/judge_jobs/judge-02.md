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


# Cases (batch 2)


## arm: whole | id: G27-periderm-function | kind: present

**Question:** What function does the paper attribute to periderm?

**Intended answer:** Constitutes the first skin permeability barrier.

**Reader's answer:** The periderm constitutes the first permeability barrier of the skin.

**Reader's quote:** “neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation”


## arm: whole | id: G28-periderm-structure | kind: present

**Question:** What does the paper say about the structure or morphology of periderm?

**Intended answer:** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Hazard:** thin - a layer description and a sloughing observation, not morphology proper

**Reader's answer:** The periderm is described as sloughing off from 11 PCW, a structural/morphological change in the epidermal layer.

**Reader's quote:** “with the periderm seen sloughing from 11 PCW”


## arm: whole | id: G29-hoxc5-location | kind: present

**Question:** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** The upper dermis.

**Reader's answer:** HOXC5+ early fibroblasts are located in the upper dermis.

**Reader's quote:** “HOXC5+ early fibroblasts (located in the upper dermis”


## arm: whole | id: G30-hoxc5-function | kind: present

**Question:** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer:** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Reader's answer:** HOXC5+ early fibroblasts act as a common fibroblast progenitor that gives rise to hair-specialized fibroblasts (pre-Dc, Dc, Dp) and dermal fibroblasts (WNT2+ and PEAR1+ fibroblasts).

**Reader's quote:** “pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)”


## arm: whole | id: G31-dpysl2-markers | kind: present

**Question:** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer:** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Hazard:** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Reader's answer:** DPYSL2+ basal cells are marked by DPYSL2, and along the ORS/CL trajectory they upregulate AGR2.

**Reader's quote:** “Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW”

**Reader's quote:** “we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2”


## arm: whole | id: G33-caparteriole-markers | kind: present

**Question:** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Reader's answer:** Capillary arterioles belong to the arteriolar differentiation pathway, characterised by expression of GJA5.

**Reader's quote:** “early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).”


## arm: whole | id: G34-caparteriole-function | kind: present

**Question:** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer:** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Reader's answer:** The paper reports that capillary arteriole cells (in both SkO and prenatal skin) show increased sprouting angiogenesis potential, based on scoring of the 'tip' cell state.

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells”


## arm: whole | id: G35-pear1-markers | kind: present

**Question:** Which genes mark PEAR1+ fibroblast?

**Intended answer:** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Reader's answer:** PEAR1+ fibroblasts are defined by PEAR1, and genes such as APOE, IGFBP7 and ITM2A are upregulated during the transition into this state.

**Reader's quote:** “the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)”

**Reader's quote:** “Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts”


## arm: whole | id: G36-pear1-function | kind: present

**Question:** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer:** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Reader's answer:** PEAR1+ fibroblasts (together with WNT2+ fibroblasts) express genes involved in cellular senescence, cytokine pathways and collagen deposition, resembling genes highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

**Reader's quote:** “WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)”


## arm: whole | id: G38-postn-function | kind: present

**Question:** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer:** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Reader's answer:** POSTN+ basal cells show increased cellular migration that may contribute to placode specification and dermal invagination.

**Reader's quote:** “increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination”


## arm: whole | id: G39-arteriole-markers | kind: present

**Question:** Which genes mark arteriole?

**Intended answer:** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Hazard:** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Reader's answer:** GJA5 is given as the characteristic gene for the arteriolar pathway.

**Reader's quote:** “with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)”


## arm: whole | id: G40-arteriole-function | kind: present

**Question:** What function does the paper attribute to arteriole?

**Intended answer:** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Reader's answer:** The paper reports that sprouting angiogenesis potential (scored via a 'tip' cell state) was increased in prenatal skin arteriole cells (along with capillary arteriole and capillary cells).

**Reader's quote:** “sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).”


## arm: whole | id: G41-cuticle-location | kind: present

**Question:** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Part of the inner layers of the hair follicle.

**Reader's answer:** Cuticle/cortex cells are part of the inner layers of the hair follicle.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: whole | id: G45-dermal-condensate-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** The paper states that following HF invagination, the dermal condensate becomes encapsulated at its base as it forms the dermal papilla.

**Reader's quote:** “Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)”


## arm: whole | id: G55-cuticle-cortex-structure-absent | kind: absent

**Question:** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer:** Not stated in this paper. Gopee et al. describe the transcriptional identity, location and inferred function of this cell type but not its morphology or ultrastructure.

**Reader's answer:** Cuticle/cortex cells are described as part of the inner layers of the hair follicle.

**Reader's quote:** “cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)”


## arm: local | id: G01-placode-structure | kind: present

**Question:** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Reader's answer:** The hair placode is described as a focal site of epidermal layer thickening.

**Reader's quote:** “epidermal placodes (focal sites of epidermal layer thickening)”


## arm: local | id: G02-placode-location | kind: present

**Question:** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Reader's answer:** The hair placode is an epidermal structure, arising via budding of basal cells in the epidermis, described in the paper as the 'epidermal placode.'

**Reader's quote:** “At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed”

**Reader's quote:** “hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs”


## arm: local | id: G03-placode-function | kind: present

**Question:** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer:** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Reader's answer:** The Dc's interaction with the placode (via FAM3C/EFNB1 and receptors on the placode) has been reported to promote cell migration and invasion, and RSPO3 from the dermal papilla interacts with matrix cells overlying the placode to contribute to proliferation of HF epithelial cells, which includes the placode-derived matrix.

**Reader's quote:** “The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion”


## arm: local | id: G06-macrophage-location | kind: present

**Question:** Where in prenatal human skin is macrophage found?

**Intended answer:** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Reader's answer:** Macrophages seed the skin as early as 6 PCW, co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation.

**Reader's quote:** “immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes”

**Reader's quote:** “In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation”


## arm: local | id: G07-macrophage-function | kind: present

**Question:** What function does the paper attribute to macrophage?

**Intended answer:** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Reader's answer:** Macrophages support wound healing (improving scratch-wound closure of co-cultured fibroblasts) and, across their four subsets, express gene programs that drive angiogenesis.

**Reader's quote:** “Using a scratch assay of SkO-derived fibroblasts cultured with or without iPS cell-derived macrophages, we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g).”

**Reader's quote:** “Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).”


## arm: local | id: G08-wnt2fib-markers | kind: present

**Question:** Which genes mark WNT2+ fibroblast?

**Intended answer:** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Reader's answer:** WNT2+ fibroblasts are marked by the gene WNT2 itself, and depending on gestational age express COL1A1 (late) or SFRP1 (early); together with PEAR1+ fibroblasts they also express CDKN1A, IL1R1 and POSTN.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

**Reader's quote:** “Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.”


## arm: local | id: G10-wnt2fib-function | kind: present

**Question:** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer:** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Reader's answer:** WNT2+ fibroblasts show gestation-dependent gene expression: in late gestation they upregulate extracellular matrix and collagen deposition genes, while in early gestation they upregulate genes involved in cellular growth and differentiation.

**Reader's quote:** “Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).”

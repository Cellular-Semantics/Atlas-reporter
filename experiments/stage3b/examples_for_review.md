# Judged reads, for human review

Source paper: **gopee2024** — every quote below is text from this paper and
nothing else. The reader saw only the context block named under each case.

Each case had its outcome set by an Opus judge rather than by string matching.
The readers' quotes were machine-verified as verbatim before the judge saw them,
so the judge was ruling only on whether the answer *meant* the right thing.
In run 1 the judge was Opus grading Opus's own answers; that is the main reason
to check these by hand.

`verbatim` on a quote means it is an exact substring of that item's own context,
by the same test the scorer used. `leaked` means it is real text from the paper
that reached the reader through a different question batched with this one —
a flaw in how the batch was built, not a fabrication by the reader.

---

## Context: whole

### G01-placode-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Gold span** (paragraph 1 of 37)

> epidermal placodes (focal sites of epidermal layer thickening)

**The gold span in its paragraph**

> … rm (apart from facial and cranial skin, where it arises from ectoderm-derived neural crest cells). The skin appendages, which include hair follicles (HFs) and sebaceous glands, form in a cephalocaudal direction. Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW. There is, however, a paucity of information about the precise cellular composition of human prenatal skin over these developmental periods and whether cells interact in functional microanatomical niches that …

**Opus/Fable** → `correct` — judge: *Gives focal epidermal thickening, budding of basal cells and invagination, matching the intended answer.*

> The placode is described as a focal thickening of the epidermal layer; histologically it is seen as budding of basal cells at 14-15 PCW, and its formation is accompanied by invagination into the dermis.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > epidermal placodes (focal sites of epidermal layer thickening)

- *verbatim, paragraph 9 — **not the gold span's paragraph (1)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

- *verbatim, paragraph 16 — **not the gold span's paragraph (1)***

  > The Dc, for which formation is accompanied by invagination of the placode

**Sonnet** → `correct` — judge: *Names focal epidermal thickening, the main structural point, though it omits budding and invagination.*

> The paper describes hair placodes as focal sites of epidermal layer thickening.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (paragraph 13 of 37)

> which abuts the epithelial hair placode

**The gold span in its paragraph**

> … esenchymal differentiation We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,. Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

**Opus/Fable** → `correct` — judge: *Places the placode in the epidermis/basal epidermis with the dermal condensate abutting it from below.*

> The placode is an epidermal/epithelial structure in the basal epidermis of prenatal skin, appearing as budding basal cells from 14-15 PCW, and it is abutted by the dermal condensate beneath it.

- *verbatim, paragraph 9 — **not the gold span's paragraph (13)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

- *verbatim, paragraph 13 — same paragraph as the gold span*

  > aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

- *verbatim, paragraph 10 — **not the gold span's paragraph (13)***

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells

**Sonnet** → `correct` — judge: *Places the placode in the epidermis at focal thickenings with underlying dermal condensate, as intended.*

> Hair placodes are focal sites of epidermal layer thickening, situated in the epidermis where they interact with underlying dermal condensates.

- *verbatim, paragraph 1 — **not the gold span's paragraph (13)***

  > epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 11 of 37)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity ( …

**Opus/Fable** → `correct` — judge: *States initiation of hair follicle formation with the dermal condensate and origin of hair matrix cells; extra trajectory detail is additive.*

> The placode initiates hair follicle formation through interaction with the dermal condensate, and it gives rise to hair matrix cells; it lies on the IRS differentiation trajectory and receives migration/invasion-promoting signals from the Dc.

- *verbatim, paragraph 1 — **not the gold span's paragraph (11)***

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 11 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

- *verbatim, paragraph 12 — **not the gold span's paragraph (11)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

**Sonnet** → `substituted` — judge: *Quote is real but the answer describes Dc-to-placode ligand signalling rather than the placode's role in initiating hair follicle formation.*

> The placode expresses receptors (LAMP1/CXADR and EPHB6) for Dc-derived FAM3C and EFNB1, interactions reported to promote cell migration and invasion.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G05-macrophage-markers — markers, expect present

**Question** Which genes mark macrophage?

**Intended answer** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Gold span** (paragraph 25 of 37)

> share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

**The gold span in its paragraph**

> ## Scarless healing and potential macrophage contribution We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f). Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for …

**Hazard note given to the judge** broad label; four subsets each have their own markers

**Opus/Fable** → `correct` — judge: *Correctly handles the broad label by giving per-subset markers including MHCII and the TREM2/P2RY12/CX3CR1/OLFML3 microglia-like set.*

> The paper identifies macrophage subsets by marker genes rather than giving pan-macrophage markers: LYVE1+, MHCII+, TREM2+ microglia-like (TREM2, P2RY12, CX3CR1, OLFML3) and iron-recycling subsets.

- *verbatim, paragraph 29 — **not the gold span's paragraph (25)***

  > the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads

**Sonnet** → `correct` — judge: *Correctly treats the broad label as four subsets and names their defining markers, accurate as far as it goes.*

> Macrophage subsets are marked by LYVE1, MHCII, TML (TREM2+), and iron-recycling markers.

- *verbatim, paragraph 29 — **not the gold span's paragraph (25)***

  > the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G06-macrophage-location — location, expect present

**Question** Where in prenatal human skin is macrophage found?

**Intended answer** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Gold span** (paragraph 6 of 37)

> Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’

**The gold span in its paragraph**

> … edict significant cellular co-locations that are not readily evident in conventional histopathology analyses,. Our analysis predicted distinct microenvironments in prenatal skin comprising epidermal, dermal, vascular and neural cells, each including specific types of immune cells (Fig. 1d and Extended Data Fig. 1e,f). Macrophages co-located with endothelial and neural cells in 'early and late neurovascular microenvironments' (ME1 and ME5, respectively), whereas pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses (Fig. 1d and Extended Data Fig. 1e,f). These observations indicated that immune cells may occupy defined microanatomical niches where they have non-immune functions durin …

**Opus/Fable** → `correct` — judge: *Names seeding from 6 PCW and co-location with endothelial/neural cells in ME1 and ME5, plus fibroblast co-location.*

> Macrophages seed the skin from as early as 6 PCW and are present throughout gestation, co-locating with endothelial and neural cells in early and late neurovascular microenvironments (ME1 and ME5) and, for the LYVE1+ subset, with WNT2+ dermal fibroblasts.

- *verbatim, paragraph 2 — **not the gold span's paragraph (6)***

  > immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’ (ME1 and ME5, respectively)

- *verbatim, paragraph 24 — **not the gold span's paragraph (6)***

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

**Sonnet** → `correct` — judge: *Gives the neurovascular microenvironment co-location accurately, missing only the 6 PCW seeding detail.*

> Macrophages co-locate with endothelial and neural cells within 'early and late neurovascular microenvironments' in prenatal skin.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’ (ME1 and ME5, respectively), whereas pre-dermal condensate (pre-Dc) cells co-located with dendritic and lymphoid cells based on correlation analyses (Fig. 1d and Extended Data Fig. 1e,f).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G07-macrophage-function — function, expect present

**Question** What function does the paper attribute to macrophage?

**Intended answer** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Gold span** (paragraph 34 of 37)

> Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**The gold span in its paragraph**

> … iscussion In this study, we characterized the dynamic composition of human prenatal skin during the early stages of de novo HF formation and highlighted the crucial skin immune and non-immune crosstalk that contributes to skin morphogenesis, results that are in line with emerging evidence in animal and human studies,. Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development. This is in part contributed to by yolk-sac derived TML macrophages, which suggests that these cells have broader functions outside the central nervous system in early gestation. The presence of TML macrophages has previously been identified in several prenatal organs,,.

**Opus/Fable** → `correct` — judge: *Covers angiogenesis/vessel remodelling, scarless repair, fibroblast homeostasis and neural development.*

> Macrophages are proposed to support skin morphogenesis: maintaining dermal fibroblasts, contributing to scarless repair, supporting peripheral nerve development, and driving angiogenesis and vascular network remodelling (shown by adding iPS-derived macrophages to skin organoids).

- *verbatim, paragraph 34 — same paragraph as the gold span*

  > Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

- *verbatim, paragraph 24 — **not the gold span's paragraph (34)***

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 28 — **not the gold span's paragraph (34)***

  > These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

- *verbatim, paragraph 33 — **not the gold span's paragraph (34)***

  > Collectively, our findings demonstrate that interactions between macrophages and endothelial cells are required to support angiogenesis through blood vessel remodelling.

**Sonnet** → `correct` — judge: *Matches the intended scarless repair, fibroblast homeostasis and neurovascular development roles.*

> Macrophages are attributed roles in scarless skin repair, fibroblast homeostasis, and neurovascular (angiogenesis and nerve) development in prenatal skin.

- *verbatim, paragraph 34 — same paragraph as the gold span*

  > Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (paragraph 23 of 37)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**The gold span in its paragraph**

> … ted during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18). Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine …

**Opus/Fable** → `correct` — judge: *Reports WNT2, late COL1A1/ECM, early SFRP1, plus CDKN1A, IL1R1, POSTN and downregulated IL6.*

> Beyond WNT2 itself, the paper reports genes differentially expressed by this subset: late-gestation WNT2+ fibroblasts upregulate COL1A1, early ones SFRP1, and the subset expresses CDKN1A, IL1R1 and POSTN, with downregulated IL6 relative to adult fibroblasts.

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

**Sonnet** → `correct` — judge: *Correctly reports the late COL1A1 versus early SFRP1 split, a partial but accurate marker answer.*

> Late gestation WNT2+ fibroblasts upregulate COL1A1, while early WNT2+ fibroblasts upregulate SFRP1.

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (paragraph 24 of 37)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**The gold span in its paragraph**

> … e of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as s …

**Opus/Fable** → `correct` — judge: *Dermal, co-locating with LYVE1+ macrophages and with TML macrophages at 6-8 PCW, as intended.*

> WNT2+ fibroblasts are dermal fibroblasts of prenatal skin that become abundant in later gestation; they co-locate with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), with TML macrophages.

- *verbatim, paragraph 23 — **not the gold span's paragraph (24)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 24 — same paragraph as the gold span*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

- *verbatim, paragraph 25 — **not the gold span's paragraph (24)***

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

**Sonnet** → `miss`

> The supplied context does not state a spatial location for WNT2+ fibroblasts.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (paragraph 23 of 37)

> we observed differences within the WNT2+ fibroblast population across gestation time

**The gold span in its paragraph**

> … b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary  …

**Opus/Fable** → `correct` — judge: *Captures the early growth/differentiation to late ECM-collagen shift and acquisition of a senescent, pro-inflammatory adult-like profile.*

> WNT2+ fibroblasts form the dermal fibroblast branch of the fibroblast trajectory and shift function across gestation: early cells express growth and differentiation genes, whereas late cells deposit extracellular matrix and collagen and express senescence/cytokine genes characteristic of pathogenic fibrotic fibroblasts, linking them to the loss of scarless healing.

- *verbatim, paragraph 14 — **not the gold span's paragraph (23)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 24 — **not the gold span's paragraph (23)***

  > were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts

**Sonnet** → `miss`

> The supplied context does not explicitly attribute a function to WNT2+ fibroblasts; it only describes genes they upregulate at different gestational stages.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G11-tml-markers — markers, expect present

**Question** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Gold span** (paragraph 25 of 37)

> Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia

**The gold span in its paragraph**

> ## Scarless healing and potential macrophage contribution We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f). Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properti …

**Opus/Fable** → `correct` — judge: *Gives TREM2 with P2RY12, CX3CR1, OLFML3 and GAS6, matching the intended marker set.*

> TML macrophages are TREM2+ and share a microglial expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11, and express GAS6.

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

**Sonnet** → `correct` — judge: *Names TREM2 with P2RY12, CX3CR1 and OLFML3 as intended.*

> TML macrophages are marked by TREM2, and share an expression profile with P2RY12, CX3CR1 and OLFML3; they also co-express CX3CR1 and SYT11.

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G12-tml-location — location, expect present

**Question** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Gold span** (paragraph 25 of 37)

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin

**The gold span in its paragraph**

> … odulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properties in mouse skin transplants and in fetal wounds,. TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a). This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin. Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact w …

**Opus/Fable** → `correct` — judge: *Names WNT2+ fibroblast co-location at 6-8 PCW, Schwann cells in ME1, and proximity to endothelial cells.*

> TML macrophages are found in early prenatal skin, where they are predicted to co-locate with WNT2+ fibroblasts (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1), and are seen close to endothelial cells.

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 28 — **not the gold span's paragraph (25)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g)

- *verbatim, paragraph 29 — **not the gold span's paragraph (25)***

  > multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**Sonnet** → `correct` — judge: *Reports co-location with WNT2+ fibroblasts and Schwann cells in ME1 as intended.*

> TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin and with Schwann cells in the 'early neurovascular microenvironment' (ME1).

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW)

- *verbatim, paragraph 28 — **not the gold span's paragraph (25)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G13-tml-function — function, expect present

**Question** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Gold span** (paragraph 28 of 37)

> contributing to synapse formation and axon guidance

**The gold span in its paragraph**

> …  1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin. TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

**Opus/Fable** → `correct` — judge: *Includes sprouting angiogenesis and the Schwann cell interaction for synapse formation and axon guidance; other roles are additive, not contradictory.*

> TML macrophages are yolk-sac derived, microglia-like cells implicated in immunomodulation and anti-fibrogenic/scarless healing (IL-6 regulation, GAS6-AXL signalling to fibroblasts), in supporting cutaneous neural development via interactions with Schwann cells, and in promoting sprouting angiogenesis.

- *verbatim, paragraph 25 — **not the gold span's paragraph (28)***

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

- *verbatim, paragraph 25 — **not the gold span's paragraph (28)***

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair

- *verbatim, paragraph 28 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1)

- *verbatim, paragraph 29 — **not the gold span's paragraph (28)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages

**Sonnet** → `correct` — judge: *Captures sprouting angiogenesis plus Schwann cell interaction for synapse formation and axon guidance.*

> TML macrophages are attributed roles in promoting sprouting angiogenesis and in interacting with Schwann cells to support synapse formation and axon guidance.

- *verbatim, paragraph 29 — **not the gold span's paragraph (28)***

  > sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages

- *verbatim, paragraph 28 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G14-dc-markers — markers, expect present

**Question** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Gold span** (paragraph 16 of 37)

> expressed FAM3C and EFNB1

**The gold span in its paragraph**

> ## HF mesenchymal differentiation The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8). Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig.  …

**Opus/Fable** → `correct` — judge: *Gives FOXD1+SOX2+ with the PDGFRA+FOXD1+SOX2low pre-Dc precursor and FAM3C/EFNB1.*

> The dermal condensate is annotated as FOXD1+SOX2+ (arising from PDGFRA+FOXD1+SOX2low pre-Dc cells) and expresses FAM3C and EFNB1, with COL6A3, MFAP4 and PTK7 expressed as pre-Dc cells aggregate into the Dc.

- *verbatim, paragraph 13 — **not the gold span's paragraph (16)***

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

- *verbatim, paragraph 16 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1

- *verbatim, paragraph 14 — **not the gold span's paragraph (16)***

  > Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc

**Sonnet** → `correct` — judge: *FOXD1 and SOX2 are the intended Dc markers.*

> The dermal condensate is marked by FOXD1 and SOX2.

- *verbatim, paragraph 13 — **not the gold span's paragraph (16)***

  > the Dc (FOXD1+SOX2+)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 10 of 37)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> … abasal IFE cells increased after 11 PCW, whereas POSTN+ basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b). Sebaceous and apocrine gland cells, which mature after 16 PCW, were not captured at these stages. Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation. Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Dermal compartment from 12 PCW abutting the epithelial hair placode, as intended.*

> The Dc sits in the dermal compartment of prenatal skin from 12 PCW, as a hair-follicle-specialized fibroblast aggregate abutting the epithelial hair placode; after invagination it becomes encapsulated at the follicle base as the dermal papilla.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 13 — **not the gold span's paragraph (10)***

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.

- *verbatim, paragraph 13 — **not the gold span's paragraph (10)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

**Sonnet** → `correct` — judge: *Dermal compartment from 12 PCW matches the intended location.*

> The dermal condensate is found within the dermal compartment, observed from 12 PCW alongside other HF-specialized fibroblasts and the dermal papilla.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (paragraph 16 of 37)

> have been reported to promote cell migration and invasion

**The gold span in its paragraph**

> ## HF mesenchymal differentiation The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8). Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells. Notably, the highlighted interactions were …

**Opus/Fable** → `correct` — judge: *Conveys Dc-placode crosstalk driving hair follicle formation and the FAM3C/EFNB1 migration-invasion point.*

> The Dc participates in mesenchymal-epithelial crosstalk driving hair follicle formation: its formation accompanies placode invagination, and it expresses FAM3C and EFNB1 predicted to signal to receptors on the placode and reported to promote cell migration and invasion. Prenatal hair follicle formation more broadly is initiated by interactions between epidermal placodes and dermal condensates.

- *verbatim, paragraph 16 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion, (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

- *verbatim, paragraph 1 — **not the gold span's paragraph (16)***

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

**Sonnet** → `correct` — judge: *Reports the FAM3C/EFNB1 migration and invasion role during placode invagination, part of the intended answer.*

> The Dc expresses FAM3C and EFNB1, predicted to interact with receptors on the placode (LAMP1/CXADR and EPHB6), interactions reported to promote cell migration and invasion during HF invagination.

- *verbatim, paragraph 16 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (paragraph 12 of 37)

> known matrix markers such as SHH and WNT10B, were upregulated

**The gold span in its paragraph**

> … and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration. Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *Names SHH and WNT10B as the known matrix markers, correctly scoped to hair matrix.*

> Matrix cells are identified as SHH+, with SHH and WNT10B described as known matrix markers upregulated along the IRS trajectory. Relative to adult hair follicles, prenatal matrix cells also show increased CXCL14 and CD24 expression.

- *verbatim, paragraph 10 — **not the gold span's paragraph (12)***

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a–c, Extended Data Fig. 3a,b and Supplementary Table 6).

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 11 — **not the gold span's paragraph (12)***

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).

**Sonnet** → `correct` — judge: *Correctly identifies hair matrix markers SHH and WNT10B, not the extracellular-matrix sense.*

> Hair matrix cells are marked by SHH, and SHH and WNT10B are described as known matrix markers.

- *verbatim, paragraph 10 — **not the gold span's paragraph (12)***

  > matrix (SHH+)

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > known matrix markers such as SHH and WNT10B, were upregulated

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 11 of 37)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell a …

**Opus/Fable** → `correct` — judge: *Hair follicle, arising from the epidermal placode, prenatal-specific and from 14 PCW - all present.*

> Matrix cells are hair follicle epithelial cells detected in prenatal skin from 14 PCW; they arise from the epidermal placode and lie overlying the dermal papilla. They are a prenatal-specific state absent from established adult hair follicles.

- *verbatim, paragraph 10 — **not the gold span's paragraph (11)***

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a–c, Extended Data Fig. 3a,b and Supplementary Table 6).

- *verbatim, paragraph 11 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

**Sonnet** → `correct` — judge: *Placing matrix cells overlying the dermal papilla is an accurate in-follicle location supported by the quote.*

> Hair matrix cells are located overlying the dermal papilla (Dp).

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 11 of 37)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). Treg cells are known to localize around the HF  …

**Opus/Fable** → `correct` — judge: *Gives the CXCL14/CD24 chemotaxis and Treg immune-protection role; added differentiation detail is also supported.*

> Matrix cells differentiate along the IRS trajectory towards cuticle/cortex and inner root sheath, and prenatal matrix cells express chemotactic and immune-regulatory genes (CXCL14, CD24) suggesting a role in Treg cell recruitment and immune protection during early matrix differentiation. Their differentiation is coordinated by Dp-derived signals (RSPO3, WNT5A), with RSPO3-LGR4/LGR6 contributing to proliferation of hair follicle epithelial cells.

- *verbatim, paragraph 11 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

- *verbatim, paragraph 14 — **not the gold span's paragraph (11)***

  > Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

**Sonnet** → `substituted` — judge: *Grounded quote but answers with RSPO3-LGR proliferation signalling instead of the intended chemotaxis and immune-protection role.*

> Matrix cells are predicted to receive RSPO3 signalling from the dermal papilla via LGR4/LGR6, contributing to proliferation of HF epithelial cells.

- *verbatim, paragraph 16 — **not the gold span's paragraph (11)***

  > Finally, RSPO3 from the Dp was predicted to interact with LGR4 and LGR6 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8) in overlying matrix cells to contribute to the proliferation of HF epithelial cells.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (paragraph 25 of 37)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**The gold span in its paragraph**

> …  macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a). This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin. Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *Identifies LYVE1 and GAS6 and correctly flags that no full marker panel is in the text.*

> The subset is named for LYVE1 expression and is one of four prenatal skin macrophage subsets; the only other gene the context states it expresses is GAS6 (shared with TML macrophages). No full marker panel is given.

- *verbatim, paragraph 29 — **not the gold span's paragraph (25)***

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23–26).

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Sonnet** → `correct` — judge: *GAS6 is one of the intended markers and body-text marker evidence is thin, so the partial answer stands.*

> GAS6 is expressed by LYVE1+ macrophages, according to the supplied context.

- *verbatim, paragraph 25 — same paragraph as the gold span*

  > GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G21-lyve1-location — location, expect present

**Question** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Gold span** (paragraph 29 of 37)

> showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**The gold span in its paragraph**

> … genesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27). Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1). Predicted ligand-receptor interactions were consistent with reciprocal communication between macrophages and endothelial cells to support angiogenesis, chemotaxis and cell migration (for example, CXCL8-ACKR1 and CCL8-ACKR1), (Extended Data Fig. 9a and Supplementary Table 28).

**Opus/Fable** → `correct` — judge: *Co-location with WNT2+ fibroblasts and imaging proximity to endothelial cells both given.*

> LYVE1+ macrophages are found in prenatal skin co-located with WNT2+ fibroblasts, and imaging placed LYVE1+ macrophages in close proximity to endothelial cells; macrophage subsets more generally were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct microenvironments in early gestation.

- *verbatim, paragraph 24 — **not the gold span's paragraph (29)***

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 29 — same paragraph as the gold span*

  > Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

- *verbatim, paragraph 24 — **not the gold span's paragraph (29)***

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).

**Sonnet** → `correct` — judge: *Co-location with WNT2+ fibroblasts and proximity to endothelial cells match the intended answer.*

> LYVE1+ macrophages co-locate with WNT2+ fibroblasts, and were also shown by imaging to lie in close proximity to endothelial cells.

- *verbatim, paragraph 24 — **not the gold span's paragraph (29)***

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

- *verbatim, paragraph 29 — same paragraph as the gold span*

  > multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G22-lyve1-function — function, expect present

**Question** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Gold span** (paragraph 29 of 37)

> blood vessel morphogenesis by LYVE1+ macrophages

**The gold span in its paragraph**

> … Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26). Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27). Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1+ and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1). Predicted lig …

**Opus/Fable** → `correct` — judge: *Sprouting angiogenesis, vessel morphogenesis and fibroblast maintenance via PDGF and GAS6-AXL all conveyed.*

> LYVE1+ macrophages are proposed to maintain prenatal skin dermal fibroblasts through PDGF, IGF1-IGF1R and GRN-EGFR interactions, and to promote angiogenesis - specifically sprouting angiogenesis and blood vessel morphogenesis. Their GAS6 is predicted to engage AXL on WNT2+ fibroblasts, an interaction linked to immunosuppression and tissue repair.

- *verbatim, paragraph 24 — **not the gold span's paragraph (29)***

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 29 — same paragraph as the gold span*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

- *verbatim, paragraph 25 — **not the gold span's paragraph (29)***

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Sonnet** → `correct` — judge: *Covers fibroblast maintenance plus blood vessel morphogenesis and sprouting angiogenesis.*

> LYVE1+ macrophages are proposed to help maintain dermal fibroblasts via growth factor signalling, and their gene expression programme is associated with blood vessel morphogenesis and sprouting angiogenesis.

- *verbatim, paragraph 24 — **not the gold span's paragraph (29)***

  > suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts

- *verbatim, paragraph 29 — same paragraph as the gold span*

  > blood vessel morphogenesis by LYVE1+ macrophages

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 22 of 37)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> … sets expressed high levels of inflammatory cytokines and receptors (for example, IL6 and IL1RA) and genes involved in antigen presentation (for example, HLA-A), innate immune and inflammatory responses (for example, CD55 and PTGES) and cellular senescence (CDKN1A) (Fig. 3a and Supplementary Tables 13-15). By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Subset-specific marker answer is licensed by the hazard note and it captures the COL13A1-negative point.*

> Prenatal skin fibroblast subsets are defined by HOXC5 (early fibroblasts), WNT2, PEAR1 and FRZB; hair-specialized fibroblasts are marked by PDGFRA/FOXD1/SOX2low (pre-Dc), FOXD1+SOX2+ (Dc) and NDP+SOX2+ (Dp). Human prenatal fibroblasts did not significantly express the papillary fibroblast marker COL13A1.

- *verbatim, paragraph 14 — **not the gold span's paragraph (22)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

- *verbatim, paragraph 13 — **not the gold span's paragraph (22)***

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.

- *verbatim, paragraph 13 — **not the gold span's paragraph (22)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

- *verbatim, paragraph 18 — **not the gold span's paragraph (22)***

  > Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1) (Extended Data Fig. 5j), which suggested that the distinction between papillary and reticular fibroblasts emerges after 17 PCW.

**Sonnet** → `miss`

> The supplied context does not give marker genes for fibroblasts as a general cell type (only for specific fibroblast subsets).

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G24-fibroblast-location — location, expect present

**Question** Where in prenatal human skin is fibroblast found?

**Intended answer** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Gold span** (paragraph 14 of 37)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Dermal compartment, HOXC5+ in upper dermis, Dc/Dp from 12 PCW - matches intended.*

> Fibroblasts are dermal cells: HOXC5+ early fibroblasts sit in the upper dermis, and hair-specialized fibroblasts (Dc, Dp) are found in the dermal compartment from 12 PCW; dermal condensates are aggregates of dermal fibroblasts abutting the epidermal placode. Mesoderm-derived cells including skin fibroblasts are present throughout gestation.

- *verbatim, paragraph 14 — same paragraph as the gold span*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

- *verbatim, paragraph 10 — **not the gold span's paragraph (14)***

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 5 — **not the gold span's paragraph (14)***

  > Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *Dermal compartment with HOXC5+ fibroblasts in the upper dermis matches the intended answer.*

> Fibroblasts are found within the dermal compartment, including HOXC5+ early fibroblasts located in the upper dermis.

- *verbatim, paragraph 10 — **not the gold span's paragraph (14)***

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW.

- *verbatim, paragraph 14 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (paragraph 27 of 37)

> may favour tissue regeneration over scarring

**The gold span in its paragraph**

> ## Scarless healing and potential macrophage contribution Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to  …

**Opus/Fable** → `correct` — judge: *States the regeneration-over-scarring conclusion with the ECM/collagen/inflammation downregulation.*

> Fibroblasts produce the collagen whose aggregation causes scars, and prenatal fibroblasts instead upregulate immune suppression, inflammation regulation and tissue regeneration genes, which may favour scarless healing before they progressively acquire scar-promoting, pro-inflammatory profiles in later gestation. Hair-specialized fibroblasts also drive hair follicle morphogenesis through crosstalk with epidermal cells, including CXCL12-ACKR3-mediated pre-Dc migration.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13–15).

- *verbatim, paragraph 27 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

- *verbatim, paragraph 13 — **not the gold span's paragraph (27)***

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).

**Sonnet** → `substituted` — judge: *Quote is real background about scarring but the answer is a different claim than the paper's finding on early fibroblast downregulation of ECM and inflammation.*

> The paper attributes collagen production to dermal fibroblasts, noting that aggregation of this collagen (along with failed epidermal regeneration) is what produces scars.

- *verbatim, paragraph 22 — **not the gold span's paragraph (27)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G26-periderm-location — location, expect present

**Question** Where in prenatal human skin is periderm found?

**Intended answer** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Gold span** (paragraph 9 of 37)

> with the periderm seen sloughing from 11 PCW

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Opus/Fable** → `correct` — judge: *Outermost epidermal layer over dermal stroma, from 7 PCW, sloughing from 11 PCW.*

> Periderm is an ectoderm-derived immature interfollicular epidermal cell type of prenatal skin, present from 7 PCW and enriched in early gestation; it overlies the dermal stroma as part of the epidermal layer and is seen sloughing from 11 PCW.

- *verbatim, paragraph 5 — **not the gold span's paragraph (9)***

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 10 — **not the gold span's paragraph (9)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Correct on early-gestation presence from 7 PCW and sloughing from 11 PCW, omitting only the outermost-layer wording.*

> Periderm is one of the immature interfollicular epidermal cell types present from 7 PCW, and it sloughs off starting at 11 PCW.

- *verbatim, paragraph 10 — **not the gold span's paragraph (9)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > with the periderm seen sloughing from 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G27-periderm-function — function, expect present

**Question** What function does the paper attribute to periderm?

**Intended answer** Constitutes the first skin permeability barrier.

**Gold span** (paragraph 5 of 37)

> the periderm, which constitutes the first skin permeability barrier

**The gold span in its paragraph**

> … fine-grained annotations of cell states were assigned on the basis of differentially expressed genes (DEGs) (Fig. 1b, Extended Data Fig. 1c and Supplementary Table 3). Differential abundance analysis testing revealed how different cell populations varied across gestation. Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extende …

**Opus/Fable** → `correct` — judge: *Exactly the first skin permeability barrier.*

> The periderm constitutes the first skin permeability barrier.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *States the first skin permeability barrier, exactly the intended function.*

> The periderm constitutes the first permeability barrier of the skin.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 9 of 37)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Gives the layer description and sloughing observation and notes nothing further is said.*

> The only morphological statement is histological: the periderm is seen sloughing from 11 PCW, above the layer of epidermal cells overlying the dermal stroma; it is classed as an immature interfollicular epidermal cell state. No further structural description is given.

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 10 — **not the gold span's paragraph (9)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *The sloughing observation is the substance of the thin structural evidence the paper offers.*

> The periderm is described as sloughing off from 11 PCW, a structural/morphological change in the epidermal layer.

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > with the periderm seen sloughing from 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G29-hoxc5-location — location, expect present

**Question** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** The upper dermis.

**Gold span** (paragraph 14 of 37)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

- *verbatim, paragraph 14 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

**Sonnet** → `correct` — judge: *Upper dermis matches the intended answer.*

> HOXC5+ early fibroblasts are located in the upper dermis.

- *verbatim, paragraph 14 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G30-hoxc5-function — function, expect present

**Question** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Gold span** (paragraph 18 of 37)

> originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**The gold span in its paragraph**

> … acode specification, bone morphogenetic protein (BMP) and noggin to inhibit hair formation in IFE cells, and PDGFA and TGFβ signalling for HF down growth (Extended Data Fig. 5f). Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast) (Fig. 2e and Extended Data Fig. 4d). However, cross-species data integration of human and mouse HF showed that human pre-Dc cells and the Dc aligned not only to their counterparts in mouse skin but also to fibroblasts in earlier stages of differentiation (Extended Data Fig. 5g-i and Supplementary Tables 10 and 11). Th …

**Opus/Fable** → `correct` — judge: *States the common fibroblast progenitor role and both trajectories exactly as intended.*

> They act as a common fibroblast progenitor, differentiating along a hair fibroblast trajectory (pre-Dc, Dc and Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

- *verbatim, paragraph 14 — **not the gold span's paragraph (18)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 18 — same paragraph as the gold span*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**Sonnet** → `correct` — judge: *Identifies the common fibroblast progenitor with both hair and dermal trajectories.*

> HOXC5+ early fibroblasts act as a common fibroblast progenitor that gives rise to hair-specialized fibroblasts (pre-Dc, Dc, Dp) and dermal fibroblasts (WNT2+ and PEAR1+ fibroblasts).

- *verbatim, paragraph 18 — same paragraph as the gold span*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G31-dpysl2-markers — markers, expect present

**Question** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Gold span** (paragraph 12 of 37)

> we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**The gold span in its paragraph**

> … ed prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2,  …

**Hazard note given to the judge** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Opus/Fable** → `correct` — judge: *Gives DPYSL2 and AGR2 as the newly identified gene without claiming BARX2/SOX9 as new.*

> Mature basal interfollicular epidermal cells are marked by DPYSL2, and AGR2 is newly identified as upregulated by DPYSL2+ basal cells along the ORS/CL trajectory.

- *verbatim, paragraph 10 — **not the gold span's paragraph (12)***

  > Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

**Sonnet** → `correct` — judge: *Gives DPYSL2 and AGR2 as newly identified, avoiding the BARX2/SOX9 attribution trap.*

> DPYSL2+ basal cells are marked by DPYSL2, and along the ORS/CL trajectory they upregulate AGR2.

- *verbatim, paragraph 10 — **not the gold span's paragraph (12)***

  > Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (paragraph 12 of 37)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Exten …

**Opus/Fable** → `correct` — judge: *Places the cell type on the ORS/CL trajectory downstream of POSTN+ basal cells as intended.*

> DPYSL2+ basal cells are an intermediate state on the ORS/CL differentiation trajectory downstream of POSTN+ basal cells, upregulating AGR2 and genes related to outer root sheath differentiation.

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

**Sonnet** → `miss`

> The supplied context does not state a function for DPYSL2+ basal cells; it only notes them as a marker-defined mature basal cell population and mentions AGR2 (a gene they upregulate) promoting cell migration, but no function is attributed to the DPYSL2+ basal cells themselves.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G33-caparteriole-markers — markers, expect present

**Question** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Gold span** (paragraph 32 of 37)

> their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin

**The gold span in its paragraph**

> … re highly expressed in SkO, whereas pro-angiogenic genes (for example, CXCL8) were upregulated in prenatal skin and primarily expressed by macrophages (Extended Data Fig. 11a and Supplementary Tables 30-34). Although expression of vascular endothelial growth factors (VEGF), VEGFA and VEGFB were increased in SkO cells, their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin (Extended Data Fig. 11b,c). These receptors are known downstream targets of GATA2, which has a key role in angiogenesis during development and regulates VEGF-induced endothelial cell migration and sprouting in vitro. Regulon analysis showed that GATA2 and related regulons (for example, NFATC1) were downregulated in Sk …

**Opus/Fable** → `miss`

> The supplied context does not give marker genes specific to capillary arteriole cells.

*No quotes given.*

**Sonnet** → `correct` — judge: *GJA5 arteriolar identity is accurate, a partial answer omitting the organoid comparison genes.*

> Capillary arterioles belong to the arteriolar differentiation pathway, characterised by expression of GJA5.

- *verbatim, paragraph 30 — **not the gold span's paragraph (32)***

  > early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a–c).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G34-caparteriole-function — function, expect present

**Question** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 30 of 37)

> prenatal skin capillary arteriole cells could further differentiate into arterioles

**The gold span in its paragraph**

> … ted into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid, which also lacked immune cells, further demonstrated the limited vasculature differentiation of this mesoderm-geared blood vessel organoid model (Extended Data Fig. 10d). This result con …

**Opus/Fable** → `correct` — judge: *Conveys both the further differentiation into arterioles (unlike SkO) and the raised tip-cell score.*

> Capillary arteriole cells lie on the arteriolar differentiation pathway and in prenatal skin can differentiate further into arterioles; they also show an increased sprouting angiogenesis 'tip' cell signature, though SkO capillary arterioles cannot guide stalk cells for new vessel formation.

- *verbatim, paragraph 30 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles

- *verbatim, paragraph 31 — **not the gold span's paragraph (30)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

**Sonnet** → `correct` — judge: *Reports the tip-cell sprouting angiogenesis scoring, part of the intended answer.*

> The paper reports that capillary arteriole cells (in both SkO and prenatal skin) show increased sprouting angiogenesis potential, based on scoring of the 'tip' cell state.

- *verbatim, paragraph 31 — **not the gold span's paragraph (30)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (paragraph 23 of 37)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**The gold span in its paragraph**

> …  healing and potential macrophage contribution The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extrace …

**Opus/Fable** → `correct` — judge: *Names PEAR1 plus the pro-inflammatory APOE/IGFBP7/ITM2A set, with supported extra genes.*

> Beyond PEAR1 itself, the transition into PEAR1+ fibroblasts upregulates pro-inflammatory genes APOE, IGFBP7 and ITM2A, and PEAR1+ fibroblasts express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

**Sonnet** → `correct` — judge: *PEAR1 plus APOE, IGFBP7 and ITM2A match the intended markers.*

> PEAR1+ fibroblasts are defined by PEAR1, and genes such as APOE, IGFBP7 and ITM2A are upregulated during the transition into this state.

- *verbatim, paragraph 14 — **not the gold span's paragraph (23)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 23 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (paragraph 14 of 37)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**The gold span in its paragraph**

> … lysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7). Along the hair fibroblast pseudotime, genes involved in regulation of cell adhesion (ADAMST1), cell-cell contacts (CLDN11) and directed migration (CXCL12) were upregulated as pre-Dc cells migrated towards the epidermis, which indicated a process of co …

**Opus/Fable** → `correct` — judge: *Captures the later-gestation dermal endpoint with adult pro-inflammatory, senescence and collagen genes.*

> PEAR1+ fibroblasts, abundant in later gestation, carry the adult-like pro-inflammatory and scar-promoting profile, expressing senescence, cytokine and collagen-deposition genes seen in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 23 — **not the gold span's paragraph (14)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 23 — **not the gold span's paragraph (14)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

**Sonnet** → `correct` — judge: *Senescence, cytokine and collagen deposition programme matches the intended pro-inflammatory endpoint profile.*

> PEAR1+ fibroblasts (together with WNT2+ fibroblasts) express genes involved in cellular senescence, cytokine pathways and collagen deposition, resembling genes highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 23 — **not the gold span's paragraph (14)***

  > WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G38-postn-function — function, expect present

**Question** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Gold span** (paragraph 12 of 37)

> may be involved in placode specification and dermal invagination

**The gold span in its paragraph**

> … ory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration. Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Opus/Fable** → `correct` — judge: *Gives both the ORS/CL and IRS trajectory origin and the migration/placode-invagination role.*

> POSTN+ basal cells are the predicted origin of both the ORS/CL and IRS epidermal trajectories, and their increased cellular migration is suggested to contribute to placode specification and dermal invagination.

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Sonnet** → `correct` — judge: *Increased migration contributing to placode specification and dermal invagination is the intended point.*

> POSTN+ basal cells show increased cellular migration that may contribute to placode specification and dermal invagination.

- *verbatim, paragraph 12 — same paragraph as the gold span*

  > increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G39-arteriole-markers — markers, expect present

**Question** Which genes mark arteriole?

**Intended answer** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Gold span** (paragraph 30 of 37)

> for example, GJA5 for arteriolar and PLVAP for venular

**The gold span in its paragraph**

> … ata Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid, which also lacked immun …

**Hazard note given to the judge** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Opus/Fable** → `correct` — judge: *Identifies GJA5 as the characteristic arteriolar gene, correctly attributed to the arteriolar pathway.*

> GJA5 is given as a characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles).

- *verbatim, paragraph 30 — same paragraph as the gold span*

  > early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

**Sonnet** → `correct` — judge: *GJA5 is correctly attributed to the arteriolar pathway as intended.*

> GJA5 is given as the characteristic gene for the arteriolar pathway.

- *verbatim, paragraph 30 — same paragraph as the gold span*

  > with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 30 of 37)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *States the arteriolar pathway endpoint and the sprouting angiogenesis tip-cell scoring.*

> Arterioles are the endpoint of the arteriolar differentiation pathway from early endothelial cells and show increased sprouting angiogenesis ('tip' cell state) potential in prenatal skin.

- *verbatim, paragraph 30 — same paragraph as the gold span*

  > early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules)

- *verbatim, paragraph 31 — **not the gold span's paragraph (30)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

**Sonnet** → `correct` — judge: *Tip-cell sprouting angiogenesis scoring in prenatal skin arterioles is part of the intended answer.*

> The paper reports that sprouting angiogenesis potential (scored via a 'tip' cell state) was increased in prenatal skin arteriole cells (along with capillary arteriole and capillary cells).

- *verbatim, paragraph 31 — **not the gold span's paragraph (30)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G41-cuticle-location — location, expect present

**Question** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** Part of the inner layers of the hair follicle.

**Gold span** (paragraph 10 of 37)

> part of the inner layers of the HF

**The gold span in its paragraph**

> ## Epidermal placode and matrix formation Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embry …

**Opus/Fable** → `correct` — judge: *Correctly places cuticle/cortex in the inner layers of the hair follicle.*

> Cuticle and cortex cells form part of the inner layers of the hair follicle, identified in HF cells from 14 PCW.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `correct` — judge: *Inner layers of the hair follicle matches the intended location.*

> Cuticle/cortex cells are part of the inner layers of the hair follicle.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G45-dermal-condensate-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `overreach` — judge: *Presents aggregation and encapsulation as a morphological description rather than declining.*

> The dermal condensate is described structurally as an aggregate of dermal fibroblasts that abuts the epithelial hair placode, and after hair follicle invagination it becomes encapsulated at its base to form the dermal papilla.

- *verbatim, paragraph 1*

  > dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 13*

  > the Dc becomes encapsulated at its base as the Dp

**Sonnet** → `overreach` — judge: *Presents Dc encapsulation at the base as a structural description when the paper offers no morphology.*

> The paper states that following HF invagination, the dermal condensate becomes encapsulated at its base as it forms the dermal papilla.

- *verbatim, paragraph 13*

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct` — judge: *Notes the statement is merely positional and says no morphological detail is given.*

> The only structural statement is positional: cuticle and cortex cells are described as forming part of the inner layers of the hair follicle. No morphological detail beyond this is given.

- *verbatim, paragraph 10*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `overreach` — judge: *Offers a positional statement as a structural description without noting that morphology is not described.*

> Cuticle/cortex cells are described as part of the inner layers of the hair follicle.

- *verbatim, paragraph 10*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/whole/shared.txt`*

---

## Context: local

### G01-placode-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Gold span** (paragraph 1 of 11)

> epidermal placodes (focal sites of epidermal layer thickening)

**The gold span in its paragraph**

> … rm (apart from facial and cranial skin, where it arises from ectoderm-derived neural crest cells). The skin appendages, which include hair follicles (HFs) and sebaceous glands, form in a cephalocaudal direction. Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

**Opus/Fable** → `correct` — judge: *Describes the focal epidermal thickening and basal cell budding as intended.*

> The placode is described as a focal thickening of the epidermal layer, seen histologically at 14-15 PCW as budding of basal cells that precedes elongation of the hair follicle into hair pegs.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

**Sonnet** → `correct` — judge: *Focal epidermal thickening is the main structural point, partial but accurate.*

> The hair placode is described as a focal site of epidermal layer thickening.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > epidermal placodes (focal sites of epidermal layer thickening)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G01-placode-structure.txt`*

---

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (paragraph 5 of 10)

> which abuts the epithelial hair placode

**The gold span in its paragraph**

> We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,. Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

**Opus/Fable** → `correct` — judge: *Places the placode in the epidermis at focal thickenings abutted from below by the dermal condensate.*

> The placode is an epidermal structure — a focal thickening of the epidermal layer — that is abutted from below by the dermal condensate; placode cells were identified among hair follicle cells in scRNA-seq data from 14 PCW.

- *verbatim, paragraph 1 — **not the gold span's paragraph (5)***

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

- *verbatim, paragraph 3 — **not the gold span's paragraph (5)***

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells

**Sonnet** → `correct` — judge: *Locates the placode in the epidermis arising by budding of basal cells, as intended.*

> The hair placode is an epidermal structure, arising via budding of basal cells in the epidermis, described in the paper as the 'epidermal placode.'

- *verbatim, paragraph 2 — **not the gold span's paragraph (5)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

- *verbatim, paragraph 4 — **not the gold span's paragraph (5)***

  > hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G02-placode-location.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 2 of 11)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity ( …

**Opus/Fable** → `correct` — judge: *Names the placode as origin of hair matrix cells, WNT/EDA specification and dermal condensate signalling during invagination, matching the intended answer.*

> The placode is the epidermal origin of hair matrix cells and the first step of the IRS differentiation trajectory; its specification is linked to increased cellular migration in POSTN+ basal cells and to WNT and EDA signalling, and it receives dermal condensate signals (FAM3C and EFNB1 acting on LAMP1/CXADR and EPHB6) as invagination proceeds.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

- *verbatim, paragraph 4 — **not the gold span's paragraph (2)***

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 9 — **not the gold span's paragraph (2)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode

- *verbatim, paragraph 10 — **not the gold span's paragraph (2)***

  > Similar signalling pathways were upregulated, including WNT and EDA for hair placode specification

**Sonnet** → `substituted` — judge: *Quotes are real but the answer is about Dc and Dp signalling rather than the placode initiating hair follicle formation.*

> The Dc's interaction with the placode (via FAM3C/EFNB1 and receptors on the placode) has been reported to promote cell migration and invasion, and RSPO3 from the dermal papilla interacts with matrix cells overlying the placode to contribute to proliferation of HF epithelial cells, which includes the placode-derived matrix.

- *verbatim, paragraph 9 — **not the gold span's paragraph (2)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G03-placode-function.txt`*

---

### G06-macrophage-location — location, expect present

**Question** Where in prenatal human skin is macrophage found?

**Intended answer** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Gold span** (**not in this context** — the retriever never supplied it)

> Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’

**Opus/Fable** → `correct` — judge: *Gives the 6 PCW seeding and the co-location with fibroblasts, neural and vascular cells in distinct early-gestation microenvironments, matching the intended answer even without naming ME1/ME5.*

> The context does not give a strict anatomical compartment, but it states macrophages seed prenatal skin from as early as 6 PCW and that macrophage subsets were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation, with LYVE1+ macrophages specifically co-located with WNT2+ fibroblasts.

- *verbatim, paragraph 3*

  > immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes

- *verbatim, paragraph 6*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).

- *verbatim, paragraph 6*

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

**Sonnet** → `correct` — judge: *Seeding from 6 PCW and co-location with fibroblasts, neural and vascular cells match the intended answer.*

> Macrophages seed the skin as early as 6 PCW, co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation.

- *verbatim, paragraph 3*

  > immune cells such as macrophages seed the skin as early as 6 PCW and express a range of pro-inflammatory genes

- *verbatim, paragraph 6*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G06-macrophage-location.txt`*

---

### G07-macrophage-function — function, expect present

**Question** What function does the paper attribute to macrophage?

**Intended answer** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Gold span** (**not in this context** — the retriever never supplied it)

> Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Opus/Fable** → `correct` — judge: *Covers angiogenesis, scarless healing, fibroblast maintenance and neurovascular development, all four intended roles.*

> The paper attributes to macrophages non-immune roles in skin morphogenesis: maintenance of dermal fibroblasts (via PDGF, IGF1-IGF1R, GRN-EGFR and GAS6-AXL interactions), a contribution to scarless wound healing (supported by an in vitro scratch assay), and promotion of angiogenesis and neurovascular development; antigen presentation is suggested not to be a key early function.

- *verbatim, paragraph 10*

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 11*

  > This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin.

- *verbatim, paragraph 12*

  > we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g)

- *verbatim, paragraph 13*

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23–26).

- *verbatim, paragraph 3*

  > Decoupling of the expression of pro-inflammatory genes from MHCII genes before 11 PCW suggests that antigen presentation may not be a key function of human macrophages during early gestation.

**Sonnet** → `correct` — judge: *Wound healing support and angiogenesis-driving programmes align with the intended repair and angiogenesis roles.*

> Macrophages support wound healing (improving scratch-wound closure of co-cultured fibroblasts) and, across their four subsets, express gene programs that drive angiogenesis.

- *verbatim, paragraph 12*

  > Using a scratch assay of SkO-derived fibroblasts cultured with or without iPS cell-derived macrophages, we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g).

- *verbatim, paragraph 13*

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23–26).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G07-macrophage-function.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (paragraph 7 of 10)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**The gold span in its paragraph**

> … ted during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

**Opus/Fable** → `correct` — judge: *Gives WNT2, COL1A1/ECM late, SFRP1 early, plus CDKN1A, IL1R1 and POSTN; only the IL6 downregulation is omitted.*

> The context names WNT2 in the subset's label and reports genes expressed or upregulated in these cells rather than a formal defining marker panel: COL1A1 in late-gestation WNT2+ fibroblasts, SFRP1 in early WNT2+ fibroblasts, and CDKN1A, IL1R1 and POSTN in WNT2+ (and PEAR1+) prenatal fibroblasts.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

**Sonnet** → `correct` — judge: *WNT2 plus the early/late split and CDKN1A, IL1R1, POSTN match the intended markers.*

> WNT2+ fibroblasts are marked by the gene WNT2 itself, and depending on gestational age express COL1A1 (late) or SFRP1 (early); together with PEAR1+ fibroblasts they also express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G08-wnt2fib-markers.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (paragraph 7 of 10)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**The gold span in its paragraph**

> … e of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as s …

**Opus/Fable** → `correct` — judge: *Dermal location with LYVE1+ macrophage co-location is accurate; omitting the TML co-location is a permitted partial.*

> They are a dermal fibroblast subset, arising on the dermal fibroblast trajectory and abundant after 11 PCW; spatially they are described by co-location with LYVE1+ macrophages. The context gives no finer dermal compartment (e.g. upper versus lower dermis) for them.

- *verbatim, paragraph 1 — **not the gold span's paragraph (7)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

**Sonnet** → `miss`

> The supplied context does not give a spatial location for WNT2+ fibroblasts, only their temporal abundance and gene expression.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G09-wnt2fib-location.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (paragraph 5 of 10)

> we observed differences within the WNT2+ fibroblast population across gestation time

**The gold span in its paragraph**

> … b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary  …

**Opus/Fable** → `correct` — judge: *ECM/collagen deposition late, growth and differentiation early, and acquisition of a pro-inflammatory/senescence profile are all conveyed.*

> Late-gestation WNT2+ fibroblasts are linked to extracellular matrix and collagen deposition and to scar-promoting/pro-inflammatory programs, while early WNT2+ fibroblasts show growth and differentiation genes and downregulated IL6, which the paper connects to scarless healing; they also receive macrophage signals.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 6 — **not the gold span's paragraph (5)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 8 — **not the gold span's paragraph (5)***

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

**Sonnet** → `correct` — judge: *Late-gestation ECM and collagen deposition versus early growth and differentiation is the intended function.*

> WNT2+ fibroblasts show gestation-dependent gene expression: in late gestation they upregulate extracellular matrix and collagen deposition genes, while in early gestation they upregulate genes involved in cellular growth and differentiation.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G10-wnt2fib-function.txt`*

---

### G11-tml-markers — markers, expect present

**Question** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Gold span** (paragraph 5 of 11)

> Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia

**The gold span in its paragraph**

> We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f). Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properti …

**Opus/Fable** → `correct` — judge: *TREM2 plus the microglia-like P2RY12/CX3CR1/OLFML3 profile is exactly the intended panel.*

> TML macrophages are TREM2+ and share a microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

**Sonnet** → `correct` — judge: *Names TREM2 plus P2RY12, CX3CR1 and OLFML3; the extra SYT11 is supported by the second quote.*

> TML macrophages are marked by TREM2, and share an expression profile with microglia-like macrophages including P2RY12, CX3CR1 and OLFML3; they also co-express CX3CR1 and SYT11.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f).

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19–23).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G11-tml-markers.txt`*

---

### G12-tml-location — location, expect present

**Question** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Gold span** (paragraph 5 of 11)

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin

**The gold span in its paragraph**

> … odulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properties in mouse skin transplants and in fetal wounds,. TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

**Opus/Fable** → `correct` — judge: *Reports both WNT2+ fibroblast co-location at 6-8 PCW and Schwann cell co-location in ME1.*

> TML macrophages are located in prenatal skin where they are predicted to co-locate with WNT2+ fibroblasts in early gestation (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1).

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 8 — **not the gold span's paragraph (5)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g)

**Sonnet** → `correct` — judge: *Gives both the WNT2+ fibroblast and Schwann cell/ME1 co-locations.*

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin, and separately with Schwann cells within an 'early neurovascular microenvironment' of prenatal skin.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 8 — **not the gold span's paragraph (5)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G12-tml-location.txt`*

---

### G13-tml-function — function, expect present

**Question** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Gold span** (paragraph 7 of 11)

> contributing to synapse formation and axon guidance

**The gold span in its paragraph**

> …  1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin. TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

**Opus/Fable** → `correct` — judge: *States sprouting angiogenesis and Schwann cell interaction in synapse formation and axon guidance, the two intended functions.*

> The paper attributes to TML macrophages immunomodulatory/anti-fibrogenic signalling supporting scarless healing (including GAS6-AXL interactions with WNT2+ fibroblasts), support of peripheral nervous system development via Schwann cell interactions in synapse formation and axon guidance, and promotion of sprouting angiogenesis.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages

**Sonnet** → `correct` — judge: *Covers sprouting angiogenesis and the Schwann cell synapse/axon guidance interaction.*

> TML macrophages are predicted to interact with Schwann cells to support synapse formation and axon guidance, and along with LYVE1+ macrophages promote sprouting angiogenesis, contributing to establishment of the peripheral nervous system and vascular development in prenatal skin.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1) (Extended Data Fig. 8h and Supplementary Table 8).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G13-tml-function.txt`*

---

### G14-dc-markers — markers, expect present

**Question** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Gold span** (**not in this context** — the retriever never supplied it)

> expressed FAM3C and EFNB1

**Opus/Fable** → `correct` — judge: *Identifies the Dc as FOXD1+SOX2+ via mouse orthologues, the key intended marker pair.*

> The Dc is defined by the mouse orthologous markers FOXD1 and SOX2 (FOXD1+SOX2+), which were used to annotate it in human prenatal skin; COL6A3, MFAP4 and PTK7 are expressed as pre-Dc cells aggregate into the Dc.

- *verbatim, paragraph 6*

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,.

- *verbatim, paragraph 8*

  > Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc

**Sonnet** → `correct` — judge: *FOXD1+SOX2+ is the main point, accurate as far as it goes.*

> The dermal condensate (Dc) is marked by FOXD1 and SOX2 (FOXD1+SOX2+), based on orthologous mouse marker genes.

- *verbatim, paragraph 6*

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G14-dc-markers.txt`*

---

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 4 of 10)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation. Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Dermal compartment from 12 PCW abutting the epithelial hair placode matches the intended answer.*

> The dermal condensate sits in the dermal compartment of prenatal skin, observed from 12 PCW, and lies immediately beneath/abutting the epithelial hair placode; after hair follicle invagination it becomes encapsulated at the follicle base as the dermal papilla.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 5 — **not the gold span's paragraph (4)***

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,.

- *verbatim, paragraph 5 — **not the gold span's paragraph (4)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

**Sonnet** → `correct` — judge: *Dermal compartment from 12 PCW, abutting the epithelial hair placode.*

> The dermal condensate is found within the dermal compartment of prenatal skin, from 12 PCW onward, where it abuts the epithelial hair placode.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

- *verbatim, paragraph 5 — **not the gold span's paragraph (4)***

  > which abuts the epithelial hair placode

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G15-dc-location.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (**not in this context** — the retriever never supplied it)

> have been reported to promote cell migration and invasion

**Opus/Fable** → `correct` — judge: *Conveys aggregation from pre-Dc cells and dermal-epidermal crosstalk in hair follicle development; omission of FAM3C/EFNB1 migration detail is a partial, not an error.*

> The Dc is presented as a hair-follicle-specialised dermal population that takes part in dermal–epidermal crosstalk during hair follicle development: it forms by aggregation of pre-Dc cells next to the epithelial hair placode and subsequently becomes the dermal papilla, which expresses genes coordinating differentiation of adjacent hair matrix cells.

- *verbatim, paragraph 7*

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c).

- *verbatim, paragraph 7*

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

- *verbatim, paragraph 9*

  > Genes implicated in collagen fibril formation and cell adhesion (COL6A3, MFAP4 and PTK7) were expressed as the pre-Dc cells aggregated into the Dc (Extended Data Fig. 4f and Supplementary Table 7).

**Sonnet** → `honest_miss`

> The supplied context describes formation and origin of the dermal condensate but does not state a function attributed to it.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G16-dc-function.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (paragraph 3 of 11)

> known matrix markers such as SHH and WNT10B, were upregulated

**The gold span in its paragraph**

> … and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration.

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *Names SHH and WNT10B as known hair matrix markers, correctly avoiding the extracellular-matrix sense.*

> SHH and WNT10B are cited as known matrix markers, upregulated along the IRS trajectory. Compared with adult hair follicles, prenatal matrix cells also showed increased expression of CXCL14 and CD24.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 2 — **not the gold span's paragraph (3)***

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).

**Sonnet** → `correct` — judge: *SHH and WNT10B named as known hair matrix markers, matching the intended answer.*

> The paper identifies SHH and WNT10B as known markers of the hair matrix.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > known matrix markers such as SHH and WNT10B, were upregulated

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G17-matrix-markers.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 4 of 11)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell a …

**Opus/Fable** → `miss`

> The supplied context does not state where in prenatal skin hair matrix cells are located; it only says they arise from the epidermal placode and are a prenatal-specific state absent from established adult hair follicles.

*No quotes given.*

**Sonnet** → `correct` — judge: *Placode origin and prenatal-specific state are accurate; omitting 14 PCW is only detail.*

> Hair matrix cells arise from the epidermal placode and are a prenatal-specific cell state not found in established adult hair follicles.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G18-matrix-location.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 2 of 11)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). Treg cells are known to localize around the HF  …

**Opus/Fable** → `correct` — judge: *Reports chemotaxis genes CXCL14 and CD24 and the inferred Treg accumulation and immune protection role.*

> Matrix cells are an epidermal-placode-derived, prenatal-specific state on the IRS differentiation trajectory (placode to matrix to cuticle/cortex to IRS). Their raised chemotaxis and autoimmunity-control gene expression is interpreted as a role in Treg cell accumulation and immune protection during early matrix differentiation, and their differentiation is coordinated by dermal papilla genes.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e).

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

- *verbatim, paragraph 6 — **not the gold span's paragraph (2)***

  > Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

**Sonnet** → `correct` — judge: *CXCL14-mediated Treg recruitment and immune protection during matrix differentiation.*

> The paper suggests that prenatal hair matrix cells, through increased expression of the chemokine CXCL14, may recruit regulatory T (Treg) cells, pointing to a potential role in Treg cell accumulation and immune protection during early matrix differentiation.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24).

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G19-matrix-function.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (paragraph 4 of 10)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**The gold span in its paragraph**

> This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin. Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *Gives LYVE1 and GAS6 and correctly notes the body text offers no fuller marker panel.*

> The context gives no marker gene list for this subset; besides LYVE1 in the subset's own name, the only gene explicitly stated to be expressed by LYVE1+ macrophages is GAS6 (shared with TML macrophages).

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Sonnet** → `correct` — judge: *LYVE1 is the main marker; omitting GAS6 is a partial but accurate answer.*

> The only gene explicitly indicated in the supplied context as marking this macrophage population is LYVE1 itself, as reflected in the population's name throughout the text.

- *verbatim, paragraph 3 — **not the gold span's paragraph (4)***

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G20-lyve1-markers.txt`*

---

### G21-lyve1-location — location, expect present

**Question** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Gold span** (**not in this context** — the retriever never supplied it)

> showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**Opus/Fable** → `correct` — judge: *Names co-location with WNT2+ fibroblasts and proximity to endothelial cells, matching the intended answer.*

> LYVE1+ macrophages are predicted to co-locate with WNT2+ fibroblasts in prenatal skin; more broadly, macrophage subsets co-locate with fibroblasts, neural and vascular cells in distinct tissue microenvironments in early gestation, including with endothelial cells in the early and late neurovascular microenvironments.

- *verbatim, paragraph 3*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 3*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).

- *verbatim, paragraph 8*

  > Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells (‘early and late neurovascular microenvironments’, ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).

**Sonnet** → `correct` — judge: *Co-location with WNT2+ fibroblasts is the main point, accurate as far as it goes.*

> LYVE1+ macrophages co-locate with WNT2+ fibroblasts.

- *verbatim, paragraph 3*

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G21-lyve1-location.txt`*

---

### G22-lyve1-function — function, expect present

**Question** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Gold span** (paragraph 8 of 12)

> blood vessel morphogenesis by LYVE1+ macrophages

**The gold span in its paragraph**

> … Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26). Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

**Opus/Fable** → `correct` — judge: *Covers both sprouting angiogenesis/vessel morphogenesis and maintenance of dermal fibroblasts via growth-factor interactions.*

> LYVE1+ macrophages are attributed a role in maintaining prenatal skin dermal fibroblasts, via growth-factor interactions with WNT2+ fibroblasts, and a pro-angiogenic role: they are predicted to promote sprouting angiogenesis and blood vessel morphogenesis.

- *verbatim, paragraph 4 — **not the gold span's paragraph (8)***

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

- *verbatim, paragraph 5 — **not the gold span's paragraph (8)***

  > Additionally, GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair,.

**Sonnet** → `correct` — judge: *Fibroblast maintenance plus sprouting angiogenesis and vessel morphogenesis.*

> LYVE1+ macrophages co-locate and interact with WNT2+ fibroblasts via growth factor signalling, playing a part in maintaining prenatal skin dermal fibroblasts, and also promote sprouting angiogenesis and blood vessel morphogenesis.

- *verbatim, paragraph 4 — **not the gold span's paragraph (8)***

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G22-lyve1-function.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 7 of 10)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Per the hazard note a subset-specific answer is legitimate; the HOXC5/WNT2/PEAR1 markers are accurate for this paper's fibroblast subsets and it also states the COL13A1 negative from the intended answer.*

> The context gives no general marker set for fibroblasts as a class; it instead names genes that label particular prenatal skin fibroblast subsets or states — HOXC5 for the common early fibroblast progenitor, and WNT2 and PEAR1 for the two subsets that carry the adult-like expression profile. It also notes that the papillary fibroblast marker COL13A1 was not significantly expressed in these prenatal fibroblasts.

- *verbatim, paragraph 3 — **not the gold span's paragraph (7)***

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 4 — **not the gold span's paragraph (7)***

  > Our human prenatal skin fibroblasts did not significantly express papillary fibroblast markers (for example, COL13A1)

**Sonnet** → `substituted` — judge: *Quote is real but concerns gene therapy relevance of COL7A1, not the paper's fibroblast marker profile.*

> Fibroblasts expressing COL7A1 are noted, with COL7A1 expression observed across several fibroblast subsets in prenatal skin and SkOs.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Gene therapy studies for dystrophic EB have identified fibroblasts expressing COL7A1 as a promising therapeutic strategy. We observed COL7A1 expression across several fibroblast subsets in prenatal skin and SkOs (Extended Data Fig. 6d), which lends support to the gene therapy approaches.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G23-fibroblast-markers.txt`*

---

### G24-fibroblast-location — location, expect present

**Question** Where in prenatal human skin is fibroblast found?

**Intended answer** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Gold span** (paragraph 2 of 11)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Places fibroblasts in the dermis with HOXC5+ early fibroblasts in the upper dermis and hair-specialised subsets as derivatives.*

> Fibroblasts are dermal cells; HOXC5+ early fibroblasts are specifically located in the upper dermis, and hair-specialized fibroblast derivatives (pre-Dc cells, Dc, Dp) sit adjacent to the epidermis as pre-Dc cells migrate towards it.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Upper dermis for HOXC5+ early fibroblasts is accurate, if subset-specific as the hazard allows.*

> One fibroblast subtype, HOXC5+ early fibroblasts, is described as located in the upper dermis of prenatal skin.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G24-fibroblast-location.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (**not in this context** — the retriever never supplied it)

> may favour tissue regeneration over scarring

**Opus/Fable** → `correct` — judge: *States early fibroblasts downregulate ECM/collagen programs favouring scarless healing, the intended point.*

> Fibroblasts are attributed roles in extracellular matrix and collagen deposition (and hence scarring, which early prenatal fibroblasts avoid by downregulating these programs), and hair-specialized fibroblasts coordinate hair follicle formation, including differentiation of adjacent hair matrix cells.

- *verbatim, paragraph 7*

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 8*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

- *verbatim, paragraph 2*

  > Formation of the Dp was characterized by genes (RSPO3 and WNT5A) (Extended Data Fig. 4f and Supplementary Table 7) that coordinate the differentiation of adjacent hair matrix cells,.

- *verbatim, paragraph 9*

  > A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.

**Sonnet** → `leaked`

> Fibroblasts (in early gestation) downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring; combined with macrophage interactions, this contributes to scarless healing.

- ***leaked** — from another question's context*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G25-fibroblast-function.txt`*

---

### G26-periderm-location — location, expect present

**Question** Where in prenatal human skin is periderm found?

**Intended answer** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Gold span** (paragraph 6 of 11)

> with the periderm seen sloughing from 11 PCW

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Opus/Fable** → `correct` — judge: *Outermost epidermal layer over dermal stroma, present from 7 PCW, sloughing from 11 PCW - all intended elements.*

> Periderm is an ectoderm-derived, immature interfollicular epidermal cell type forming the outermost layer of prenatal epidermis; it is present from 7 PCW, enriched in early gestation, and is seen sloughing from 11 PCW.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 7 — **not the gold span's paragraph (6)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

- *verbatim, paragraph 4 — **not the gold span's paragraph (6)***

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *Outermost layer over dermal stroma to 8 PCW and sloughing from 11 PCW.*

> The periderm forms the outer layer of prenatal skin overlying the dermal stroma up to 8 PCW, and is seen sloughing from 11 PCW.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G26-periderm-location.txt`*

---

### G27-periderm-function — function, expect present

**Question** What function does the paper attribute to periderm?

**Intended answer** Constitutes the first skin permeability barrier.

**Gold span** (paragraph 5 of 13)

> the periderm, which constitutes the first skin permeability barrier

**The gold span in its paragraph**

> … fine-grained annotations of cell states were assigned on the basis of differentially expressed genes (DEGs) (Fig. 1b, Extended Data Fig. 1c and Supplementary Table 3). Differential abundance analysis testing revealed how different cell populations varied across gestation. Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extende …

**Opus/Fable** → `correct` — judge: *Exactly the intended answer: the first skin permeability barrier.*

> The periderm is described as constituting the first skin permeability barrier.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *First skin permeability barrier, exactly as intended.*

> The periderm constitutes the first permeability barrier of the skin.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > the periderm, which constitutes the first skin permeability barrier

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G27-periderm-function.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 7 of 13)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Gives the layer-over-dermal-stroma description and sloughing from 11 PCW, and flags that no further morphology is offered.*

> The only structural/morphological observation given is histological: the periderm is part of the layer of epidermal cells overlying the dermal stroma in early prenatal skin and is seen sloughing from 11 PCW. It is classed among the immature interfollicular epidermal cells; no further morphological description is provided.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Reports the sloughing observation, which is part of the thin structural evidence intended.*

> The periderm is described as sloughing off from 11 PCW, a structural/morphological change in the epidermal layer.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > with the periderm seen sloughing from 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G28-periderm-structure.txt`*

---

### G29-hoxc5-location — location, expect present

**Question** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** The upper dermis.

**Gold span** (paragraph 1 of 9)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis of prenatal human skin, and are abundant before 11 PCW.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths

**Sonnet** → `correct` — judge: *Upper dermis, matching the intended answer.*

> HOXC5+ early fibroblasts are located in the upper dermis.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G29-hoxc5-location.txt`*

---

### G30-hoxc5-function — function, expect present

**Question** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Gold span** (paragraph 4 of 9)

> originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**The gold span in its paragraph**

> … acode specification, bone morphogenetic protein (BMP) and noggin to inhibit hair formation in IFE cells, and PDGFA and TGFβ signalling for HF down growth (Extended Data Fig. 5f). Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast) (Fig. 2e and Extended Data Fig. 4d). However, cross-species data integration of human and mouse HF showed that human pre-Dc cells and the Dc aligned not only to their counterparts in mouse skin but also to fibroblasts in earlier stages of differentiation (Extended Data Fig. 5g-i and Supplementary Tables 10 and 11).

**Opus/Fable** → `correct` — judge: *Identifies it as the common fibroblast progenitor with both hair and dermal fibroblast trajectories.*

> The paper casts HOXC5+ early fibroblast as the common fibroblast progenitor of prenatal skin dermal cells: it differentiates along a hair fibroblast trajectory (pre-Dc cells, Dc and Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**Sonnet** → `correct` — judge: *Common progenitor with both hair and dermal fibroblast trajectories described correctly.*

> HOXC5+ early fibroblasts act as a common progenitor that differentiates along two paths: one forming hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the other forming WNT2+ and PEAR1+ dermal fibroblasts.

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G30-hoxc5-function.txt`*

---

### G31-dpysl2-markers — markers, expect present

**Question** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Gold span** (paragraph 6 of 11)

> we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**The gold span in its paragraph**

> … ed prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2,  …

**Hazard note given to the judge** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Opus/Fable** → `correct` — judge: *Leads with DPYSL2 and AGR2 as the new gene and keeps BARX2/SOX9 correctly attributed as previously reported ORS differentiation genes.*

> The population is defined by DPYSL2 expression (mature basal IFE cells), and along the ORS/CL trajectory these cells upregulate AGR2 as well as the ORS differentiation genes BARX2 and SOX9.

- *verbatim, paragraph 4 — **not the gold span's paragraph (6)***

  > Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

**Sonnet** → `correct` — judge: *Names AGR2 as newly identified and correctly attributes BARX2/SOX9 as previously reported, avoiding the hazard.*

> DPYSL2+ basal cells are marked by DPYSL2 itself, and along the ORS/CL trajectory upregulate AGR2 as well as previously reported ORS-differentiation genes BARX2 and SOX9.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G31-dpysl2-markers.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (paragraph 7 of 11)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**The gold span in its paragraph**

> Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Exten …

**Opus/Fable** → `correct` — judge: *Places the cells on the ORS/CL trajectory from POSTN+ basal cells, as intended.*

> The only role attributed to DPYSL2+ basal cells is developmental: they form part of the ORS/CL differentiation trajectory arising from POSTN+ basal cells, upregulating AGR2 and ORS differentiation genes. No other function is stated in the supplied context.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

**Sonnet** → `correct` — judge: *ORS/CL trajectory downstream of POSTN+ basal cells, as intended.*

> DPYSL2+ basal cells lie along the ORS/CL differentiation trajectory, downstream of POSTN+ basal cells, contributing to formation of the outer root sheath and companion layer.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G32-dpysl2-function.txt`*

---

### G34-caparteriole-function — function, expect present

**Question** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 6 of 12)

> prenatal skin capillary arteriole cells could further differentiate into arterioles

**The gold span in its paragraph**

> … ted into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

**Opus/Fable** → `correct` — judge: *Notes further differentiation into arterioles unlike SkO cells, and high tip-cell sprouting angiogenesis score.*

> Capillary arteriole cells are an intermediate stage of the arteriolar endothelial differentiation pathway; in prenatal skin (unlike in the skin organoid) they can differentiate further into arterioles, and they score highly for sprouting angiogenesis 'tip' cell potential.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles

- *verbatim, paragraph 8 — **not the gold span's paragraph (6)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

**Sonnet** → `correct` — judge: *Tip-cell sprouting angiogenesis scoring is accurate; omitting the further arteriole differentiation is only partial.*

> The paper reports that capillary arteriole cells showed increased sprouting angiogenesis potential, based on scoring of a 'tip' cell state, alongside arteriole and capillary cells.

- *verbatim, paragraph 8 — **not the gold span's paragraph (6)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G34-caparteriole-function.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (paragraph 9 of 11)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**The gold span in its paragraph**

> The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extrace …

**Opus/Fable** → `correct` — judge: *Gives PEAR1 plus APOE, IGFBP7 and ITM2A as the pro-inflammatory transition genes; the extra senescence/collagen genes are accurately attributed.*

> Beyond PEAR1 itself, the paper reports that PEAR1+ prenatal fibroblasts express cellular senescence, cytokine and collagen deposition genes (CDKN1A, IL1R1, POSTN), and that pro-inflammatory genes APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ into PEAR1+ fibroblasts.

- *verbatim, paragraph 10 — **not the gold span's paragraph (9)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**Sonnet** → `correct` — judge: *PEAR1 plus APOE, IGFBP7 and ITM2A upregulated in the transition, as intended.*

> PEAR1+ fibroblasts are defined by PEAR1, and genes such as APOE, IGFBP7 and ITM2A are upregulated during the transition into this state.

- *verbatim, paragraph 1 — **not the gold span's paragraph (9)***

  > the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G35-pear1-markers.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (paragraph 1 of 10)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**The gold span in its paragraph**

> … lysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Opus/Fable** → `correct` — judge: *Dermal endpoint abundant after 11 PCW with adult-like pro-inflammatory, senescence and collagen deposition profile.*

> PEAR1+ fibroblasts are an abundant-after-11-PCW dermal fibroblast subset that acquires an adult-like pro-inflammatory phenotype and expresses senescence, cytokine and collagen-deposition genes of the kind found in pathogenic fibroblasts of fibrotic skin, so they are linked to the progressive acquisition of scar-promoting properties in later gestation.

- *verbatim, paragraph 8 — **not the gold span's paragraph (1)***

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c).

- *verbatim, paragraph 9 — **not the gold span's paragraph (1)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

**Sonnet** → `correct` — judge: *Adult pro-inflammatory profile with senescence and collagen deposition genes, as intended.*

> PEAR1+ fibroblasts express genes associated with an adult, pro-inflammatory phenotype, cellular senescence, cytokine signalling and collagen deposition — a gene programme the paper links to pathogenic, scar-promoting fibroblast states seen in fibrotic skin disorders and in later-gestation scarring.

- *verbatim, paragraph 8 — **not the gold span's paragraph (1)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation

- *verbatim, paragraph 9 — **not the gold span's paragraph (1)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G36-pear1-function.txt`*

---

### G38-postn-function — function, expect present

**Question** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Gold span** (paragraph 8 of 11)

> may be involved in placode specification and dermal invagination

**The gold span in its paragraph**

> Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Opus/Fable** → `correct` — judge: *Names both the migration/placode-specification role and the origin of the ORS/CL and IRS trajectories, matching the intended answer.*

> POSTN+ basal cells act as an epidermal progenitor state that differentiates along two trajectories (ORS/CL and IRS), and their increased cellular migration is proposed to contribute to hair placode specification and dermal invagination.

- *verbatim, paragraph 7 — **not the gold span's paragraph (8)***

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Sonnet** → `correct` — judge: *Increased migration in placode specification and dermal invagination is the main point.*

> POSTN+ basal cells show increased cellular migration that may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G38-postn-function.txt`*

---

### G39-arteriole-markers — markers, expect present

**Question** Which genes mark arteriole?

**Intended answer** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Gold span** (paragraph 7 of 11)

> for example, GJA5 for arteriolar and PLVAP for venular

**The gold span in its paragraph**

> … ata Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

**Hazard note given to the judge** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Opus/Fable** → `correct` — judge: *Gives GJA5 as the characteristic arteriolar gene contrasted with PLVAP, attributed to the arteriolar pathway sentence as intended.*

> GJA5 is given as a characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles), in contrast to PLVAP for the venular pathway.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a–c).

**Sonnet** → `correct` — judge: *GJA5 correctly attributed to the arteriolar pathway rather than capillary arterioles.*

> GJA5 is given as the characteristic gene for the arteriolar pathway.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G39-arteriole-markers.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 11 of 12)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Covers both the endpoint of the arteriolar differentiation pathway and the increased sprouting angiogenesis tip-cell score.*

> The context attributes no distinct biological role to arterioles beyond their place in the endothelial differentiation scheme: they are the endpoint of the arteriolar pathway, and prenatal skin arterioles show increased sprouting angiogenesis potential when scored for the 'tip' cell state.

- *verbatim, paragraph 12 — **not the gold span's paragraph (11)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `correct` — judge: *Tip-cell sprouting angiogenesis is accurate; omitting the differentiation endpoint is only partial.*

> The paper reports that arteriole cells (along with capillary arteriole and capillary cells) showed increased sprouting angiogenesis potential, based on scoring of a 'tip' cell state.

- *verbatim, paragraph 12 — **not the gold span's paragraph (11)***

  > sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G40-arteriole-function.txt`*

---

### G41-cuticle-location — location, expect present

**Question** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** Part of the inner layers of the hair follicle.

**Gold span** (paragraph 5 of 11)

> part of the inner layers of the HF

**The gold span in its paragraph**

> Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embry …

**Opus/Fable** → `correct` — judge: *Correctly places cuticle/cortex in the inner layers of the hair follicle, with accurate added detail about 14 PCW.*

> Cuticle and cortex cells are part of the inner layers of the hair follicle, and were identified in the scRNA-seq data from 14 PCW.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a–c, Extended Data Fig. 3a,b and Supplementary Table 6).

**Sonnet** → `correct` — judge: *Part of the inner layers of the hair follicle, as intended.*

> Cuticle/cortex cells are part of the inner layers of the hair follicle, identified alongside other HF cell types from 14 PCW.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a–c, Extended Data Fig. 3a,b and Supplementary Table 6).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G41-cuticle-location.txt`*

---

### G45-dermal-condensate-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `overreach` — judge: *Presents aggregation and encapsulation statements as a structural/morphological description instead of declining.*

> The dermal condensate is described structurally as an aggregate of dermal fibroblasts that forms by aggregation of pre-Dc cells and abuts the epithelial hair placode; after hair follicle invagination it becomes encapsulated at the base of the follicle as the dermal papilla.

- *verbatim, paragraph 1*

  > dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 7*

  > In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

- *verbatim, paragraph 7*

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)

**Sonnet** → `overreach` — judge: *Presents encapsulation at the base as a morphological description where the paper offers none.*

> The paper states that following HF invagination, the dermal condensate becomes encapsulated at its base as it forms the dermal papilla.

- *verbatim, paragraph 7*

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G45-dermal-condensate-structure-absent.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of cuticle/cortex cells; it names them among the identified hair follicle cell types and places them on the IRS trajectory, without any morphological description.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Offers a location statement as a structural description without declining.*

> The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

- *verbatim, paragraph 6*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local/G55-cuticle-cortex-structure-absent.txt`*

---

## Context: local-comb

### G01-placode-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Gold span** (paragraph 1 of 11)

> epidermal placodes (focal sites of epidermal layer thickening)

**The gold span in its paragraph**

> … rm (apart from facial and cranial skin, where it arises from ectoderm-derived neural crest cells). The skin appendages, which include hair follicles (HFs) and sebaceous glands, form in a cephalocaudal direction. Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

**Opus/Fable** → `correct` — judge: *Focal epidermal thickening formed by budding of basal cells; omitting invagination is an accurate partial.*

> Epidermal placodes are focal sites of thickening of the epidermal layer, seen histologically as budding of basal cells at 14–15 PCW.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

**Sonnet** → `correct` — judge: *Gives the focal epidermal thickening description, the core structural point.*

> The hair (epidermal) placode is described structurally as a focal site of epidermal layer thickening.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > epidermal placodes (focal sites of epidermal layer thickening)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G01-placode-structure.txt`*

---

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (paragraph 7 of 11)

> which abuts the epithelial hair placode

**The gold span in its paragraph**

> We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA+FOXD1+SOX2low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode,. Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin,. Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP+, SOX2+), (Fig. 2c and Extended Data Fig. 3h).

**Opus/Fable** → `correct` — judge: *Epidermis at focal sites of thickening, abutted by the dermal condensate.*

> The hair placode is located in the epidermis, as a focal site of epidermal layer thickening, positioned adjacent to (abutting) the dermal condensate.

- *verbatim, paragraph 1 — **not the gold span's paragraph (7)***

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > pre-Dc cells aggregate to form the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

**Sonnet** → `correct` — judge: *Locates the placode in the epidermis with the dermal condensate beneath.*

> Hair placode arises from budding basal cells of the epidermis and appears at 14-15 PCW, prior to elongation into hair pegs (hair follicles), and is abutted by the dermal condensate below.

- *verbatim, paragraph 2 — **not the gold span's paragraph (7)***

  > At 14–15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G02-placode-location.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 4 of 11)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity ( …

**Opus/Fable** → `correct` — judge: *Initiates hair follicle formation with the dermal condensate and gives rise to hair matrix cells.*

> The epidermal placode initiates hair follicle formation through interactions with dermal condensates, and it gives rise to hair matrix cells.

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

**Sonnet** → `correct` — judge: *States initiation of hair follicle formation via interaction with the dermal condensate.*

> The epidermal (hair) placode interacts with the dermal condensate to initiate hair follicle formation.

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G03-placode-function.txt`*

---

### G06-macrophage-location — location, expect present

**Question** Where in prenatal human skin is macrophage found?

**Intended answer** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Gold span** (**not in this context** — the retriever never supplied it)

> Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’

**Opus/Fable** → `correct` — judge: *Seeding from 6 PCW plus co-location with fibroblasts, neural and vascular cells in the microenvironments.*

> Macrophages seed prenatal skin from as early as 6 PCW and are predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments; LYVE1+ macrophages co-locate with WNT2+ fibroblasts, and TML macrophages co-locate with Schwann cells in an early neurovascular microenvironment.

- *verbatim, paragraph 2*

  > immune cells such as macrophages seed the skin as early as 6 PCW

- *verbatim, paragraph 5*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

- *verbatim, paragraph 9*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1)

**Sonnet** → `correct` — judge: *Reports co-location with fibroblasts, neural and vascular cells in early-gestation microenvironments.*

> Macrophage subsets are predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation.

- *verbatim, paragraph 5*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G06-macrophage-location.txt`*

---

### G07-macrophage-function — function, expect present

**Question** What function does the paper attribute to macrophage?

**Intended answer** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Gold span** (paragraph 10 of 10)

> Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**The gold span in its paragraph**

> In this study, we characterized the dynamic composition of human prenatal skin during the early stages of de novo HF formation and highlighted the crucial skin immune and non-immune crosstalk that contributes to skin morphogenesis, results that are in line with emerging evidence in animal and human studies,. Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development. This is in part contributed to by yolk-sac derived TML macrophages, which suggests that these cells have broader functions outside the central nervous system in early gestation. The presence of TML macrophages has previously been identified in several prenatal organs,,.

**Opus/Fable** → `correct` — judge: *Scarless repair, fibroblast homeostasis, neurovascular development and vascular network formation all named.*

> The paper attributes to prenatal skin macrophages contributions to scarless skin repair, fibroblast homeostasis and neurovascular development, including a role in vascular network formation and support for establishing the skin peripheral nervous system.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

- *verbatim, paragraph 3 — **not the gold span's paragraph (10)***

  > We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.

- *verbatim, paragraph 9 — **not the gold span's paragraph (10)***

  > These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

**Sonnet** → `correct` — judge: *Covers scarless repair, fibroblast homeostasis, neurovascular development and vascular network formation.*

> The paper attributes to macrophages roles in scarless skin repair, fibroblast homeostasis, and neurovascular development, including validated contributions to vascular network formation.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

- *verbatim, paragraph 3 — **not the gold span's paragraph (10)***

  > We used a hair-bearing SkO model to validate the role of macrophages in prenatal skin vascular network formation.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G07-macrophage-function.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (paragraph 5 of 9)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**The gold span in its paragraph**

> … ted during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

**Opus/Fable** → `correct` — judge: *WNT2 plus COL1A1/ECM late, SFRP1 early, and CDKN1A, IL1R1, POSTN.*

> Beyond the defining WNT2 in the subset name, the context does not give a marker list, but it reports genes expressed by WNT2+ fibroblasts: CDKN1A, IL1R1 and POSTN (shared with PEAR1+ fibroblasts), with COL1A1 upregulated in late gestation and SFRP1 among DEGs of early WNT2+ fibroblasts.

- *verbatim, paragraph 6 — **not the gold span's paragraph (5)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

**Sonnet** → `correct` — judge: *Names COL1A1, SFRP1, CDKN1A, IL1R1 and POSTN as intended.*

> WNT2+ fibroblasts are marked by COL1A1 (late gestation, ECM/collagen deposition), SFRP1 (early gestation, growth/differentiation), and, shared with PEAR1+ fibroblasts, CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

- *verbatim, paragraph 6 — **not the gold span's paragraph (5)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G08-wnt2fib-markers.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (paragraph 7 of 9)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**The gold span in its paragraph**

> … e of macrophages in promoting wound healing has been described in postnatal mouse skin and in adult human skin. In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d). Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8). Interactions between macrophages and fibroblasts maintain tissue homeostasis in diverse organs such as s …

**Opus/Fable** → `correct` — judge: *Dermal fibroblasts co-locating with LYVE1+ and TML macrophages in early prenatal skin.*

> WNT2+ fibroblasts are dermal fibroblasts, formed along the dermal fibroblast trajectory, and they co-locate with LYVE1+ and TML macrophages in early prenatal skin.

- *verbatim, paragraph 1 — **not the gold span's paragraph (7)***

  > the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

**Sonnet** → `correct` — judge: *Gives the LYVE1+ and TML macrophage co-location; accurate as far as it goes.*

> The context does not give a discrete anatomical location for WNT2+ fibroblasts, but notes that they co-locate with LYVE1+ macrophages and, in early gestation, with TML macrophages.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G09-wnt2fib-location.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (paragraph 5 of 9)

> we observed differences within the WNT2+ fibroblast population across gestation time

**The gold span in its paragraph**

> … b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary  …

**Opus/Fable** → `correct` — judge: *Early growth/differentiation versus late ECM and collagen deposition, with acquisition of senescence and inflammatory profile.*

> Early WNT2+ fibroblasts express genes involved in cellular growth and differentiation, whereas late gestation WNT2+ fibroblasts upregulate extracellular matrix and collagen deposition genes; together with PEAR1+ fibroblasts they express senescence, cytokine and collagen deposition genes, reflecting progressive acquisition of scar-promoting features.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 6 — **not the gold span's paragraph (5)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

**Sonnet** → `correct` — judge: *Conveys the late-gestation ECM/collagen versus early growth and differentiation programmes.*

> WNT2+ fibroblasts show gestation-stage-dependent gene programmes: in late gestation they upregulate extracellular matrix and collagen deposition genes, while earlier they express genes tied to cellular growth and differentiation.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2+ fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16–18).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G10-wnt2fib-function.txt`*

---

### G11-tml-markers — markers, expect present

**Question** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Gold span** (paragraph 4 of 10)

> Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia

**The gold span in its paragraph**

> We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads, (Extended Data Fig. 7e,f). Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properti …

**Opus/Fable** → `correct` — judge: *TREM2 with P2RY12, CX3CR1 and OLFML3; omitting GAS6 is an accurate partial.*

> TML macrophages are TREM2+ and share a microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2+ macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

**Sonnet** → `correct` — judge: *Gives the P2RY12/CX3CR1/OLFML3 microglial profile; added SYT11 is supported by the quote.*

> TML macrophages share an expression profile of P2RY12, CX3CR1 and OLFML3, and co-express immunomodulatory genes including CX3CR1 and SYT11.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G11-tml-markers.txt`*

---

### G12-tml-location — location, expect present

**Question** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Gold span** (paragraph 4 of 10)

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin

**The gold span in its paragraph**

> … odulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23). Downregulation of inflammation and IL-6 confers anti-fibrogenic properties in mouse skin transplants and in fetal wounds,. TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

**Opus/Fable** → `correct` — judge: *WNT2+ fibroblasts at 6-8 PCW and Schwann cells in the early neurovascular microenvironment.*

> TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment of prenatal skin.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 8 — **not the gold span's paragraph (4)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g)

**Sonnet** → `correct` — judge: *Matches co-location with WNT2+ fibroblasts at 6-8 PCW and Schwann cells in ME1.*

> TML macrophages co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1) of prenatal skin.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6–8 PCW) (Fig. 3c,d) and WNT2+ fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

- *verbatim, paragraph 8 — **not the gold span's paragraph (4)***

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin (‘early neurovascular microenvironment’, ME1) (Figs. 1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G12-tml-location.txt`*

---

### G13-tml-function — function, expect present

**Question** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Gold span** (paragraph 8 of 10)

> contributing to synapse formation and axon guidance

**The gold span in its paragraph**

> …  1d and 3g) and expressed genes related to cell migration and neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin. TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin.

**Opus/Fable** → `correct` — judge: *Sprouting angiogenesis plus Schwann cell interactions in synapse formation and axon guidance.*

> TML macrophages express immunomodulatory genes and are inferred to contribute to scarless healing, to support establishment of the skin peripheral nervous system through predicted interactions with Schwann cells in synapse formation and axon guidance, and to promote sprouting angiogenesis.

- *verbatim, paragraph 4 — **not the gold span's paragraph (8)***

  > Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1)

- *verbatim, paragraph 9 — **not the gold span's paragraph (8)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages

**Sonnet** → `correct` — judge: *States Schwann cell interaction for synapse formation and axon guidance plus sprouting angiogenesis.*

> TML macrophages are predicted to interact with Schwann cells to support synapse formation and axon guidance, and to promote sprouting angiogenesis.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA–NRP1, VEGFA–NRP2, SEMA3C–NRP2 and SEMA3E–PLXND1)

- *verbatim, paragraph 9 — **not the gold span's paragraph (8)***

  > sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G13-tml-function.txt`*

---

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 8 of 11)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation. Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Names the dermal compartment from 12 PCW; omitting the placode adjacency is a permissible partial.*

> The dermal condensate is found in the dermal compartment of prenatal skin, as an aggregate of dermal fibroblasts, observed from 12 PCW.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 1 — **not the gold span's paragraph (8)***

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

**Sonnet** → `leaked`

> The dermal condensate is found within the dermal compartment of prenatal skin, first observed from 12 PCW, and it abuts the epithelial hair placode.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

- ***leaked** — from another question's context*

  > the Dc (FOXD1+SOX2+), which abuts the epithelial hair placode

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G15-dc-location.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (**not in this context** — the retriever never supplied it)

> have been reported to promote cell migration and invasion

**Opus/Fable** → `correct` — judge: *Captures the main point that Dc initiates hair follicle formation via placode interaction.*

> Dermal condensates initiate prenatal hair follicle formation through their interactions with epidermal placodes.

- *verbatim, paragraph 1*

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

**Sonnet** → `correct` — judge: *Names initiation of hair follicle formation with the placode, the main intended point.*

> The dermal condensate, described as an aggregate of dermal fibroblasts, interacts with the epidermal placode to initiate hair follicle formation.

- *verbatim, paragraph 1*

  > initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G16-dc-function.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 6 of 11)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell a …

**Opus/Fable** → `correct` — judge: *Places matrix in the hair follicle arising from the placode, from 14 PCW, as intended.*

> Hair matrix cells are part of the hair follicle: they arise from the epidermal placode and are identified among the hair follicle cell states present from 14 PCW.

- *verbatim, paragraph 5 — **not the gold span's paragraph (6)***

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

**Sonnet** → `miss`

> The supplied context states that hair matrix cells arise from the epidermal placode but does not give their spatial location within prenatal skin.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G18-matrix-location.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 6 of 11)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). Treg cells are known to localize around the HF  …

**Opus/Fable** → `correct` — judge: *Reproduces the chemotaxis/CXCL14/CD24 Treg immune-protection account exactly.*

> Prenatal hair matrix cells show increased expression of chemotaxis genes (e.g. CXCL14, which recruits Treg cells) and autoimmunity-control genes (CD24), suggesting a role in Treg cell accumulation and immune protection during early matrix differentiation.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (Treg) cells, and in control of autoimmunity (CD24). This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

**Sonnet** → `correct` — judge: *Conveys Treg accumulation and immune protection during early matrix differentiation.*

> The paper suggests hair matrix cells have a potential role in accumulating regulatory T cells and providing immune protection during early hair follicle differentiation, linked to their expression of chemotaxis and autoimmunity-control genes.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > This result highlighted the potential role of Treg cell accumulation and immune protection in the early stages of matrix differentiation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G19-matrix-function.txt`*

---

### G21-lyve1-location — location, expect present

**Question** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Gold span** (**not in this context** — the retriever never supplied it)

> showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**Opus/Fable** → `correct` — judge: *Gives the WNT2+ fibroblast co-location in dermal microenvironments, the main intended point.*

> LYVE1+ macrophages are predicted to co-locate with WNT2+ fibroblasts in prenatal skin, within distinct tissue microenvironments in early gestation.

- *verbatim, paragraph 4*

  > Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 4*

  > In prenatal skin, macrophage subsets (Extended Data Fig. 7e,f) were predicted to co-locate with fibroblasts, neural cells and vascular cells in distinct tissue microenvironments in early gestation (Fig. 1d).

**Sonnet** → `correct` — judge: *Gives co-location with WNT2+ fibroblasts; accurate partial answer.*

> LYVE1+ macrophages co-locate with WNT2+ fibroblasts in prenatal skin.

- *verbatim, paragraph 4*

  > LYVE1+ macrophages co-located with WNT2+ fibroblasts (Fig. 3c–e)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G21-lyve1-location.txt`*

---

### G22-lyve1-function — function, expect present

**Question** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Gold span** (paragraph 9 of 10)

> blood vessel morphogenesis by LYVE1+ macrophages

**The gold span in its paragraph**

> … Gene ontology analysis showed that the four macrophage subsets (LYVE1+, MHCII+, TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26). Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

**Opus/Fable** → `correct` — judge: *Covers fibroblast maintenance, GAS6-AXL and sprouting angiogenesis/vessel morphogenesis.*

> LYVE1+ macrophages are suggested to maintain prenatal skin dermal fibroblasts through growth factor interactions, to contribute via GAS6-AXL signalling to immunosuppression and tissue repair, and to promote angiogenesis, specifically sprouting angiogenesis and blood vessel morphogenesis.

- *verbatim, paragraph 4 — **not the gold span's paragraph (9)***

  > Our identification of additional growth factor interactions (IGF1–IGF1R and GRN–EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 6 — **not the gold span's paragraph (9)***

  > GAS6, expressed by TML macrophages and LYVE1+ macrophages, was predicted to interact with AXL receptors on WNT2+ fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1+ and TML macrophages, blood vessel morphogenesis by LYVE1+ macrophages

**Sonnet** → `correct` — judge: *Covers dermal fibroblast maintenance and blood vessel morphogenesis/sprouting angiogenesis.*

> LYVE1+ macrophages are proposed to help maintain dermal fibroblasts via growth-factor signalling (PDGF, IGF1, GRN) and to drive blood vessel morphogenesis and sprouting angiogenesis.

- *verbatim, paragraph 4 — **not the gold span's paragraph (9)***

  > suggests that LYVE1+ macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > blood vessel morphogenesis by LYVE1+ macrophages

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G22-lyve1-function.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (**not in this context** — the retriever never supplied it)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Subset-specific markers are legitimate for this broad label per the hazard note.*

> The context gives no single pan-fibroblast marker, but prenatal skin fibroblast subsets are distinguished by marker genes: FRZB (FRZB+ fibroblasts), HOXC5 (HOXC5+ early fibroblasts), and WNT2 and PEAR1 (WNT2+ and PEAR1+ fibroblasts).

- *verbatim, paragraph 1*

  > We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW)

- *verbatim, paragraph 1*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**Sonnet** → `honest_miss`

> The supplied context does not say. It only lists markers for specific fibroblast subsets (e.g. HOXC5+, WNT2+, PEAR1+, FRZB+), not a generic fibroblast marker.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G23-fibroblast-markers.txt`*

---

### G24-fibroblast-location — location, expect present

**Question** Where in prenatal human skin is fibroblast found?

**Intended answer** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Gold span** (paragraph 1 of 9)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Dermis, with HOXC5+ early fibroblasts in the upper dermis, matches the intended answer.*

> Fibroblasts are found in the dermis of prenatal skin; HOXC5+ early fibroblasts are located in the upper dermis, and dermal fibroblasts produce the collagen of the dermal stroma.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

- *verbatim, paragraph 5 — **not the gold span's paragraph (1)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

**Sonnet** → `correct` — judge: *Places HOXC5+ early fibroblasts in the upper dermis, matching the intended dermal location.*

> HOXC5+ early fibroblasts, a fibroblast progenitor population, are located in the upper dermis.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G24-fibroblast-location.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (paragraph 7 of 9)

> may favour tissue regeneration over scarring

**The gold span in its paragraph**

> Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to  …

**Opus/Fable** → `correct` — judge: *States the early-gestation downregulation of ECM/collagen/inflammation favouring regeneration.*

> Dermal fibroblasts produce collagen, whose aggregation causes scarring; early prenatal fibroblasts downregulate extracellular matrix, collagen and inflammation genes, which may favour scarless tissue regeneration, and later-gestation WNT2+ fibroblasts upregulate extracellular matrix and collagen deposition genes.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Sonnet** → `substituted` — judge: *Quote is real but describes scar formation generally rather than the paper's claim about early-gestation downregulation favouring regeneration.*

> Dermal fibroblasts produce the collagen that aggregates to form scars when the overlying epidermis fails to regenerate.

- *verbatim, paragraph 5 — **not the gold span's paragraph (7)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G25-fibroblast-function.txt`*

---

### G26-periderm-location — location, expect present

**Question** Where in prenatal human skin is periderm found?

**Intended answer** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Gold span** (paragraph 6 of 11)

> with the periderm seen sloughing from 11 PCW

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Opus/Fable** → `correct` — judge: *Outermost/overlying position, presence from 7 PCW and sloughing from 11 PCW are conveyed.*

> The periderm is an immature interfollicular epidermal cell state that constitutes the first skin permeability barrier; it overlies the epidermis and was seen sloughing from the skin surface from 11 PCW.

- *verbatim, paragraph 4 — **not the gold span's paragraph (6)***

  > neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation

- *verbatim, paragraph 7 — **not the gold span's paragraph (6)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

**Sonnet** → `correct` — judge: *Outer epidermal layer overlying dermal stroma, sloughing from 11 PCW, as intended.*

> The periderm is an immature interfollicular epidermal (IFE) cell type forming the outer epidermal layer overlying the dermal stroma in early prenatal skin, and it sloughs off from 11 PCW.

- *verbatim, paragraph 7 — **not the gold span's paragraph (6)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G26-periderm-location.txt`*

---

### G27-periderm-function — function, expect present

**Question** What function does the paper attribute to periderm?

**Intended answer** Constitutes the first skin permeability barrier.

**Gold span** (paragraph 4 of 11)

> the periderm, which constitutes the first skin permeability barrier

**The gold span in its paragraph**

> … fine-grained annotations of cell states were assigned on the basis of differentially expressed genes (DEGs) (Fig. 1b, Extended Data Fig. 1c and Supplementary Table 3). Differential abundance analysis testing revealed how different cell populations varied across gestation. Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Extende …

**Opus/Fable** → `correct` — judge: *Identifies the first skin permeability barrier, the intended function.*

> The periderm constitutes the first skin permeability barrier and is enriched in early gestation.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier, were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *States the first skin permeability barrier.*

> The periderm constitutes the first permeability barrier of the skin.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > the periderm, which constitutes the first skin permeability barrier

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G27-periderm-function.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 6 of 11)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Conveys the thin layer description plus sloughing from 11 PCW that the paper offers.*

> Histologically the periderm is described as being seen sloughing from 11 PCW, overlying the layer of epidermal cells of early prenatal skin, and it is counted among the immature interfollicular epidermal cells.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 7 — **not the gold span's paragraph (6)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `miss`

> The supplied context does not describe the structure or morphology of the periderm, only its function and the timing of its sloughing.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G28-periderm-structure.txt`*

---

### G29-hoxc5-location — location, expect present

**Question** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** The upper dermis.

**Gold span** (paragraph 1 of 9)

> HOXC5+ early fibroblasts (located in the upper dermis

**The gold span in its paragraph**

> …  We excluded FRZB+ fibroblasts, which were primarily observed in one sample from the earliest gestation stage (7 PCW) (Extended Data Fig. 3c). Although rare in prenatal skin, FRZB-expressing fibroblasts were present in several other developing organs (Extended Data Fig. 4e). Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (F …

**Opus/Fable** → `correct` — judge: *Upper dermis, exactly as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

**Sonnet** → `correct` — judge: *Upper dermis, matching the intended answer.*

> HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G29-hoxc5-location.txt`*

---

### G30-hoxc5-function — function, expect present

**Question** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Gold span** (paragraph 3 of 9)

> originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**The gold span in its paragraph**

> … acode specification, bone morphogenetic protein (BMP) and noggin to inhibit hair formation in IFE cells, and PDGFA and TGFβ signalling for HF down growth (Extended Data Fig. 5f). Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast) (Fig. 2e and Extended Data Fig. 4d). However, cross-species data integration of human and mouse HF showed that human pre-Dc cells and the Dc aligned not only to their counterparts in mouse skin but also to fibroblasts in earlier stages of differentiation (Extended Data Fig. 5g-i and Supplementary Tables 10 and 11).

**Opus/Fable** → `correct` — judge: *Describes the common progenitor with both hair and dermal fibroblast trajectories.*

> HOXC5+ early fibroblasts act as the common fibroblast progenitor in prenatal skin, differentiating along a hair fibroblast trajectory into hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and along a dermal fibroblast trajectory into WNT2+ and PEAR1+ fibroblasts.

- *verbatim, paragraph 1 — **not the gold span's paragraph (3)***

  > Inferred trajectory analysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**Sonnet** → `correct` — judge: *Identifies the common fibroblast progenitor role with both trajectories.*

> HOXC5+ early fibroblasts act as the common fibroblast progenitor that gives rise to pre-Dc, Dc, Dp and other dermal fibroblast subsets.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G30-hoxc5-function.txt`*

---

### G31-dpysl2-markers — markers, expect present

**Question** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Gold span** (paragraph 8 of 10)

> we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**The gold span in its paragraph**

> … ed prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7). AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B, were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2,  …

**Hazard note given to the judge** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Opus/Fable** → `correct` — judge: *Gives DPYSL2 and the newly identified AGR2 without miscrediting BARX2/SOX9.*

> Mature basal cells are marked by DPYSL2, and DPYSL2+ basal cells also upregulate newly identified genes such as AGR2 along the ORS/CL trajectory.

- *verbatim, paragraph 6 — **not the gold span's paragraph (8)***

  > Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**Sonnet** → `correct` — judge: *Gives DPYSL2 and AGR2 and labels BARX2/SOX9 as ORS-differentiation genes, so the attribution is not reversed.*

> DPYSL2+ basal cells are defined by DPYSL2 expression and upregulate AGR2, as well as the ORS-differentiation genes BARX2 and SOX9.

- *verbatim, paragraph 6 — **not the gold span's paragraph (8)***

  > Mature basal (DPYSL2+)

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G31-dpysl2-markers.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (paragraph 8 of 10)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**The gold span in its paragraph**

> Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Exten …

**Opus/Fable** → `correct` — judge: *Places the cells on the ORS/CL trajectory towards ORS and companion layer, with correct attribution of BARX2/SOX9 as ORS-differentiation genes.*

> DPYSL2+ (mature) basal cells lie on the ORS/CL differentiation trajectory, where they upregulate new genes such as AGR2 and genes related to outer root sheath differentiation (BARX2 and SOX9), indicating a role in differentiating towards the outer root sheath and companion layer.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9), (Extended Data Fig. 4b,c and Supplementary Table 7).

**Sonnet** → `miss`

> The supplied context does not attribute a specific function to DPYSL2+ basal cells; it only describes their place in the ORS/CL differentiation trajectory and genes they upregulate.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G32-dpysl2-function.txt`*

---

### G34-caparteriole-function — function, expect present

**Question** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 7 of 11)

> prenatal skin capillary arteriole cells could further differentiate into arterioles

**The gold span in its paragraph**

> … ted into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

**Opus/Fable** → `correct` — judge: *Both intended points present: further differentiation into arterioles and tip-cell sprouting score.*

> Prenatal skin capillary arteriole cells can differentiate further into arterioles, and they show increased sprouting angiogenesis potential as assessed by 'tip' cell state scoring.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `correct` — judge: *Both the differentiation-into-arterioles contrast and the tip-cell score are conveyed.*

> In prenatal skin, capillary arteriole cells are able to further differentiate into arterioles (unlike in the SkO model), and they show increased sprouting angiogenesis potential as assessed by a 'tip' cell state score.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G34-caparteriole-function.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (paragraph 7 of 10)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**The gold span in its paragraph**

> The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts (Extended Data Fig. 7c). In addition to transcriptomics differences between fibroblast subsets enriched in early versus late gestation, we observed differences within the WNT2+ fibroblast population across gestation time (Extended Data Fig. 1d). Late gestation WNT2+ fibroblasts had upregulated genes related to extrace …

**Opus/Fable** → `miss`

> The supplied context does not state which genes mark PEAR1+ fibroblasts; it only describes genes upregulated during the transition into them and genes shared with WNT2+ fibroblasts, not defining markers.

*No quotes given.*

**Sonnet** → `correct` — judge: *APOE, IGFBP7, ITM2A in the HOXC5+ transition plus the shared senescence/collagen genes.*

> PEAR1+ fibroblasts upregulate a pro-inflammatory phenotype including APOE, IGFBP7 and ITM2A during their transition from HOXC5+ fibroblasts, and (together with WNT2+ fibroblasts) express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A), were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G35-pear1-markers.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (paragraph 1 of 10)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**The gold span in its paragraph**

> … lysis predicted that HOXC5+ early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Opus/Fable** → `correct` — judge: *Later-gestation adult pro-inflammatory profile with senescence and collagen deposition genes.*

> PEAR1+ fibroblasts, abundant in later gestation, acquire an adult pro-inflammatory, scar-promoting profile, expressing genes involved in cellular senescence, cytokine pathways and collagen deposition that are characteristic of pathogenic fibroblasts in fibrotic skin disorders.

- *verbatim, paragraph 8 — **not the gold span's paragraph (1)***

  > Notably, WNT2+ and PEAR1+ prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders.

- *verbatim, paragraph 7 — **not the gold span's paragraph (1)***

  > The adult fibroblast gene expression profile was increased in WNT2+ and PEAR1+ prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b).

**Sonnet** → `miss`

> The supplied context does not say. It describes PEAR1+ fibroblasts in terms of gene expression changes (senescence, cytokine pathway, collagen deposition genes) and their emergence after 11 PCW, but does not state a specific function attributed to them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G36-pear1-function.txt`*

---

### G37-postn-location — location, expect present

**Question** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Gold span** (paragraph 7 of 11)

> whereas POSTN+ basal cells were present throughout gestation

**The gold span in its paragraph**

> … d mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b). Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW, whereas POSTN+ basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b). Sebaceous and apocrine gland cells, which mature after 16 PCW, were not captured at these stages.

**Opus/Fable** → `correct` — judge: *Basal interfollicular epidermis, present throughout gestation, as intended.*

> POSTN+ basal cells are part of the interfollicular epidermis, where they were present throughout gestation; trajectory analysis places them as the starting basal population of the epidermal differentiation paths.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > In addition, we observed immature and mature interfollicular epidermal (IFE) cells.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Mature basal (DPYSL2+) and suprabasal IFE cells increased after 11 PCW, whereas POSTN+ basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

- *verbatim, paragraph 9 — **not the gold span's paragraph (7)***

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths

**Sonnet** → `correct` — judge: *Basal IFE population present throughout gestation, as intended.*

> POSTN+ basal cells are one of the basal-cell populations of the interfollicular epidermis (IFE), and they are present throughout gestation.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > In addition, we observed immature and mature interfollicular epidermal (IFE) cells.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > whereas POSTN+ basal cells were present throughout gestation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G37-postn-location.txt`*

---

### G38-postn-function — function, expect present

**Question** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Gold span** (paragraph 10 of 11)

> may be involved in placode specification and dermal invagination

**The gold span in its paragraph**

> Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

**Opus/Fable** → `correct` — judge: *Gives both the ORS/CL and IRS trajectory origin and the migration/placode specification role.*

> POSTN+ basal cells are proposed to give rise to two epidermal differentiation paths (ORS/CL and IRS trajectories), and their increased cellular migration may contribute to placode specification and dermal invagination.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 9 — **not the gold span's paragraph (10)***

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN+ basal cells into two paths: ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).

**Sonnet** → `correct` — judge: *States increased migration involved in placode specification and dermal invagination.*

> The paper suggests that increased cell migration in POSTN+ basal cells contributes to hair placode specification and dermal invagination.

- *verbatim, paragraph 10 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G38-postn-function.txt`*

---

### G39-arteriole-markers — markers, expect present

**Question** Which genes mark arteriole?

**Intended answer** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Gold span** (paragraph 7 of 10)

> for example, GJA5 for arteriolar and PLVAP for venular

**The gold span in its paragraph**

> … ata Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

**Hazard note given to the judge** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Opus/Fable** → `correct` — judge: *GJA5 correctly attributed as the characteristic arteriolar gene.*

> GJA5 is given as a characteristic gene of the arteriolar pathway, which comprises capillaries, capillary arterioles and arterioles.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a–c).

**Sonnet** → `correct` — judge: *GJA5 correctly attributed to the arteriolar lineage against PLVAP.*

> GJA5 is given as the characteristic gene marking the arteriolar lineage (as opposed to PLVAP for venular).

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G39-arteriole-markers.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 7 of 10)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Accurate partial: names the tip-cell sprouting angiogenesis potential attributed to arterioles.*

> The paper attributes sprouting angiogenesis potential to prenatal skin arteriole cells: they showed an increased 'tip' cell state score, indicating capacity for new blood vessel growth.

- *verbatim, paragraph 8 — **not the gold span's paragraph (7)***

  > However, sprouting angiogenesis potential, assessed by scoring the ‘tip’ cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `miss`

> The supplied context does not describe a function for arteriole itself; it only describes arterioles as an endpoint of the differentiation trajectory of endothelial cells.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G40-arteriole-function.txt`*

---

### G41-cuticle-location — location, expect present

**Question** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** Part of the inner layers of the hair follicle.

**Gold span** (paragraph 5 of 11)

> part of the inner layers of the HF

**The gold span in its paragraph**

> Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embry …

**Opus/Fable** → `correct` — judge: *Inner layers of the hair follicle, as intended.*

> Cuticle and cortex cells are part of the inner layers of the hair follicle, identified among hair follicle cells from 14 PCW.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH+), outer root sheath (ORS) (SLC26A7+), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `correct` — judge: *Inner layers of the hair follicle, as intended.*

> Cuticle/cortex cells are part of the inner layers of the hair follicle (HF).

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G41-cuticle-location.txt`*

---

### G45-dermal-condensate-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `overreach` — judge: *Presents 'aggregates of dermal fibroblasts' as a structural description instead of declining.*

> The paper describes dermal condensates structurally as aggregates of dermal fibroblasts.

- *verbatim, paragraph 1*

  > Prenatal HFs start forming between 11 and 14 post-conception weeks (PCW), initiated by interactions between epidermal placodes (focal sites of epidermal layer thickening) and dermal condensates (aggregates of dermal fibroblasts), whereas sebaceous glands develop from around 16 PCW.

**Sonnet** → `overreach` — judge: *Presents 'aggregate of dermal fibroblasts' as a structural description where the paper offers no morphology.*

> The dermal condensate is described structurally as an aggregate of dermal fibroblasts.

- *verbatim, paragraph 1*

  > dermal condensates (aggregates of dermal fibroblasts)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/local-comb/G45-dermal-condensate-structure-absent.txt`*

---

## Context: asta-sep

### G01-placode-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Gold span** (**not in this context** — the retriever never supplied it)

> epidermal placodes (focal sites of epidermal layer thickening)

**Opus/Fable** → `correct` — judge: *Captures the budding of basal cells and the invagination accompanying dermal condensate formation.*

> The placode is described as a bud of basal cells seen at 14-15 PCW, and its formation involves invagination of the placode as the dermal condensate forms.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 5*

  > The Dc, for which formation is accompanied by invagination of the placode

**Sonnet** → `correct` — judge: *Budding of basal cells is the intended structural point, with follicle elongation added.*

> The hair placode is described as arising via budding of basal cells, alongside germ cells, with subsequent elongation of hair follicles into hair pegs.

- *verbatim, paragraph 2*

  > budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G01-placode-structure.txt`*

---

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (paragraph 4 of 10)

> which abuts the epithelial hair placode

**The gold span in its paragraph**

> We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).

**Opus/Fable** → `correct` — judge: *Places the placode in the epidermis as a basal-cell bud, matching the intended location.*

> The hair placode is found in the epidermis as a bud of basal cells, observed histologically at 14-15 PCW, and placode cells were captured in the hair follicle scRNA-seq data from 14 PCW.

- *verbatim, paragraph 2 — **not the gold span's paragraph (4)***

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (4)***

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `correct` — judge: *Epidermal budding site abutted by the dermal condensate.*

> The hair placode arises from budding of basal cells in the epidermis at 14-15 PCW, and it is abutted by the dermal condensate.

- *verbatim, paragraph 2 — **not the gold span's paragraph (4)***

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > which abuts the epithelial hair placode 26,28

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G02-placode-location.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (**not in this context** — the retriever never supplied it)

> We evaluated hair matrix cells, which arise from the epidermal placode

**Opus/Fable** → `correct` — judge: *Names the main point - the placode is the epithelial partner instructing early hair follicle formation - accurate though partial.*

> The context describes the placode only as the epithelial partner in the mesenchymal-epithelial interactions that instruct early hair follicle formation, bearing receptors (LAMP1 or CXADR and EPHB6) for Dc-derived ligands reported to promote cell migration and invasion.

- *verbatim, paragraph 5*

  > We explored the mesenchymal-epithelial interactions that instruct early HF formation.

- *verbatim, paragraph 5*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

**Sonnet** → `substituted` — judge: *Quote is real but describes Dc-to-placode signalling, not the placode's role in initiating hair follicle formation.*

> The placode is a site of ligand-receptor signalling (via EPHB6, among others) that is reported to promote cell migration and invasion.

- *verbatim, paragraph 5*

  > EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G03-placode-function.txt`*

---

### G05-macrophage-markers — markers, expect present

**Question** Which genes mark macrophage?

**Intended answer** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Gold span** (paragraph 9 of 9)

> share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

**The gold span in its paragraph**

> We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f). Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory recep …

**Hazard note given to the judge** broad label; four subsets each have their own markers

**Opus/Fable** → `correct` — judge: *Correctly notes there is no pan-macrophage panel and gives subset-level markers, as the hazard anticipates.*

> The context gives no pan-macrophage marker list; it names the genes that define subsets - TREM2 with a P2RY12, CX3CR1 and OLFML3 microglia-like profile, and LYVE1, MHCII and iron-recycling subsets.

- *verbatim, paragraph 9 — same paragraph as the gold span*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).

- *verbatim, paragraph 2 — **not the gold span's paragraph (9)***

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).

**Sonnet** → `miss`

> The supplied context does not list specific genes marking macrophages generally; it only refers to unnamed 'marker genes' used to annotate macrophage subsets without naming them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G05-macrophage-markers.txt`*

---

### G06-macrophage-location — location, expect present

**Question** Where in prenatal human skin is macrophage found?

**Intended answer** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Gold span** (**not in this context** — the retriever never supplied it)

> Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’

**Opus/Fable** → `correct` — judge: *Reports co-location with fibroblasts and Schwann cells in ME1; partial but accurate.*

> Macrophages are described by co-location: TREM2 + microglia-like macrophages co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in an early neurovascular microenvironment (ME1).

- *verbatim, paragraph 8*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 12*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)

**Sonnet** → `correct` — judge: *Gives the ME1 neurovascular co-location and flags its own partiality.*

> Within this context, the only macrophage subset given an explicit skin location is the TML macrophage, which was predicted to co-locate with Schwann cells in an early neurovascular microenvironment.

- *verbatim, paragraph 12*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G06-macrophage-location.txt`*

---

### G07-macrophage-function — function, expect present

**Question** What function does the paper attribute to macrophage?

**Intended answer** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Gold span** (**not in this context** — the retriever never supplied it)

> Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Opus/Fable** → `correct` — judge: *Covers angiogenesis, fibroblast maintenance and peripheral nervous system support as intended.*

> Macrophages are attributed non-immune morphogenetic roles: contributing to prenatal skin angiogenesis, maintaining dermal fibroblasts via growth factor interactions, and supporting establishment of the skin peripheral nervous system in early gestation.

- *verbatim, paragraph 5*

  > Our data suggested that macrophages contribute to prenatal skin angiogenesis.

- *verbatim, paragraph 1*

  > Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 3*

  > These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .

**Sonnet** → `correct` — judge: *Angiogenesis, fibroblast homeostasis and neurovascular development all covered.*

> The paper attributes several functions to macrophages in prenatal skin, including promoting angiogenesis and vascular network formation, interacting with fibroblasts to maintain tissue homeostasis, and supporting neural development alongside Schwann cells.

- *verbatim, paragraph 4*

  > Macrophages have been implicated in angiogenesis during prenatal organ development and in the postnatal setting such as cancerrelated angiogenesis 67,68 .

- *verbatim, paragraph 5*

  > Our data suggested that macrophages contribute to prenatal skin angiogenesis.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G07-macrophage-function.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (**not in this context** — the retriever never supplied it)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**Opus/Fable** → `correct` — judge: *Gives COL1A1, SFRP1, CDKN1A, IL1R1 and POSTN alongside WNT2, matching the intended set.*

> Beyond WNT2 in the subset name, the context reports COL1A1 upregulated in late gestation and SFRP1 in early gestation WNT2+ fibroblasts, and expression of CDKN1A, IL1R1 and POSTN by WNT2+ and PEAR1+ prenatal fibroblasts.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b)

**Sonnet** → `correct` — judge: *COL1A1 late and SFRP1 early are accurate; omitting WNT2 itself is only partial.*

> WNT2+ fibroblasts are marked by differentially expressed genes that vary with gestational age: COL1A1 in late gestation and SFRP1 in early gestation.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G08-wnt2fib-markers.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (**not in this context** — the retriever never supplied it)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**Opus/Fable** → `correct` — judge: *Reports co-location with LYVE1+ macrophages and flags the absence of a compartment statement; accurate as far as it goes.*

> The context gives no anatomical compartment beyond co-location: WNT2+ fibroblasts are predicted to co-locate with LYVE1+ macrophages (and are abundant in later gestation) in prenatal skin.

- *verbatim, paragraph 4*

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 2*

  > The adult fibroblast gene expression profile was increased in WNT2 + and PEAR1 + prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b).

**Sonnet** → `correct` — judge: *Co-location with LYVE1+ macrophages is the main point, accurate as far as it goes.*

> WNT2+ fibroblasts are found co-located with LYVE1+ macrophages in distinct tissue microenvironments in prenatal skin.

- *verbatim, paragraph 4*

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G09-wnt2fib-location.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (**not in this context** — the retriever never supplied it)

> we observed differences within the WNT2+ fibroblast population across gestation time

**Opus/Fable** → `correct` — judge: *Matches the late/early ECM-versus-growth contrast and the senescent, pro-inflammatory drift.*

> WNT2+ fibroblasts are linked to extracellular matrix and collagen deposition in late gestation versus cellular growth and differentiation in early gestation, and they express senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibroblasts, supporting progressive acquisition of scar-promoting programmes.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

**Sonnet** → `correct` — judge: *Late-gestation extracellular matrix and collagen deposition, as intended.*

> Late gestation WNT2+ fibroblasts are attributed a function in extracellular matrix and collagen deposition.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G10-wnt2fib-function.txt`*

---

### G11-tml-markers — markers, expect present

**Question** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia

**Opus/Fable** → `correct` — judge: *TREM2 with P2RY12, CX3CR1, OLFML3 and GAS6, exactly as intended.*

> TML macrophages are TREM2+ and share the microglia-like profile P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11, and express GAS6.

- *verbatim, paragraph 2*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).

- *verbatim, paragraph 2*

  > Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

**Sonnet** → `correct` — judge: *TREM2 with P2RY12, CX3CR1 and OLFML3, matching the intended answer.*

> TML macrophages are marked by TREM2, and share an expression profile of P2RY12, CX3CR1 and OLFML3 with microglia-like macrophages from other developing organs.

- *verbatim, paragraph 2*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G11-tml-markers.txt`*

---

### G12-tml-location — location, expect present

**Question** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Gold span** (**not in this context** — the retriever never supplied it)

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin

**Opus/Fable** → `correct` — judge: *Reports both co-locations (WNT2+ fibroblasts at 6-8 PCW and Schwann cells in ME1).*

> TML macrophages are predicted to sit alongside WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and to co-locate with Schwann cells in the 'early neurovascular microenvironment' (ME1).

- *verbatim, paragraph 2*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)

- *verbatim, paragraph 3*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)

**Sonnet** → `correct` — judge: *Both the ME1 Schwann cell and early WNT2+ fibroblast co-locations given.*

> TML macrophages are predicted to co-locate with Schwann cells in the 'early neurovascular microenvironment' (ME1) and with WNT2+ fibroblasts in early prenatal skin (6-8 PCW).

- *verbatim, paragraph 3*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)

- *verbatim, paragraph 2*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G12-tml-location.txt`*

---

### G13-tml-function — function, expect present

**Question** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Gold span** (paragraph 4 of 9)

> contributing to synapse formation and axon guidance

**The gold span in its paragraph**

> neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin 65 . TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .

**Opus/Fable** → `correct` — judge: *Includes sprouting angiogenesis and the Schwann cell synapse/axon-guidance interactions.*

> TML macrophages are attributed immunomodulatory functions (potentially contributing to scarless healing via IL-6 regulation and GAS6-AXL signalling to WNT2+ fibroblasts), support of the developing skin peripheral nervous system through Schwann cell interactions, and promotion of sprouting angiogenesis.

- *verbatim, paragraph 2 — **not the gold span's paragraph (4)***

  > Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11)

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1)

- *verbatim, paragraph 5 — **not the gold span's paragraph (4)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages

**Sonnet** → `correct` — judge: *Sprouting angiogenesis and the Schwann cell synapse/axon guidance role both named.*

> TML macrophages are attributed roles including anti-fibrogenic/scarless-healing contributions, sprouting angiogenesis, and interacting with Schwann cells to contribute to synapse formation and axon guidance.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G13-tml-function.txt`*

---

### G14-dc-markers — markers, expect present

**Question** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Gold span** (paragraph 4 of 9)

> expressed FAM3C and EFNB1

**The gold span in its paragraph**

> … Notably, lymphoid tissue inducer and ILC3 cells were also predicted to co-locate and interact with pre-Dc cells through ligand-receptor signals implicated in the regulation of cellular adhesion and migration (CXCL12-CXCR4 and CXCL12-DPP4) 35,36 The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

**Opus/Fable** → `correct` — judge: *FOXD1/SOX2 identity plus FAM3C and EFNB1 match the intended markers.*

> The dermal condensate is defined by FOXD1 and SOX2 expression (annotated in human using orthologous marker genes from mouse), and the Dc is also reported to express FAM3C and EFNB1.

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 .

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1

**Sonnet** → `correct` — judge: *FOXD1 and SOX2 are the intended markers.*

> The dermal condensate is marked by FOXD1 and SOX2.

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > the Dc (FOXD1 + SOX2 + )

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G14-dc-markers.txt`*

---

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 5 of 8)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation 1 . Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Dermal compartment from 12 PCW abutting the placode, matching the intended answer.*

> The dermal condensate lies in the dermal compartment of prenatal skin from 12 PCW, adjacent to (abutting) the epithelial hair placode, and after hair follicle invagination it becomes encapsulated at the follicle base as the dermal papilla.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 1 — **not the gold span's paragraph (5)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp

**Sonnet** → `correct` — judge: *Dermal compartment from 12 PCW, abutting the epithelial hair placode.*

> The dermal condensate is found within the dermal compartment of prenatal skin, from 12 PCW, and abuts the epithelial hair placode.

- *verbatim, paragraph 5 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 1 — **not the gold span's paragraph (5)***

  > which abuts the epithelial hair placode 26,28

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G15-dc-location.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (paragraph 8 of 8)

> have been reported to promote cell migration and invasion

**The gold span in its paragraph**

> … d-receptor signals implicated in the regulation of cellular adhesion and migration (CXCL12-CXCR4 and CXCL12-DPP4) 35,36 The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

**Opus/Fable** → `correct` — judge: *Captures the Dc signalling to the placode via FAM3C/EFNB1 promoting migration and invasion.*

> The dermal condensate signals to the overlying epithelium during hair follicle formation - its formation accompanies placode invagination and it expresses FAM3C and EFNB1 predicted to engage LAMP1/CXADR and EPHB6 on the placode, molecules reported to promote cell migration and invasion; it subsequently becomes the dermal papilla.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

- *verbatim, paragraph 1 — **not the gold span's paragraph (8)***

  > Following HF invagination, the Dc becomes encapsulated at its base as the Dp

**Sonnet** → `correct` — judge: *FAM3C/EFNB1 signalling to the placode promoting migration and invasion, as intended.*

> The paper attributes a migration/invasion-promoting function to the dermal condensate: it expresses FAM3C and EFNB1, predicted to signal to the overlying placode via LAMP1/CXADR and EPHB6, and these interactions have been reported to promote cell migration and invasion.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G16-dc-function.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (**not in this context** — the retriever never supplied it)

> known matrix markers such as SHH and WNT10B, were upregulated

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *Gives SHH as the annotating marker; the added CXCL14/CD24 comparison is supported and does not misstate the paper.*

> The matrix population is annotated as SHH+; relative to adult hair follicles, prenatal matrix cells also show increased CXCL14 and CD24 expression.

- *verbatim, paragraph 10*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

**Sonnet** → `substituted` — judge: *SHH is right but CXCL14 and CD24 are presented as markers when the quote gives them as chemotaxis/autoimmunity genes raised versus adult.*

> Hair matrix cells are marked by SHH, and matrix-specific genes include CXCL14 and CD24, which are increased compared with adult hair follicles.

- *verbatim, paragraph 10*

  > which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G17-matrix-markers.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 2 of 9)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role o …

**Opus/Fable** → `correct` — judge: *Hair follicle origin from the epidermal placode, prenatal-specific, from 14 PCW - all as intended.*

> Hair matrix cells are a hair follicle cell state of prenatal skin, arising from the epidermal placode and detected in the scRNA-seq data from 14 PCW; they are prenatal-specific and absent from established adult hair follicles.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).

- *verbatim, paragraph 5 — **not the gold span's paragraph (2)***

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `correct` — judge: *Conveys placode origin and prenatal-specific state, matching the intended answer.*

> Hair matrix cells arise from the epidermal placode and are described as a prenatal-specific cell state absent in established adult hair follicles.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G18-matrix-location.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 2 of 9)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). T reg cells are known to localize ar …

**Opus/Fable** → `correct` — judge: *Chemotaxis via CXCL14 and CD24 with Treg accumulation and immune protection, matching the intended answer.*

> Prenatal hair matrix cells are attributed a chemotactic/immune-recruiting role: they upregulate chemotaxis genes such as CXCL14 (which recruits regulatory T cells) and CD24, suggesting they promote Treg accumulation and immune protection during early matrix differentiation.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

**Sonnet** → `correct` — judge: *Reproduces the chemotaxis/CXCL14/CD24 and Treg immune-protection account exactly as intended.*

> The paper reports that prenatal skin matrix cells have increased expression of chemotaxis genes such as CXCL14 (a chemokine that recruits regulatory T cells) and CD24 (involved in control of autoimmunity), suggesting a role in Treg cell recruitment and immune protection during matrix differentiation.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G19-matrix-function.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *Correctly reports LYVE1 plus GAS6 and flags the thin body-text evidence, as the hazard anticipates.*

> The supplied context gives no marker gene list for this subset beyond the defining LYVE1 label; the only gene it explicitly states is expressed by LYVE1+ macrophages is GAS6.

- *verbatim, paragraph 5*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts

**Sonnet** → `substituted` — judge: *Quotes are antibody-panel method lines; CD45/CD31 are staining reagents, not markers of this subset, and GAS6 is missed.*

> The paper identifies LYVE1+ macrophages by LYVE1 protein expression, using anti-LYVE1 immunofluorescence/RNAscope staining alongside other markers such as CD45 and CD31 to detect these cells.

- *verbatim, paragraph 7*

  > n = 1 biological replicate with n = 2 technical replicates for immunofluorescence slides with anti-LYVE1, anti-CD45 and anti-VIM (Fig. 3e)

- *verbatim, paragraph 7*

  > n = 3 biological replicates for prenatal skin whole-mount immunofluorescence with anti-CD31 and anti-LYVE1 (Fig. 4a)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G20-lyve1-markers.txt`*

---

### G21-lyve1-location — location, expect present

**Question** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Gold span** (**not in this context** — the retriever never supplied it)

> showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**Opus/Fable** → `correct` — judge: *Reports the endothelial proximity shown by staining; partial but accurate.*

> LYVE1+ macrophages sit close to endothelial cells in prenatal skin - macrophages co-locate with endothelial cells in the early and late neurovascular microenvironments (ME1 and ME5), and staining showed LYVE1+ macrophages in close proximity to endothelial cells.

- *verbatim, paragraph 1*

  > Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).

- *verbatim, paragraph 1*

  > Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

**Sonnet** → `correct` — judge: *Names endothelial proximity, a main point of the intended answer, accurately if partially.*

> LYVE1+ macrophages were shown by multiplex RNAscope and immunofluorescence staining to be in close proximity to endothelial cells in prenatal skin.

- *verbatim, paragraph 1*

  > LYVE1 + and TML macrophages in close proximity to endothelial cells

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G21-lyve1-location.txt`*

---

### G22-lyve1-function — function, expect present

**Question** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Gold span** (**not in this context** — the retriever never supplied it)

> blood vessel morphogenesis by LYVE1+ macrophages

**Opus/Fable** → `correct` — judge: *Sprouting angiogenesis, blood vessel morphogenesis and dermal fibroblast maintenance, as intended.*

> LYVE1+ macrophages are attributed pro-angiogenic roles (promoting sprouting angiogenesis and blood vessel morphogenesis, in close proximity to endothelial cells) and a part in maintaining prenatal skin dermal fibroblasts through growth factor interactions.

- *verbatim, paragraph 1*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

- *verbatim, paragraph 4*

  > Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

**Sonnet** → `correct` — judge: *Gives blood vessel morphogenesis and dermal fibroblast maintenance as intended.*

> LYVE1+ macrophages are attributed roles in blood vessel morphogenesis and in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 1*

  > blood vessel morphogenesis by LYVE1 + macrophages

- *verbatim, paragraph 4*

  > LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G22-lyve1-function.txt`*

---

### G23-fibroblast-markers — markers, expect present

**Question** Which genes mark fibroblast?

**Intended answer** Prenatal skin fibroblasts upregulate immune-suppression and regeneration genes (CD200, RAMP2, MDK) relative to adult, which express IL6, IL1RA, HLA-A, CD55, PTGES and CDKN1A. They do not significantly express papillary markers such as COL13A1.

**Gold span** (paragraph 5 of 9)

> prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200)

**The gold span in its paragraph**

> … sets expressed high levels of inflammatory cytokines and receptors (for example, IL6 and IL1RA) and genes involved in antigen presentation (for example, HLA-A), innate immune and inflammatory responses (for example, CD55 and PTGES) and cellular senescence (CDKN1A) (Fig. 3a and Supplementary Tables 13-15). By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Hazard note given to the judge** broad label spanning five fine subsets; answers may legitimately be subset-specific

**Opus/Fable** → `correct` — judge: *Legitimately subset-specific per the hazard, and correctly states no general panel is given.*

> The context does not give a general fibroblast marker panel; it reports PDGFRalpha and PDGFRbeta receptors expressed on fibroblasts, and subset-level genes such as COL1A1, SFRP1, CDKN1A, IL1R1 and POSTN in WNT2+ and PEAR1+ prenatal fibroblasts.

- *verbatim, paragraph 4 — **not the gold span's paragraph (5)***

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 3 — **not the gold span's paragraph (5)***

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b)

**Sonnet** → `miss`

> The supplied context does not say which genes generically mark fibroblasts; it only discusses genes specific to particular fibroblast subsets (e.g. WNT2+, PEAR1+, HOXC5+).

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G23-fibroblast-markers.txt`*

---

### G24-fibroblast-location — location, expect present

**Question** Where in prenatal human skin is fibroblast found?

**Intended answer** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Gold span** (**not in this context** — the retriever never supplied it)

> HOXC5+ early fibroblasts (located in the upper dermis

**Opus/Fable** → `correct` — judge: *Dermis, with HOXC5+ early fibroblasts in the upper dermis, matching the intended answer.*

> Fibroblasts sit in the dermis of prenatal skin; HOXC5+ early fibroblasts are specifically located in the upper dermis, and other subsets are described as dermal fibroblast subsets.

- *verbatim, paragraph 6*

  > HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c))

- *verbatim, paragraph 3*

  > To identify the cellular and molecular mechanisms that may endow early prenatal skin with scarless healing properties, we investigated the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets (Extended Data Figs. 3c and 7a).

**Sonnet** → `correct` — judge: *Dermal compartment plus HOXC5+ upper dermis matches the intended answer.*

> Fibroblasts in prenatal human skin are found in the dermal compartment, producing collagen there, with subsets such as HOXC5+ early fibroblasts located in the upper dermis.

- *verbatim, paragraph 3*

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate 51 .

- *verbatim, paragraph 6*

  > HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G24-fibroblast-location.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (**not in this context** — the retriever never supplied it)

> may favour tissue regeneration over scarring

**Opus/Fable** → `correct` — judge: *Conveys the reduced collagen/inflammation early profile favouring scarless healing.*

> Fibroblasts are attributed extracellular matrix and collagen deposition (in late gestation WNT2 + fibroblasts) versus cellular growth and differentiation programmes in early gestation, and fibroblast features are proposed to underlie the capacity of prenatal skin to heal without scarring.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1)

- *verbatim, paragraph 5*

  > A combination of fibroblast and macrophage-associated molecular features potentially contribute to the ability of prenatal skin to heal without scarring, including the presence of fibroblast progenitors, a downregulated immune milieu and reduced collagen expression.

**Sonnet** → `leaked`

> Prenatal skin fibroblasts are attributed roles in immune suppression, regulation of inflammation, and tissue regeneration, based on upregulated genes CD200, RAMP2 and MDK.

- ***leaked** — from another question's context*

  > prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G25-fibroblast-function.txt`*

---

### G26-periderm-location — location, expect present

**Question** Where in prenatal human skin is periderm found?

**Intended answer** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Gold span** (paragraph 2 of 13)

> with the periderm seen sloughing from 11 PCW

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Opus/Fable** → `correct` — judge: *Outermost epidermal layer over the dermal stroma, from 7 PCW, sloughing from 11 PCW.*

> Periderm belongs to the immature interfollicular epidermis, forming the outermost layer of the epidermis overlying the dermal stroma; it is present from 7 PCW and is seen sloughing from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Outer epidermal layer over dermal stroma, from 7 PCW, sloughing from 11 PCW — all as intended.*

> Periderm is one of the immature interfollicular epidermal (IFE) cell types, present in the epidermal layer overlying the dermal stroma from 7 PCW, and it sloughs from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > with the periderm seen sloughing from 11 PCW

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G26-periderm-location.txt`*

---

### G27-periderm-function — function, expect present

**Question** What function does the paper attribute to periderm?

**Intended answer** Constitutes the first skin permeability barrier.

**Gold span** (paragraph 7 of 9)

> the periderm, which constitutes the first skin permeability barrier

**The gold span in its paragraph**

> … fine-grained annotations of cell states were assigned on the basis of differentially expressed genes (DEGs) (Fig. 1b, Extended Data Fig. 1c and Supplementary Table 3). Differential abundance analysis testing revealed how different cell populations varied across gestation. Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier 2 , were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4). Mesoderm-derived cells, including skin fibroblasts and endothelial cells, and immune cells were present throughout gestation (Fig. 1c, Exte …

**Opus/Fable** → `correct` — judge: *States the first skin permeability barrier, exactly as intended.*

> The periderm is described as constituting the first skin permeability barrier, and it is enriched in early gestation.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Among ectoderm-derived cells, neural cells and the periderm, which constitutes the first skin permeability barrier 2 , were enriched in early gestation, whereas suprabasal epidermal and HF cells were mainly observed in later gestation (Fig. 1c, Extended Data Fig. 1d and Supplementary Table 4).

**Sonnet** → `correct` — judge: *States the first skin permeability barrier, exactly the intended function.*

> The periderm is described as constituting the first skin permeability barrier.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > the periderm, which constitutes the first skin permeability barrier

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G27-periderm-function.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 2 of 10)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Gives the layer description and sloughing observation, which is all the paper offers.*

> Histologically, the periderm is an outermost layer of the early epidermis that is seen sloughing from 11 PCW, and it is classed among the immature interfollicular epidermal cells present from 7 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Gives the layer plus sloughing description, which is all the paper offers here.*

> The periderm is described as a layer that is seen sloughing from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > with the periderm seen sloughing from 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G28-periderm-structure.txt`*

---

### G29-hoxc5-location — location, expect present

**Question** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** The upper dermis.

**Gold span** (**not in this context** — the retriever never supplied it)

> HOXC5+ early fibroblasts (located in the upper dermis

**Opus/Fable** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

- *verbatim, paragraph 4*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths

**Sonnet** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

- *verbatim, paragraph 4*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G29-hoxc5-location.txt`*

---

### G30-hoxc5-function — function, expect present

**Question** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Gold span** (**not in this context** — the retriever never supplied it)

> originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**Opus/Fable** → `correct` — judge: *Names the common fibroblast progenitor and both hair and dermal trajectories exactly as intended.*

> HOXC5+ early fibroblasts are described as the common fibroblast progenitor of prenatal skin dermal and hair-follicle fibroblasts, giving rise along two trajectories to pre-Dc/Dc/Dp cells and to WNT2+ and PEAR1+ fibroblasts.

- *verbatim, paragraph 2*

  > Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).

- *verbatim, paragraph 4*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW)

**Sonnet** → `correct` — judge: *Identifies the common fibroblast progenitor role and both downstream fates.*

> HOXC5+ early fibroblasts function as a common fibroblast progenitor, giving rise to pre-Dc cells, the dermal condensate, dermal papilla and other dermal fibroblasts.

- *verbatim, paragraph 2*

  > pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G30-hoxc5-function.txt`*

---

### G31-dpysl2-markers — markers, expect present

**Question** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Gold span** (**not in this context** — the retriever never supplied it)

> we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**Hazard note given to the judge** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Opus/Fable** → `correct` — judge: *Attribution is the right way round: AGR2 newly identified, BARX2/SOX9 flagged as previously reported.*

> Along the ORS/CL trajectory the paper reports AGR2 as a newly identified gene upregulated by DPYSL2+ basal cells, alongside previously reported ORS differentiation genes BARX2 and SOX9.

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Gives DPYSL2 accurately and avoids the BARX2/SOX9 attribution trap; partial but not wrong.*

> DPYSL2 is the marker gene used to identify the mature basal cell population (DPYSL2+ basal cells).

- *verbatim, paragraph 7*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G31-dpysl2-markers.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (**not in this context** — the retriever never supplied it)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**Opus/Fable** → `correct` — judge: *Places the cell on the ORS/CL differentiation trajectory as intended, with accurate supporting detail.*

> DPYSL2+ (mature) basal cells sit on the ORS/CL differentiation trajectory, upregulating AGR2 and outer root sheath differentiation genes (BARX2, SOX9), and they increase in the interfollicular epidermis after 11 PCW.

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 4*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

**Sonnet** → `honest_miss`

> The supplied context describes DPYSL2+ basal cells' place in a differentiation trajectory and their upregulated genes, but does not attribute a specific function to them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G32-dpysl2-function.txt`*

---

### G34-caparteriole-function — function, expect present

**Question** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 1 of 9)

> prenatal skin capillary arteriole cells could further differentiate into arterioles

**The gold span in its paragraph**

> … ted into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid 71 , which also lacked immune cells, further demonstrated the limited vasculature differentiation of this mesoderm-geared blood vessel organoid model (Extended Data Fig. 10d). This result …

**Opus/Fable** → `correct` — judge: *Covers both further differentiation into arterioles (unlike SkO) and the tip-cell sprouting angiogenesis score.*

> Capillary arterioles are an intermediate stage of the arteriolar endothelial pathway that in prenatal skin can differentiate further into arterioles, and they score highly for sprouting angiogenesis ('tip' cell) potential, i.e. new blood vessel formation.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `correct` — judge: *Captures the tip-cell sprouting angiogenesis score and the prenatal/SkO contrast.*

> Capillary arteriole cells show sprouting angiogenesis potential (assessed by the 'tip' cell state score) in both prenatal skin and SkO, though in SkO these cells appear unable to guide stalk cells for new blood vessel formation despite this signature.

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h)

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G34-caparteriole-function.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (**not in this context** — the retriever never supplied it)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**Opus/Fable** → `correct` — judge: *Gives PEAR1 plus APOE/IGFBP7/ITM2A from the HOXC5 transition, correctly framed as upregulated genes.*

> Beyond the defining PEAR1 label, the context lists genes upregulated in these fibroblasts rather than a formal marker set: APOE, IGFBP7 and ITM2A during the transition from HOXC5+ fibroblasts, plus CDKN1A, IL1R1 and POSTN shared with WNT2+ fibroblasts.

- *verbatim, paragraph 2*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).

- *verbatim, paragraph 5*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

**Sonnet** → `correct` — judge: *Names PEAR1 and the APOE/IGFBP7/ITM2A pro-inflammatory set from the HOXC5+ transition.*

> The supplied context does not give a specific marker gene panel identifying PEAR1+ fibroblasts beyond the PEAR1 name itself, but it notes that a pro-inflammatory gene set (APOE, IGFBP7, ITM2A) was upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts.

- *verbatim, paragraph 2*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G35-pear1-markers.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (**not in this context** — the retriever never supplied it)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**Opus/Fable** → `correct` — judge: *Late-gestation dermal fibroblast with pro-inflammatory, senescence and collagen-deposition profile matches the intended answer.*

> PEAR1+ fibroblasts are late-gestation dermal fibroblasts with a pro-inflammatory, scar-promoting profile: they express senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibroblasts in fibrotic skin disorders.

- *verbatim, paragraph 8*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

**Sonnet** → `correct` — judge: *Reports the senescence, cytokine and collagen-deposition profile linking them to fibrotic phenotypes.*

> PEAR1+ fibroblasts express genes involved in cellular senescence, cytokine pathways and collagen deposition that are highly expressed in pathogenic fibroblasts of fibrotic skin disorders, linking them to progressive acquisition of scar-promoting properties in later gestation.

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G36-pear1-function.txt`*

---

### G37-postn-location — location, expect present

**Question** Where in prenatal human skin is POSTN+ basal cell found? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Basal epidermis; present throughout gestation, unlike mature DPYSL2+ basal and suprabasal IFE cells which increase after 11 PCW.

**Gold span** (**not in this context** — the retriever never supplied it)

> whereas POSTN+ basal cells were present throughout gestation

**Opus/Fable** → `correct` — judge: *Epidermal basal cells present throughout gestation, contrasted with DPYSL2+ mature basal after 11 PCW.*

> The context places POSTN+ basal cells among the epidermal basal cells and states they are present throughout gestation, unlike mature basal and suprabasal IFE cells that increase after 11 PCW; no finer spatial compartment is given.

- *verbatim, paragraph 4*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

**Sonnet** → `honest_miss`

> The supplied context only states when POSTN+ basal cells are present (throughout gestation), not their spatial location.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G37-postn-location.txt`*

---

### G38-postn-function — function, expect present

**Question** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Gold span** (paragraph 1 of 10)

> may be involved in placode specification and dermal invagination

**The gold span in its paragraph**

> … as known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration 27 . Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

**Opus/Fable** → `correct` — judge: *Captures both the ORS/CL and IRS trajectory origin and the migration/placode-invagination role.*

> POSTN+ basal cells act as an epidermal progenitor that gives rise to both the ORS/CL and IRS trajectories, and their increased cellular migration is suggested to contribute to placode specification and dermal invagination.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

**Sonnet** → `correct` — judge: *States increased migration in placode specification and dermal invagination as intended.*

> The paper suggests that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G38-postn-function.txt`*

---

### G39-arteriole-markers — markers, expect present

**Question** Which genes mark arteriole?

**Intended answer** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Gold span** (paragraph 3 of 9)

> for example, GJA5 for arteriolar and PLVAP for venular

**The gold span in its paragraph**

> … ata Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid 71 , which also lacked i …

**Hazard note given to the judge** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Opus/Fable** → `correct` — judge: *GJA5 as the characteristic arteriolar gene against PLVAP for venular, attributed to the right pathway.*

> GJA5 is given as the characteristic gene of the arteriolar pathway (as opposed to PLVAP for the venular pathway).

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).

**Sonnet** → `correct` — judge: *GJA5 as the characteristic arteriolar gene, correctly attributed.*

> GJA5 is given as the characteristic gene for the arteriolar pathway (which includes arterioles).

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > GJA5 for arteriolar and PLVAP for venular

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G39-arteriole-markers.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 1 of 9)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Partial but accurate: names the tip-cell sprouting angiogenesis role, omitting only the pathway-endpoint framing.*

> Prenatal skin arterioles are among the endothelial cell types scored as having increased sprouting angiogenesis ('tip' cell state) potential, i.e. a role in new blood vessel formation.

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

**Sonnet** → `miss`

> The supplied context does not attribute a specific function to arteriole cells themselves; it discusses their differentiation trajectory and marker genes but no functional role.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G40-arteriole-function.txt`*

---

### G41-cuticle-location — location, expect present

**Question** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** Part of the inner layers of the hair follicle.

**Gold span** (paragraph 3 of 11)

> part of the inner layers of the HF

**The gold span in its paragraph**

> Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embry …

**Opus/Fable** → `correct` — judge: *Correctly places cuticle/cortex in the inner layers of the hair follicle.*

> Cuticle and cortex cells are hair follicle cells forming part of the inner layers of the follicle, identified in prenatal skin from 14 PCW.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

**Sonnet** → `correct` — judge: *Inner layers of the hair follicle, as intended.*

> Cuticle and cortex cells are described as part of the inner layers of the hair follicle, identified in the scRNA-seq data from 14 PCW.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G41-cuticle-location.txt`*

---

### G45-dermal-condensate-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of the dermal condensate itself.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Presents abutting the placode and encapsulation as a structural description where the paper offers no morphology.*

> The dermal condensate is described structurally as abutting the epithelial hair placode, and after HF invagination it becomes encapsulated at its base to form the dermal papilla.

- *verbatim, paragraph 1*

  > which abuts the epithelial hair placode

- *verbatim, paragraph 1*

  > the Dc becomes encapsulated at its base as the Dp

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G45-dermal-condensate-structure-absent.txt`*

---

### G55-cuticle-cortex-structure-absent — structure, expect absent

**Question** What does the paper say about the structure or morphology of cuticle/cortex? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** decline — the paper says nothing about this cell type's structure or morphology.

**Opus/Fable** → `correct_decline`

> The supplied context does not describe the structure or morphology of cuticle/cortex cells.

*No quotes given.*

**Sonnet** → `overreach` — judge: *Offers a location statement as the structural description without flagging that morphology is absent.*

> The paper describes cuticle/cortex cells as part of the inner layers of the hair follicle.

- *verbatim, paragraph 3*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-sep/G55-cuticle-cortex-structure-absent.txt`*

---

## Context: asta-comb

### G01-placode-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** A focal thickening of the epidermal layer, formed by budding of basal cells; placode formation is accompanied by invagination as the dermal condensate forms beneath it.

**Gold span** (**not in this context** — the retriever never supplied it)

> epidermal placodes (focal sites of epidermal layer thickening)

**Opus/Fable** → `correct` — judge: *Describes budding of basal cells and subsequent invagination accompanying dermal condensate formation.*

> Morphologically the hair placode appears as budding of basal cells at 14-15 PCW, seen alongside germ cells and elongating hair pegs; the placode subsequently invaginates, an event accompanying dermal condensate formation.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 5*

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

**Sonnet** → `correct` — judge: *Names budding of basal cells and follicle elongation, the main structural point available.*

> The paper describes the placode as arising from budding of basal cells at 14-15 PCW, alongside germ cells, with elongation into hair pegs.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G01-placode-structure.txt`*

---

### G02-placode-location — location, expect present

**Question** Where in prenatal human skin is hair placode found? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** In the epidermis, at focal sites of epidermal thickening; the dermal condensate abuts the epithelial hair placode from below.

**Gold span** (**not in this context** — the retriever never supplied it)

> which abuts the epithelial hair placode

**Opus/Fable** → `correct` — judge: *Locates the placode in the epidermal basal layer as budding basal cells, consistent with the intended answer.*

> The hair placode appears in the epidermal basal layer of prenatal skin as budding basal cells, observed histologically at 14-15 PCW, with HF cells including placode detected in scRNA-seq from 14 PCW.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

- *verbatim, paragraph 3*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).

**Sonnet** → `substituted` — judge: *Quote is real but answers timing/morphogenesis rather than where the placode sits in the epidermis.*

> Hair placode was observed at 14-15 PCW as budding of basal cells, elongating into hair follicles.

- *verbatim, paragraph 2*

  > At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G02-placode-location.txt`*

---

### G03-placode-function — function, expect present

**Question** What function does the paper attribute to hair placode? (hair placode is also referred to as: placode, epidermal placode, epithelial hair placode.)

**Intended answer** Initiates hair follicle formation together with the dermal condensate; hair matrix cells arise from the epidermal placode. WNT and EDA signalling drive placode specification.

**Gold span** (paragraph 8 of 8)

> We evaluated hair matrix cells, which arise from the epidermal placode

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoi …

**Opus/Fable** → `correct` — judge: *States matrix cells arise from the placode and it initiates the IRS trajectory with Dc crosstalk; omits only WNT/EDA.*

> The placode is the prenatal-specific epidermal cell state that gives rise to hair matrix cells and sits on the inner root sheath differentiation trajectory; its invagination accompanies dermal condensate formation, and it receives migration/invasion-promoting signals (FAM3C, EFNB1) from the Dc via LAMP1/CXADR and EPHB6.

- *verbatim, paragraph 8 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).

- *verbatim, paragraph 5 — **not the gold span's paragraph (8)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion 37,38 (Fig. 2g, Extended Data Fig. 5b and Supplementary Table 8).

- *verbatim, paragraph 4 — **not the gold span's paragraph (8)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7)

**Sonnet** → `substituted` — judge: *Quote is real but describes Dc-derived ligands and placode receptors, not the placode's own role in initiating HF formation.*

> The placode expresses receptors (CXADR and EPHB6) for Dc-derived ligands FAM3C and EFNB1 that have been reported to promote cell migration and invasion, linking the placode to Dc invagination.

- *verbatim, paragraph 5 — **not the gold span's paragraph (8)***

  > The Dc, for which formation is accompanied by invagination of the placode, expressed FAM3C and EFNB1, which were, respectively, predicted to interact with LAMP1 or CXADR and EPHB6 on the placode, and have been reported to promote cell migration and invasion

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G03-placode-function.txt`*

---

### G05-macrophage-markers — markers, expect present

**Question** Which genes mark macrophage?

**Intended answer** MHCII genes (upregulated only after 11 PCW), TREM2 on the microglia-like subset with P2RY12, CX3CR1 and OLFML3; GAS6 and VEGFA and CXCL8 also macrophage-expressed.

**Gold span** (**not in this context** — the retriever never supplied it)

> share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages

**Hazard note given to the judge** broad label; four subsets each have their own markers

**Opus/Fable** → `honest_miss`

> The supplied context does not give marker genes for macrophages; it names four subsets (LYVE1+, MHCII+, TML and iron-recycling) and refers to marker genes used for annotation without listing them.

*No quotes given.*

**Sonnet** → `correct` — judge: *Names MHCII and the marker-defined subsets accurately, a fair partial answer for this broad label.*

> The paper identifies four macrophage subsets marked by LYVE1 and MHCII, alongside the TML and iron-recycling subsets.

- *verbatim, paragraph 1*

  > the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G05-macrophage-markers.txt`*

---

### G06-macrophage-location — location, expect present

**Question** Where in prenatal human skin is macrophage found?

**Intended answer** Seed the skin from 6 PCW; co-locate with endothelial and neural cells in the early and late neurovascular microenvironments (ME1 and ME5), and with fibroblasts (ME1, ME4, ME5).

**Gold span** (**not in this context** — the retriever never supplied it)

> Macrophages co-located with endothelial and neural cells in ‘early and late neurovascular microenvironments’

**Opus/Fable** → `correct` — judge: *Gives the ME1/ME5 neurovascular co-location with endothelial and Schwann cells; omits fibroblast co-location but is accurate.*

> Macrophages are predicted and imaged to sit alongside endothelial cells in the early and late neurovascular microenvironments (ME1 and ME5), with LYVE1+ and TML macrophages in close proximity to endothelial cells; TML macrophages also co-locate with Schwann cells in ME1.

- *verbatim, paragraph 1*

  > Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).

- *verbatim, paragraph 1*

  > Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

- *verbatim, paragraph 10*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g)

**Sonnet** → `correct` — judge: *Gives the ME1/ME5 neurovascular co-location with endothelial cells, the main intended point.*

> Macrophages in prenatal skin co-locate with endothelial cells in neurovascular microenvironments, and TML macrophages specifically co-locate with Schwann cells.

- *verbatim, paragraph 1*

  > Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G06-macrophage-location.txt`*

---

### G07-macrophage-function — function, expect present

**Question** What function does the paper attribute to macrophage?

**Intended answer** Support angiogenesis via vascular network remodelling, contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Gold span** (**not in this context** — the retriever never supplied it)

> Our atlas indicated that macrophages contribute to scarless skin repair, fibroblast homeostasis and neurovascular development.

**Opus/Fable** → `correct` — judge: *Angiogenesis, neurovascular development and scarless repair all present, matching the intended roles.*

> Macrophages are attributed non-immune developmental roles in prenatal skin: driving angiogenesis and vascular network formation through communication with endothelial cells, supporting establishment of the skin peripheral nervous system via interaction with Schwann cells, and contributing to scarless healing and wound closure alongside fibroblasts. Antigen presentation is suggested not to be a key early function.

- *verbatim, paragraph 1*

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).

- *verbatim, paragraph 2*

  > Our data suggested that macrophages contribute to prenatal skin angiogenesis.

- *verbatim, paragraph 3*

  > These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .

- *verbatim, paragraph 9*

  > Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin.

- *verbatim, paragraph 8*

  > Using a scratch assay of SkO-derived fibroblasts cultured with or without iPS cell-derived macrophages, we demonstrated that scratch wound width closure was improved when fibroblasts were co-cultured with macrophages over 72 h (Extended Data Fig. 8g).

**Sonnet** → `correct` — judge: *Covers angiogenesis, neurovascular development, homeostasis and scarless healing as intended.*

> Macrophages are attributed roles in prenatal skin angiogenesis (via co-location with endothelial cells and ligand-receptor interactions supporting chemotaxis and cell migration), in supporting establishment of the skin peripheral nervous system through interactions with Schwann cells, and possibly in scarless healing and tissue homeostasis, raising the question of a contribution to early skin morphogenesis.

- *verbatim, paragraph 1*

  > Predicted ligandreceptor interactions were consistent with reciprocal communication between macrophages and endothelial cells to support angiogenesis, chemotaxis and cell migration (for example, CXCL8-ACKR1 and CCL8-ACKR1) 10,70 (Extended Data Fig. 9a and Supplementary Table 28).

- *verbatim, paragraph 2*

  > Our data suggested that macrophages contribute to prenatal skin angiogenesis.

- *verbatim, paragraph 3*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).

- *verbatim, paragraph 4*

  > Together with evidence of their role in tissue homeostasis 6,7 and healing in mouse models 8,9 , this raises the question of whether macrophages contribute to human early skin morphogenesis.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G07-macrophage-function.txt`*

---

### G08-wnt2fib-markers — markers, expect present

**Question** Which genes mark WNT2+ fibroblast?

**Intended answer** WNT2 itself; late-gestation cells upregulate COL1A1 and extracellular matrix/collagen genes, early cells SFRP1; the population also expresses CDKN1A, IL1R1 and POSTN, and has downregulated IL6 relative to adult.

**Gold span** (**not in this context** — the retriever never supplied it)

> Late gestation WNT2+ fibroblasts had upregulated genes related to extracellular matrix and collagen deposition

**Opus/Fable** → `honest_miss`

> The supplied context does not give marker genes for WNT2+ fibroblasts. It reports genes differentially expressed within the subset across gestation (COL1A1, SFRP1) and genes shared with PEAR1+ fibroblasts (CDKN1A, IL1R1, POSTN), but none is presented as a marker defining the cell type.

*No quotes given.*

**Sonnet** → `correct` — judge: *Reports WNT2, COL1A1/ECM late, SFRP1 early, plus CDKN1A, IL1R1 and POSTN.*

> WNT2+ fibroblasts show stage-dependent gene expression: late-gestation cells upregulate extracellular matrix/collagen genes such as COL1A1, early cells upregulate growth/differentiation genes such as SFRP1, and both WNT2+ and PEAR1+ fibroblasts express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G08-wnt2fib-markers.txt`*

---

### G09-wnt2fib-location — location, expect present

**Question** Where in prenatal human skin is WNT2+ fibroblast found?

**Intended answer** Dermal; co-locate with LYVE1+ macrophages, and with TML macrophages in early prenatal skin (6-8 PCW).

**Gold span** (**not in this context** — the retriever never supplied it)

> Specifically, LYVE1+ macrophages co-located with WNT2+ fibroblasts

**Opus/Fable** → `correct` — judge: *Dermal fibroblast subset co-locating with LYVE1+ and, at 6-8 PCW, TML macrophages.*

> WNT2+ fibroblasts are a dermal fibroblast subset of prenatal skin; the context locates them by co-location, with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), TML macrophages, but gives no finer anatomical compartment.

- *verbatim, paragraph 2*

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

- *verbatim, paragraph 8*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

**Sonnet** → `correct` — judge: *Co-location with LYVE1+ and early TML macrophages matches the intended answer.*

> WNT2+ fibroblasts co-locate with LYVE1+ macrophages and, in early prenatal skin (6-8 PCW), with TML macrophages.

- *verbatim, paragraph 2*

  > LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e)

- *verbatim, paragraph 8*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G09-wnt2fib-location.txt`*

---

### G10-wnt2fib-function — function, expect present

**Question** What function does the paper attribute to WNT2+ fibroblast?

**Intended answer** Extracellular matrix and collagen deposition in late gestation, growth and differentiation early; acquire an adult pro-inflammatory and senescence profile with gestational age.

**Gold span** (**not in this context** — the retriever never supplied it)

> we observed differences within the WNT2+ fibroblast population across gestation time

**Opus/Fable** → `correct` — judge: *Early growth/differentiation versus late ECM and collagen deposition, plus the pro-inflammatory/senescence profile.*

> WNT2+ fibroblasts change function across gestation: early ones express growth and differentiation genes while late ones upregulate extracellular matrix and collagen deposition genes, and together with PEAR1+ fibroblasts they acquire senescence, cytokine and collagen-deposition genes characteristic of pathogenic fibrotic fibroblasts. They are also partners of macrophages, receiving PDGF signals from co-located LYVE1+ macrophages.

- *verbatim, paragraph 1*

  > Late gestation WNT2 + fibroblasts had upregulated genes related to extracellular matrix and collagen deposition (for example, COL1A1), whereas early WNT2 + fibroblasts had DEGs involved in cellular growth and differentiation (for example, SFRP1) (Fig. 3b, Extended Data Fig. 7d and Supplementary Tables 16-18).

- *verbatim, paragraph 1*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

- *verbatim, paragraph 2*

  > Specifically, LYVE1 + macrophages co-located with WNT2 + fibroblasts (Fig. 3c-e) and were predicted to interact through platelet-derived growth factors (PDGFs) and corresponding receptors (PDGFRα and PDGFRβ) expressed on fibroblasts (Extended Data Fig. 7g and Supplementary Table 8).

**Sonnet** → `honest_miss`

> The supplied context does not say. It describes gene expression changes in WNT2+ fibroblasts across gestation and their co-location with macrophages, but does not state a function attributed to WNT2+ fibroblasts themselves.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G10-wnt2fib-function.txt`*

---

### G11-tml-markers — markers, expect present

**Question** Which genes mark TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** TREM2, with P2RY12, CX3CR1 and OLFML3; also express GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> Prenatal skin TREM2+ microglia-like (TML) macrophages were highly correlated with embryonic brain microglia

**Opus/Fable** → `correct` — judge: *TREM2 with the P2RY12/CX3CR1/OLFML3 microglia-like profile; extra SYT11 is accurately attributed.*

> TML macrophages are TREM2+ and share the microglia-like expression profile of P2RY12, CX3CR1 and OLFML3; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

- *verbatim, paragraph 2*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).

- *verbatim, paragraph 2*

  > Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59

**Sonnet** → `correct` — judge: *TREM2 with P2RY12, CX3CR1 and OLFML3, as intended.*

> TML macrophages are TREM2+ and share an expression profile of P2RY12, CX3CR1 and OLFML3 with microglia-like macrophages elsewhere; they also co-express immunomodulatory genes such as CX3CR1 and SYT11.

- *verbatim, paragraph 2*

  > We recently identified yolk-sac derived TREM2 + macrophages that share an expression profile (P2RY12, CX3CR1 and OLFML3) with microglia-like macrophages from other developing organs, such as the brain, prenatal skin and gonads 57,58 (Extended Data Fig. 7e,f).

- *verbatim, paragraph 2*

  > Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59 (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 19-23).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G11-tml-markers.txt`*

---

### G12-tml-location — location, expect present

**Question** Where in prenatal human skin is TREM2+ microglia-like (TML) macrophage found? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the early neurovascular microenvironment (ME1); seen in close proximity to endothelial cells.

**Gold span** (**not in this context** — the retriever never supplied it)

> TML macrophages were predicted to co-locate with WNT2+ fibroblasts in early prenatal skin

**Opus/Fable** → `correct` — judge: *WNT2+ fibroblasts at 6-8 PCW, Schwann cells in ME1, and proximity to endothelial cells, as intended.*

> TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1); macrophages more generally were predicted to co-locate with endothelial cells in microenvironments ME1 and ME5.

- *verbatim, paragraph 2*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a).

- *verbatim, paragraph 4*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1) (Figs. 1d and 3g) and expressed genes related to cell migration and

- *verbatim, paragraph 5*

  > Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

**Sonnet** → `correct` — judge: *WNT2+ fibroblasts at 6-8 PCW and Schwann cells in ME1, as intended.*

> TML macrophages are predicted to co-locate with WNT2+ fibroblasts in early prenatal skin (6-8 PCW) and with Schwann cells in the 'early neurovascular microenvironment' (ME1).

- *verbatim, paragraph 2*

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW)

- *verbatim, paragraph 4*

  > TML macrophages were also predicted to co-locate with Schwann cells in prenatal skin ('early neurovascular microenvironment', ME1)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G12-tml-location.txt`*

---

### G13-tml-function — function, expect present

**Question** What function does the paper attribute to TREM2+ microglia-like (TML) macrophage? (TREM2+ microglia-like (TML) macrophage is also referred to as: TML macrophage.)

**Intended answer** Promote sprouting angiogenesis, and interact with Schwann cells to contribute to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2, SEMA3E-PLXND1).

**Gold span** (paragraph 3 of 9)

> contributing to synapse formation and axon guidance

**The gold span in its paragraph**

> neural development (Fig. 3f, Extended Data Fig. 8c and Supplementary Tables 22 and 23), which mirrored the functions of brain microglia and peripheral nerve-associated macrophages in mouse skin 65 . TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8). These findings suggest that prenatal skin macrophages may support the establishment of the skin peripheral nervous system during early gestation, as previously reported in mouse skin 65 .

**Opus/Fable** → `correct` — judge: *Includes sprouting angiogenesis and the Schwann-cell synapse formation and axon guidance interactions.*

> TML macrophages are assigned immunomodulatory and anti-inflammatory roles that may support scarless healing (including GAS6-AXL signalling to WNT2+ fibroblasts inducing immunosuppression and tissue repair), support of the developing peripheral nervous system via interaction with Schwann cells, and promotion of sprouting angiogenesis.

- *verbatim, paragraph 2 — **not the gold span's paragraph (3)***

  > Prenatal skin TREM2 + microglia-like (TML) macrophages were highly correlated with embryonic brain microglia 57 (Extended Data Fig. 8a,b) and co-expressed immunomodulatory genes, including immune-inhibitory receptors (for example, CX3CR1) and regulators of IL-6 production (for example, SYT11) 59

- *verbatim, paragraph 2 — **not the gold span's paragraph (3)***

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).

- *verbatim, paragraph 5 — **not the gold span's paragraph (3)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

**Sonnet** → `correct` — judge: *Includes sprouting angiogenesis and the Schwann cell synapse/axon guidance interactions.*

> TML macrophages are implicated in scarless healing through anti-inflammatory/anti-fibrogenic signalling with WNT2+ fibroblasts, in supporting establishment of the skin peripheral nervous system through interactions with Schwann cells (synapse formation and axon guidance), and in promoting sprouting angiogenesis.

- *verbatim, paragraph 2 — **not the gold span's paragraph (3)***

  > TML macrophages were predicted to co-locate with WNT2 + fibroblasts in early prenatal skin (6-8 PCW) (Fig. 3c,d) and WNT2 + fibroblasts had downregulated IL6 expression compared with adult fibroblasts (Fig. 3a). This led us to infer a potential contribution of macrophages in scarless healing in prenatal skin.

- *verbatim, paragraph 3 — same paragraph as the gold span*

  > TML macrophages were predicted to interact with Schwann cells, contributing to synapse formation and axon guidance (VEGFA-NRP1, VEGFA-NRP2, SEMA3C-NRP2 and SEMA3E-PLXND1) 66 (Extended Data Fig. 8h and Supplementary Table 8).

- *verbatim, paragraph 5 — **not the gold span's paragraph (3)***

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G13-tml-function.txt`*

---

### G14-dc-markers — markers, expect present

**Question** Which genes mark dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** FOXD1+SOX2+ (the precursor pre-Dc is PDGFRA+FOXD1+SOX2-low); the Dc expresses FAM3C and EFNB1.

**Gold span** (**not in this context** — the retriever never supplied it)

> expressed FAM3C and EFNB1

**Opus/Fable** → `correct` — judge: *FOXD1+SOX2+ correctly given with the pre-Dc contrast; misses FAM3C/EFNB1 but is accurate as far as it goes.*

> The dermal condensate is defined by FOXD1 and SOX2 expression, the mouse orthologous markers the authors used to annotate the Dc in human prenatal skin; the derived dermal papilla is NDP+ SOX2+.

- *verbatim, paragraph 8*

  > In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 .

**Sonnet** → `correct` — judge: *FOXD1+SOX2+ identity is the main intended marker point.*

> The dermal condensate is marked by FOXD1 and SOX2, based on orthologous marker genes used to annotate it in human prenatal skin.

- *verbatim, paragraph 8*

  > In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G14-dc-markers.txt`*

---

### G15-dc-location — location, expect present

**Question** Where in prenatal human skin is dermal condensate found? (dermal condensate is also referred to as: Dc.)

**Intended answer** In the dermal compartment from 12 PCW, directly beneath and abutting the epithelial hair placode.

**Gold span** (paragraph 1 of 9)

> Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW

**The gold span in its paragraph**

> Accordingly, sebocyte progenitors are present from day 133 of SkO differentiation 1 . Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

**Opus/Fable** → `correct` — judge: *Dermal compartment from 12 PCW abutting the epithelial hair placode, exactly as intended.*

> The dermal condensate sits in the dermal compartment of prenatal skin, observed from 12 PCW; it forms from aggregating pre-Dc fibroblasts and abuts the epithelial hair placode, later becoming encapsulated at the base of the invaginating follicle as the dermal papilla.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

- *verbatim, paragraph 8 — **not the gold span's paragraph (1)***

  > In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).

**Sonnet** → `correct` — judge: *Dermal compartment from 12 PCW, as intended.*

> The dermal condensate is found within the dermal compartment of prenatal skin, observed alongside HF-specialized fibroblasts and the dermal papilla from 12 PCW.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Within the dermal compartment, we observed HF-specialized fibroblasts, the dermal condensate (Dc) and dermal papilla (Dp), from 12 PCW (Extended Data Fig. 3c).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G15-dc-location.txt`*

---

### G16-dc-function — function, expect present

**Question** What function does the paper attribute to dermal condensate? (dermal condensate is also referred to as: Dc.)

**Intended answer** Aggregates from pre-Dc fibroblasts to initiate hair follicle formation with the placode; its FAM3C and EFNB1 are predicted to promote cell migration and invasion.

**Gold span** (**not in this context** — the retriever never supplied it)

> have been reported to promote cell migration and invasion

**Opus/Fable** → `correct` — judge: *Aggregation from pre-Dc cells and dermal-epidermal crosstalk in HF development conveys the intended role.*

> The dermal condensate is presented as a hair-follicle-specialized dermal cell state that takes part in dermal-epidermal crosstalk during hair follicle development; it forms from aggregating pre-Dc fibroblasts next to the hair placode and, after follicle invagination, becomes the dermal papilla.

- *verbatim, paragraph 8*

  > We delineated the dermal cell types involved in crosstalk with epidermal cells during HF development and captured the precursors of the human Dc (Extended Data Figs. 2b and 3c). In mice, transitional PDGFRA + FOXD1 + SOX2 low fibroblasts termed pre-Dc cells aggregate to form the Dc (FOXD1 + SOX2 + ), which abuts the epithelial hair placode 26,28 . Using orthologous marker genes, we annotated pre-Dc cells and the Dc in human prenatal skin 28,29 . Following HF invagination, the Dc becomes encapsulated at its base as the Dp (NDP + , SOX2 + ) 26,28 (Fig. 2c and Extended Data Fig. 3h).

**Sonnet** → `honest_miss`

> The supplied context does not state a specific function for the dermal condensate; it only describes how pre-Dc cells aggregate to form the Dc and its spatial relationship to the hair placode.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G16-dc-function.txt`*

---

### G17-matrix-markers — markers, expect present

**Question** Which genes mark hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** SHH, and WNT10B; both described as known matrix markers.

**Gold span** (**not in this context** — the retriever never supplied it)

> known matrix markers such as SHH and WNT10B, were upregulated

**Hazard note given to the judge** "Matrix" alone is ambiguous in this paper -- extracellular matrix and several linear-algebra senses dominate raw matches. The question must say hair matrix.

**Opus/Fable** → `correct` — judge: *SHH and WNT10B named as known matrix markers, with the hair-matrix sense correctly identified.*

> The context names SHH and WNT10B as known matrix markers, upregulated along the IRS trajectory, and reports that prenatal matrix cells have increased expression of CXCL14 and CD24 relative to adult hair follicles.

- *verbatim, paragraph 8*

  > AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 4*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

**Sonnet** → `leaked`

> Hair matrix cells are marked by SHH, and known matrix markers SHH and WNT10B were found upregulated along the IRS trajectory.

- *verbatim, paragraph 8*

  > known matrix markers such as SHH and WNT10B 25,26 were upregulated

- ***leaked** — from another question's context*

  > matrix (SHH + )

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G17-matrix-markers.txt`*

---

### G18-matrix-location — location, expect present

**Question** Where in prenatal human skin is hair matrix found? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** In the hair follicle, arising from the epidermal placode; a prenatal-specific cell state absent from established adult follicles. Identified from 14 PCW.

**Gold span** (paragraph 4 of 10)

> a prenatal-specific cell state absent in established adult HFs

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role o …

**Opus/Fable** → `correct` — judge: *Hair follicle epithelium arising from the epidermal placode and prenatal-specific; timing given as the quoted 12 PCW cohort.*

> Hair matrix cells belong to the hair follicle epithelial compartment, arising from the epidermal placode, and are counted among the late epithelial cell states present from 12 PCW onwards. The context gives no finer spatial position within the follicle.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).

- *verbatim, paragraph 5 — **not the gold span's paragraph (4)***

  > late epithelial cells (≥12 PCW; DPYSL2 + basal, POSTN + basal, placode, matrix, ORS, CL, IRS, cuticle/cortex)

**Sonnet** → `correct` — judge: *Epidermal placode origin and prenatal-specific state, as intended.*

> Hair matrix cells arise from the epidermal placode, a prenatal-specific cell state not present in established adult hair follicles.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G18-matrix-location.txt`*

---

### G19-matrix-function — function, expect present

**Question** What function does the paper attribute to hair matrix? (hair matrix is also referred to as: matrix, hair matrix cells, matrix cells.)

**Intended answer** Expresses chemotaxis genes including CXCL14, reported to recruit regulatory T cells, and CD24 in control of autoimmunity - suggesting Treg accumulation and immune protection during early matrix differentiation.

**Gold span** (paragraph 4 of 10)

> increased expression of genes involved in chemotaxis, such as CXCL14

**The gold span in its paragraph**

> We evaluated hair matrix cells, which arise from the epidermal placode, a prenatal-specific cell state absent in established adult HFs 20 (Extended Data Fig. 3d,e). Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f). T reg cells are known to localize ar …

**Opus/Fable** → `correct` — judge: *CXCL14/CD24 chemotaxis and Treg accumulation/immune protection reproduced as intended.*

> Prenatal hair matrix cells upregulate chemotaxis genes such as CXCL14 (a chemokine reported to recruit regulatory T cells) and the autoimmunity-control gene CD24, which the authors interpret as a role for Treg cell accumulation and immune protection during early matrix differentiation. Matrix is also placed on the IRS differentiation trajectory downstream of placode, expressing matrix markers SHH and WNT10B.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 . This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

- *verbatim, paragraph 8 — **not the gold span's paragraph (4)***

  > AGR2 was downregulated along the IRS trajectory, whereas known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Chemotaxis genes CXCL14 and CD24 with Treg accumulation and immune protection, as intended.*

> Prenatal skin matrix cells had increased expression of chemotaxis genes such as CXCL14, previously reported to recruit regulatory T cells, and CD24, involved in control of autoimmunity, suggesting a role for matrix cells in Treg cell accumulation and immune protection during early hair follicle differentiation.

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > Compared with adult HFs, prenatal skin matrix cells had increased expression of genes involved in chemotaxis, such as CXCL14, a chemokine previously reported to recruit regulatory T (T reg ) cells 21 , and in control of autoimmunity (CD24) 22 .

- *verbatim, paragraph 4 — same paragraph as the gold span*

  > This result highlighted the potential role of T reg cell accumulation and immune protection in the early stages of matrix differentiation (Extended Data Fig. 3f).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G19-matrix-function.txt`*

---

### G20-lyve1-markers — markers, expect present

**Question** Which genes mark LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** LYVE1; also expresses GAS6.

**Gold span** (**not in this context** — the retriever never supplied it)

> GAS6, expressed by TML macrophages and LYVE1+ macrophages

**Hazard note given to the judge** The roster label writes LYVE1++, the paper writes LYVE1+. Marker evidence in the body text is thin - the subset's DEG panel is in Supplementary Table 22.

**Opus/Fable** → `correct` — judge: *LYVE1 itself plus GAS6, with an honest note that the context carries no fuller marker panel.*

> The supplied context gives no marker gene list for this subset; the only gene it ties to the subset's identity is LYVE1 itself, used to name the macrophage subset, and it additionally reports GAS6 as expressed by LYVE1+ macrophages (shared with TML macrophages).

- *verbatim, paragraph 1*

  > Gene ontology analysis showed that the four macrophage subsets (LYVE1 + , MHCII + , TML and iron-recycling) expressed gene programs that drive angiogenesis (Supplementary Tables 23-26).

- *verbatim, paragraph 4*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .

**Sonnet** → `honest_miss`

> The supplied context does not list specific marker genes that define LYVE1+ macrophage identity beyond LYVE1 itself; it only notes that marker genes were used to annotate macrophage subsets without naming them.

*No quotes given.*

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G20-lyve1-markers.txt`*

---

### G21-lyve1-location — location, expect present

**Question** Where in prenatal human skin is LYVE1+ macrophage found? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Co-locate with WNT2+ fibroblasts in the dermis, and are seen in close proximity to endothelial cells by RNAscope and immunofluorescence.

**Gold span** (**not in this context** — the retriever never supplied it)

> showed LYVE1+ and TML macrophages in close proximity to endothelial cells

**Opus/Fable** → `correct` — judge: *Names both endothelial-cell proximity and WNT2+ fibroblast co-location in the dermis.*

> LYVE1+ macrophages are found in close proximity to endothelial cells in prenatal skin (macrophages co-locate with endothelial cells in the early and late neurovascular microenvironments ME1 and ME5), and they also co-locate with WNT2+ fibroblasts in the dermis.

- *verbatim, paragraph 1*

  > Visium deconvolution analysis predicted co-location of prenatal skin macrophages with endothelial cells ('early and late neurovascular microenvironments', ME1 and ME5) (Fig. 1d and Extended Data Fig. 1e).

- *verbatim, paragraph 1*

  > Consistent with this finding, multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

- *verbatim, paragraph 5*

  > (g) Circos plot visualisation of representative significant (adjusted p-value <0.05, significance calculated in CellphoneDB using empirical shuffling and FDR-adjusted) predicted interactions between macrophages (LYVE1 + and TML macrophage) and co-localising WNT2 + fibroblasts in prenatal skin.

**Sonnet** → `correct` — judge: *Close proximity to endothelial cells by RNAscope/immunofluorescence, a main intended point.*

> LYVE1+ macrophages are found in close proximity to endothelial cells, as shown by RNAscope and immunofluorescence staining.

- *verbatim, paragraph 1*

  > multiplex RNAscope and immunofluorescence staining showed LYVE1 + and TML macrophages in close proximity to endothelial cells (Fig. 4a and Supplementary Video 1).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G21-lyve1-location.txt`*

---

### G22-lyve1-function — function, expect present

**Question** What function does the paper attribute to LYVE1+ macrophage? (LYVE1+ macrophage is also referred to as: LYVE1++ macrophage.)

**Intended answer** Promote sprouting angiogenesis and blood vessel morphogenesis, and maintain prenatal skin dermal fibroblasts (via PDGF-PDGFR and GAS6-AXL).

**Gold span** (**not in this context** — the retriever never supplied it)

> blood vessel morphogenesis by LYVE1+ macrophages

**Opus/Fable** → `correct` — judge: *Covers sprouting angiogenesis, vessel morphogenesis and fibroblast maintenance via growth factor and GAS6-AXL interactions.*

> LYVE1+ macrophages are attributed pro-angiogenic roles (promoting sprouting angiogenesis and blood vessel morphogenesis), maintenance of prenatal skin dermal fibroblasts through growth factor interactions, and GAS6-AXL signalling to WNT2+ fibroblasts that can induce immunosuppression and tissue repair.

- *verbatim, paragraph 1*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

- *verbatim, paragraph 3*

  > Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 4*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .

**Sonnet** → `correct` — judge: *Sprouting angiogenesis, vessel morphogenesis and dermal fibroblast maintenance including GAS6-AXL.*

> LYVE1+ macrophages are attributed roles in promoting sprouting angiogenesis and blood vessel morphogenesis, in maintaining prenatal skin dermal fibroblasts via growth factor interactions, and in inducing immunosuppression and tissue repair through GAS6-AXL signalling with WNT2+ fibroblasts.

- *verbatim, paragraph 1*

  > Gene module expression profiles suggested that sprouting angiogenesis (growth of new vessels) was promoted by LYVE1 + and TML macrophages, blood vessel morphogenesis by LYVE1 + macrophages and endothelial cell chemotaxis by iron-recycling macrophages (Extended Data Fig. 8i and Supplementary Table 27).

- *verbatim, paragraph 3*

  > Our identification of additional growth factor interactions (IGF1-IGF1R and GRN-EGFR) (Extended Data Fig. 7g and Supplementary Table 8) suggests that LYVE1 + macrophages play a part in the maintenance of prenatal skin dermal fibroblasts.

- *verbatim, paragraph 4*

  > Additionally, GAS6, expressed by TML macrophages and LYVE1 + macrophages, was predicted to interact with AXL receptors on WNT2 + fibroblasts (Extended Data Fig. 7g and Supplementary Table 8), and these interactions can induce immunosuppression and tissue repair 62,63 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G22-lyve1-function.txt`*

---

### G24-fibroblast-location — location, expect present

**Question** Where in prenatal human skin is fibroblast found?

**Intended answer** Dermal compartment. HOXC5+ early fibroblasts sit in the upper dermis; HF-specialised subsets (Dc, Dp) are within the dermal compartment from 12 PCW.

**Gold span** (**not in this context** — the retriever never supplied it)

> HOXC5+ early fibroblasts (located in the upper dermis

**Opus/Fable** → `correct` — judge: *Places fibroblasts in the dermis and HOXC5+ early fibroblasts in the upper dermis; omitting Dc/Dp is an accurate partial.*

> Fibroblasts occupy the dermis of prenatal skin (the dermal stroma), where they are analysed as dermal fibroblast subsets; HOXC5+ early fibroblasts specifically are located in the upper dermis.

- *verbatim, paragraph 3*

  > To identify the cellular and molecular mechanisms that may endow early prenatal skin with scarless healing properties, we investigated the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets (Extended Data Figs. 3c and 7a).

- *verbatim, paragraph 9*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Dermal compartment is accurate as far as it goes.*

> Fibroblasts are found in the dermal compartment of prenatal skin, described as dermal fibroblast subsets.

- *verbatim, paragraph 3*

  > the temporal changes in composition and transcriptional profile of the dermal fibroblast subsets

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G24-fibroblast-location.txt`*

---

### G25-fibroblast-function — function, expect present

**Question** What function does the paper attribute to fibroblast?

**Intended answer** Early-gestation fibroblasts downregulate extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

**Gold span** (paragraph 7 of 11)

> may favour tissue regeneration over scarring

**The gold span in its paragraph**

> Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring. Based on our data and previous studies, we also posit a potential role for early skin macrophages in conferring the distinct property of scarless healing in early prenatal skin. However, further studies are required to fully elucidate the interactions between macrophages and fibroblasts in human prenatal skin and to  …

**Opus/Fable** → `correct` — judge: *States the downregulation of ECM, collagen and inflammation genes favouring regeneration over scarring.*

> Dermal fibroblasts produce the collagen whose aggregation causes scars; in early gestation prenatal skin fibroblasts downregulate extracellular matrix, collagen deposition and inflammation genes and instead express immune-suppressive and regenerative genes, which the paper links to tissue regeneration rather than scarring.

- *verbatim, paragraph 3 — **not the gold span's paragraph (7)***

  > Scars result from aggregation of collagen produced by dermal fibroblasts and failure of the overlying epidermis to completely regenerate 51 .

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

- *verbatim, paragraph 3 — **not the gold span's paragraph (7)***

  > By contrast, prenatal skin fibroblasts had upregulated genes involved in immune suppression (CD200), regulation of inflammation (for example, RAMP2) and tissue regeneration (MDK) (Fig. 3a and Supplementary Tables 13-15).

**Sonnet** → `correct` — judge: *Downregulated ECM, collagen and inflammation favouring regeneration over scarring, exactly as intended.*

> The paper attributes to prenatal fibroblasts a role in favouring tissue regeneration over scarring, by downregulating genes involved in extracellular matrix formation, collagen deposition and inflammation during early gestation.

- *verbatim, paragraph 7 — same paragraph as the gold span*

  > Collectively, our findings suggest that prenatal skin fibroblasts in early gestation downregulate genes involved in extracellular matrix formation, collagen deposition and inflammation, which may favour tissue regeneration over scarring.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G25-fibroblast-function.txt`*

---

### G26-periderm-location — location, expect present

**Question** Where in prenatal human skin is periderm found?

**Intended answer** The outermost layer, overlying the dermal stroma in skin up to 8 PCW; present from 7 PCW, enriched in early gestation, and seen sloughing from 11 PCW.

**Gold span** (paragraph 2 of 11)

> with the periderm seen sloughing from 11 PCW

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Opus/Fable** → `correct` — judge: *Epidermal layer overlying dermal stroma, present from 7 PCW, sloughing from 11 PCW.*

> The periderm is an immature interfollicular epidermal cell state in the epidermal layer overlying the dermal stroma; it is present from 7 PCW and is seen sloughing off from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Superficial epidermal layer over dermal stroma, from 7 PCW, sloughing from 11 PCW.*

> Periderm is one of the immature interfollicular epidermal (IFE) cell types, present as a superficial epidermal layer overlying the dermal stroma, and it sloughs from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G26-periderm-location.txt`*

---

### G28-periderm-structure — structure, expect present

**Question** What does the paper say about the structure or morphology of periderm?

**Intended answer** A layer of epidermal cells overlying the dermal stroma, which sloughs from 11 PCW.

**Gold span** (paragraph 2 of 11)

> consisted of a layer of epidermal cells overlying the dermal stroma

**The gold span in its paragraph**

> Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a). At 14-15 PCW, budding of basal cells (hair placode and germ cells) and elongation of HFs (hair pegs) were observed (Fig. 2a). At 17 PCW, hair pegs were evident beneath a stratified epidermal layer (Fig. 2a).

**Hazard note given to the judge** thin - a layer description and a sloughing observation, not morphology proper

**Opus/Fable** → `correct` — judge: *Gives the layer description and the sloughing observation, matching the thin intended answer.*

> The periderm is described histologically as the outermost layer of the early prenatal epidermis, seen sloughing from 11 PCW, and it is classed among the immature interfollicular epidermal cells present from 7 PCW that decline after 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

- *verbatim, paragraph 3 — **not the gold span's paragraph (2)***

  > Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embryonic to fetal skin (Fig. 2b).

**Sonnet** → `correct` — judge: *Layer of epidermal cells over dermal stroma plus sloughing, all the paper offers.*

> Periderm is described as part of a layer of epidermal cells overlying the dermal stroma in early prenatal skin, which sloughs from 11 PCW.

- *verbatim, paragraph 2 — same paragraph as the gold span*

  > Prenatal skin up to 8 PCW consisted of a layer of epidermal cells overlying the dermal stroma, with the periderm seen sloughing from 11 PCW (Fig. 2a).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G28-periderm-structure.txt`*

---

### G29-hoxc5-location — location, expect present

**Question** Where in prenatal human skin is HOXC5+ early fibroblast found? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** The upper dermis.

**Gold span** (**not in this context** — the retriever never supplied it)

> HOXC5+ early fibroblasts (located in the upper dermis

**Opus/Fable** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis of prenatal skin and are abundant before 11 PCW.

- *verbatim, paragraph 2*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Upper dermis, as intended.*

> HOXC5+ early fibroblasts are located in the upper dermis and are abundant before 11 PCW.

- *verbatim, paragraph 2*

  > HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G29-hoxc5-location.txt`*

---

### G30-hoxc5-function — function, expect present

**Question** What function does the paper attribute to HOXC5+ early fibroblast? (HOXC5+ early fibroblast is also referred to as: HOXC5+ fibroblast.)

**Intended answer** A common fibroblast progenitor: differentiates along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts).

**Gold span** (**not in this context** — the retriever never supplied it)

> originated from a common fibroblast progenitor (HOXC5+ early fibroblast)

**Opus/Fable** → `correct` — judge: *Identifies the common progenitor role and both hair and dermal fibroblast trajectories.*

> HOXC5+ early fibroblasts act as the common fibroblast progenitor of prenatal skin dermis, differentiating along a hair fibroblast trajectory (pre-Dc, Dc, Dp) and a dermal fibroblast trajectory (WNT2+ and PEAR1+ fibroblasts); their transition into PEAR1+ fibroblasts is accompanied by upregulation of pro-inflammatory phenotype genes.

- *verbatim, paragraph 2*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW)

- *verbatim, paragraph 8*

  > Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).

- *verbatim, paragraph 4*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).

**Sonnet** → `correct` — judge: *Common progenitor with both hair and dermal fibroblast trajectories named correctly.*

> HOXC5+ early fibroblasts act as a common fibroblast progenitor that differentiates along two trajectories: one forming hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp), and the other forming WNT2+ and PEAR1+ dermal fibroblasts.

- *verbatim, paragraph 2*

  > Inferred trajectory analysis predicted that HOXC5 + early fibroblasts (located in the upper dermis (Fig. 2f) and abundant before 11 PCW (Extended Data Fig. 3c)) differentiated along two paths: the first (hair fibroblast trajectory) formed hair-specialized fibroblasts (pre-Dc cells, the Dc and Dp) and the second (dermal fibroblast trajectory) formed WNT2 + fibroblasts and PEAR1 + fibroblasts (abundant after 11 PCW) (Fig. 2e, Extended Data Figs. 3c and 4d and Supplementary Table 7).

- *verbatim, paragraph 8*

  > Additionally, similar to fibroblast differentiation in mouse skin, pre-Dcs, the Dc and Dp and dermal fibroblasts in human prenatal skin also originated from a common fibroblast progenitor (HOXC5 + early fibroblast) (Fig. 2e and Extended Data Fig. 4d).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G30-hoxc5-function.txt`*

---

### G31-dpysl2-markers — markers, expect present

**Question** Which genes mark DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** DPYSL2 itself, and AGR2 - reported as newly identified along the ORS/CL trajectory. BARX2 and SOX9 are named in the same sentence but explicitly as previously reported ORS-differentiation genes.

**Gold span** (**not in this context** — the retriever never supplied it)

> we identified new genes upregulated by DPYSL2+ basal cells, such as AGR2

**Hazard note given to the judge** This is the rule-1 trap. An answer of "AGR2" is right; "BARX2, SOX9" is reading the paper's attribution backwards. Judge must be told the distinction, not left to infer it.

**Opus/Fable** → `correct` — judge: *Gives DPYSL2 and AGR2 as the newly identified gene without claiming BARX2/SOX9 as new markers.*

> The subset is defined by DPYSL2 expression in mature basal interfollicular epidermal cells; along the ORS/CL trajectory these cells also upregulate AGR2, a newly identified gene.

- *verbatim, paragraph 7*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

**Sonnet** → `correct` — judge: *Gives DPYSL2 and AGR2 with the correct newly-identified attribution, avoiding the BARX2/SOX9 trap.*

> DPYSL2 itself defines this basal cell state, and the paper reports AGR2 as a newly identified gene upregulated by DPYSL2+ basal cells.

- *verbatim, paragraph 7*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G31-dpysl2-markers.txt`*

---

### G32-dpysl2-function — function, expect present

**Question** What function does the paper attribute to DPYSL2+ basal cell? (DPYSL2+ basal cell is also referred to as: DPYSL2+ basal, mature basal.)

**Intended answer** Part of the ORS/CL differentiation trajectory from POSTN+ basal cells, towards outer root sheath and companion layer.

**Gold span** (**not in this context** — the retriever never supplied it)

> ORS/CL trajectory, comprising DPYSL2+ basal cells, ORS and CL

**Opus/Fable** → `correct` — judge: *Places the cells on the ORS/CL trajectory downstream of POSTN+ basal cells and attributes BARX2/SOX9 correctly as ORS differentiation genes.*

> DPYSL2+ (mature) basal cells sit on the ORS/CL differentiation trajectory downstream of POSTN+ basal cells and upregulate AGR2 together with genes associated with outer root sheath differentiation (BARX2, SOX9); as mature interfollicular epidermal basal cells they increase in abundance after 11 PCW.

- *verbatim, paragraph 1*

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7). Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26 (Extended Data Fig. 4b,c and Supplementary Table 7).

- *verbatim, paragraph 7*

  > Mature basal (DPYSL2 + ) and suprabasal IFE cells increased after 11 PCW, whereas POSTN + basal cells were present throughout gestation (Fig. 2b and Extended Data Fig. 3b).

**Sonnet** → `correct` — judge: *Names the ORS/CL differentiation trajectory role and attributes BARX2/SOX9 correctly as previously reported ORS genes.*

> DPYSL2+ basal cells lie along the ORS/CL differentiation trajectory and upregulate genes such as AGR2, along with previously reported ORS differentiation genes BARX2 and SOX9.

- *verbatim, paragraph 1*

  > Along the ORS/CL trajectory, we identified new genes upregulated by DPYSL2 + basal cells, such as AGR2, and previously reported genes related to ORS differentiation (BARX2 and SOX9) 25,26

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G32-dpysl2-function.txt`*

---

### G33-caparteriole-markers — markers, expect present

**Question** Which genes mark capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** Arteriolar identity is marked by GJA5. In the organoid comparison, KDR and FLT1 (VEGF receptors) and the GATA2/NFATC1 regulons with targets such as VWF are downregulated in SkO capillary arterioles relative to prenatal skin.

**Gold span** (paragraph 4 of 8)

> their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin

**The gold span in its paragraph**

> … re highly expressed in SkO, whereas pro-angiogenic genes (for example, CXCL8) were upregulated in prenatal skin and primarily expressed by macrophages (Extended Data Fig. 11a and Supplementary Tables 30-34). Although expression of vascular endothelial growth factors (VEGF), VEGFA and VEGFB were increased in SkO cells, their receptors (KDR and FLT1) on SkO capillary arterioles were downregulated compared to prenatal skin (Extended Data Fig. 11b,c). These receptors are known downstream targets of GATA2, which has a key role in angiogenesis during development and regulates VEGF-induced endothelial cell migration and sprouting in vitro 72 . Regulon analysis showed that GATA2 and related regulons (for example, NFATC1) were downregulated i …

**Opus/Fable** → `miss`

> The supplied context does not give marker genes for capillary arterioles. It names GJA5 as characteristic of the arteriolar pathway as a whole and discusses genes downregulated in SkO capillary arterioles (KDR, FLT1, VWF), but no genes are stated to mark this cell type.

*No quotes given.*

**Sonnet** → `correct` — judge: *Gives GJA5 as the arteriolar characteristic gene, the main point of the intended answer.*

> The paper reports GJA5 as a characteristic gene of the arteriolar pathway, which includes capillary arterioles (as opposed to PLVAP marking the venular pathway).

- *verbatim, paragraph 1 — **not the gold span's paragraph (4)***

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G33-caparteriole-markers.txt`*

---

### G34-caparteriole-function — function, expect present

**Question** What function does the paper attribute to capillary arteriole? (capillary arteriole is also referred to as: capillary arteriole cells.)

**Intended answer** In prenatal skin they can differentiate further into arterioles, which SkO capillary arteriole cells cannot; they score highly for the sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 1 of 8)

> prenatal skin capillary arteriole cells could further differentiate into arterioles

**The gold span in its paragraph**

> … ted into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid 71 , which also lacked immune cells, further demonstrated the limited vasculature differentiation of this mesoderm-geared blood vessel organoid model (Extended Data Fig. 10d). This result …

**Opus/Fable** → `correct` — judge: *Notes further differentiation into arterioles unlike SkO cells, plus the tip-cell sprouting state.*

> Capillary arterioles are an intermediate stage of the arteriolar endothelial pathway that in prenatal skin can differentiate further into arterioles, and they carry sprouting-angiogenesis potential ('tip' cell state); in the organoid they express the sprouting signature but fail to guide stalk cells for new vessel formation, with VEGF receptors KDR and FLT1 and the GATA2 regulon downregulated.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a).

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h). This suggests that despite strong expression of the sprouting angiogenesis gene signature, SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation.

**Sonnet** → `correct` — judge: *Captures further differentiation into arterioles in prenatal but not SkO cells.*

> Capillary arteriole cells in prenatal skin can further differentiate into arterioles, whereas the equivalent SkO cells cannot; SkO capillary arteriole cells also fail to guide stalk cells for new blood vessel formation despite expressing sprouting angiogenesis genes.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > prenatal skin capillary arteriole cells could further differentiate into arterioles

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > SkO capillary arteriole cells are unable to guide stalk cells for new blood vessel formation

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G34-caparteriole-function.txt`*

---

### G35-pear1-markers — markers, expect present

**Question** Which genes mark PEAR1+ fibroblast?

**Intended answer** PEAR1 itself; APOE, IGFBP7 and ITM2A are upregulated during the transition from HOXC5+ fibroblasts, as a pro-inflammatory fibroblast phenotype.

**Gold span** (**not in this context** — the retriever never supplied it)

> were also upregulated during the transition from HOXC5+ fibroblasts into PEAR1+ fibroblasts

**Opus/Fable** → `correct` — judge: *PEAR1 plus APOE, IGFBP7, ITM2A upregulated in the HOXC5+ transition as a pro-inflammatory phenotype.*

> Beyond the defining PEAR1 label, the context reports that pro-inflammatory fibroblast genes APOE, IGFBP7 and ITM2A are upregulated in the transition from HOXC5+ to PEAR1+ fibroblasts, and that PEAR1+ (with WNT2+) fibroblasts express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 2*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).

- *verbatim, paragraph 5*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

**Sonnet** → `correct` — judge: *Gives APOE, IGFBP7 and ITM2A as the pro-inflammatory transition genes plus supported extras.*

> PEAR1+ fibroblasts are marked by upregulation of APOE, IGFBP7 and ITM2A (pro-inflammatory phenotype genes), and express CDKN1A, IL1R1 and POSTN.

- *verbatim, paragraph 2*

  > Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts

- *verbatim, paragraph 5*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G35-pear1-markers.txt`*

---

### G36-pear1-function — function, expect present

**Question** What function does the paper attribute to PEAR1+ fibroblast?

**Intended answer** A dermal fibroblast endpoint, abundant after 11 PCW, carrying the adult pro-inflammatory gene expression profile along with senescence and collagen deposition genes.

**Gold span** (**not in this context** — the retriever never supplied it)

> formed WNT2+ fibroblasts and PEAR1+ fibroblasts (abundant after 11 PCW)

**Opus/Fable** → `correct` — judge: *Late-gestation dermal endpoint with adult pro-inflammatory, senescence and collagen deposition profile.*

> PEAR1+ fibroblasts are a late-gestation dermal fibroblast subset that acquires an adult-like, pro-inflammatory and scar-promoting profile, expressing senescence (CDKN1A), cytokine (IL1R1) and collagen deposition (POSTN) genes found in pathogenic fibroblasts of fibrotic skin disorders. They arise from HOXC5+ early fibroblasts along the dermal fibroblast trajectory.

- *verbatim, paragraph 2*

  > The adult fibroblast gene expression profile was increased in WNT2 + and PEAR1 + prenatal fibroblasts, which were abundant in later gestation (Fig. 3a and Extended Data Figs. 3c and 7b). Genes associated with a pro-inflammatory fibroblast phenotype (APOE, IGFBP7 and ITM2A) 43,52 were also upregulated during the transition from HOXC5 + fibroblasts into PEAR1 + fibroblasts (Extended Data Fig. 7c).

- *verbatim, paragraph 5*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

**Sonnet** → `correct` — judge: *Conveys the senescence/cytokine/collagen pro-inflammatory profile shared with adult pathogenic fibroblasts.*

> PEAR1+ fibroblasts, together with WNT2+ fibroblasts, express genes involved in cellular senescence, cytokine pathways and collagen deposition that are highly expressed in pathogenic fibroblasts of fibrotic skin disorders, linking them to a scar-promoting phenotype.

- *verbatim, paragraph 5*

  > Notably, WNT2 + and PEAR1 + prenatal fibroblasts expressed several genes involved in cellular senescence (CDKN1A), cytokine pathways (for example, IL1R1) and collagen deposition (for example, POSTN) (Fig. 3a,b), which are highly expressed in pathogenic fibroblasts of fibrotic skin disorders 53 .

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G36-pear1-function.txt`*

---

### G38-postn-function — function, expect present

**Question** What function does the paper attribute to POSTN+ basal cell? (POSTN+ basal cell is also referred to as: POSTN+ basal.)

**Intended answer** Increased cellular migration, suggested to be involved in placode specification and dermal invagination; the origin of both the ORS/CL and IRS differentiation trajectories.

**Gold span** (paragraph 1 of 8)

> may be involved in placode specification and dermal invagination

**The gold span in its paragraph**

> … as known matrix markers such as SHH and WNT10B 25,26 were upregulated (Extended Data Fig. 4b,c and Supplementary Table 7). Loss of AGR2, which functions in the assembly of cysteine-rich receptors enriched in HFs, promotes cell migration 27 . Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

**Opus/Fable** → `correct` — judge: *Origin of both ORS/CL and IRS trajectories, with increased migration linked to placode specification and dermal invagination.*

> POSTN+ basal cells act as the epidermal progenitor state that gives rise to both the ORS/CL and IRS trajectories, and their increased cellular migration is proposed to contribute to placode specification and dermal invagination.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory and pseudotime analysis of epidermal cells in the integrated prenatal skin and SkO data predicted the differentiation of POSTN + basal cells into two paths: ORS/CL trajectory, comprising DPYSL2 + basal cells, ORS and CL; and IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7).

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

**Sonnet** → `correct` — judge: *States the migration role in placode specification and dermal invagination.*

> The paper suggests that increased cellular migration in POSTN+ basal cells may be involved in placode specification and dermal invagination.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Our findings suggest that increased cellular migration in POSTN + basal cells may be involved in placode specification and dermal invagination.

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G38-postn-function.txt`*

---

### G39-arteriole-markers — markers, expect present

**Question** Which genes mark arteriole?

**Intended answer** GJA5, given as the characteristic arteriolar gene (against PLVAP for venular).

**Gold span** (paragraph 1 of 8)

> for example, GJA5 for arteriolar and PLVAP for venular

**The gold span in its paragraph**

> … ata Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig. 4d and Extended Data Fig. 10a). Additional comparison with a human ES cell-derived and iPS cell-derived blood vessel organoid 71 , which also lacked i …

**Hazard note given to the judge** Shares nearly every sentence with Capillary arterioles; an answer drawn from the capillary-arteriole evidence should not be marked wrong without checking which label the sentence attributes it to.

**Opus/Fable** → `correct` — judge: *GJA5 as the characteristic arteriolar gene against PLVAP for venular, correctly attributed to the arteriolar pathway.*

> GJA5 is given as the characteristic gene of the arteriolar pathway (capillaries, capillary arterioles and arterioles), in contrast to PLVAP for the venular pathway; no arteriole-specific marker list beyond this is provided.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).

**Sonnet** → `correct` — judge: *GJA5 correctly attributed to the arteriolar side of the contrast.*

> GJA5 is given as the characteristic gene marking the arteriolar pathway.

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G39-arteriole-markers.txt`*

---

### G40-arteriole-function — function, expect present

**Question** What function does the paper attribute to arteriole?

**Intended answer** The endpoint of the arteriolar differentiation pathway from early endothelial cells via capillaries and capillary arterioles; scores for sprouting angiogenesis tip-cell state.

**Gold span** (paragraph 1 of 8)

> differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles)

**The gold span in its paragraph**

> …  fewer and less heterogeneous endothelial cells in the immunodeficient SkOs compared to prenatal skin, despite the formation of well-developed HFs, epidermis and neural cells (Fig. 4b,c, Extended Data Fig. 9b and Supplementary Table 29). Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c). Unlike SkO capillary arteriole cells, prenatal skin capillary arteriole cells could further differentiate into arterioles (Fig …

**Opus/Fable** → `correct` — judge: *Gives both the tip-cell sprouting score and the arteriolar differentiation endpoint.*

> The only function the context attributes to arterioles is a sprouting-angiogenesis (new blood vessel growth) potential: prenatal skin arterioles, along with capillary arterioles and capillaries, showed increased 'tip' cell state scoring. Arterioles are also described as the endpoint of the arteriolar differentiation pathway from early endothelial cells.

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > However, sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells (Extended Data Fig. 10g,h).

- *verbatim, paragraph 1 — same paragraph as the gold span*

  > Inferred trajectory analysis showed that early endothelial cells in prenatal skin differentiated into either an arteriolar pathway (capillaries, capillary arterioles and arterioles) or venular pathway (postcapillary venules and venules), with expression of characteristic genes (for example, GJA5 for arteriolar and PLVAP for venular) (Fig. 4d and Extended Data Fig. 10a-c).

**Sonnet** → `correct` — judge: *Accurate partial answer naming the tip-cell sprouting angiogenesis score for arterioles.*

> Prenatal skin arteriole cells (along with capillary arteriole and capillary cells) showed increased sprouting angiogenesis potential, as assessed by scoring the 'tip' cell state.

- *verbatim, paragraph 2 — **not the gold span's paragraph (1)***

  > sprouting angiogenesis potential, assessed by scoring the 'tip' cell state, was increased in both SkO capillary arteriole cells and prenatal skin arteriole, capillary arteriole and capillary cells

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G40-arteriole-function.txt`*

---

### G41-cuticle-location — location, expect present

**Question** Where in prenatal human skin is cuticle/cortex found? (cuticle/cortex is also referred to as: cuticle and cortex cells.)

**Intended answer** Part of the inner layers of the hair follicle.

**Gold span** (paragraph 6 of 10)

> part of the inner layers of the HF

**The gold span in its paragraph**

> Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6). In addition, we observed immature and mature interfollicular epidermal (IFE) cells. Immature IFE cells, including periderm, immature basal and immature suprabasal cells, were present from 7 PCW and decreased after 11 PCW, during the transition from embry …

**Opus/Fable** → `correct` — judge: *Identifies cuticle/cortex as part of the inner layers of the hair follicle.*

> Cuticle and cortex cells are hair follicle cells forming part of the inner layers of the follicle, identified in the scRNA-seq data from 14 PCW; they lie on the inner root sheath differentiation trajectory.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > Consistent with our histological observations, we identified HF cells from 14 PCW in our scRNA-seq data, which comprised placode, matrix (SHH + ), outer root sheath (ORS) (SLC26A7 + ), companion layer (CL), inner root sheath (IRS) and cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6).

- *verbatim, paragraph 1 — **not the gold span's paragraph (6)***

  > IRS trajectory, involving placode, matrix, cuticle/cortex and IRS (Fig. 2d, Extended Data Fig. 4a and Supplementary Table 7)

**Sonnet** → `correct` — judge: *Places cuticle/cortex in the inner layers of the hair follicle as intended.*

> Cuticle/cortex cells form part of the inner layers of the hair follicle.

- *verbatim, paragraph 6 — same paragraph as the gold span*

  > cuticle and cortex cells (cuticle/cortex; part of the inner layers of the HF) (Fig. 2a-c, Extended Data Fig. 3a,b and Supplementary Table 6)

*Context both readers saw: `/Users/do12/Documents/GitHub/Atlas-reporter-wt/retrieval-matrix/experiments/stage3b/contexts/asta-comb/G41-cuticle-location.txt`*

---

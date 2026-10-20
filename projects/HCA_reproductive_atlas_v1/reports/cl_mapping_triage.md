# CL mapping triage — HCA_reproductive_atlas_v1/cas.json

CL release 2026-06-08 (OLS4 and Ubergraph agree). 312 annotations; 223 carry a
CL term, 89 do not (nearly all L1–L3 grouping levels).

Method (crude first pass, no paper reading): for each curated CURIE, pull its
CL descendants once and match them against keywords in `cell_fullname`;
then a batch of `exact`/`stemmed` lexical probes for terms that would not be
descendants of the curated parent. Nothing here is confirmed against the
report text — this is a shortlist for review.

## 1. Outright errors (fix regardless of specificity)

> **Status: all six corrected in `cas.json` on 2026-10-16.** Five were a build
> bug, not curation (see `FIELD_PROVENANCE.md` §4); `Immune_T_Cyc` is wrong in
> the source spreadsheet and is corrected by an override. The table below shows
> the mapping **as it was**; `cl_mapping_revisions.tsv` tracks both the old and
> the current value per row in `current_cl_id` / `cl_id_in_cas_now`.

| cell_label | curated | problem | fix |
|---|---|---|---|
| `Immune_T_Cyc` | CL:0000076 "cycling T cell" | CL:0000076 is **squamous epithelial cell** | **CL:4033069** cycling T cell |
| `Immune_uNK1` | CL:4052028 "uterine natural killer cell 1, human" | CL:4052028 is the parent `uterine natural killer cell` | **CL:4052051** uterine natural killer cell 1, human |
| `Immune_uNK2` | CL:4052028 "…2, human" | same | **CL:4052052** |
| `Immune_uNK3` | CL:4052028 "…3, human" | same | **CL:4052053** |
| `Granulosa_AMHneg_Atretic`, `Granulosa_sq_Fetal` | CL:0000501 "squamous granulosa cell" | CL:0000501 is `granulosa cell` | **CL:4033083** squamous granulosa cell |

## 2. A more specific CL term already exists (high confidence)

| cell_label(s) | curated | proposed |
|---|---|---|
| `Granulosa_AMHneg_Squamous`, `Granulosa_sq_Fetal` | CL:0000501 granulosa cell | CL:4033083 squamous granulosa cell |
| `Granulosa_AMHneg_Atretic`, `Granulosa_AMHpos_Atretic` | CL:0000501 | CL:4033090 atretic granulosa cell (sits under `atretic follicular cell of ovary`, not under granulosa cell) |
| `Gonadal_preGranulosa-OSEderived_early/_late` | CL:0000501 | CL:4033066 pre-granulosa cell |
| `Gonadal_preGranulosa-CEderived` (L3, first wave) | CL:0000630 supporting cell | CL:4033066 pre-granulosa cell |
| `Mesen_Theca_Atretic` | CL:4052012 interna theca cell | CL:4052027 atretic theca cell (sits under `atretic follicular cell of ovary`, not under theca cell) |
| `Mesen_UterusSMCs_Fetal` | CL:0000192 smooth muscle cell | CL:0002601 uterine smooth muscle cell |
| `Mesen_FallopianSMCs_Fetal` | CL:0000192 | CL:4052022 fallopian tube smooth muscle cell |
| `Epi_EndoGlandLum_Prof/_eSec/_mSec` (+ L3 `Endometrial luminal glandular epithelial`) | CL:0009084 glandular epithelial cell of endometrium | CL:4052050 luminal epithelial cell of endometrium — a *sibling* of the current term under `CL:0002149 epithelial cell of uterus`, so a lateral correction rather than a refinement |
| `Epi_CervixSquamous`, `Epi_CervixSquamous_Cyc` | CL:0002535 epithelial cell of cervix | CL:0002244 squamous cell of ectocervix (already used by L3 `Epi_EctocervixVaginaSquamous`), or CL:1001575 uterine cervix squamous cell |
| `Cervix mucinous secretory epithelial` (L3) | CL:0002535 | CL:1001587 uterine cervix secretory cell / CL:0002152 columnar cell of endocervix |
| `Epi_Vagina_Upper_Fetal` | CL:0000076 squamous epithelial cell | CL:1001578 vagina squamous cell |
| `Epi_MesonephricTub_Fetal` | CL:1100001 secretory epithelial cell | CL:1000022 mesonephric nephron tubule epithelial cell |
| `Mesen_OvarianFibs_Outcor` | CL:0002132 stromal cell of ovary | CL:0002133 stromal cell of ovarian cortex |
| `Mesen_OvarianFibs_InncorMedulla`, `_Medulla_SMCsLike` | CL:0002132 | CL:0002134 stromal cell of ovarian medulla (note: the `_InncorMedulla` composition is 91 % `Cortex_outer`, so the label and the data disagree — check before mapping) |
| `Mesen_EndoStromalFib_nEMC_Sec` ("decidualised") | CL:0002255 stromal cell of endometrium | CL:2000002 decidual cell |
| `Immune_CD8_T_EM` | CL:0001203 CD8+ memory T, CD45RO+ | CL:0000913 effector memory CD8-positive, alpha-beta T cell |
| `Mesen_vSMCs_largeArt`, `_medArt` | CL:0000359 vascular associated SMC | CL:0019018 blood vessel smooth muscle cell (modest; all arterial CL terms are organ-specific) |

## 3. Needs a judgement call before mapping (evidence required)

- **`Granulosa_AMHpos_*` (5 sets, all CL:0000501).** AMH+/FSHR+ growing-follicle
  granulosa. CL offers `CL:4033084 cuboidal granulosa cell`, and the
  steroidogenic / non-steroidogenic split plausibly tracks
  `CL:4033067 mural granulosa cell` vs `CL:0000711 cumulus granulosa cell`.
  Strong candidates but the mapping needs the paper, not the label.
- **Secretory-phase endometrial stroma** (`_eSec/_mSec/_lSec`, DKK1+): these are
  decidualising; whether to use `CL:2000002 decidual cell` or keep
  `CL:0002255` plus a state is a curation policy question.
- **`Immune_Mac_LYVE1hi`** (CL:0000864 tissue-resident macrophage) —
  `CL:4033064 uterine resident macrophage` exists but this set spans ovary and
  fallopian tube, so the uterine term is probably too narrow.
- **`Immune_uMac_Inf`** currently `CL:0000863 M1 macrophage`; M1 is a
  polarisation term, and 92 % of these cells are menstrual fluid. Worth revisiting.

## 4. Nothing in CL — new term candidates

Confirmed absent by exact + stemmed probes.

**Highest value (collapses the most annotations):**
- **endometrial basalis vs functionalis** — CL has neither. 14 annotations share
  `CL:0009084` and 12 share `CL:0002255` precisely because the
  basalis/functionalis distinction has no term. Two new terms
  (glandular epithelial cell of endometrial basalis / of functionalis, and the
  stromal pair) would carry most of the endometrial nomenclature.
- **post-capillary venular endothelial cell** (`Endo_ven_pcv`, `_apcv`, `_tpcv`
  and their L3 parent, four annotations in all, at
  `CL:1000414 endothelial cell of venule`; ACKR1+/SELE+).

**Fetal / developmental structures with no CL term at all:**
rete ovarii epithelial cell · epoophoron fibroblast · Müllerian
(paramesonephric) duct stromal fibroblast and undifferentiated epithelial cell ·
urogenital sinus fibroblast (upper and lower), UGS smooth muscle cell,
UGS-derived vaginal epithelial cell · labioscrotal swelling fibroblast · labial
fibroblast · glans fibroblast · prepuce fibroblast and preputial squamous
epithelial cell · corpus cavernosum fibroblast · corpus spongiosum fibroblast ·
genital surface squamous epithelial cell · uterine ligament fibroblast ·
fallopian tube ligament fibroblast.

**Adult regional mesenchyme with no term:**
cervical stromal cell · vaginal stromal cell · fallopian tube stromal cell ·
uterine interstitial fibroblast · cervical smooth muscle cell · vaginal smooth
muscle cell · ovarian inclusion fibroblast.

**Other:**
tolerogenic dendritic cell (`Immune_tolDC`, currently the bare `CL:0000451
dendritic cell`) · pericyte–smooth muscle intermediate · endometrial
pericyte-stromal-like cell.

## 5. Location consistency

Every proposed mapping and every new-term candidate was checked against the
atlas's own `composition` evidence (`Organ`, `Organ_part`, `Tissue_ROI`) and,
where the CL term carries an anatomical axiom, against that axiom. Results are
in the `location_evidence` / `location_check` / `location_note` columns of both
TSVs.

**Three suggested mappings contradict the location evidence — do not adopt:**

- `Mesen_OvarianFibs_InncorMedulla` and `Mesen_OvarianFibs_Medulla_SMCsLike` →
  `CL:0002134`, which is axiomatised `part_of ovarian medulla`. Both sets are
  overwhelmingly cortical (92% and 82% cortex by `Organ_part`; 91% and 82%
  `Cortex_outer` by ROI). The label says medulla and the data says cortex; that
  conflict is the atlas team's to resolve.
- `Granulosa_AMHpos_nonSteroidogenic` → `CL:0000711 cumulus granulosa cell`.
  Cumulus cells form the cumulus-oocyte complex of antral follicles, but this
  set is 99% `Cortex_outer` with **zero** antral follicle. **Suggestion changed
  to `CL:4033084 cuboidal granulosa cell`**, which carries no conflicting
  location axiom.

**Four more are supported only weakly** — `Mesen_UterusSMCs_Fetal` (30% uterus,
21% fallopian tube, against a `part_of uterus` term), `Epi_MesonephricTub_Fetal`
(13% mesonephros), `Mesen_FallopianSMCs_Fetal` (36% gonad block) and
`Immune_uNK3` (17% fallopian tube). The fetal dissection blocks are coarse
enough that none of these is a contradiction, but none confirms its term either.

**Four new-term candidates contradict their own proposed names:**

- **`glandular epithelial cell of endometrial basalis`** — the most important
  one, because the basalis/functionalis pair is the highest-priority ask.
  `Epi_EndoGlandBas` is **98% `Superficial_Endometrium`**, i.e. the set named
  basalis sits in the superficial compartment. Either the ROI vocabulary does
  not encode the distinction or the set is misnamed; resolve before requesting.
  Relatedly, the functionalis sets split ~50/50 between `Endometrium` and
  `Superficial_Endometrium`, so these ROIs do not discriminate the compartment
  at all. The case for the terms rests on the biology and the 14-way collapse
  onto `CL:0009084`, not on location.
- **`vaginal stromal cell`** — `Mesen_VaginaFib_Lower_Fetal`, grouped here as
  lower vaginal stroma, is 96% `Gonad_and_extragonadal` (96% Ovary by organ).
  The adult `Mesen_VaginaFibs` is 100% Vagina and is sound. Split the group.
- **`labial fibroblast`** — 94% the "uterus, cervix, vagina" block, only 5%
  external genitalia, for a structure that *is* external genitalia.
- **`uterine interstitial fibroblast`** — its largest block is Fallopian Tube
  (0.28), above every uterus-containing block.

**One pair looks close to swapped:** the paramesonephric (Müllerian) duct set
has Mesonephros as its top organ (0.38), while the mesonephric duct set is only
6% Mesonephros. The ducts are adjacent and co-dissected so this may be block
coarseness, but the two should be checked together.

Everything else is either consistent with its location evidence (10 new-term
rows, 3 revision rows) or proposes a term with no anatomical commitment for
location to speak to.

## 6. Verification

Every claim in the two TSVs was re-checked mechanically against CL (release
2026-06-08) and against the atlas file: all 53 cited CURIEs resolve, every
suggested term label matches its CL label exactly, every labelset, cell name,
cell count and current mapping recomputes from the atlas, and every composition
percentage quoted was confirmed. Four "is a descendant of the current term"
claims were **false** and have been corrected — `CL:4033090`, `CL:4052027` and
`CL:4052050` are lateral moves, not refinements. Two counts in this document
were wrong and are fixed above.

The absence claims in section 4 rest on exact/stemmed probes plus
label-or-synonym surveys of CL; they are good evidence but not proof, since an
unprobed phrasing could exist.

## 7. Out of scope for this pass
- **89 annotations carry no CL term**, almost all L1–L3 grouping levels
  (`T`, `NK`, `Macrophages`, `Granulosa`, `Theca`, `Mesothelial`, …). Most have
  obvious CL terms; that is a separate, mostly mechanical pass.
- **Cycling / menstrual-phase / atretic variants** are arguably cell *states*
  rather than types. CL does carry some (`cycling T cell`, `cycling NK cell`,
  `cycling macrophage`, `atretic granulosa cell`), so the question is where this
  project draws the line, not what CL offers.

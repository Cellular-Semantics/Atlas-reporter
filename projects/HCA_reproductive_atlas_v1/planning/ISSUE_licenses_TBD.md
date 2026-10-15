# [licensing] What is still TBD after recording the corpus licences

`Paper.license` now exists on `supplement_manifest.schema.json`
(`feature/supplement-licence`), and
`projects/HCA_reproductive_atlas_v1/scripts/record_licenses.py` has populated it
for all 22 papers in the reproductive corpus. Fourteen licences came from
`<permissions>` blocks in Europe PMC JATS already sitting in the store, unread.

Where that leaves the corpus:

| verdict | n | papers |
|---|---|---|
| `CC-BY-4.0`, redistributable | 10 | incl. the atlas preprint |
| `CC-BY-NC-ND-4.0` | 3 | devcel.2024.01.006, s41467-024-55440-2, pnas.2404775121 |
| `CC-BY-NC-4.0` | 1 | sciadv.adm7506 |
| `unknown` | 8 | 3× Dev Cell, Nat Cell Biol, Nat Med, Clin Exp Immunol, science.adx0659, — |

Five things are deliberately unresolved. None blocks the triage work; all of
them bear on what this public repository may carry.

---

## 1. Is this repository's distribution non-commercial? (one paper turns on it)

`10.1126/sciadv.adm7506` is `CC-BY-NC-4.0` — NonCommercial, but **no**
NoDerivatives. So unlike the three NC-ND papers, the chunks and extracted text
derived from it are permitted *if* redistribution here counts as
non-commercial.

`record_licenses.py` declines to decide and records `redistributable: false`
with the reasoning in `license.note`. This is the only judgement call in the
corpus, and it is a decision about this repository rather than a fact about the
licence.

**To change it:** edit the verdict in the script's `REDISTRIBUTABLE_SPDX` /
`NEEDS_HUMAN_CALL` tables and re-run, so the data stays derived rather than
hand-edited.

## 2. Eight papers are `unknown` because no JATS is in the store

`unknown` is a recorded verdict — the check was made locally and came up empty.
It does **not** mean closed access, and three of the eight are plausibly open:

- `10.1016/j.devcel.2022.02.017`, `10.1016/j.devcel.2023.07.014`,
  `10.1016/j.devcel.2025.09.011`
- `10.1038/s41556-022-00961-5` (Nat Cell Biol), `10.1038/s41591-020-1040-z` (Nat Med)
- `10.1093/cei/uxad029`, `10.1126/science.adx0659`

**To settle:** fetch their JATS (Europe PMC, where a PMCID exists) and re-run
`record_licenses.py` — it overwrites from current evidence each pass, so this
needs no code change. Papers with no PMCID need a `manual` assertion read off
the article page.

## 3. Should the ten CC-BY manifests be committed?

Currently the whole supplement store is ignored:

```gitignore
projects/**/supplements/
projects/**/units/
```

That was the right default when nothing recorded a licence. Now that ten papers
are recorded CC-BY-4.0, committing *their* manifests — and arguably their
`text/` and prose `units/` — is defensible, and would restore bibliographic
provenance that is currently local-only.

The shape would mirror what `local_index` already does: ignore by default,
re-include the permissive ones. The hard part is that a `.gitignore` cannot read
a manifest, so the re-include has to be written out per slug, which is the
problem in §4.

**Open question:** manifests only, or the derived text too?

## 4. `local_index` has the same question and no field to answer it

The local-index manifests carry no licence at all, and `.gitignore` re-includes
the preprint's text by **hardcoded slug**:

```gitignore
!projects/**/local_index/papers/10.64898_*/chunks/
```

That works for one paper and does not generalise. The licence that justifies it
is now recorded — but on the *supplement* manifest, not the local-index one, so
the rule still cannot cite it.

**Proposal:** give the local-index manifest the same `license` object (reuse the
`$defs/License` definition), and generate the re-include list from recorded
licences rather than maintaining slugs by hand.

## 5. `feature/supplement-licence` is not on `dev`

The schema change was merged into `HCA_reproductive_atlas_v1` directly, because
the licences to record are here and `gh` auth was invalid at the time (no token
in `.env`, keyring token rejected). The branch is unchanged and ready.

**Action:** open the PR into `dev` once `gh auth login` is done.

---

## Note on provenance

`license.source` says where each claim came from: `europepmc` for the 14 read
from JATS, `biorxiv` for the atlas preprint, `manual` for the eight `unknown`.
Any re-derivation should preserve that distinction — a licence read from a
publisher's own XML and one asserted by a person are not equally strong, and
§1 is exactly the case where the difference matters.

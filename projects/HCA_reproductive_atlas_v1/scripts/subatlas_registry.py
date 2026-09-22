#!/usr/bin/env python3
"""Populate source.subatlas_papers, and the two measures it is the denominator for.

An enrichment pass over an existing cas.json, run after build_cas.py. Two passes,
deliberately separate — they have different characters and different failure modes.

Pass 1 — counting, from the parquet. Per contributing-study obs column, a value
count. `cell_sets[].n_cells` is the denominator for share_of_subatlas_label: a
count of cells from that source cell set *present in the atlas*, which where the
integration subsampled its source is not the published cell set's size. In the
same pass — because that is the rule that keeps a stored ratio honest — every
transferred annotation gets subatlas_label_total_cells and the two shares whose
denominators are now beside them. The third measure, share_of_atlas_cell_set, is
`cell_ratio`, already written by build_cas.py from n_cells.

Never sum cell_count over a set of cell sets to get any of these. The hierarchy
happens to validate on this atlas, which is exactly what makes the shortcut
tempting and its result indistinguishable from a counted one. Run as a *check*
it is worth a lot, and check 2 below runs it three ways.

Pass 2 — resolving, per study. The DOI is already in source_taxonomy for eight of
the nine; the rest is bibliographic detail resolved from it (RESOLVED, table
below — this script does no network I/O). celltype_OvarySanger2026 has no
publication and gets status "unresolved" with no doi: an entry saying "this is a
real contributor with nothing to read" is worth more than an absence, and at
15.3% of cells it is the single largest contributor. `status` on the resolved
eight, and asta_indexing, are left for a later pass — they are about reachability
of text, not about the atlas.

NOTE — why this is an enrichment pass and not part of build_cas.py.
Re-running build_cas.py on the committed cas.json renumbers 311 of 312
cell_set_accessions: the accession index is the node insertion order, and the
committed file predates the `sorted(objcodes)` fix that made that order stable.
Endo_ven_apcv, the reference cell set, moves from HCArepro:L4:0204 to
HCArepro:L4:0011. Those accessions are cited in the planning documents, the
reports, the notes and the test project, so this pass edits cas.json in place
instead, leaving every existing value untouched and adding only new keys.

Run from the project root:
    python scripts/subatlas_registry.py            # enrich + check
    python scripts/subatlas_registry.py --check    # check only, no write
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict

import pyarrow.parquet as pq

CAS = "cas.json"
PARQUET = "h5ad_obs/obs.categoricals.parquet"

#: Contributing-study obs columns. The column name IS the registry label and the
#: source_labelset on every transfer — recorded verbatim, untidy or not.
STUDIES = [
    "celltype_GarciaAlonso2021",
    "celltype_GarciaAlonso2022",
    "celltype_HECA",
    "celltype_Lardenois2026",
    "celltype_Lorenzi2025",
    "celltype_OvarySanger2026",
    "celltype_Ulrich2022",
    "celltype_Ulrich2024",
    "celltype_Weigert2025",
]

#: Pass 2, resolved from the DOI in source_taxonomy via Europe PMC. Recorded here
#: rather than re-fetched so the pass is reproducible offline and so what was
#: resolved is reviewable in the diff. `venue` is Europe PMC's journal title
#: verbatim. Two labels disagree with the year their publication resolves to;
#: `label` is the obs column and stays verbatim, `year` is the publication's.
RESOLVED: dict[str, dict[str, object]] = {
    "celltype_GarciaAlonso2021": {
        "first_author": "Garcia-Alonso",
        "year": 2021,
        "title": "Mapping the temporal and spatial dynamics of the human endometrium in vivo and in vitro",
        "venue": "Nature genetics",
    },
    "celltype_GarciaAlonso2022": {
        "first_author": "Garcia-Alonso",
        "year": 2022,
        "title": "Single-cell roadmap of human gonadal development",
        "venue": "Nature",
    },
    # A consortium column, not a first-author study: the DOI resolves to the HECA
    # paper, whose first author is Marečková. label and first_author will not look
    # alike, which is the point of keeping label verbatim.
    "celltype_HECA": {
        "first_author": "Marečková",
        "year": 2024,
        "title": "An integrated single-cell reference atlas of the human endometrium",
        "venue": "Nature genetics",
    },
    "celltype_Lardenois2026": {
        "first_author": "Lardenois",
        "year": 2026,
        "title": "Single-cell exploration of gonadal somatic cell lineage specification during human sex determination",
        "venue": "Developmental cell",
    },
    # Label says 2025 (first published online 2025-12-17); the issue is Feb 2026.
    "celltype_Lorenzi2025": {
        "first_author": "Lorenzi",
        "year": 2026,
        "title": "Spatiotemporal cellular map of the developing human reproductive tract",
        "venue": "Nature",
    },
    "celltype_Ulrich2022": {
        "first_author": "Ulrich",
        "year": 2022,
        "title": "Cellular heterogeneity of human fallopian tubes in normal and hydrosalpinx disease states identified using scRNA-seq",
        "venue": "Developmental cell",
    },
    "celltype_Ulrich2024": {
        "first_author": "Ulrich",
        "year": 2024,
        "title": "Cellular heterogeneity and dynamics of the human uterus in healthy premenopausal women",
        "venue": "Proceedings of the National Academy of Sciences of the United States of America",
    },
    "celltype_Weigert2025": {
        "first_author": "Weigert",
        "year": 2025,
        "title": "A cell atlas of the human fallopian tube throughout the menstrual cycle and menopause",
        "venue": "Nature communications",
    },
}

#: Newly generated at the Sanger and unpublished. Recorded as a contributor with
#: nothing to read rather than left out.
UNRESOLVED = {"celltype_OvarySanger2026"}

ROUND = 4

# --------------------------------------------------------------- fine codes per cell set
_MINTED_CODE = re.compile(r"Minted generic leaf for celltype_HCA_fine='([^']+)'")


def leaf_codes(ann: dict) -> set[str] | None:
    """The celltype_HCA_fine codes a leaf cell set is made of.

    Three shapes, because build_cas.py prunes composition.celltype_HCA_fine
    wherever it merely restates the cell set:
      - the ordinary leaf, whose cell_label IS the verbatim code;
      - the two merged-code leaves, which keep composition.celltype_HCA_fine;
      - the 13 minted generic leaves, whose code is named in their comment.
    """
    comp = (ann.get("composition") or {}).get("celltype_HCA_fine")
    if comp:
        return {v["author_value"] for v in comp["values"]}
    minted = _MINTED_CODE.search(ann.get("comment") or "")
    if minted:
        return {minted.group(1)}
    return {ann["cell_label"]}


def codes_by_accession(annotations: list[dict]) -> dict[str, set[str]]:
    """Fine codes per cell set: leaves directly, internal nodes as the union below."""
    children = defaultdict(list)
    for a in annotations:
        if a.get("parent_cell_set_accession"):
            children[a["parent_cell_set_accession"]].append(a["cell_set_accession"])
    by_acc = {a["cell_set_accession"]: a for a in annotations}

    codes: dict[str, set[str]] = {}

    def walk(acc: str) -> set[str]:
        if acc in codes:
            return codes[acc]
        kids = children.get(acc)
        codes[acc] = (
            set().union(*(walk(k) for k in kids)) if kids else leaf_codes(by_acc[acc])
        )
        return codes[acc]

    for acc in by_acc:
        walk(acc)
    return codes


# --------------------------------------------------------------- pass 1: counting
def build_registry(obs) -> tuple[list[dict], dict[str, dict[str, int]]]:
    """source.subatlas_papers[], and the label totals keyed for the transfer pass."""
    totals = {c: {str(k): int(v) for k, v in obs[c].value_counts().items()} for c in STUDIES}

    papers = []
    for label in sorted(STUDIES):
        counts = totals[label]
        entry: dict[str, object] = {"label": label}
        if label in UNRESOLVED:
            entry["status"] = "unresolved"
        else:
            entry.update(RESOLVED[label])
        entry["total_cells"] = sum(counts.values())
        entry["cell_sets"] = [
            {"source_labelset": label, "cell_label": name, "n_cells": n}
            for name, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ]
        papers.append(entry)
    return papers, totals


def stamp_measures(annotations: list[dict], totals: dict[str, dict[str, int]]) -> int:
    """subatlas_label_total_cells and the two shares it and the purity count divide."""
    stamped = 0
    for ann in annotations:
        for t in ann.get("transferred_annotations") or []:
            total = totals[t["source_labelset"]].get(t["transferred_cell_label"])
            if total is None:
                continue
            t["subatlas_label_total_cells"] = total
            contribution = t.get("subatlas_contribution_cells")
            if contribution:
                t["share_of_subatlas_contribution"] = round(
                    t["cell_count"] / contribution, ROUND
                )
            t["share_of_subatlas_label"] = round(t["cell_count"] / total, ROUND)
            stamped += 1
    return stamped


# --------------------------------------------------------------- doi from source_taxonomy
def dois_from_transfers(annotations: list[dict]) -> dict[str, str]:
    """The DOI each study is already identified by, stripped of its 'DOI:' prefix."""
    found: dict[str, set[str]] = defaultdict(set)
    for ann in annotations:
        for t in ann.get("transferred_annotations") or []:
            taxonomy = t.get("source_taxonomy") or ""
            if taxonomy.startswith("DOI:"):
                found[t["source_labelset"]].add(taxonomy[4:])
    return {k: next(iter(v)) for k, v in found.items() if len(v) == 1}


# --------------------------------------------------------------- checks
def run_checks(doc: dict, obs, codes: dict[str, set[str]]) -> list[str]:
    """The five consistency checks, ordered by how much they would cost to get wrong."""
    failures: list[str] = []
    annotations = doc["annotations"]
    papers = {p["label"]: p for p in doc["source"]["subatlas_papers"]}

    def report(name: str, bad: list[str], n_checked: int) -> None:
        status = "OK" if not bad else f"FAIL ({len(bad)})"
        print(f"  {name}: {status}  [{n_checked} checked]")
        for line in bad[:5]:
            print(f"      {line}")
        if bad:
            failures.append(name)

    # 1. every (source_labelset, transferred_cell_label) has a cell_sets[] entry
    registered = {
        (p["label"], cs["cell_label"]) for p in papers.values() for cs in p["cell_sets"]
    }
    bad, n = [], 0
    for ann in annotations:
        for t in ann.get("transferred_annotations") or []:
            n += 1
            key = (t["source_labelset"], t["transferred_cell_label"])
            if key not in registered:
                bad.append(f"{ann['cell_label']}: {key} has no cell_sets[] entry")
    report("1. transfer joins the registry", bad, n)

    # 2. sum(cell_count) over a covering set == cell_sets[].n_cells, run three ways
    parents = {
        a.get("parent_cell_set_accession")
        for a in annotations
        if a.get("parent_cell_set_accession")
    }
    coverings = {
        "leaves": [a for a in annotations if a["cell_set_accession"] not in parents],
        "L1": [a for a in annotations if a["labelset"] == "L1"],
        "L2": [a for a in annotations if a["labelset"] == "L2"],
    }
    bad, n = [], 0
    for name, covering in coverings.items():
        assert sum(a["n_cells"] for a in covering) == len(obs), name
        summed: dict[tuple[str, str], int] = defaultdict(int)
        for ann in covering:
            for t in ann.get("transferred_annotations") or []:
                summed[(t["source_labelset"], t["transferred_cell_label"])] += t["cell_count"]
        for (labelset, cell_label), total in summed.items():
            n += 1
            counted = next(
                cs["n_cells"]
                for cs in papers[labelset]["cell_sets"]
                if cs["cell_label"] == cell_label
            )
            if total != counted:
                bad.append(f"over {name}: {labelset}/{cell_label} sums {total}, counted {counted}")
    report("2. covering sum == counted total (3 ways)", bad, n)

    # 3. subatlas_contribution_cells reproduces from the parquet
    fine = obs["celltype_HCA_fine"]
    present = {c: obs[c].notna() for c in STUDIES}
    bad, n = [], 0
    for ann in annotations:
        transfers = ann.get("transferred_annotations") or []
        if not transfers:
            continue
        mask = fine.isin(codes[ann["cell_set_accession"]])
        per_source: dict[str, int] = {}
        for t in transfers:
            n += 1
            source = t["source_labelset"]
            if source not in per_source:
                per_source[source] = int((mask & present[source]).sum())
            if t["subatlas_contribution_cells"] != per_source[source]:
                bad.append(
                    f"{ann['cell_label']}/{source}: stored "
                    f"{t['subatlas_contribution_cells']}, counted {per_source[source]}"
                )
    report("3. subatlas_contribution_cells reproduces", bad, n)

    # 4. each ratio recomputes from its own two counts
    measures = [
        ("cell_ratio", "cell_count", None),
        ("share_of_subatlas_contribution", "cell_count", "subatlas_contribution_cells"),
        ("share_of_subatlas_label", "cell_count", "subatlas_label_total_cells"),
    ]
    bad, n = [], 0
    for ann in annotations:
        for t in ann.get("transferred_annotations") or []:
            for measure, num, den in measures:
                if measure not in t:
                    continue
                n += 1
                denominator = ann["n_cells"] if den is None else t[den]
                expected = t[num] / denominator
                if abs(expected - t[measure]) > 5e-4:
                    bad.append(
                        f"{ann['cell_label']}/{t['transferred_cell_label']}: {measure} "
                        f"is {t[measure]}, recomputes {expected:.4f}"
                    )
    report("4. each ratio recomputes", bad, n)

    # 5. total_cells == sum(cell_sets[].n_cells)
    bad = []
    for label, paper in papers.items():
        summed = sum(cs["n_cells"] for cs in paper["cell_sets"])
        if summed != paper["total_cells"]:
            bad.append(f"{label}: total_cells {paper['total_cells']}, cell_sets sum {summed}")
    report("5. total_cells == sum(cell_sets)", bad, len(papers))

    return failures


# --------------------------------------------------------------- main
def main() -> int:
    check_only = "--check" in sys.argv

    doc = json.loads(open(CAS).read())
    annotations = doc["annotations"]
    obs = pq.read_table(PARQUET, columns=STUDIES + ["celltype_HCA_fine"]).to_pandas()
    print(f"obs: {len(obs):,} cells | annotations: {len(annotations)}")

    codes = codes_by_accession(annotations)
    covered = set().union(*codes.values())
    observed = set(obs["celltype_HCA_fine"].dropna().unique())
    if covered != observed:
        print(f"  !! fine codes: {len(covered - observed)} unmatched, {len(observed - covered)} missing")
        return 1

    if not check_only:
        papers, totals = build_registry(obs)
        doc["source"]["subatlas_papers"] = papers
        stamped = stamp_measures(annotations, totals)

        dois = dois_from_transfers(annotations)
        for paper in papers:
            doi = dois.get(paper["label"])
            if doi:
                paper["doi"] = doi
            elif paper["label"] not in UNRESOLVED:
                print(f"  !! {paper['label']}: no single DOI in source_taxonomy")
                return 1

        # doi next to the rest of the bibliography, before the counts it is not part of
        order = ["label", "first_author", "year", "title", "venue", "doi", "status",
                 "total_cells", "cell_sets"]
        doc["source"]["subatlas_papers"] = [
            {k: p[k] for k in order if k in p} for p in papers
        ]

        print(f"registry: {len(papers)} studies, "
              f"{sum(len(p['cell_sets']) for p in papers)} cell sets, "
              f"{sum(p['total_cells'] for p in papers):,} labelled cells")
        print(f"measures: stamped {stamped} transferred annotations")

    print("checks:")
    failures = run_checks(doc, obs, codes)
    if failures:
        print(f"\n{len(failures)} check(s) failed — not writing {CAS}")
        return 1

    if not check_only:
        with open(CAS, "w") as fh:
            json.dump(doc, fh, indent=2, ensure_ascii=False)
        print(f"\nwrote {CAS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

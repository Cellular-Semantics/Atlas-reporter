"""Fill the missing matrix cells: ASTA retrieval, and combined-query retrieval.

The run so far covered blind / whole / local-with-per-axis-queries. The matrix
the experiment was for also needs:

* ``asta-sep``   -- ASTA snippet_search, one query per item (the per-axis
                    question), packed to the same ~2k budget as local.
* ``asta-comb``  -- ASTA snippet_search with the PRODUCTION compound query,
                    one query per label, shared by that label's items.
* ``local-comb`` -- local RRF hybrid with the same compound query.

The compound query is rendered verbatim from CLAUDE.md's template, warts
included (label repeated when the resolved name matches, `/` collision,
"fetal" where the paper says "prenatal"):

    {label} / {resolved_name} in {scope} {tissue}: location, structure, function, markers

ASTA snippets are packed in score order (ASTA reports no reliable document
position); local slices are restored to document order as before. Both are
written to contexts/<arm>/<id>.txt so scoring stays a substring check against
the exact bytes the reader saw.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus  # noqa: E402
import stage1  # noqa: E402
import asta_probe  # noqa: E402
from prep import NARRATIVE_END, LOCAL_BUDGET_TOKENS  # noqa: E402

PAPER_ID = "DOI:10.1038/s41586-024-08002-x"
COMPOUND = "{label} / {resolved_name} in {scope} {tissue}: location, structure, function, markers"


def asta_slice(query: str, budget: int) -> str:
    payload = asta_probe.call_tool(
        "snippet_search", {"query": query, "paper_ids": PAPER_ID, "limit": 100}
    )
    rows = asta_probe._rows(payload)
    picked, used = [], 0
    for r in rows:  # score order
        txt = (r.get("text") or (r.get("snippet") or {}).get("text") or "").strip()
        if not txt:
            continue
        t = max(1, len(txt) // 4)
        if used + t > budget:
            continue
        picked.append(txt)
        used += t
        if used >= budget * 0.9:
            break
    return "\n\n".join(picked)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, required=True)
    ap.add_argument("--arms", nargs="+", default=["asta-sep", "asta-comb", "local-comb"])
    args = ap.parse_args()
    root = args.dir

    manifest = json.loads((root / "manifest.json").read_text())
    items = manifest["items"]
    paper = manifest["paper"]

    # Narrative chunks for the local backend, as in prep.py.
    paras = corpus.paragraphs(paper)
    titles = [t for t, _ in paras]
    cut = max(i for i, t in enumerate(titles) if t == NARRATIVE_END) + 1
    narrative_text = " ".join(x for _, x in paras[:cut])
    chs = [c for c in corpus.chunks(paper) if c["text"][:60] in narrative_text]

    # One compound query per label. `primary` is the grounded resolved name --
    # the best case for the production template.
    compound: dict[str, str] = {}
    for it in items:
        compound.setdefault(
            it["label"],
            COMPOUND.format(label=it["label"], resolved_name=it["primary"], scope="fetal", tissue="skin"),
        )

    for arm in args.arms:
        out = root / "contexts" / arm
        out.mkdir(parents=True, exist_ok=True)
        cache: dict[str, str] = {}  # query -> context (comb arms share per label)
        for it in items:
            query = it["question"] if arm.endswith("-sep") else compound[it["label"]]
            if query not in cache:
                if arm.startswith("asta"):
                    cache[query] = asta_slice(query, LOCAL_BUDGET_TOKENS)
                else:
                    order = stage1.rrf_order(paper, chs, query)
                    picked, used = [], 0
                    for i in order:
                        c = chs[i]
                        if used + c["n_tokens"] > LOCAL_BUDGET_TOKENS:
                            continue
                        picked.append(i)
                        used += c["n_tokens"]
                        if used >= LOCAL_BUDGET_TOKENS * 0.9:
                            break
                    picked.sort()
                    cache[query] = "\n\n".join(chs[i]["text"] for i in picked)
            (out / f"{it['id']}.txt").write_text(cache[query])
        # Pre-measure the retrieval ceiling for this arm.
        hits = sum(
            1
            for it in items
            if it["expect"] == "present"
            and it.get("span")
            and it["span"] in (out / f"{it['id']}.txt").read_text()
        )
        n_present = sum(1 for it in items if it["expect"] == "present")
        print(f"  {arm:<11} {len(cache)} retrievals, gold span present: {hits}/{n_present}")


if __name__ == "__main__":
    main()

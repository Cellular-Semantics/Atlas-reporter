#!/usr/bin/env python3
"""Run Stage 1 and write results/stage1.json. Throwaway harness."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import stage1  # noqa: E402
from corpus import chunks  # noqa: E402

items = [i for i in json.loads((HERE / "items.json").read_text()) if i["span"]]
papers = sorted({i["paper"] for i in items})
CH = {p: chunks(p) for p in papers}

rows = []
asta_cache: dict[tuple[str, str], list] = {}

for n, it in enumerate(items, 1):
    paper, span = it["paper"], it["span"]
    chs = CH[paper]
    forms = {"question": it["question"], "keywords": stage1.keywords(it["question"])}

    # chance null: which chunks carry the span
    hits = [c["i"] for c in chs if stage1.cost_to_answer([c], span)[0] is not None]
    null = stage1.permutation_null(chs, hits or [len(chs) - 1], n=2000)

    for form, q in forms.items():
        orders = {
            "document": chs,
            "lexical": [chs[i] for i in stage1.bm25_order(chs, q)],
            "local": [chs[i] for i in stage1.dense_order(paper, chs, q)],
        }
        key = (paper, q)
        if key not in asta_cache:
            try:
                asta_cache[key] = stage1.asta_snippets(paper, q, limit=100)
            except Exception as e:  # noqa: BLE001
                print(f"  asta failed for {it['id']}/{form}: {e}", file=sys.stderr)
                asta_cache[key] = []
            time.sleep(0.4)
        orders["asta"] = asta_cache[key]

        for arm, ordered in orders.items():
            if not ordered:
                continue
            rank, toks = stage1.cost_to_answer(ordered, span)
            rows.append({
                "id": it["id"], "group": it["group"], "tag": it["tag"], "paper": paper,
                "form": form, "arm": arm, "rank": rank, "tokens": toks,
                "found": rank is not None,
                "total_tokens": sum(c["n_tokens"] for c in ordered),
                "null_median": null["median"],
            })
    print(f"[{n}/{len(items)}] {it['id']}", flush=True)

(HERE / "results").mkdir(exist_ok=True)
(HERE / "results" / "stage1.json").write_text(json.dumps(rows, indent=1))
print(f"\nwrote {len(rows)} rows to results/stage1.json")

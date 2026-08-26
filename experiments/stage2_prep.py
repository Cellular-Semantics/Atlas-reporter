#!/usr/bin/env python3
"""Stage 2 preparation — everything deterministic, no model calls.

Writes one context file per (item, condition) plus an answer key per item, so the
reading step can run as subagents on quota and the scoring afterwards is pure code.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import stage1  # noqa: E402
from corpus import chunks  # noqa: E402

OUT = HERE / "stage2"
BUDGETS = {"b2k": 2000, "b8k": 8000}
ARMS = ("hybrid", "asta", "document")

# Gene symbols, gene-like tokens, numbers with units, and PCW ages. These are what
# the answers actually consist of, so they make a scorable key without a judge.
GENE = re.compile(r"\b[A-Z][A-Z0-9]{2,}[0-9A-Z]?\b")
NUM = re.compile(r"\b\d+(?:\.\d+)?\b")
STOPWORDS = {"DEG", "DEGS", "RNA", "PCW", "MHC", "MHCII", "UMAP", "HF", "HFS", "ORS",
             "IRS", "CL", "DOI", "JATS", "PMC", "AND", "THE", "NOT"}


def answer_key(item: dict) -> dict:
    """Entities a correct answer must contain, derived from the gold answer text."""
    ans = item.get("answer") or ""
    genes = sorted({g for g in GENE.findall(ans) if g not in STOPWORDS})
    nums = sorted(set(NUM.findall(ans)))
    return {"genes": genes, "numbers": nums,
            "n_required": len(genes) + len(nums)}


def build_orders(paper: str, item: dict, chs: list[dict]) -> dict[str, list[dict]]:
    q = item["question"]
    orders = {
        "document": chs,
        "hybrid": [chs[i] for i in stage1.rrf_order(paper, chs, q)],
    }
    try:
        orders["asta"] = stage1.asta_snippets(paper, q, limit=100)
    except Exception as e:  # noqa: BLE001
        print(f"  asta failed for {item['id']}: {e}", file=sys.stderr)
    return orders


def take(ordered: list[dict], budget: int) -> list[dict]:
    out, used = [], 0
    for c in ordered:
        if used + c["n_tokens"] > budget and out:
            break
        out.append(c)
        used += c["n_tokens"]
    return out


def main() -> int:
    items = [i for i in json.loads((HERE / "items.json").read_text())
             if i["paper"] == "gopee2024" and i["group"] in ("A", "B", "C", "D", "F")]
    chs = chunks("gopee2024")
    whole = "\n\n".join(c["text"] for c in chs)
    OUT.mkdir(exist_ok=True)
    (OUT / "contexts").mkdir(exist_ok=True)

    manifest = []
    for n, it in enumerate(items, 1):
        key = answer_key(it)
        conditions = {}
        if it["span"]:  # A/B/F-style items get the retrieval arms
            orders = build_orders("gopee2024", it, chs)
            for arm, ordered in orders.items():
                for bname, budget in BUDGETS.items():
                    picked = take(ordered, budget)
                    cid = f"{arm}_{bname}"
                    text = "\n\n".join(c["text"] for c in picked)
                    p = OUT / "contexts" / f"{it['id']}__{cid}.txt"
                    p.write_text(text)
                    conditions[cid] = {"path": str(p.relative_to(HERE)),
                                       "n_tokens": sum(c["n_tokens"] for c in picked),
                                       "n_chunks": len(picked),
                                       "span_present": stage1.cost_to_answer(picked, it["span"])[0] is not None}
        # whole paper: identical for every item, written once
        conditions["whole"] = {"path": "stage2/contexts/__whole_paper.txt",
                               "n_tokens": sum(c["n_tokens"] for c in chs),
                               "n_chunks": len(chs), "span_present": bool(it["span"])}
        manifest.append({**it, "answer_key": key, "conditions": conditions})
        print(f"[{n}/{len(items)}] {it['id']}  {len(conditions)} conditions", flush=True)

    (OUT / "contexts" / "__whole_paper.txt").write_text(whole)
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(f"\nwrote {len(manifest)} items to stage2/manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

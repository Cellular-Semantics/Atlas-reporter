"""Generate question text and per-arm contexts for the Stage 3b run.

Questions are *generated*, never hand-written: axis template + the grounded
primary name + the standard synonym clause. The gold answers are hand-authored;
the asks are mechanical. That split keeps phrasing a controlled factor rather
than accidental variation.

Arms:

* ``blind``  -- no context. The correct behaviour is a decline: the reader is
  required to supply a supporting quote, and with no context there is none.
  This is the fabrication check.
* ``whole``  -- the paper's nine narrative sections (~13k tokens). Methods is
  excluded: 46% of the body text, and it says nothing about cell types.
* ``local``  -- an RRF hybrid slice of ~2k tokens over the same narrative
  chunks, retrieved with the item's own question. The Stage 2 cost arm.

Contexts are precomputed to files so a read is reproducible and so the same
bytes can be checked for the quote afterwards.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus  # noqa: E402
import stage1  # noqa: E402

AXIS_TEMPLATES = {
    "location": "Where in prenatal human skin is {n} found?",
    "function": "What function does the paper attribute to {n}?",
    "markers": "Which genes mark {n}?",
    "structure": "What does the paper say about the structure or morphology of {n}?",
}

NARRATIVE_END = "Discussion"
LOCAL_BUDGET_TOKENS = 2000


def narrative_chunks(paper: str) -> list[dict]:
    """Chunks from the narrative sections only, in document order."""
    paras = corpus.paragraphs(paper)
    titles = [t for t, _ in paras]
    cut = max(i for i, t in enumerate(titles) if t == NARRATIVE_END) + 1
    keep = {id(t) for t in [p[1] for p in paras[:cut]]}
    return [c for c in corpus.chunks(paper) if any(c["text"] in t for t in [p[1] for p in paras[:cut]])] or [
        c for c in corpus.chunks(paper) if id(c) in keep
    ]


def build_questions(items: list[dict], syn: dict) -> dict[str, dict]:
    by_label = {e["label"]: e for e in syn["labels"]}
    out: dict[str, dict] = {}
    for item in items:
        entry = by_label.get(item["label"])
        primary = entry["primary"] if entry else (item.get("ask_as") or item["label"])
        accepted = [a["name"] for a in (entry.get("accepted") or [])] if entry else []
        clause = f" ({primary} is also referred to as: {', '.join(accepted)}.)" if accepted else ""
        out[item["id"]] = {
            "question": AXIS_TEMPLATES[item["axis"]].format(n=primary) + clause,
            "primary": primary,
            "synonyms": accepted,
        }
    return out


def local_slice(paper: str, chs: list[dict], question: str, budget: int) -> str:
    order = stage1.rrf_order(paper, chs, question)
    picked, used = [], 0
    for i in order:
        c = chs[i]
        if used + c["n_tokens"] > budget:
            continue
        picked.append(i)
        used += c["n_tokens"]
        if used >= budget * 0.9:
            break
    picked.sort()  # restore document order; a reader should not see rank order
    return "\n\n".join(chs[i]["text"] for i in picked)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--items", type=Path, required=True)
    ap.add_argument("--synonyms", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    doc = yaml.safe_load(args.items.read_text())
    syn = yaml.safe_load(args.synonyms.read_text())
    paper = doc["paper"]
    items = doc["items"]

    questions = build_questions(items, syn)

    paras = corpus.paragraphs(paper)
    titles = [t for t, _ in paras]
    cut = max(i for i, t in enumerate(titles) if t == NARRATIVE_END) + 1
    narrative_paras = paras[:cut]
    whole = "\n\n".join(f"## {t}\n{x}" for t, x in narrative_paras)
    narrative_text = " ".join(x for _, x in narrative_paras)
    chs = [c for c in corpus.chunks(paper) if c["text"][:60] in narrative_text]

    (args.out / "contexts" / "local").mkdir(parents=True, exist_ok=True)
    (args.out / "contexts" / "whole").mkdir(parents=True, exist_ok=True)
    (args.out / "contexts" / "whole" / "shared.txt").write_text(whole)

    manifest = []
    for item in items:
        q = questions[item["id"]]
        local = local_slice(paper, chs, q["question"], LOCAL_BUDGET_TOKENS)
        (args.out / "contexts" / "local" / f"{item['id']}.txt").write_text(local)
        manifest.append(
            {
                "id": item["id"],
                "label": item["label"],
                "axis": item["axis"],
                "expect": item["expect"],
                "scoring": item["scoring"],
                "question": q["question"],
                "primary": q["primary"],
                "synonyms": q["synonyms"],
                "answer": item["answer"].strip(),
                "span": item.get("span"),
                "hazard": item.get("hazard"),
                "local_tokens": max(1, len(local) // 4),
                "span_in_local": bool(item.get("span") and item["span"] in local),
            }
        )

    (args.out / "manifest.json").write_text(json.dumps({"paper": paper, "items": manifest}, indent=1))

    n_present = [m for m in manifest if m["expect"] == "present"]
    hit = sum(1 for m in n_present if m["span_in_local"])
    print(f"{args.out}/manifest.json: {len(manifest)} items")
    print(f"  whole context: {len(whole)//4} tokens, {len(narrative_paras)} paragraphs")
    print(f"  local slices : median {sorted(m['local_tokens'] for m in manifest)[len(manifest)//2]} tokens")
    print(f"  gold span retrieved into local slice: {hit}/{len(n_present)} present items")


if __name__ == "__main__":
    main()

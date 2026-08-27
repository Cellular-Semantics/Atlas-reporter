#!/usr/bin/env python3
"""Stage 2 scoring — deterministic, no model calls.

Reads every answer JSON the reader subagents wrote and scores it against the
precomputed answer key. Four modes:

  entities  — all required gene symbols / numbers present in the answer
  reference — the cited paper recovered (author surname or DOI)
  refusal   — correct only if the reader reported the question unanswerable
  judge     — left unscored; prose answers a human or judge must read

Also records two things the raw score cannot show:
  grounded  — is the support quote actually in the context it was given?
  span_present — did that context contain the gold passage at all? Crossing this
                 with correctness separates "missed it" from "invented it".
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
S2 = HERE / "stage2"


def norm_quote(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip().lower()


def score_entities(ans: str, key: dict) -> tuple[bool, float, list[str]]:
    want = list(key.get("genes", [])) + list(key.get("numbers", []))
    if not want:
        return False, 0.0, []
    found = [w for w in want if re.search(rf"\b{re.escape(w)}\b", ans or "", re.I)]
    return len(found) == len(want), len(found) / len(want), sorted(set(want) - set(found))


def score_reference(ans: str, key: dict) -> tuple[bool, float, list[str]]:
    authors = key.get("authors", [])
    dois = key.get("dois", [])
    a = ans or ""
    hit_auth = [x for x in authors if re.search(rf"\b{re.escape(x)}\b", a, re.I)]
    hit_doi = [d for d in dois if d.lower() in a.lower()]
    want = len(authors) or 1
    got = max(len(hit_auth), len(hit_doi))
    return got >= want, got / want, sorted(set(authors) - set(hit_auth))


JUDGE = {}
for _jf in ("judge_verdicts.json", "judge_verdicts2.json", "judge_verdicts3.json"):
    _p = S2 / _jf
    if _p.exists():
        JUDGE.update(json.loads(_p.read_text()))


def main() -> int:
    manifest = {i["id"]: i for i in json.loads((S2 / "manifest.json").read_text())}
    rows = []
    for p in sorted((S2 / "answers").glob("*.json")):
        stem = p.stem
        try:
            item_id, cond, model = stem.split("__")
        except ValueError:
            print(f"  skipping unparseable name: {p.name}", file=sys.stderr)
            continue
        it = manifest.get(item_id)
        if it is None:
            print(f"  unknown item: {item_id}", file=sys.stderr)
            continue
        try:
            a = json.loads(p.read_text())
        except Exception as e:  # noqa: BLE001
            print(f"  bad JSON in {p.name}: {e}", file=sys.stderr)
            continue

        answerable = bool(a.get("answerable"))
        ans, quote = a.get("answer") or "", a.get("support_quote") or ""
        mode = it.get("scoring", "entities")
        cdata = it["conditions"].get(cond, {})

        ctx = ""
        cpath = cdata.get("path")
        if cpath and (HERE / cpath).exists():
            ctx = (HERE / cpath).read_text()
        # only meaningful when the reader claimed an answer
        grounded = (bool(quote) and norm_quote(quote) in norm_quote(ctx)) if answerable else None

        if mode == "refusal":
            correct, frac, missing = (not answerable), float(not answerable), []
        elif mode == "reference":
            correct, frac, missing = score_reference(ans, it["answer_key"])
        elif mode == "entities":
            correct, frac, missing = score_entities(ans, it["answer_key"])
        else:
            correct, frac, missing = None, None, []

        # Outcome taxonomy — the metric that matters. "Wrong" and "correctly
        # reported absent" are different things and must not be averaged.
        sp = cdata.get("span_present")
        if mode == "judge":
            # Judge-scored items have no entity key; a verdict file decides them.
            # A DECLINE is never the judge's to rule on — absence is adjudicated the same
            # way as for every other mode, against whether the passage was actually there.
            if not answerable:
                outcome = "correct_absence" if sp is False else "missed"
            else:
                v = JUDGE.get(f"{item_id}__{cond}__{model}", {}).get("verdict") or "unjudged"
                outcome = {"correct": "correct", "partial": "partial",
                           "incorrect": "wrong"}.get(v, "unjudged")
        elif mode == "refusal":
            outcome = "correct_absence" if not answerable else "fabricated"
        elif not answerable:
            outcome = "correct_absence" if sp is False else "missed"
        elif correct:
            outcome = "correct" if sp else "correct_without_span"
        elif grounded:
            # Answered, and the quote really is in the supplied text — so the context
            # supported an answer the key did not anticipate. Not fabrication.
            outcome = "wrong" if sp else "other_supported_answer"
        else:
            outcome = "wrong" if sp else "fabricated"

        rows.append({
            "outcome": outcome,
            "id": item_id, "group": it["group"], "tag": it.get("tag"),
            "condition": cond, "model": model, "mode": mode,
            "answerable": answerable, "correct": correct, "fraction": frac,
            "missing": missing, "grounded": grounded,
            "span_present": cdata.get("span_present"),
            "ctx_tokens": cdata.get("n_tokens"),
            "answer": ans[:300],
        })

    (S2 / "scores.json").write_text(json.dumps(rows, indent=1))
    print(f"scored {len(rows)} answers\n")

    by = defaultdict(list)
    for r in rows:
        by[(r["model"], r["condition"])].append(r)
    print(f"{'model':8} {'condition':15} {'n':>3} {'correct':>8} {'corr-abs':>9} {'wrong':>6} {'missed':>7} {'FABRICATED':>11} {'grounded':>9}")
    for (m, c), rs in sorted(by.items()):
        o = Counter(r["outcome"] for r in rs)
        gq = [r for r in rs if r["grounded"] is not None]
        gr = sum(1 for r in gq if r["grounded"])
        print(f"{m:8} {c:15} {len(rs):3} {o['correct']+o['correct_without_span']:>8} "
              f"{o['correct_absence']:>9} {o['wrong']:>6} {o['missed']:>7} {o['fabricated']:>11} {f'{gr}/{len(gq)}':>9}"
              + (f"   [{o['other_supported_answer']} other-supported]" if o['other_supported_answer'] else ""))

    fab = [r for r in rows if r["span_present"] is False and r["correct"] and r["mode"] != "refusal"]
    if fab:
        print("\nCorrect WITHOUT the gold passage in context (prior knowledge or leakage):")
        for r in fab:
            print(f"   {r['id']:5} {r['condition']:16} {r['model']:8} grounded={r['grounded']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

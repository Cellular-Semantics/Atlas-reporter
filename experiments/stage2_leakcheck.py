#!/usr/bin/env python3
"""Detect cross-item leakage in batched Stage 2 jobs, and quote splicing.

Two independent checks, both deterministic:

1. LEAKAGE — for a batched b2k job, is an answer's support quote absent from its own
   context but present in a SIBLING item's context from the same job? That is direct
   evidence the reader used another item's text.

2. SPLICING — is the quote absent verbatim from its own context, but its longest
   verbatim prefix a large fraction of it? That is the "two passages joined into one
   quote" failure: each half real, the join invented.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
S2 = HERE / "stage2"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip().lower()


def longest_prefix_in(q: str, ctx: str) -> int:
    lo, hi = 0, len(q)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if q[:mid] in ctx:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main() -> int:
    manifest = {i["id"]: i for i in json.loads((S2 / "manifest.json").read_text())}
    jobs = json.loads((S2 / "jobs_index.json").read_text()) if (S2 / "jobs_index.json").exists() else []
    job_of = {(j["model"], j["condition"], iid): j for j in jobs for iid in j["items"]}

    ctx_cache: dict[str, str] = {}

    def ctx_for(iid: str, cond: str) -> str:
        it = manifest.get(iid)
        if not it or cond not in it["conditions"]:
            return ""
        p = it["conditions"][cond]["path"]
        if p not in ctx_cache:
            fp = HERE / p
            ctx_cache[p] = norm(fp.read_text()) if fp.exists() else ""
        return ctx_cache[p]

    verdicts, splices, leaks = Counter(), [], []
    for f in sorted((S2 / "answers").glob("*.json")):
        try:
            iid, cond, model = f.stem.split("__")
            a = json.loads(f.read_text())
        except Exception:
            continue
        if not a.get("answerable"):
            verdicts["declined"] += 1
            continue
        q = norm(a.get("support_quote"))
        if not q:
            verdicts["no_quote"] += 1
            continue
        own = ctx_for(iid, cond)
        if q in own:
            verdicts["exact"] += 1
            continue

        pref = longest_prefix_in(q, own)
        frac = pref / len(q) if q else 0
        # sibling check
        job = job_of.get((model, cond, iid))
        sib_hit = None
        own_path = manifest[iid]["conditions"][cond]["path"] if iid in manifest else None
        if job:
            for other in job["items"]:
                if other == iid or other not in manifest:
                    continue
                other_path = manifest[other]["conditions"].get(cond, {}).get("path")
                # A sibling sharing the same context file (the whole-paper condition)
                # carries no information: identical text cannot show cross-item leakage.
                if not other_path or other_path == own_path:
                    continue
                # Require a substantial contiguous match, not a short prefix, so a
                # within-document splice is not misread as a cross-item leak.
                probe = q[:400] if len(q) >= 400 else q
                if probe and probe in ctx_for(other, cond):
                    sib_hit = other
                    break
        if sib_hit:
            verdicts["LEAKED"] += 1
            leaks.append((model, cond, iid, sib_hit))
        elif frac >= 0.25:
            verdicts["spliced"] += 1
            splices.append((model, cond, iid, len(q), pref, frac))
        else:
            verdicts["not_in_context"] += 1
            splices.append((model, cond, iid, len(q), pref, frac))

    print("quote verdicts:", dict(verdicts))
    if leaks:
        print("\nCROSS-ITEM LEAKAGE (quote found in a sibling item's context):")
        for m, c, i, s in leaks:
            print(f"   {m:7} {c:14} {i:5} <- {s}")
    else:
        print("\nno cross-item leakage detected")
    if splices:
        print("\nspliced / unverifiable quotes (verbatim prefix, then divergence):")
        for m, c, i, n, pref, frac in sorted(splices, key=lambda x: -x[5]):
            print(f"   {m:7} {c:14} {i:5} {n:4} chars, prefix {pref:4} ({frac:.0%})")
    (S2 / "quote_audit.json").write_text(json.dumps(
        {"verdicts": dict(verdicts), "leaks": leaks, "splices": splices}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

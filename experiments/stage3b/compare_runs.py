"""Compare two runs of the same item set read by different models.

Items, contexts, reader contract and scoring code are shared, so a difference
between runs is attributable to the reader model (plus batching, where the arm
has per-item contexts -- see runs/run1-mixed/README.md).

Reports, per arm: each run's score, the per-item agreement, and the items where
the two runs disagree. Disagreements are the useful output -- they are where a
reader-model choice actually changes what the pipeline would report.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

GOOD = {"correct", "correct_decline"}


def load(path: Path) -> dict[tuple[str, str], dict]:
    return {(r["arm"], r["id"]): r for r in json.loads(path.read_text())}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run1", type=Path, required=True, help="final.json of the earlier run")
    ap.add_argument("--run2", type=Path, required=True, help="final.json of the later run")
    ap.add_argument("--provenance", type=Path, help="reader_provenance.json for run1")
    ap.add_argument("--label1", default="run1")
    ap.add_argument("--label2", default="run2")
    args = ap.parse_args()

    a, b = load(args.run1), load(args.run2)
    prov = {}
    if args.provenance and args.provenance.exists():
        prov = json.loads(args.provenance.read_text())["jobs"]

    arms = sorted({k[0] for k in a} | {k[0] for k in b})
    print(f"{'arm':<12}{args.label1:>10}{args.label2:>10}{'agree':>8}{'shared':>8}  run1 reader")
    for arm in arms:
        shared = [k for k in a if k[0] == arm and k in b]
        if not shared:
            continue
        s1 = sum(1 for k in shared if a[k]["outcome"] in GOOD)
        s2 = sum(1 for k in shared if b[k]["outcome"] in GOOD)
        agree = sum(1 for k in shared if (a[k]["outcome"] in GOOD) == (b[k]["outcome"] in GOOD))
        models = {prov[j]["dominant_model"] for j in prov if j.startswith(arm + "-")} if prov else set()
        tag = ",".join(sorted(m.replace("claude-", "") for m in models)) or "?"
        print(f"{arm:<12}{s1:>10}{s2:>10}{agree:>8}{len(shared):>8}  {tag}")

    print("\ndisagreements (item passed in one run, not the other):")
    for k in sorted(set(a) & set(b)):
        g1, g2 = a[k]["outcome"] in GOOD, b[k]["outcome"] in GOOD
        if g1 != g2:
            winner = args.label1 if g1 else args.label2
            print(f"  {k[0]:<12}{k[1]:<38} {args.label1}={a[k]['outcome']:<16} "
                  f"{args.label2}={b[k]['outcome']:<16} -> {winner}")

    net = Counter()
    for k in set(a) & set(b):
        g1, g2 = a[k]["outcome"] in GOOD, b[k]["outcome"] in GOOD
        if g1 != g2:
            net[args.label1 if g1 else args.label2] += 1
    print(f"\n  net: {dict(net)}")


if __name__ == "__main__":
    main()

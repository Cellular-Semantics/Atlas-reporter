"""Merge judge verdicts into the deterministic scores and report the run."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

# A judge verdict maps onto the outcome taxonomy. `overreach` is the absence
# arm's failure: the paper says nothing and the reader said something anyway.
VERDICT_TO_OUTCOME = {
    "correct": "correct",
    "substituted": "substituted",
    "wrong": "wrong",
    "overreach": "overreach",
}
GOOD = {"correct", "correct_decline"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, required=True)
    args = ap.parse_args()
    root = args.dir

    scores = json.loads((root / "scores.json").read_text())
    verdicts: dict[tuple[str, str], dict] = {}
    for path in sorted((root / "verdicts").glob("*.json")):
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", path.read_text().strip())
        for v in json.loads(raw):
            verdicts[(v["arm"], v["id"])] = v

    unresolved = []
    for row in scores:
        if row["outcome"] != "pending":
            continue
        v = verdicts.get((row["arm"], row["id"]))
        if not v:
            unresolved.append((row["arm"], row["id"]))
            continue
        row["outcome"] = VERDICT_TO_OUTCOME.get(v["verdict"], v["verdict"])
        row["judge_why"] = v.get("why")

    # Rule 5, enforced rather than assumed: nothing may stay pending.
    still = [r for r in scores if r["outcome"] == "pending"]
    if still or unresolved:
        print(f"!! {len(still)} reads still pending, {len(unresolved)} missing a verdict")
        for a, i in unresolved[:10]:
            print("   missing:", a, i)

    (root / "final.json").write_text(json.dumps(scores, indent=1))

    arms = ["blind", "whole", "local", "asta-sep", "asta-comb", "local-comb"]
    print(f"\n{'':<9}" + "".join(f"{a:>10}" for a in arms))
    outcomes = sorted({r["outcome"] for r in scores})
    for o in outcomes:
        cells = "".join(f"{sum(1 for r in scores if r['arm']==a and r['outcome']==o):>10}" for a in arms)
        print(f"{o:<9}{cells}")

    print(f"\n{'':<28}" + "".join(f"{a:>10}" for a in arms))
    for group, label in (("present", "present items (n=41)"), ("absent", "absent items (n=14)")):
        cells = ""
        for a in arms:
            rows = [r for r in scores if r["arm"] == a and r["expect"] == group]
            ok = sum(1 for r in rows if r["outcome"] in GOOD)
            cells += f"{ok}/{len(rows):<7}"
        print(f"  {label:<26}{cells}")

    cells = ""
    for a in arms:
        rows = [r for r in scores if r["arm"] == a]
        ok = sum(1 for r in rows if r["outcome"] in GOOD)
        cells += f"{ok}/{len(rows):<7}"
    print(f"  {'all items (n=55)':<26}{cells}")

    # Retrieval ceiling: the local arm cannot answer what was never retrieved.
    print()
    for a in arms[2:]:
        reachable = [r for r in scores if r["arm"] == a and r["expect"] == "present" and r["span_in_context"]]
        if not reachable:
            continue
        ok = sum(1 for r in reachable if r["outcome"] in GOOD)
        print(f"  {a}: gold span retrieved for {len(reachable)}/41; correct on those: {ok}/{len(reachable)}")

    print("\n  by axis (correct / n), present items only:")
    print(f"    {'':<11}" + "".join(f"{a:>10}" for a in arms))
    for axis in ("markers", "location", "function", "structure"):
        cells = ""
        for a in arms:
            rows = [r for r in scores if r["arm"] == a and r["axis"] == axis and r["expect"] == "present"]
            cells += f"{sum(1 for r in rows if r['outcome'] in GOOD)}/{len(rows):<8}"
        print(f"    {axis:<11}{cells}")


if __name__ == "__main__":
    main()

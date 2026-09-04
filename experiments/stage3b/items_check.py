"""Validate a hand-authored item file against the paper it claims to quote.

The item set is only as good as its spans. This checks, deterministically:

* every ``span`` is a verbatim substring of the paper's narrative text;
* no span comes from a Methods section (46% of the body text, and no statement
  about a cell type lives there);
* ``expect: absent`` items carry no span and are scored by absence, never by a
  judge (handoff rule 3: a judge will call a correct decline "incorrect");
* ids are unique, and every label named is a real roster label.

Run it after any edit to the item file. It is the only thing standing between a
mis-transcribed quote and four correction cycles.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus  # noqa: E402

# The nine narrative sections. Everything after "Discussion" in this paper's
# JATS is Methods, and Methods must not be cited as evidence about a cell type.
NARRATIVE_END = "Discussion"


def narrative_text(paper: str) -> tuple[str, str]:
    """Return (narrative text, methods text), split at the Discussion boundary."""
    paras = corpus.paragraphs(paper)
    titles = [t for t, _ in paras]
    try:
        cut = max(i for i, t in enumerate(titles) if t == NARRATIVE_END) + 1
    except ValueError:
        cut = len(paras)
    return (
        " ".join(t for _, t in paras[:cut]),
        " ".join(t for _, t in paras[cut:]),
    )


def normalise(text: str) -> str:
    """Collapse whitespace and unify the quote/dash characters that drift."""
    text = re.sub(r"[‘’“”]", lambda m: "'" if m.group() in "‘’" else '"', text)
    text = text.replace("–", "-").replace("—", "-").replace("−", "-")
    return re.sub(r"\s+", " ", text).strip()


def check(items_path: Path, roster_path: Path | None) -> list[str]:
    doc = yaml.safe_load(items_path.read_text())
    narrative, methods = (normalise(t) for t in narrative_text(doc["paper"]))

    roster: set[str] = set()
    if roster_path and roster_path.exists():
        roster = {e["cell_label"] for e in json.loads(roster_path.read_text())["entries"]}

    errors: list[str] = []
    seen: set[str] = set()
    for item in doc["items"]:
        iid = item["id"]
        if iid in seen:
            errors.append(f"{iid}: duplicate id")
        seen.add(iid)

        if roster and item["label"] not in roster:
            errors.append(f"{iid}: label {item['label']!r} is not in the roster")

        if item["expect"] == "absent":
            if item.get("span"):
                errors.append(f"{iid}: expect=absent must not carry a span")
            if item["scoring"] != "absence":
                errors.append(f"{iid}: expect=absent must use scoring=absence, not {item['scoring']!r}")
            continue

        span = normalise(item.get("span", ""))
        if not span:
            errors.append(f"{iid}: expect=present requires a span")
        elif span not in narrative:
            where = " (found in Methods, which is not valid evidence)" if span in methods else ""
            errors.append(f"{iid}: span not in narrative text{where}: {span[:90]!r}")
        if item["scoring"] == "absence":
            errors.append(f"{iid}: expect=present must not use scoring=absence")

    return errors


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("items", type=Path)
    ap.add_argument("--roster", type=Path)
    args = ap.parse_args()

    errors = check(args.items, args.roster)
    doc = yaml.safe_load(args.items.read_text())
    print(f"{args.items}: {len(doc['items'])} items")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)
    print("  all spans verified against the paper's narrative sections")


if __name__ == "__main__":
    main()

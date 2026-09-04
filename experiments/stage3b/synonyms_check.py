"""Validate a grounded synonym file and render the standard name clause.

Two jobs, both deterministic:

* **Check.** Every accepted synonym must carry a span that is a verbatim
  substring of the paper (narrative sections *or* figure legends -- glossary
  expansions live only in legends). A null span is allowed only when the entry
  declares a non-textual ``source``, such as the supplementary roster label.
  Rejected entries are checked too: a rejection resting on a misquote is not a
  rejection anyone can audit.

* **Render.** Emit the query clause for each label, in one fixed form, so that
  question text is generated rather than hand-written:

      {question about PRIMARY} (PRIMARY is also referred to as: A, B.)

  The clause is omitted entirely when nothing was accepted -- no empty
  parenthetical, and no clause built out of rejected candidates.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus  # noqa: E402
from atlas_chat.services import _jats_parser as J  # noqa: E402

AXIS_TEMPLATES = {
    "location": "Where in prenatal human skin is {n} found?",
    "function": "What function does the paper attribute to {n}?",
    "markers": "Which genes mark {n}?",
    "structure": "What does the paper say about the structure or morphology of {n}?",
}


def paper_text(paper: str, xml_path: Path) -> str:
    """Narrative prose plus figure legends, normalised for substring matching."""
    body = " ".join(t for _, t in corpus.paragraphs(paper))
    root = ET.fromstring(J._clean_xml(xml_path.read_text()))
    J._strip_namespace_from_tree(root)
    legends = " ".join("".join(f.itertext()) for f in root.iter("fig"))
    text = body + " " + legends
    text = re.sub(r"[‘’]", "'", text).replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text)


def clause(entry: dict) -> str:
    """The standard name clause, or an empty string when nothing was accepted."""
    accepted = [a["name"] for a in (entry.get("accepted") or [])]
    if not accepted:
        return ""
    primary = entry["primary"]
    return f" ({primary} is also referred to as: {', '.join(accepted)}.)"


def check(doc: dict, text: str) -> list[str]:
    errors: list[str] = []
    for entry in doc["labels"]:
        label = entry["label"]
        if not entry.get("primary"):
            errors.append(f"{label}: no primary name")
        for group in ("accepted", "rejected"):
            for item in entry.get(group) or []:
                span = item.get("span")
                if span is None:
                    if group == "accepted" and not item.get("source"):
                        errors.append(f"{label}/{item['name']}: null span needs an explicit source")
                    continue
                norm = re.sub(r"\s+", " ", span.replace("–", "-").replace("—", "-")).strip()
                norm = re.sub(r"[‘’]", "'", norm)
                if norm not in text:
                    errors.append(f"{label}/{item['name']} ({group}): span not in paper: {norm[:80]!r}")
        # A name must not be both accepted and rejected.
        acc = {a["name"] for a in entry.get("accepted") or []}
        rej = {r["name"] for r in entry.get("rejected") or []}
        for dupe in acc & rej:
            errors.append(f"{label}: {dupe!r} is both accepted and rejected")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("synonyms", type=Path)
    ap.add_argument("--xml", type=Path, required=True)
    ap.add_argument("--render", action="store_true", help="print the query clauses")
    args = ap.parse_args()

    doc = yaml.safe_load(args.synonyms.read_text())
    text = paper_text(doc["paper"], args.xml)
    errors = check(doc, text)

    n_acc = sum(len(e.get("accepted") or []) for e in doc["labels"])
    n_rej = sum(len(e.get("rejected") or []) for e in doc["labels"])
    print(f"{args.synonyms}: {len(doc['labels'])} labels, {n_acc} accepted, {n_rej} rejected")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)
    print("  all spans verified against the paper (narrative + legends)")

    if args.render:
        print("\n--- rendered questions ---")
        for entry in doc["labels"][:16]:
            print(AXIS_TEMPLATES["location"].format(n=entry["primary"]) + clause(entry))


if __name__ == "__main__":
    main()

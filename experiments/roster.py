"""Grounded name/synonym roster for an atlas paper's cell types.

The roster is the input to test-item generation: for each author label we want
every form the authors actually use, plus an honest record of how much the
paper's text says about that cell type. Every derived string carries the span
it came from, so a wrong entry can be traced rather than argued about.

Sources, in order of authority:

1. **Supplementary tables** give the label vocabulary verbatim (Gopee's
   logistic-regression sheets carry one column per annotation, so their header
   row *is* the roster). Nothing is inferred here.
2. **Figure legends** carry the abbreviation glossary — ``ASDC, Axl+Siglec6+
   dendritic cells; DC, dendritic cells; ...`` — which for many labels is the
   only place the expansion appears at all.
3. **Body prose** carries two further patterns: inline definitions
   (``outer root sheath (ORS) (SLC26A7+)``) and qualified forms
   (``hair placode``, ``hair matrix cells``) that disambiguate labels which are
   generic on their own.

Lift-out note: this is experiment code. The extraction rules are paper-agnostic
but the source *locations* are passed in, not derived — so promoting this to
``services/`` would mean wrapping ``build_roster`` in a CLI that takes a CAS+
document and a supplement manifest, and writing the result to CAS+ ``synonyms``
/ ``cell_fullname``. Nothing here reaches into the repo layout.

Usage::

    uv run python experiments/roster.py --xml experiments/papers/gopee2024.xml \\
        --fine  "<store>/Supplementary Table 11.xlsx" \\
        --broad "<store>/Supplementary Table 10.xlsx" \\
        --out   experiments/roster/gopee2024.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).parent))
import corpus  # noqa: E402
from atlas_chat.services import _jats_parser as J  # noqa: E402

# Columns present in the LR sheets that are not cell-type labels. `original_labels`
# holds the *other* species' annotation in these cross-species tables, so it is
# not a synonym source for this paper.
NON_LABEL_COLUMNS = {"LR_assignment", "original_labels"}

# A short token containing a capital is an abbreviation: it must match
# case-sensitively and on word boundaries. Without that, "LE" pluralised matches
# inside "cells" and "Matrix" matches "extracellular matrix".
ABBREV_MAX_LEN = 5

CONTENT_CUES = {
    "markers": re.compile(
        r"\b(express\w*|marker|marked by|positive for|co-express\w*|upregulat\w+|"
        r"enriched for|signature)\b",
        re.I,
    ),
    "location": re.compile(
        r"\b(dermis|dermal|epidermis|epidermal|peri-?follicular|localis\w+|localiz\w+|"
        r"spatial\w*|niche|compartment|adjacent to|surround\w+|resid\w+|located|"
        r"distribut\w+|zone|layer)\b",
        re.I,
    ),
    "function": re.compile(
        r"\b(promot\w+|induc\w+|role in|function\w*|recruit\w+|secret\w+|signal\w+|"
        r"regulat\w+|mediat\w+|contribut\w+|drives?|crosstalk|interact\w+|support\w*)\b",
        re.I,
    ),
    "structure": re.compile(
        r"\b(morpholog\w+|shapes?d?|dendrit\w+|elongat\w+|stellate|ultrastructur\w+|"
        r"cytoplasm\w*|stratifi\w+|columnar|cuboidal|invaginat\w+|budding)\b",
        re.I,
    ),
}


@dataclass
class Derived:
    """One derived string plus the span that justifies it."""

    value: str
    span: str
    source: str  # "legend_glossary" | "inline_definition" | "qualified_form" | ...


@dataclass
class RosterEntry:
    cell_label: str
    labelset: str
    expansions: list[Derived] = field(default_factory=list)
    qualified_forms: list[Derived] = field(default_factory=list)
    marker_hints: list[Derived] = field(default_factory=list)
    ambiguous_label: bool = False
    collides_with: list[str] = field(default_factory=list)
    n_body_passages: int = 0
    n_legend_passages: int = 0
    content_cues: dict[str, int] = field(default_factory=dict)
    answerable_for: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Source readers
# ---------------------------------------------------------------------------


def labels_from_lr_sheet(path: Path, header_row: int = 2) -> list[str]:
    """Read an annotation roster from a logistic-regression sheet's header row.

    These sheets carry one column per annotation, so the header *is* the
    author's label vocabulary — no interpretation involved.
    """
    import openpyxl

    ws = openpyxl.load_workbook(path, read_only=True, data_only=True).worksheets[0]
    rows = list(ws.iter_rows(min_row=header_row, max_row=header_row, values_only=True))
    if not rows:
        return []
    return [str(h).strip() for h in rows[0] if h and str(h).strip() not in NON_LABEL_COLUMNS]


def passages(xml_path: Path) -> tuple[list[str], list[str], str]:
    """Return (body paragraphs, figure-legend sentences).

    Returns body paragraphs, legend sentences, and the unsplit legend text.
    Legends are kept deliberately: for many labels the expansion appears
    nowhere else. They stay separate from body prose so callers can exclude
    them — an arm reading a rendering that drops legends must not be scored on
    legend-derived answers.
    """
    xml = J._clean_xml(xml_path.read_text())
    root = ET.fromstring(xml)
    J._strip_namespace_from_tree(root)

    body = [t for _, t in corpus.paragraphs(xml_path.stem)]
    legends: list[str] = []
    whole: list[str] = []
    for fig in root.iter("fig"):
        text = re.sub(r"\s+", " ", "".join(fig.itertext())).strip()
        whole.append(text)
        legends.extend(s for s in re.split(r"(?<=[.;]) +", text) if len(s) > 30)
    # The glossary must be parsed from the unsplit text: its entries ("LC,
    # Langerhans cells;") are shorter than the sentence-length floor above and
    # would otherwise be filtered out before ever being read.
    return body, legends, " ".join(whole)


# ---------------------------------------------------------------------------
# Extraction rules
# ---------------------------------------------------------------------------


def legend_glossary(legend_text: str) -> dict[str, Derived]:
    """Parse ``ABBR, expansion;`` runs out of figure legends.

    Nature legends end with a glossary of every abbreviation used in the panel,
    which is where most short labels are defined. Expansions may start with a
    capital (``ASDC, Axl+Siglec6+ dendritic cells``), so case is not a filter;
    positional words ("Left, ...", "Centre, ...") come through as harmless
    noise and are dropped when entries are matched against the roster.
    """
    out: dict[str, Derived] = {}
    pattern = re.compile(r"(?:^|[.;] )([A-Za-z][A-Za-z0-9+/\-]{1,9}), ([A-Za-z][^;.]{5,70})")
    for m in pattern.finditer(legend_text):
        out.setdefault(m.group(1), Derived(m.group(2).strip(), m.group(0).strip(), "legend_glossary"))
    return out


def inline_definitions(texts: Iterable[str]) -> dict[str, Derived]:
    """Find ``full name (ABBR)`` constructions in prose.

    The complement of the legend glossary: prose introduces an abbreviation the
    first time it uses it, and often attaches a marker at the same time.
    """
    out: dict[str, Derived] = {}
    pattern = re.compile(r"([a-z][a-z\- ]{4,50}?) \(([A-Z][A-Za-z0-9]{1,7})\)")
    for text in texts:
        for m in pattern.finditer(text):
            expansion, abbr = m.group(1).strip(), m.group(2)
            out.setdefault(abbr, Derived(expansion, m.group(0), "inline_definition"))
    return out


def label_variants(label: str, expansions: Iterable[str] = ()) -> list[re.Pattern[str]]:
    """Word-bounded patterns matching how a label may be written.

    Handles the notation drift between roster and prose (``LYVE1++`` vs
    ``LYVE1+``), singular/plural, and parenthesised qualifiers.
    """
    forms = {label, label.replace("++", "+"), re.sub(r"\(.*?\)", "", label).strip()}
    for form in list(forms):
        forms.update(
            {
                form.rstrip("s"),
                form + "s",
                form.replace(" cells", " cell"),
                form.replace(" cell", " cells"),
            }
        )
    forms.update(expansions)

    patterns = []
    for form in {f.strip() for f in forms if len(f.strip()) >= 2}:
        abbrev = len(form) <= ABBREV_MAX_LEN and any(c.isupper() for c in form)
        flags = 0 if abbrev else re.I
        patterns.append(re.compile(r"(?<![\w+])" + re.escape(form) + r"(?![\w+])", flags))
    return patterns


# Modifiers that mean the label is being used in its non-cell-type sense.
# "matrix" is the clearest case: this paper uses it for the hair-follicle cell
# state *and* for extracellular matrix and for several linear-algebra objects.
NON_BIOLOGICAL_MODIFIERS = {
    "extracellular", "expression", "transition", "adjacency", "probability",
    "coincidence", "correlation", "distance", "confusion", "count", "counts",
    "schur", "sparse", "dense", "input", "output", "resulting", "normalized",
    "normalised", "negative", "positive", "identity", "design",
}

# A qualified form is worth recording only if the authors use it more than once.
# One-offs are dominated by whatever verb or connective happened to precede the
# label ("comprised placode", "showed Treg").
MIN_QUALIFIED_FORM_COUNT = 2


def qualified_forms(label: str, texts: Iterable[str]) -> tuple[list[Derived], bool]:
    """Find modifiers the authors put in front of a bare label.

    Generic labels (``Placode``, ``Matrix``, ``Companion layer``) mean something
    specific only in context, and the authors supply that context inline: *hair*
    placode, *epidermal* placode, *hair* matrix cells. Recording the qualified
    form is what makes such a label usable in a question.

    Returns the forms and whether the label looks **ambiguous** — more than one
    surviving qualified form, meaning a question must name which sense it wants.
    This deliberately does not try to pick the right sense: that is a judgement
    call on a handful of labels, better made once by a reader than guessed at by
    a regex.
    """
    bare = re.sub(r"\(.*?\)", "", label).strip()
    if len(bare.split()) > 2:
        return [], False
    pattern = re.compile(
        r"((?:[\w+\-]+ ){1,2})" + re.escape(bare) + r"(?![\w+])",
        re.I if len(bare) > ABBREV_MAX_LEN else 0,
    )
    grammatical = {
        "the", "a", "an", "of", "and", "or", "in", "on", "to", "with", "for", "that",
        "these", "those", "our", "its", "their", "we", "were", "was", "are", "is",
        "as", "by", "from", "at", "into", "between", "than", "which", "both", "all",
        "some", "other", "same", "each", "this", "also", "only", "such", "more",
        "most", "whereas", "while", "however", "within", "across", "per",
    }
    counts: dict[str, int] = {}
    spans: dict[str, str] = {}
    for text in texts:
        for m in pattern.finditer(text):
            words = [w for w in m.group(1).strip().split() if w.lower() not in grammatical]
            if not words:
                continue
            mod = words[-1].lower()
            # Participles are almost always the sentence's verb, not a qualifier.
            if len(mod) < 3 or mod.endswith(("ed", "ing")) or mod in NON_BIOLOGICAL_MODIFIERS:
                continue
            form = f"{mod} {bare.lower()}"
            counts[form] = counts.get(form, 0) + 1
            spans.setdefault(form, text[max(0, m.start() - 40) : m.end() + 40].strip())

    kept = sorted(
        (f for f, n in counts.items() if n >= MIN_QUALIFIED_FORM_COUNT),
        key=lambda f: -counts[f],
    )
    return [Derived(f, spans[f], "qualified_form") for f in kept], len(kept) > 1


def marker_hints(label: str, texts: Iterable[str]) -> list[Derived]:
    """Catch ``label (GENE+)`` — a marker attached to a label in one breath.

    An abbreviation may sit between the two, as in ``outer root sheath (ORS)
    (SLC26A7+)``, so one non-gene parenthetical is allowed to intervene.
    """
    bare = re.sub(r"\(.*?\)", "", label).strip()
    gene = r"[A-Z][A-Z0-9]{1,9}\+"
    pattern = re.compile(
        r"(?<![\w+])" + re.escape(bare) + r"s?\)?(?: \([A-Za-z][A-Za-z0-9]{1,9}\))? "
        r"\((" + gene + r"(?:" + gene + r")*)\)",
        re.I if len(bare) > ABBREV_MAX_LEN else 0,
    )
    found: dict[str, Derived] = {}
    for text in texts:
        for m in pattern.finditer(text):
            for gene in m.group(1).rstrip("+").split("+"):
                found.setdefault(gene, Derived(gene, m.group(0), "marker_hint"))
    return list(found.values())


def sibling_collisions(label: str, roster: Iterable[str]) -> list[str]:
    """Roster labels that contain this one as a trailing phrase.

    ``Arterioles`` is a label in its own right, but so is ``Capillary
    arterioles``; a passage about the latter matches a search for the former.
    Any question asked about the general label can therefore be answered with
    evidence about the specific one, which makes its gold answer contestable.
    Worth knowing before items are written, not after they are scored.
    """
    bare = re.sub(r"\(.*?\)", "", label).strip().lower()
    out = []
    for other in roster:
        o = re.sub(r"\(.*?\)", "", other).strip().lower()
        if o != bare and (o.endswith(" " + bare) or o.rstrip("s").endswith(" " + bare.rstrip("s"))):
            out.append(other)
    return out


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

# A content type is claimed answerable only with corroboration: two or more
# body passages carrying the cue. One passage is as often a passing mention as
# a statement, and the whole point of the roster is an honest answerable set.
MIN_PASSAGES_FOR_ANSWERABLE = 2


def build_roster(
    xml_path: Path,
    fine_labels: list[str],
    broad_labels: list[str],
) -> list[RosterEntry]:
    body, legends, legend_text = passages(xml_path)
    gloss = legend_glossary(legend_text)
    inline = inline_definitions(body)

    all_labels = list(dict.fromkeys(fine_labels + broad_labels))
    entries: list[RosterEntry] = []
    seen: set[str] = set()
    for labelset, labels in (("fine", fine_labels), ("broad", broad_labels)):
        for label in labels:
            if label in seen:
                continue
            seen.add(label)

            expansions = [d for k, d in {**gloss, **inline}.items() if k == label or k == label.rstrip("s")]
            pats = label_variants(label, [d.value for d in expansions])
            body_hits = [t for t in body if any(p.search(t) for p in pats)]
            legend_hits = [t for t in legends if any(p.search(t) for p in pats)]

            quals, ambiguous = qualified_forms(label, body_hits + legend_hits)
            cues = {
                name: sum(1 for t in body_hits if rx.search(t))
                for name, rx in CONTENT_CUES.items()
            }
            entries.append(
                RosterEntry(
                    cell_label=label,
                    labelset=labelset,
                    expansions=expansions,
                    qualified_forms=quals,
                    ambiguous_label=ambiguous,
                    collides_with=sibling_collisions(label, all_labels),
                    marker_hints=marker_hints(label, body_hits),
                    n_body_passages=len(body_hits),
                    n_legend_passages=len(legend_hits),
                    content_cues=cues,
                    answerable_for=[
                        name for name, n in cues.items() if n >= MIN_PASSAGES_FOR_ANSWERABLE
                    ],
                )
            )
    return entries


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--xml", required=True, type=Path, help="JATS XML of the atlas paper")
    ap.add_argument("--fine", required=True, type=Path, help="LR sheet whose header is the fine roster")
    ap.add_argument("--broad", type=Path, help="LR sheet whose header is the broad roster")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    fine = labels_from_lr_sheet(args.fine)
    broad = labels_from_lr_sheet(args.broad) if args.broad else []
    entries = build_roster(args.xml, fine, broad)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(
            {
                "paper": args.xml.stem,
                "n_fine": len(fine),
                "n_broad": len(broad),
                "entries": [asdict(e) for e in entries],
            },
            indent=1,
        )
    )

    named = [e for e in entries if e.n_body_passages or e.n_legend_passages]
    answerable = [e for e in entries if e.answerable_for]
    print(f"{args.out}: {len(entries)} labels ({len(fine)} fine, {len(broad)} broad)")
    print(f"  named in text        : {len(named)}")
    print(f"  answerable (>=2 body): {len(answerable)}")
    print(f"  with an expansion    : {sum(1 for e in entries if e.expansions)}")
    print(f"  with qualified forms : {sum(1 for e in entries if e.qualified_forms)}")
    print(f"  with marker hints    : {sum(1 for e in entries if e.marker_hints)}")
    print(f"  ambiguous labels     : {sum(1 for e in entries if e.ambiguous_label)}")
    print(f"  sibling collisions   : {sum(1 for e in entries if e.collides_with)}")
    for cue in CONTENT_CUES:
        print(f"    answerable for {cue:<10}: {sum(1 for e in answerable if cue in e.answerable_for)}")


if __name__ == "__main__":
    main()

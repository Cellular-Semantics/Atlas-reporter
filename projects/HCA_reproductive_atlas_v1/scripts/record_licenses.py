#!/usr/bin/env python3
"""Record each corpus paper's licence on its supplement manifest.

The store holds verbatim article and supplement text and the repository is
public, so what may be committed turns on the licence. Most of the answer is
already on disk: Europe PMC JATS carries a ``<permissions>`` block, and 14 of
the 22 papers have their JATS fetched. This reads it from there rather than
asking an API again, and writes ``paper.license`` per
``supplement_manifest.schema.json``.

.. code-block:: bash

    python projects/HCA_reproductive_atlas_v1/scripts/record_licenses.py --dry-run
    python projects/HCA_reproductive_atlas_v1/scripts/record_licenses.py

Re-runnable: it overwrites ``license`` from current evidence each time, so a
paper whose JATS arrives later is picked up by running it again.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
STORE = PROJECT / "supplements" / "papers"

#: Licence URL (normalised) -> SPDX identifier. Matched on a path fragment, so
#: http vs https and a trailing slash do not matter.
URL_TO_SPDX = {
    "licenses/by/4.0": "CC-BY-4.0",
    "licenses/by-nc-nd/4.0": "CC-BY-NC-ND-4.0",
    "licenses/by-nc/4.0": "CC-BY-NC-4.0",
    "licenses/by-nd/4.0": "CC-BY-ND-4.0",
    "publicdomain/zero/1.0": "CC0-1.0",
}

#: This repository's distribution is academic and non-commercial: it sells
#: nothing, carries no advertising, and is not directed towards commercial
#: advantage. Recorded here because the NonCommercial licences turn on it, and
#: as a decision about this repository rather than a fact about any licence.
#: Being hosted on a commercial platform does not make a use commercial.
NON_COMMERCIAL = True

#: Grant redistribution of the text *and* of what is derived from it (chunks,
#: extracted plain text, prose units — all of which this store holds).
REDISTRIBUTABLE_SPDX = {"CC-BY-4.0", "CC0-1.0"}
if NON_COMMERCIAL:
    REDISTRIBUTABLE_SPDX = REDISTRIBUTABLE_SPDX | {"CC-BY-NC-4.0"}

#: Grant redistribution of the article verbatim but not of anything adapted
#: from it. `redistributable` is true for these, because that field asks about
#: verbatim text — but only the fetched article source may be committed, never
#: the extracted text or the chunked index derived from it.
VERBATIM_ONLY_SPDX = {"CC-BY-ND-4.0"}
if NON_COMMERCIAL:
    VERBATIM_ONLY_SPDX = VERBATIM_ONLY_SPDX | {"CC-BY-NC-ND-4.0"}

#: Licences that need a person, not a script, and why. Recorded as not
#: redistributable meanwhile, because the default when unsure is no.
NEEDS_HUMAN_CALL: dict[str, str] = {}

#: Why a verdict says what it does, where it rests on the NON_COMMERCIAL
#: decision or on the difference between a verbatim copy and an adaptation.
#: A bare boolean cannot carry either, and both are the kind of thing somebody
#: will want to re-examine.
SCOPE_NOTE = {
    "CC-BY-NC-4.0": (
        "NonCommercial. Redistribution and adaptation are both permitted "
        "non-commercially, and this repository's distribution is recorded as "
        "non-commercial — see NON_COMMERCIAL in record_licenses.py."
    ),
    "CC-BY-NC-ND-4.0": (
        "NonCommercial-NoDerivatives. The article may be redistributed "
        "verbatim non-commercially, and this repository's distribution is "
        "recorded as non-commercial. NoDerivatives still forbids sharing "
        "anything adapted from it, so the fetched article source may be "
        "committed and the extracted text and chunked index derived from it "
        "may not."
    ),
    "CC-BY-ND-4.0": (
        "NoDerivatives. The article may be redistributed verbatim, so the "
        "fetched article source may be committed; the extracted text and "
        "chunked index derived from it may not."
    ),
}

#: Papers with no JATS in the store whose licence is known from elsewhere. The
#: atlas preprint is the one that matters: its text is the only thing in the
#: local index that travels, and this is what says why.
KNOWN: dict[str, dict[str, object]] = {
    "10.64898/2026.06.10.731198": {
        "id": "CC-BY-4.0",
        "redistributable": True,
        "source": "biorxiv",
        "url": "https://creativecommons.org/licenses/by/4.0/",
        "note": (
            "bioRxiv reports `license: cc_by` for this preprint. This is the "
            "licence the local snippet index relies on: the preprint is the "
            "only paper whose chunks and snippets are committed, and the "
            "`.gitignore` re-include for `10.64898_*` rests on it."
        ),
    },
}

NO_LOCAL_EVIDENCE_NOTE = (
    "No JATS in the store and no licence recorded elsewhere, so nothing local "
    "settles this. A verdict rather than an absence: the check was made here "
    "and came up empty. It does not rule out the paper being open access."
)


def spdx_from_permissions(jats: Path) -> tuple[str, str] | None:
    """Return ``(spdx_id, url)`` from a JATS ``<permissions>`` block.

    Reads the licence URL rather than ``license-type``, which most publishers
    omit and the rest spell differently. Returns None when the block is absent
    or names no URL this recognises.
    """
    text = jats.read_text(encoding="utf-8", errors="replace")
    block = re.search(r"<permissions>(.*?)</permissions>", text, re.S)
    if not block:
        return None
    for url in re.findall(r"https?://[^\s\"'<>]+", block.group(1)):
        for fragment, spdx in URL_TO_SPDX.items():
            if fragment in url:
                return spdx, url
    return None


def license_for(paper_dir: Path, doi: str, now: str) -> dict[str, object]:
    """Build the ``license`` object for one paper, from JATS or known facts."""
    known = KNOWN.get(doi)
    if known:
        return {**known, "asserted_at": now}

    jats = paper_dir / "source" / "paper.jats.xml"
    found = spdx_from_permissions(jats) if jats.exists() else None

    if not found:
        return {
            "id": "unknown",
            "redistributable": False,
            "source": "manual",
            "asserted_at": now,
            "note": NO_LOCAL_EVIDENCE_NOTE,
        }

    spdx, url = found
    entry: dict[str, object] = {
        "id": spdx,
        "redistributable": spdx in REDISTRIBUTABLE_SPDX or spdx in VERBATIM_ONLY_SPDX,
        "source": "europepmc",
        "url": url,
        "asserted_at": now,
    }
    if spdx in VERBATIM_ONLY_SPDX:
        entry["verbatim_only"] = True
    if spdx in SCOPE_NOTE:
        entry["note"] = SCOPE_NOTE[spdx]
    elif spdx in NEEDS_HUMAN_CALL:
        entry["note"] = NEEDS_HUMAN_CALL[spdx]
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="print, do not write")
    args = parser.parse_args()

    if not STORE.is_dir():
        print(f"no supplement store at {STORE}", file=sys.stderr)
        return 2

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    seen = 0
    for manifest_path in sorted(STORE.glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        doi = manifest["paper"]["doi"]
        entry = license_for(manifest_path.parent, doi, now)
        seen += 1
        print(f"{'yes' if entry['redistributable'] else 'no '} {entry['id']:<18} {doi}")
        if args.dry_run:
            continue
        manifest["paper"]["license"] = entry
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print(f"\n{'would write' if args.dry_run else 'wrote'} {seen} manifest(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

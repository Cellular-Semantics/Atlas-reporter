"""CLI for the evidence store.

Thin entry point so evidence is readable without a Claude Code session:

.. code-block:: bash

    python -m atlas_chat.cli_evidence collect --traversal <dir> --cell-label "Immune_oLAM"

The implementation lives in :mod:`atlas_chat.services.evidence_store`.
"""

from __future__ import annotations

from atlas_chat.services.evidence_store import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())

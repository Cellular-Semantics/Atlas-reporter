"""CLI for the differential-expression store.

Thin entry point, so a conversion can be checked without a Claude Code session:

.. code-block:: bash

    python -m atlas_chat.cli_degs --store projects/<project>/degs
    python -m atlas_chat.cli_degs --file projects/<project>/degs/<cell label>.json

The implementation lives in :mod:`atlas_chat.services.degs`.
"""

from __future__ import annotations

from atlas_chat.services.degs import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())

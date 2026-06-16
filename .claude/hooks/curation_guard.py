#!/usr/bin/env python3
"""PreToolUse hook: curation-mode write guard.

By default this project runs in **curation / content** mode (see ``CLAUDE.md``).
In that mode, writes are restricted to the content area — only paths under
``projects/`` and ``planning/`` may be edited. Everything else (``src/``,
``.claude/``, schemas, docs, root config files, and any path outside the repo)
is out of scope and blocked.

The repo developer is granted an override based on their git identity
(``git config user.email`` in ``TRUSTED_USERS``), so dev sessions are
unrestricted. This mirrors the curation gate used in the evidencell project.

Exit codes:
  0 — allow the edit
  2 — block the edit (Claude sees the stderr message)
https://docs.anthropic.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

# Users whose writes bypass the curation gate entirely (developer override).
TRUSTED_USERS = {"ub2@sanger.ac.uk"}

# Only paths whose first component is one of these may be written by non-dev
# users. Everything else (incl. paths outside the repo) is blocked.
_WRITABLE_ZONES = ("projects", "planning")

# Project root: this file is .claude/hooks/curation_guard.py → parents[2].
_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _get_current_user_email() -> str | None:
    """Return current git user.email, or None if unavailable.

    Overridable via ATLAS_CHAT_HOOK_USER env var for tests:
      - unset      → fall through to ``git config user.email``
      - empty str  → treat as untrusted (simulates no configured user)
      - any value  → use as-is
    """
    override = os.environ.get("ATLAS_CHAT_HOOK_USER")
    if override is not None:
        return override or None
    try:
        result = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip() or None
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        pass
    return None


def _is_writable(file_path: Path) -> bool:
    """True if the path is inside an allowlisted content zone under the repo.

    Paths that cannot be resolved relative to the project root (i.e. outside
    the repo) are never writable in curation mode.
    """
    try:
        rel = file_path.resolve().relative_to(_PROJECT_ROOT)
    except (ValueError, OSError):
        return False
    parts = rel.parts
    return bool(parts) and parts[0] in _WRITABLE_ZONES


def _emit_rejection(file_path: Path, user: str | None) -> None:
    print("\n" + "=" * 64, file=sys.stderr)
    print("BLOCKING EDIT: curation mode — write out of scope", file=sys.stderr)
    print("=" * 64, file=sys.stderr)
    print(f"Target: {file_path}", file=sys.stderr)
    print(f"User:   {user or '(no git user.email set)'}", file=sys.stderr)
    print("", file=sys.stderr)
    print("In curation mode you may only write under:", file=sys.stderr)
    for zone in _WRITABLE_ZONES:
        print(f"  - {zone}/", file=sys.stderr)
    print("", file=sys.stderr)
    print("Edits to src/, .claude/, schemas, docs, and root files are out of", file=sys.stderr)
    print("scope. Options:", file=sys.stderr)
    print("  - Capture the request as a note under planning/ and stop.", file=sys.stderr)
    print("  - If you are authorised for dev work, set your git user.email to", file=sys.stderr)
    print("    the repo developer identity, or start a CLAUDE_dev.md session.", file=sys.stderr)
    print("=" * 64 + "\n", file=sys.stderr)


def main() -> None:
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    if tool_name not in ("Write", "Edit", "MultiEdit"):
        sys.exit(0)

    file_path_str = data.get("tool_input", {}).get("file_path", "")
    if not file_path_str:
        sys.exit(0)
    file_path = Path(file_path_str)

    # Developer override: trusted git identities bypass the gate.
    if _get_current_user_email() in TRUSTED_USERS:
        sys.exit(0)

    if _is_writable(file_path):
        sys.exit(0)

    _emit_rejection(file_path, _get_current_user_email())
    sys.exit(2)


if __name__ == "__main__":
    main()

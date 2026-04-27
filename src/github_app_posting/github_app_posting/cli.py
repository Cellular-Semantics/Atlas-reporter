from __future__ import annotations

import argparse
import re
import sys

from github_app_posting.client import GitHubAppClient
from github_app_posting.exceptions import CredentialError, GitHubAPIError

_REPO_RE = re.compile(r"^[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+$")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="gh-app-post",
        description="Post content to GitHub as a GitHub App installation.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    _add_issue_subparser(subparsers)
    args = parser.parse_args()

    if args.command == "issue":
        sys.exit(_cmd_issue(args))


def _add_issue_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore[type-arg]
    p = subparsers.add_parser("issue", help="Create a GitHub issue.")
    p.add_argument("--repo", required=True, help="Repository in owner/repo format.")
    p.add_argument("--title", required=True, help="Issue title.")
    p.add_argument(
        "--label",
        action="append",
        dest="labels",
        metavar="LABEL",
        help="Label to apply (repeatable).",
    )
    body_group = p.add_mutually_exclusive_group()
    body_group.add_argument("--body", help="Issue body text.")
    body_group.add_argument(
        "--body-file", metavar="FILE", help="Path to a file whose contents become the issue body."
    )


def _cmd_issue(args: argparse.Namespace) -> int:
    if not _REPO_RE.match(args.repo):
        print(
            f"Error: --repo must be in 'owner/repo' format, got: {args.repo!r}",
            file=sys.stderr,
        )
        return 1

    if args.body_file:
        try:
            from pathlib import Path

            body = Path(args.body_file).read_text()
        except OSError as exc:
            print(f"Error reading --body-file: {exc}", file=sys.stderr)
            return 1
    else:
        body = args.body or ""

    try:
        result = GitHubAppClient().post_issue(
            repo=args.repo,
            title=args.title,
            body=body,
            labels=args.labels or [],
        )
    except CredentialError as exc:
        print(f"Credential error: {exc}", file=sys.stderr)
        return 1
    except GitHubAPIError as exc:
        print(f"GitHub API error {exc.status_code}: {exc.response_body}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1

    print(result["url"])
    return 0

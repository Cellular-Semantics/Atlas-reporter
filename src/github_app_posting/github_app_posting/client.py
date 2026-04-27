from __future__ import annotations

import httpx

from github_app_posting.auth import GitHubAppAuth
from github_app_posting.config import load_config
from github_app_posting.exceptions import GitHubAPIError

_GITHUB_API = "https://api.github.com"
_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


class GitHubAppClient:
    """GitHub REST API client authenticated as a GitHub App installation."""

    def __init__(self, auth: GitHubAppAuth | None = None) -> None:
        if auth is None:
            auth = GitHubAppAuth(load_config())
        self._auth = auth

    def post_issue(
        self,
        repo: str,
        title: str,
        body: str,
        labels: list[str] | None = None,
    ) -> dict[str, str | int]:
        """Create a GitHub issue.

        Args:
            repo: Repository in "owner/repo" format.
            title: Issue title.
            body: Issue body (Markdown).
            labels: Optional list of label names to apply.

        Returns:
            {"url": html_url, "number": issue_number}

        Raises:
            GitHubAPIError: If the API returns a non-2xx response.
        """
        token = self._auth.get_token()
        payload: dict[str, object] = {"title": title, "body": body}
        if labels:
            payload["labels"] = labels

        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{_GITHUB_API}/repos/{repo}/issues",
                headers={**_HEADERS, "Authorization": f"token {token}"},
                json=payload,
            )
        if not resp.is_success:
            raise GitHubAPIError(resp.status_code, resp.text)
        data = resp.json()
        return {"url": data["html_url"], "number": data["number"]}


def post_issue(
    repo: str,
    title: str,
    body: str,
    labels: list[str] | None = None,
) -> dict[str, str | int]:
    """Module-level convenience wrapper — creates a fresh GitHubAppClient each call."""
    return GitHubAppClient().post_issue(repo, title, body, labels=labels)

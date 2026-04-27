class GitHubAppError(Exception):
    """Base class for all github_app_posting errors."""


class CredentialError(GitHubAppError):
    """Raised when GitHub App credentials cannot be loaded or are incomplete."""


class GitHubAPIError(GitHubAppError):
    """Raised when the GitHub REST API returns a non-2xx response."""

    def __init__(self, status_code: int, response_body: str) -> None:
        self.status_code = status_code
        self.response_body = response_body
        super().__init__(f"GitHub API error {status_code}: {response_body}")

"""Unit tests for API client behavior."""

try:
    from src.api_client import APIClient
except ImportError:
    from project.api_client import APIClient

def test_api_client_init() -> None:
    client = APIClient(
        base_url="https://example.org",
        token="token",
        timeout_seconds=10,
        max_retries=2,
    )
    assert client.base_url == "https://example.org"

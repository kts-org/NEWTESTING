"""HTTP client for fetching upstream API data."""

from typing import Any, Dict
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class APIClient:
    def __init__(self, base_url: str, token: str, timeout_seconds: int, max_retries: int) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.session = requests.Session()
        retry = Retry(total=max_retries, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def fetch(self, endpoint: str) -> Dict[str, Any]:
        response = self.session.get(f"{self.base_url}/{endpoint.lstrip('/') }", timeout=self.timeout_seconds)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError("Expected JSON object from API")
        return data

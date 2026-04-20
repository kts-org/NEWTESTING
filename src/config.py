"""Configuration for API and Event Hub integration."""

import os
from dataclasses import dataclass

@dataclass
class Settings:
    api_base_url: str
    api_timeout_seconds: int
    api_token: str
    eventhub_connection_string: str
    eventhub_name: str
    max_retries: int

def load_settings() -> Settings:
    return Settings(
        api_base_url=os.getenv("API_BASE_URL", ""),
        api_timeout_seconds=int(os.getenv("API_TIMEOUT_SECONDS", "30")),
        api_token=os.getenv("API_TOKEN", ""),
        eventhub_connection_string=os.getenv("EVENTHUB_CONNECTION_STRING", ""),
        eventhub_name=os.getenv("EVENTHUB_NAME", ""),
        max_retries=int(os.getenv("MAX_RETRIES", "3")),
    )

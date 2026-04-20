"""Application entrypoint for API-to-EventHub pipeline."""

import logging
try:
    from src.config import load_settings
    from src.api_client import APIClient
    from src.event_hub_producer import EventHubProducer
    from src.handlers import run_pipeline
except ImportError:
    from project.config import load_settings
    from project.api_client import APIClient
    from project.event_hub_producer import EventHubProducer
    from project.handlers import run_pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    settings = load_settings()
    client = APIClient(
        base_url=settings.api_base_url,
        token=settings.api_token,
        timeout_seconds=settings.api_timeout_seconds,
        max_retries=settings.max_retries,
    )
    producer = EventHubProducer(
        connection_string=settings.eventhub_connection_string,
        eventhub_name=settings.eventhub_name,
    )
    try:
        message = run_pipeline(client, producer, endpoint="/data")
        logger.info("Published message_id=%s", message.get("message_id"))
    finally:
        producer.close()

if __name__ == "__main__":
    main()

"""Unit tests for Event Hub producer contract."""

try:
    from src.event_hub_producer import EventHubProducer
except ImportError:
    from project.event_hub_producer import EventHubProducer

def test_event_hub_producer_has_publish_method() -> None:
    assert hasattr(EventHubProducer, "publish")

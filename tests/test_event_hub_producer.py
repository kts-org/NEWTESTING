import unittest
from unittest.mock import Mock
from services.event_hub_producer import EventHubProducer
from config import config

class TestEventHubProducer(unittest.TestCase):
    def test_send_message(self):
        event_hub_producer = EventHubProducer(config)
        event_hub_producer.send_message = Mock(return_value=None)
        message = "test_message"
        event_hub_producer.send_message(message)
        self.assertIsNone(event_hub_producer.send_message(message)
import unittest
from event_hub_producer import EventHubProducer

class TestEventHubProducer(unittest.TestCase):
    def test_send_message(self):
        event_hub_producer = EventHubProducer('your_connection_string_here', 'your_event_hub_name_here')
        message = {'id': 1, 'name': 'example', 'description': 'example description'}
        event_hub_producer.send_message(message)
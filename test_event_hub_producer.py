import unittest
from event_hub_producer import EventHubProducer

class TestEventHubProducer(unittest.TestCase):
    def test_send_message(self):
        event_hub_producer = EventHubProducer()
        message = 'Hello, World!'
        event_hub_producer.send_message(message)

def main():
    unittest.main()
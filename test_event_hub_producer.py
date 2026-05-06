import unittest
from event_hub_producer import EventHubProducer

class TestEventHubProducer(unittest.TestCase):
    def test_send_message(self):
        event_hub_connection_string = 'DefaultEndpointsProtocol=https;AccountName=<account_name>;AccountKey=<account_key>;BlobEndpoint=<blob_endpoint>'
        event_hub_name = 'event_hub_name'
        event_hub_producer = EventHubProducer(event_hub_connection_string, event_hub_name)
        message = 'Hello, World!'
        event_hub_producer.send_message(message)
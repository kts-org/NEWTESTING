from azure.eventhub import EventHubProducerClient
from azure.core.credentials import SharedKeyCredential
from config import config

class EventHubProducer:
    def __init__(self, config):
        self.config = config
        self.credential = SharedKeyCredential(self.config['event_hub_connection']['sas_key_name'], self.config['event_hub_connection']['sas_key'])
        self.producer = EventHubProducerClient.from_connection_string(f"Endpoint=sb://{self.config['event_hub_connection']['namespace']}.servicebus.windows.net/;SharedAccessKeyName={self.config['event_hub_connection']['sas_key_name']};SharedAccessKey={self.config['event_hub_connection']['sas_key']}", eventhub_name=self.config['event_hub_connection']['eventhub_name'])

    def send_message(self, message):
        try:
            self.producer.send_event(message)
            print("Message sent to Event Hub successfully.")
        except Exception as e:
            print(f"Error sending message: {e}")
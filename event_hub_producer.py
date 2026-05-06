from azure.eventhub import EventHubProducerClient, EventData
from logger import Logger

class EventHubProducer:
    def __init__(self, event_hub_connection_string, event_hub_name):
        self.event_hub_connection_string = event_hub_connection_string
        self.event_hub_name = event_hub_name
        self.logger = Logger()

    def send_message(self, message):
        try:
            producer = EventHubProducerClient.from_connection_string(self.event_hub_connection_string, eventhub_name=self.event_hub_name)
            event_data = EventData(message)
            producer.send([event_data])
        except Exception as e:
            self.logger.error(f'Error sending message: {e}')

    def close(self):
        pass
from azure.eventhub import EventHubProducerClient, EventData
from config import EVENT_HUB_CONNECTION_STRING, EVENT_HUB_NAME

class EventHubProducer:
    def __init__(self, connection_string=EVENT_HUB_CONNECTION_STRING, event_hub_name=EVENT_HUB_NAME):
        self.connection_string = connection_string
        self.event_hub_name = event_hub_name
        self.producer = EventHubProducerClient.from_connection_string(self.connection_string, self.event_hub_name)
    
    def send_message(self, message):
        try:
            event_data = EventData(message)
            self.producer.send([event_data])
        except Exception as e:
            logging.getLogger(__name__).error(f'Error sending message to Event Hub: {e}')
from azure.eventhub import EventHubProducerClient, EventData
from logger import Logger

class EventHubProducer:
    def __init__(self, connection_string, event_hub_name):
        self.connection_string = connection_string
        self.event_hub_name = event_hub_name
        self.logger = Logger()

    def send_message(self, message):
        try:
            producer = EventHubProducerClient.from_connection_string(self.connection_string, self.event_hub_name)
            event_data = EventData(json.dumps(message))
            producer.send([event_data])
            self.logger.info(f'Message sent to Event Hub: {message}')
        except Exception as e:
            self.logger.error(f'Error sending message to Event Hub: {e}')
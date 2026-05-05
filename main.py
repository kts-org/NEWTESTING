import json
from api_client import ApiClient
from data_transformer import DataTransformer
from event_hub_producer import EventHubProducer
from config import Config

class Config:
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

    def get_api_config(self):
        return self.config['api']

    def get_event_hub_config(self):
        return self.config['event_hub']

def main():
    config = Config()
    api_config = config.get_api_config()
    event_hub_config = config.get_event_hub_config()

    api_client = ApiClient(api_config['base_url'], api_config['api_key'])
    data_transformer = DataTransformer()
    event_hub_producer = EventHubProducer(event_hub_config['connection_string'], event_hub_config['event_hub_name'])

    data = api_client.fetch_data('/endpoint')
    transformed_data = data_transformer.transform_data(data)
    event_hub_producer.send_message(transformed_data)

if __name__ == '__main__':
    main()
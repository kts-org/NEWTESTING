from api_client import APIClient
from data_transformer import DataTransformer
from event_hub_producer import EventHubProducer
from config import Config
from error_handler import ErrorHandler
from logger import Logger

def main():
    config = Config('config.json')
    api_endpoint = config.get_api_endpoint()
    auth_token = config.get_auth_token()
    event_hub_connection_string = config.get_event_hub_connection_string()
    event_hub_name = config.get_event_hub_name()

    api_client = APIClient(api_endpoint, auth_token)
    data_transformer = DataTransformer()
    event_hub_producer = EventHubProducer(event_hub_connection_string, event_hub_name)
    error_handler = ErrorHandler()
    logger = Logger()

    data = api_client.fetch_data()
    if data is None:
        logger.error('Error fetching data')
        return

    transformed_data = data_transformer.transform_data(data)
    if transformed_data is None:
        logger.error('Error transforming data')
        return

    event_hub_producer.send_message(json.dumps(transformed_data))
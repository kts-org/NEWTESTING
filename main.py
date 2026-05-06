from services.api_client import ApiClient
from services.data_transformer import DataTransformer
from services.event_hub_producer import EventHubProducer
from config import config
from logger import Logger

if __name__ == '__main__':
    api_client = ApiClient(config)
    data = api_client.fetch_data()
    if data:
        data_transformer = DataTransformer()
        transformed_data = data_transformer.transform_data(data)
        event_hub_producer = EventHubProducer(config)
        event_hub_producer.send_message(transformed_data)
    logger = Logger()
    logger.log_info("Data ingestion and Event Hub publishing pipeline executed successfully.")
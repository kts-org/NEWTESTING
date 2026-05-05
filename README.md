# API Data Ingestion and Event Hub Publishing Pipeline
This project fetches data from an external API, transforms the received response into the required internal protocol format, and publishes the transformed data to Azure Event Hub.
## Requirements
* Python 3.8+
* azure-eventhub
* requests
## Usage
1. Install the required packages: `pip install -r requirements.txt`
2. Configure the API endpoint, authentication token, internal protocol format, Event Hub connection string, and Event Hub name in `config.py`.
3. Run the API client: `python api_client.py`
4. Run the data transformer: `python data_transformer.py`
5. Run the Event Hub producer: `python event_hub_producer.py`
## Testing
1. Run the unit tests: `python -m unittest discover`
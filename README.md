# API Data Ingestion and Event Hub Publishing Pipeline

This project fetches data from an external API, transforms the received response into the required internal protocol format, and publishes the transformed data to Azure Event Hub.

## Requirements

* Python 3.8+
* azure-eventhub
* requests

## Configuration

Create a `config.json` file with the following format:
```json
{
    "api": {
        "base_url": "https://api.example.com",
        "api_key": "your_api_key_here"
    },
    "event_hub": {
        "connection_string": "your_connection_string_here",
        "event_hub_name": "your_event_hub_name_here"
    }
}
```
## Running the Project

Run the project using the following command:
```bash
python main.py
```
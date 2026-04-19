# API to Event Hub Pipeline

## What It Does
- Fetches data from an external API
- Transforms payload into internal protocol format
- Publishes transformed messages to Azure Event Hub

## Configuration
Set these environment variables:
- API_BASE_URL
- API_TOKEN
- API_TIMEOUT_SECONDS
- EVENTHUB_CONNECTION_STRING
- EVENTHUB_NAME
- MAX_RETRIES

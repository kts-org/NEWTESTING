import requests
import json
from config import config

class ApiClient:
    def __init__(self, config):
        self.config = config

    def fetch_data(self):
        try:
            response = requests.get(self.config['api_endpoint'], auth=(self.config['api_auth']['username'], self.config['api_auth']['password']))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
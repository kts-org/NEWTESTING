import requests
import json
from logger import Logger

class ApiClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.logger = Logger()

    def fetch_data(self, endpoint):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(f'{self.base_url}{endpoint}', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f'Error fetching data: {e}')
            return None
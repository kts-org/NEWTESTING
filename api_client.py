import requests
import json
from logger import Logger

class APIClient:
    def __init__(self, api_endpoint, auth_token):
        self.api_endpoint = api_endpoint
        self.auth_token = auth_token
        self.logger = Logger()

    def fetch_data(self):
        try:
            headers = {'Authorization': f'Bearer {self.auth_token}'}
            response = requests.get(self.api_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f'Error fetching data: {e}')
            return None

    def validate_response(self, response):
        if response is None:
            return False
        if not isinstance(response, dict):
            self.logger.error('Invalid response format')
            return False
        return True
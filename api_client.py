import requests
import logging
from config import API_ENDPOINT, API_AUTH_TOKEN

class APIClient:
    def __init__(self, endpoint=API_ENDPOINT, auth_token=API_AUTH_TOKEN):
        self.endpoint = endpoint
        self.auth_token = auth_token
        self.logger = logging.getLogger(__name__)
    
    def fetch_data(self):
        try:
            response = requests.get(self.endpoint, headers={'Authorization': f'Bearer {self.auth_token}'})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f'Error fetching data from API: {e}')
            return None
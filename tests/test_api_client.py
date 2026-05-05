import unittest
from api_client import ApiClient

class TestApiClient(unittest.TestCase):
    def test_fetch_data(self):
        api_client = ApiClient('https://api.example.com', 'your_api_key_here')
        data = api_client.fetch_data('/endpoint')
        self.assertIsNotNone(data)
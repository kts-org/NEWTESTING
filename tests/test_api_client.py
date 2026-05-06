import unittest
from unittest.mock import Mock
from services.api_client import ApiClient
from config import config

class TestApiClient(unittest.TestCase):
    def test_fetch_data(self):
        api_client = ApiClient(config)
        api_client.fetch_data = Mock(return_value={"data": "test_data"})
        data = api_client.fetch_data()
        self.assertEqual(data, {"data": "test_data"})
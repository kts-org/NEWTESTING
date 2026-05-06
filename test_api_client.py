import unittest
from api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_fetch_data(self):
        api_endpoint = 'https://example.com/api'
        auth_token = 'token'
        api_client = APIClient(api_endpoint, auth_token)
        data = api_client.fetch_data()
        self.assertIsNotNone(data)

    def test_validate_response(self):
        api_endpoint = 'https://example.com/api'
        auth_token = 'token'
        api_client = APIClient(api_endpoint, auth_token)
        response = {'id': 1, 'name': 'John'}
        self.assertTrue(api_client.validate_response(response))
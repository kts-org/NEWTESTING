import unittest
from api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_fetch_data(self):
        api_client = APIClient()
        data = api_client.fetch_data()
        self.assertIsNotNone(data)

def main():
    unittest.main()
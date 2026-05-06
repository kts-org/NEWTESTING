import unittest
from services.data_transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def test_transform_data(self):
        data_transformer = DataTransformer()
        data = {"data": "test_data"}
        transformed_data = data_transformer.transform_data(data)
        self.assertEqual(transformed_data, "{\"data\": \"test_data\"}"
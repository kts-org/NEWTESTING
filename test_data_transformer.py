import unittest
from data_transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def test_transform_data(self):
        data_transformer = DataTransformer()
        data = {'id': 1, 'name': 'John'}
        transformed_data = data_transformer.transform_data(data)
        self.assertIsNotNone(transformed_data)

    def test_validate_transformed_data(self):
        data_transformer = DataTransformer()
        transformed_data = {'id': 1, 'name': 'John'}
        self.assertTrue(data_transformer.validate_transformed_data(transformed_data))
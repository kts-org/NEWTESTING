import unittest
from data_transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def test_transform_data(self):
        data_transformer = DataTransformer()
        data = {'id': 1, 'name': 'example', 'description': 'example description'}
        transformed_data = data_transformer.transform_data(data)
        self.assertEqual(transformed_data['id'], 1)
        self.assertEqual(transformed_data['name'], 'example')
        self.assertEqual(transformed_data['description'], 'example description')
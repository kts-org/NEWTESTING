import unittest
from data_transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def test_transform_data(self):
        data_transformer = DataTransformer()
        data = {'key': 'value'}
        transformed_data = data_transformer.transform_data(data)
        self.assertIsNotNone(transformed_data)

def main():
    unittest.main()
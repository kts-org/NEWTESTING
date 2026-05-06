import json
from logger import Logger

class DataTransformer:
    def __init__(self):
        self.logger = Logger()

    def transform_data(self, data):
        try:
            transformed_data = {'id': data['id'], 'name': data['name']}
            return transformed_data
        except KeyError as e:
            self.logger.error(f'Error transforming data: {e}')
            return None

    def validate_transformed_data(self, transformed_data):
        if transformed_data is None:
            return False
        if not isinstance(transformed_data, dict):
            self.logger.error('Invalid transformed data format')
            return False
        return True
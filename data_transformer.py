import json
from logger import Logger

class DataTransformer:
    def __init__(self):
        self.logger = Logger()

    def transform_data(self, data):
        try:
            # Convert API response data into the defined internal protocol format
            transformed_data = {
                'id': data['id'],
                'name': data['name'],
                'description': data['description']
            }
            return transformed_data
        except KeyError as e:
            self.logger.error(f'Error transforming data: {e}')
            return None
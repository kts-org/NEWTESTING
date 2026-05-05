import logging
from config import INTERNAL_PROTOCOL_FORMAT

class DataTransformer:
    def __init__(self, protocol_format=INTERNAL_PROTOCOL_FORMAT):
        self.protocol_format = protocol_format
        self.logger = logging.getLogger(__name__)
    
    def transform_data(self, data):
        try:
            transformed_data = {'protocol': self.protocol_format, 'data': data}
            return transformed_data
        except Exception as e:
            self.logger.error(f'Error transforming data: {e}')
            return None
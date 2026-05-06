import logging
from logger import Logger

class ErrorHandler:
    def __init__(self):
        self.logger = Logger()

    def handle_error(self, error):
        self.logger.error(f'Error: {error}')

    def retry(self, func, *args, **kwargs):
        max_retries = 3
        for i in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f'Error: {e}')
                if i < max_retries - 1:
                    continue
                raise
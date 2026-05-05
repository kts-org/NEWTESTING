import logging
from logger import Logger

class ErrorHandler:
    def __init__(self):
        self.logger = Logger()

    def handle_error(self, error):
        self.logger.error(f'Error: {error}')
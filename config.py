import json

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print('Config file not found')
            return None

    def get_api_endpoint(self):
        return self.config['api_endpoint']

    def get_auth_token(self):
        return self.config['auth_token']

    def get_event_hub_connection_string(self):
        return self.config['event_hub_connection_string']

    def get_event_hub_name(self):
        return self.config['event_hub_name']
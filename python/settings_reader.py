import json
import os

class Settings:
    def __init__(self, settings_name):
        self.settings_name = settings_name
        self.read_settings(settings_name)

    def read_settings(self, settings_name):
        file_path = os.path.join(os.path.dirname(__file__), f'../settings/{settings_name}.json')
        with open(file_path, 'r') as file:
            settings = json.load(file)
        
        for key, value in settings.items():
            setattr(self, key, value)
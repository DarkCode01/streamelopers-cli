import os
import json

def _config():
    with open(f'{os.getcwd()}/config/config.json', 'r') as _config_file:
        return json.load(_config_file)

def config_obs():
    with open(f'{os.getcwd()}/config/config-obs.json', 'r') as _config_file:
        return json.load(_config_file)

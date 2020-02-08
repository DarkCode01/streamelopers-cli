import os
import json

def config():
    with open(f'{os.getcwd()}/config/config.json') as _config_file:
        return json.load(_config_file)

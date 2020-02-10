import os
import json
from libs.config import config_obs

HOME = os.environ.get('HOME')

def create_file(data, name):
    if not os.path.isdir(f'{HOME}/.stobs'):
        os.mkdir(f'{HOME}/.stobs')

    with open(f'{HOME}/.stobs/{name}.json', 'w') as _file:
        _file.write(data)

def parser_values(data, name):
    data['name'] = name

    return data

def _generator(name):
    data = parser_values(config_obs(), name)
    data = json.dumps(data, indent=4)

    create_file(data, name)

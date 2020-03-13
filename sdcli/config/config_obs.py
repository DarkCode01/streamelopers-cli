'''
Template of a config file with scenes collecitons.
'''

import os
import json

from sdcli.config._config import Config


class ConfigOBS(Config):
    
    @staticmethod
    def template():
        with open(f'${os.environ.get("HOME")}/.sdcli/settings.obs.json', 'r') as settings:
            return json.loads(settings.read())

import argparse
from libs import config


class Version(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(Version, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        _config = config()
        print(f'Streamelopers Generator (v{_config.get("version")})')

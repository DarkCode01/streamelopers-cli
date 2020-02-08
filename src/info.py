import argparse
from libs import config


class Info(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(Info, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        _config = config()

        print(f'''
        Medium: {_config.get('medium')}
        Github: {_config.get('github')}
        Github (Streamelopers): {_config.get('github (Stremelopers)')}
        Patron: {_config.get('patron')}
        ''')

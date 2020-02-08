import argparse
import textwrap

# actions....
from src import Info
from src import Version

def cli():
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Streamelopers - Generator Config.
            --------------------------------
            CLI create by Streamelopers for generate our configuration on OBS. 
        ''')
    )

    # Add params...
    parser.add_argument(
        'info', action=Info,
        help='Display info and social medias of Stremealopers.'
    )
    parser.add_argument(
        'version', action=Version,
        help='Prints streamelopers-gen version.'
    )

    # parser arguments...
    return parser.parse_args()

if __name__ == '__main__':
    cli()

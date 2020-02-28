import click
import colorama

from sdcli.src.lib.error import print_output_error

from sdcli.src import info
from sdcli.src import generator as creator


@click.group()
def cli():
    '''
    CLI create by Streamelopers for generate our configuration on OBS.
    '''

    pass

@cli.command(help='For generate new config file.')
# @click.option('--event', prompt='Type of event: ', help='Specificate type of event.')
@click.option('--name', '-n', nargs=1, default='speaking', required=True,
              prompt='Name of Scenes Collection', help='Name Scnenes Collection')
def generate(name):
    try:
        creator._generator(name)
    except Exception as ex:
        print_output_error(message='Error while creating config file...', ex=str(ex))

@cli.command(help='Print information of our social medias.')
def information():
    info._info()

@cli.command(help='Print version of SGen.')
def version():
    info.version()

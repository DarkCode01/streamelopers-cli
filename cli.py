import click
from src import info
from src import generator as creator

__author__ = 'Jose Segura (Darkcoder)'

@click.group()
def cli():
    '''
    CLI create by Streamelopers for generate our configuration on OBS.
    '''

    pass

@cli.command(help='For generate new config file.')
# @click.option('--event', prompt='Type of event: ', help='Specificate type of event.')
@click.option('--name', prompt='Name of Scenes Collection', help='Name Scnenes Collection')
def generator(name):
    creator._generator(name)

@cli.command(help='Print information of our social medias.')
def information():
    info._info()

@cli.command(help='Print version of SGen.')
def version():
    info.version()


if __name__ == '__main__':
    cli()

import os
import json
import click

from libs.config import config_obs


HOME = os.environ.get('HOME')

def create_file(data, name):
    click.echo(click.style('Creating config file of scenes collection...'))

    if not os.path.isdir(f'{HOME}/.stobs'):
        os.mkdir(f'{HOME}/.stobs')

    with open(f'{HOME}/.stobs/{name}.json', 'w') as _file:
        _file.write(data)

    click.echo(click.style('Created!', fg='green'))

def parser_values(data, name):
    data['name'] = name

    return data

def _generator(name):
    data = parser_values(config_obs(), name)
    data = json.dumps(data, indent=4)

    create_file(data, name)

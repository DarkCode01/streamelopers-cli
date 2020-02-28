import click
from sdcli.config import Config

def _info():
    social_medias = Config.SOCIAL_MEDIAS

    click.echo(f'''
    Medium: {social_medias.get('medium')}
    Github: {social_medias.get('github')}
    Patron: {social_medias.get('patron')}
    ''')

def version():
    click.echo(f'Streamelopers Generator (v{Config.VERSION})')

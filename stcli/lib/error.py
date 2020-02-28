import click
import colorama


def print_output_error(message, ex=None):
    click.echo(click.style(message, fg='red'))
    click.echo()
    click.echo(click.style('...More details of error...'))
    click.echo(click.style(ex, fg='red'))
    click.echo()

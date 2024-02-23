from drive_vault.backup import Backup
from drive_vault.drive import Drive
import os
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('directories', nargs=-1, type=click.Path(exists=True, file_okay=False, dir_okay=True))
def backup(directories):
    '''Backup specified directories'''
    for directory in directories:
        click.echo(f'Backup {directory}')


@cli.command()
def list():
    """List backups"""
    click.echo("Listing backups...")


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def remove(filename):
    """Remove backup"""
    click.echo(f"Removing {filename}")

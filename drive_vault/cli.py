from drive_vault.backup import Backup
from drive_vault.drive import Drive
import os
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("directories", nargs=-1, type=click.Path(exists=True, file_okay=False, dir_okay=True))
def backup(directories: list):
    """Backup specified directories"""

    backup_zip_name = Backup.create(directories)
    click.echo("> Backup made with success.")
    drive = Drive()
    drive.upload(backup_zip_name)
    os.remove(backup_zip_name)
    click.echo("> Upload made with success.")


@cli.command()
def list():
    """List backups"""

    drive = Drive()
    backups = drive.list()

    if not backups:
        click.echo("> No backups avaible.")
        return

    click.echo("> Backup list:")
    for backup in backups:
        click.echo(f"> {backup}")


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def remove(filename):
    """Remove backup"""

    click.echo(f"> Removing {filename}.")

    drive = Drive()
    result = drive.remove(filename)

    if not result:
        click.echo(f"> Error: Couldn't remove {filename} file.")
    else:
        click.echo(f"> File '{filename}' removed successfully.")

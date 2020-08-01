# -*- coding: utf-8 -*-

import click

from onefeed.app import app
from onefeed.retriever import fetch_once


@click.group()
def cli():
    pass


@cli.command()
def start():
    app.run(host='localhost', port=9487)


@cli.command()
def fetch():
    fetch_once()


if __name__ == '__main__':
    cli()

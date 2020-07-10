# -*- coding: utf-8 -*-

import click

from onefeed.app import app
from onefeed.retriever import fetch_once, fetch_job


@click.group()
def cli():
    pass


@cli.command()
def start():
    app.run(host='localhost', port=9487)


@cli.command()
def fetch():
    fetch_once()


@cli.command()
def fetch_forever():
    fetch_job()


if __name__ == '__main__':
    cli()

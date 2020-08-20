# -*- coding: utf-8 -*-
import time
import threading
from urllib import request
import webbrowser

import click

from onefeed.app import app
from onefeed.retriever import fetch_once


@click.group()
def cli():
    pass


@cli.command()
def start():
    def open_browser():
        print('Onefeed starting...')
        while True:
            try:
                request.urlopen(url="http://127.0.0.1:9487")
                break
            except Exception as e:
                time.sleep(0.5)
        print('Onefeed started !')
        webbrowser.open("http://127.0.0.1:9487")
    threading.Thread(target=open_browser).start()

    app.run(host='localhost', port=9487)


@cli.command()
@click.argument('spiders', nargs=-1)
def fetch(spiders):
    spiders = {s: {} for s in spiders}
    fetch_once(spiders)


if __name__ == '__main__':
    cli()

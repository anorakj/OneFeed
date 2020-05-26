# -*- coding: utf-8 -*-
import click
import pathlib

from scrapy.crawler import CrawlerProcess

from onefeed.app import create_app
from onefeed.retriever.github.github.spiders.trending import TrendingSpider


@click.group()
def cli():
    pass


@cli.command()
def start():
    app = create_app()
    app.run(host='localhost', port=9487)


@cli.command()
def fetch():
    process = CrawlerProcess(settings={'FEEDS': {
        pathlib.Path('onefeed_data/github_items.csv'): {'format': 'csv'}
    }, })
    process.crawl(TrendingSpider)
    process.start()


if __name__ == '__main__':
    cli()

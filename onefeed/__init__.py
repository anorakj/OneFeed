# -*- coding: utf-8 -*-

import pathlib

from scrapy.crawler import CrawlerProcess

from onefeed.app import create_app
from onefeed.retriever.github.github.spiders.trending import TrendingSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={'FEEDS': {
        pathlib.Path('data/github_items.csv'): {'format': 'csv'}
    }, })
    process.crawl(TrendingSpider)
    process.start()

    app = create_app()
    app.run(host='localhost', port=9487)

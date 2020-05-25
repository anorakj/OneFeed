# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
import pathlib
from onefeed.retriever.github.github.spiders.trending import TrendingSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={'FEEDS': {
            pathlib.Path('github_items.csv'): {'format': 'csv'}
        },})
    process.crawl(TrendingSpider)
    process.start()


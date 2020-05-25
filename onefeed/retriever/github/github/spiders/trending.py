# -*- coding: utf-8 -*-

import pathlib
import time

from ..items import TrendingItem
import scrapy


class TrendingSpider(scrapy.Spider):
    name = 'trending'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/trending']
    custom_settings = {

        'FEED_EXPORT_FIELDS': ['repository', 'description', 'star', 'language', 'timestamp'],
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):
        for box in response.xpath('//article[@class="Box-row"]'):
            item = TrendingItem()
            item['repository'] = box.xpath('./h1/a/@href').get()
            item['language'] = box.xpath('.//span[@itemprop="programmingLanguage"]/text()').get()
            item['description'] = box.xpath('./p/text()').get()
            item['star'] = box.xpath('.//a[contains(@class, "muted-link")]/text()')[1].get()
            item['timestamp'] = int(time.time())
            yield item

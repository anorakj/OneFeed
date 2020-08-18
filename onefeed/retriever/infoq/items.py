# -*- coding: utf-8 -*-

import scrapy


class ArticlesItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    source = scrapy.Field()

# -*- coding: utf-8 -*-

import scrapy


class HomepageItem(scrapy.Item):
    points = scrapy.Field()
    comments = scrapy.Field()
    source_website = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def strip_serializer(value):
    return value.strip() if isinstance(value, str) else value


class TrendingItem(scrapy.Item):
    # define the fields for your item here like:
    repository = scrapy.Field()
    language = scrapy.Field()
    description = scrapy.Field(serializer=strip_serializer)
    star = scrapy.Field(serializer=strip_serializer)
    timestamp = scrapy.Field()

# -*- coding: utf-8 -*-

import scrapy


def strip_serializer(value):
    return value.strip() if isinstance(value, str) else value


class TrendingItem(scrapy.Item):
    repository = scrapy.Field()
    language = scrapy.Field()
    description = scrapy.Field(serializer=strip_serializer)
    star = scrapy.Field(serializer=strip_serializer)
    source = scrapy.Field()

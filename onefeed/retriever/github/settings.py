# -*- coding: utf-8 -*-


BOT_NAME = 'github'

SPIDER_MODULES = ['onefeed.retriever.github.spiders']

ITEM_PIPELINES = {
    'onefeed.retriever.github.pipelines.SqlitePipeline': 300,
}

DB = 'onefeed_data/onefeed.db'

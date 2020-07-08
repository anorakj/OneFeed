# -*- coding: utf-8 -*-

BOT_NAME = 'hackernews'
SPIDER_MODULES = ['onefeed.retriever.hackernews.spiders']
ITEM_PIPELINES = {
    'onefeed.retriever.hackernews.pipelines.SqlitePipeline': 300,
}
ROBOTSTXT_OBEY = False
DB = 'onefeed_data/onefeed.db'
FORCED_TIMEOUT = 10
LOG_LEVEL = 'INFO'


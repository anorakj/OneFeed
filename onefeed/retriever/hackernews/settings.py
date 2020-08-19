# -*- coding: utf-8 -*-

BOT_NAME = 'hackernews'
SPIDER_MODULES = ['onefeed.retriever.hackernews.spiders']
ITEM_PIPELINES = {
    'onefeed.retriever.hackernews.pipelines.SqlitePipeline': 300,
}
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
CLOSESPIDER_TIMEOUT = 7
DOWNLOAD_TIMEOUT = 7




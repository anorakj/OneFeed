# -*- coding: utf-8 -*-

BOT_NAME = 'hackernews'
SPIDER_MODULES = ['onefeed.retriever.hackernews.spiders']
ITEM_PIPELINES = {
    'onefeed.retriever.hackernews.pipelines.SqlitePipeline': 300,
}
ROBOTSTXT_OBEY = False
FORCED_TIMEOUT = 10
LOG_LEVEL = 'ERROR'
SCHEDULE_TIME = '10:15'
CLOSESPIDER_TIMEOUT = 3
DOWNLOAD_TIMEOUT = 3




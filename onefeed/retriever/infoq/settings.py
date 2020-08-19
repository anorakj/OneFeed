# -*- coding: utf-8 -*-

BOT_NAME = 'infoq'
SPIDER_MODULES = ['onefeed.retriever.infoq.spiders']
ITEM_PIPELINES = {
    'onefeed.retriever.infoq.pipelines.SqlitePipeline': 300,
}
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
CLOSESPIDER_TIMEOUT = 7
DOWNLOAD_TIMEOUT = 7
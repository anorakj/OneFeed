# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from crochet import setup, wait_for

from .utils import get_spiders

setup()


@wait_for(timeout=60)
def fetch_once():
    d_list = []
    for spider, setting in get_spiders().items():
        default_setting = get_project_settings()
        default_setting.update(setting)
        crawler_runner = CrawlerRunner(default_setting)
        d_list.append(crawler_runner.crawl(spider))
    d = defer.DeferredList(d_list).addBoth(lambda _: print('all finished'))
    return d

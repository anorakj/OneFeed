# -*- coding: utf-8 -*-
import sys

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from crochet import setup, wait_for

from .utils import get_spiders

if not sys.argv[0] in ['crawl', 'shell']:  # when debugging scrapy
    setup()


@wait_for(timeout=60)
def fetch_once(spiders=None):
    """If spiders is None, crawl all spiders. ELse, fetch the spiders specified
    :param spiders: a dict whose key is spider name and value is custom setting
    :type spiders: dict
    :return: the deferred list of all the crawler_runner
    :rtype: twisted.internet.defer.DeferredList
    """
    if spiders is None:
        spiders = []
    if not spiders:
        spiders = get_spiders().items()
    else:
        temp_spiders = spiders
        spiders = [(k, v) for k, v in get_spiders().items() if k.name in spiders]
        for k, v in spiders:
            v.update(temp_spiders[k.name])
    d_list = []
    for spider, setting in spiders:
        default_setting = get_project_settings()
        default_setting.update(setting)
        crawler_runner = CrawlerRunner(default_setting)
        d_list.append(crawler_runner.crawl(spider))
    d = defer.DeferredList(d_list)
    return d

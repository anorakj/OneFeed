# -*- coding: utf-8 -*-

from multiprocessing import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .utils import get_spiders


def _crawler_func(spider, settings):
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(spider)
    crawler_process.start()
    crawler_process.stop()


def fetch_once():
    for spider, setting in get_spiders().items():
        print('start fetching {}'.format(spider.name))
        default_setting = get_project_settings()
        default_setting.update(setting)
        process = Process(target=_crawler_func, args=(spider, default_setting), daemon=True)
        process.start()
        process.join(timeout=default_setting.getint('FORCED_TIMEOUT'))
        process.terminate()
        print('finish fetching {}'.format(spider.name))

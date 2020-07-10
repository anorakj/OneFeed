# -*- coding: utf-8 -*-


from multiprocessing import Process
import time

import schedule

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .utils import get_spiders


def _crawler_func(spider, settings):
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(spider)
    crawler_process.start()


def crawl_job(spider, setting):
    print('start fetching {}'.format(spider.name))
    process = Process(target=_crawler_func, args=(spider, setting), daemon=True)
    process.start()
    process.join(timeout=setting.getint('FORCED_TIMEOUT'))
    exitcode = process.exitcode
    process.terminate()
    if exitcode is not None:
        print('finish fetching {}'.format(spider.name))
    else:
        print('{} forced stopped according to timeout'.format(spider.name))


def fetch_once():
    for spider, setting in get_spiders().items():
        default_setting = get_project_settings()
        default_setting.update(setting)
        crawl_job(spider, default_setting)


def fetch_job(run_immediately=False):
    for spider, setting in get_spiders().items():
        default_setting = get_project_settings()
        default_setting.update(setting)
        schedule.every().day.at(default_setting['SCHEDULE_TIME']).do(crawl_job, spider, default_setting)
        print('{} job scheduled'.format(spider.name))
    if run_immediately:
        schedule.run_all()
    while True:
        schedule.run_pending()
        time.sleep(1)

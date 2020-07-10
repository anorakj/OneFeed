# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import tempfile

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from onefeed.retriever.github import TrendingSpider
from onefeed.retriever.hackernews import HomepageSpider
from onefeed.retriever.sql import SCHEMA
from onefeed.retriever.db import get_db
from onefeed.retriever import fetch_job


def crawler_func(spider, settings):
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(spider)
    crawler_process.start()


def test_github_crawler():
    temp_db = tempfile.mktemp()
    db = get_db(temp_db)
    db.executescript(SCHEMA)
    db.commit()

    os.environ['SCRAPY_SETTINGS_MODULE'] = 'onefeed.retriever.github.settings'
    settings = get_project_settings()
    settings['DB'] = temp_db

    process = Process(target=crawler_func, args=(TrendingSpider, settings), daemon=True)
    process.start()
    process.join(timeout=5)
    process.terminate()
    assert db.execute("select count(*) cnt from store").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from sync").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from store join sync on store.id = sync.message_id").fetchone()['cnt'] > 10


def test_hackernews_crawler():
    temp_db = tempfile.mktemp()
    db = get_db(temp_db)
    db.executescript(SCHEMA)
    db.commit()

    os.environ['SCRAPY_SETTINGS_MODULE'] = 'onefeed.retriever.hackernews.settings'
    settings = get_project_settings()
    settings['DB'] = temp_db
    process = Process(target=crawler_func, args=(HomepageSpider, settings), daemon=True)
    process.start()
    process.join(timeout=5)
    process.terminate()
    assert db.execute("select count(*) cnt from store").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from sync").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from store join sync on store.id = sync.message_id").fetchone()['cnt'] > 10

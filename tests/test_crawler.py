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
from onefeed.retriever import fetch_once


def crawler_func(spider, settings):
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(spider)
    crawler_process.start()


def test_github_crawler():
    temp_db = tempfile.mktemp()
    db = get_db(temp_db)
    db.executescript(SCHEMA)
    db.commit()

    fetch_once({'github trending': {'DB': temp_db}})
    assert db.execute("select count(*) cnt from store").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from sync").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from store join sync on store.id = sync.message_id").fetchone()['cnt'] > 10


def test_hackernews_crawler():
    temp_db = tempfile.mktemp()
    db = get_db(temp_db)
    db.executescript(SCHEMA)
    db.commit()

    fetch_once({'hackernews homepage': {'DB': temp_db}})
    assert db.execute("select count(*) cnt from store").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from sync").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from store join sync on store.id = sync.message_id").fetchone()['cnt'] > 10


def test_infoq_crawler():
    temp_db = tempfile.mktemp()
    db = get_db(temp_db)
    db.executescript(SCHEMA)
    db.commit()

    fetch_once({'infoq_articles': {'DB': temp_db}})
    assert db.execute("select count(*) cnt from store").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from sync").fetchone()['cnt'] > 10
    assert db.execute("select count(*) cnt from store join sync on store.id = sync.message_id").fetchone()['cnt'] > 10

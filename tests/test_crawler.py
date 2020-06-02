# -*- coding: utf-8 -*-

import os
import sqlite3
import tempfile

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from onefeed.retriever.github import TrendingSpider
from onefeed.retriever.sql import CREATE_TABLE


def test_github_crawler():
    temp_db = tempfile.mktemp()
    conn = sqlite3.connect(temp_db)
    conn.execute(CREATE_TABLE)

    os.environ['SCRAPY_SETTINGS_MODULE'] = 'onefeed.retriever.github.settings'
    settings = get_project_settings()
    settings['DB'] = temp_db
    process = CrawlerProcess(settings)
    process.crawl(TrendingSpider)
    process.start()
    assert conn.execute("select count(*) from feeds").fetchone()[0] > 10

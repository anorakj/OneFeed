# -*- coding: utf-8 -*-

import json
import time

from ..db import get_db
from ..sql import INSERT_FEED


class SqlitePipeline:

    def __init__(self, db):
        self.db = db

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.get('DB'))

    def open_spider(self, spider):
        self.conn = get_db(self.db)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        feed_info = json.dumps(dict(item)).encode('utf-8')
        timestamp = int(time.time())
        self.conn.execute(INSERT_FEED, (feed_info, timestamp, timestamp))
        return item

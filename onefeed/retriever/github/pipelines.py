# -*- coding: utf-8 -*-

import json
import time

from ..db import get_db, DB
from ..sql import INSERT_STORE, INSERT_SYNC


class SqlitePipeline:

    def __init__(self, db):
        db = DB if not db else db
        self.db = get_db(db)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        db = settings.get("DB")
        return cls(db)

    def close_spider(self, spider):
        self.db.close()
        print('finish crawling github')

    def process_item(self, item, spider):
        message_info = json.dumps(dict(item)).encode('utf-8')
        timestamp = int(time.time() * 1000)
        cursor = self.db.cursor()
        cursor.execute(INSERT_STORE, (message_info, timestamp, timestamp))
        cursor.execute(INSERT_SYNC, (cursor.lastrowid, timestamp, timestamp))
        self.db.commit()
        return item

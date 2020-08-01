# -*- coding: utf-8 -*-

import json
import time

from ..db import get_db
from ..sql import INSERT_STORE, INSERT_SYNC


class SqlitePipeline:

    def __init__(self):
        self.db = get_db()

    def close_spider(self, spider):
        self.db.close()
        print('finish hackernews')

    def process_item(self, item, spider):
        message_info = json.dumps(dict(item)).encode('utf-8')
        timestamp = int(time.time())
        cursor = self.db.cursor()
        cursor.execute(INSERT_STORE, (message_info, timestamp, timestamp))
        cursor.execute(INSERT_SYNC, (cursor.lastrowid, timestamp, timestamp))
        self.db.commit()
        return item

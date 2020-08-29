# -*- coding: utf-8 -*-

import hashlib
import json
import time

from ..db import get_db, DB
from ..sql import INSERT_STORE, INSERT_SYNC, GET_ID_FROM_LINK


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
        print('finish crawling hackernews')

    def process_item(self, item, spider):
        message_info = json.dumps(dict(item)).encode('utf-8')
        link_md5 = hashlib.md5(item['link'].encode('utf-8')).hexdigest()
        timestamp = int(time.time() * 1000)
        cursor = self.db.cursor()
        cursor.execute(INSERT_STORE, {'message_info': message_info, 'create_time': timestamp,
                                      'update_time': timestamp, 'link_md5': link_md5})
        message_id = cursor.execute(GET_ID_FROM_LINK, (link_md5, )).fetchone()['id']
        cursor.execute(INSERT_SYNC, {'message_id': message_id, 'create_time': timestamp,
                                     'update_time': timestamp})
        self.db.commit()
        return item

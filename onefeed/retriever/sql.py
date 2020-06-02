# -*- coding: utf-8 -*-

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS feeds 
(feed_id INTEGER PRIMARY KEY, feed_info BLOB, create_time INTEGER, update_time INTEGER)"""

INSERT_FEED = """INSERT INTO feeds (feed_info, create_time, update_time) VALUES (?, ?, ?)"""

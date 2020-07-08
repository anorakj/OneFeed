# -*- coding: utf-8 -*-

SCHEMA = """CREATE TABLE IF NOT EXISTS store 
(message_id INTEGER PRIMARY KEY, message_info BLOB, create_time INTEGER, update_time INTEGER);
CREATE TABLE IF NOT EXISTS sync
(message_id INTEGER PRIMARY KEY, create_time INTEGER, update_time INTEGER);"""

INSERT_STORE = """INSERT INTO store(message_id, message_info, create_time, update_time) VALUES (?, ?, ?, ?)"""
INSERT_SYNC = """INSERT INTO sync(message_id, message_info, create_time, update_time) VALUES(?. ?, ?. ?)"""

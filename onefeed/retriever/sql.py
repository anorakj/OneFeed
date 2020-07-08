# -*- coding: utf-8 -*-

SCHEMA = """CREATE TABLE IF NOT EXISTS store 
(id INTEGER PRIMARY KEY AUTOINCREMENT, message_info BLOB, create_time INTEGER, update_time INTEGER);
CREATE TABLE IF NOT EXISTS sync
(id INTEGER PRIMARY KEY AUTOINCREMENT, message_id INTEGER, create_time INTEGER, update_time INTEGER);"""

INSERT_STORE = """INSERT INTO store(message_info, create_time, update_time) VALUES (?, ?, ?)"""
INSERT_SYNC = """INSERT INTO sync(message_id, create_time, update_time) VALUES(?, ?, ?)"""

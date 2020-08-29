# -*- coding: utf-8 -*-

SCHEMA = """CREATE TABLE IF NOT EXISTS store 
(id INTEGER PRIMARY KEY AUTOINCREMENT, message_info BLOB, create_time INTEGER, update_time INTEGER);
ALTER TABLE store ADD COLUMN link_md5 TEXT;
ALTER TABLE store ADD COLUMN is_favorite INTEGER DEFAULT 0;
CREATE UNIQUE INDEX store_link_index 
on store (link_md5);

CREATE TABLE IF NOT EXISTS sync
(id INTEGER PRIMARY KEY AUTOINCREMENT, message_id INTEGER, create_time INTEGER, update_time INTEGER);
CREATE UNIQUE INDEX sync_message_id_index 
on sync (message_id);

CREATE TABLE IF NOT EXISTS favorite 
(id INTEGER PRIMARY KEY AUTOINCREMENT, message_id INTEGER, message_info BLOB, create_time INTEGER, update_time INTEGER);
CREATE UNIQUE INDEX favorite_message_id_index 
on favorite (message_id);
;"""

INSERT_STORE = """INSERT INTO store(message_info, create_time, update_time, link_md5) VALUES (:message_info, :create_time,
                  :update_time, :link_md5) ON CONFLICT(link_md5) DO UPDATE SET message_info=:message_info,
                  update_time=:update_time"""
INSERT_SYNC = """INSERT INTO sync(message_id, create_time, update_time) VALUES(:message_id, :create_time, :update_time)
                 ON CONFLICT(message_id) DO UPDATE SET update_time = :update_time"""

GET_ID_FROM_LINK = """SELECT ID FROM STORE WHERE link_md5 = ?"""

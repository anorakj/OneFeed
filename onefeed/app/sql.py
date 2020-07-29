# -*- coding: utf-8 -*-


GET_MESSAGE = """SELECT store.id, message_info FROM sync JOIN store ON sync.message_id = store.id 
                 WHERE json_extract(store.message_info, '$.source') = ?"""
DELETE_MESSAGE = """ DELETE FROM sync
                     WHERE id NOT IN ( SELECT id FROM sync ORDER BY update_time desc LIMIT ? )"""


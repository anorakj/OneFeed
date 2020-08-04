# -*- coding: utf-8 -*-


GET_MESSAGE = """SELECT store.id, message_info FROM sync JOIN store ON sync.message_id = store.id 
                 WHERE json_extract(store.message_info, '$.source') = ?"""
DELETE_MESSAGE = """ DELETE FROM sync
                     WHERE id  IN ( SELECT id FROM (SELECT sync.id, ROW_NUMBER() OVER(ORDER BY sync.update_time desc) r
                     FROM sync JOIN store ON sync.message_id = store.id 
                     WHERE json_extract(store.message_info, '$.source') = ?) WHERE r > ?) """

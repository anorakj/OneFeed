# -*- coding: utf-8 -*-


GET_MESSAGE = """SELECT store.id, message_info FROM sync JOIN store ON sync.message_id = store.id 
                 WHERE json_extract(store.message_info, '$.source') = ?"""
DELETE_MESSAGE = "DELETE FROM sync where message_id in ({message_ids})"

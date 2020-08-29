# -*- coding: utf-8 -*-


GET_MESSAGE = """SELECT id, message_info, is_favorite FROM (
                 SELECT store.id, sync.update_time, message_info, store.is_favorite FROM sync JOIN store ON sync.message_id = store.id 
                 WHERE json_extract(store.message_info, '$.source') = ? ) t ORDER BY update_time desc
              """

DELETE_MESSAGE = """DELETE FROM sync
                    WHERE id  IN ( SELECT id FROM (SELECT sync.id, ROW_NUMBER() OVER(ORDER BY sync.update_time desc) r
                    FROM sync JOIN store ON sync.message_id = store.id 
                    WHERE json_extract(store.message_info, '$.source') = ?) WHERE r > ?)
                 """

INSERT_FAVORITES = """INSERT INTO favorite(message_id, message_info, create_time, update_time) 
                      SELECT id, message_info, :create_time, :update_time  FROM store WHERE id = :id
                   """

UPDATE_FAVORITES = """UPDATE store SET is_favorite = :is_favorite WHERE id = :message_id;
                   """

GET_FAVORITES = """SELECT id, message_id, message_info FROM favorite ORDER BY update_time desc
                """

DELETE_FAVORITES = """DELETE FROM favorite WHERE message_id = :message_id
                   """

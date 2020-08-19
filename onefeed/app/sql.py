# -*- coding: utf-8 -*-


GET_MESSAGE = """SELECT id, message_info FROM (
                 SELECT store.id, sync.update_time, message_info FROM sync JOIN store ON sync.message_id = store.id 
                 WHERE json_extract(store.message_info, '$.source') = ? ) t ORDER BY update_time desc
              """

DELETE_DUPLICATE = """DELETE FROM sync
                      WHERE id IN ( SELECT id FROM (
                      SELECT ROW_NUMBER() OVER(PARTITION BY json_extract(store.message_info, '$.title') ORDER BY sync.update_time desc) rn,
                      sync.id FROM sync JOIN store ON sync.message_id = store.id 
                      WHERE json_extract(store.message_info, '$.source') = ?) t where rn > 1)
                   """

DELETE_MESSAGE = """DELETE FROM sync
                    WHERE id  IN ( SELECT id FROM (SELECT sync.id, ROW_NUMBER() OVER(ORDER BY sync.update_time desc) r
                    FROM sync JOIN store ON sync.message_id = store.id 
                    WHERE json_extract(store.message_info, '$.source') = ?) WHERE r > ?)
                 """

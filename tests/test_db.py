# -*- coding: utf-8 -*-

import tempfile

from onefeed.retriever.db import init_db, get_db


def test_schema():
    temp_db = tempfile.mktemp()
    init_db(temp_db)
    db = get_db(temp_db)
    assert db.execute("SELECT count(*) as cnt FROM sqlite_master WHERE type='table' AND name='store'").fetchone()['cnt'] == 1
    assert db.execute("SELECT count(*) as cnt FROM sqlite_master WHERE type='table' AND name='sync'").fetchone()['cnt'] == 1

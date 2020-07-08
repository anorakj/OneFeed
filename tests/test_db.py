# -*- coding: utf-8 -*-

import tempfile

from onefeed.retriever.db import init_db, get_db


def test_schema():
    temp_db = tempfile.mktemp()
    init_db(temp_db)
    db = get_db(temp_db)
    assert db.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='store'").fetchone()[0] == 1
    assert db.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='sync'").fetchone()[0] == 1

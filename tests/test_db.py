# -*- coding: utf-8 -*-

import tempfile

from onefeed.retriever.db import init_database, get_conn


def test_db():
    temp_db = tempfile.mktemp()
    init_database(temp_db)
    conn = get_conn(temp_db)
    assert conn.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='feeds'").fetchone()[0] == 1

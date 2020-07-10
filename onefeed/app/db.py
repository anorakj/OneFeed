# -*- coding: utf-8 -*-

import sqlite3

from flask import current_app, g


def get_db(isolation_level='IMMEDIATE'):
    """get sqlite db connection with autocommit

    :param db_path: path of the sqlite database
    :type db_path: str
    :param isolation_level: isolation level of db: DEFERRED, IMMEDIATE, EXCLUSIVE or None
    :type isolation_level: str or None

    :return: db_path connection.
    :rtype: sqlite3.Connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DB'], isolation_level=isolation_level)
        g.db.row_factory = _make_dicts
    return g.db


def _make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))

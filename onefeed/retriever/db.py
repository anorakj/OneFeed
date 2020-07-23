# -*- coding: utf-8 -*-

import sqlite3

from .sql import SCHEMA
from ..config import DB


def init_db(db_path=DB):
    """init sqlite database and create feed table

    :param db_path: path of the sqlite database
    """
    db = get_db(db_path)
    db.executescript(SCHEMA)
    db.commit()
    db.close()
    print('Init onefeed database in {}'.format(db_path))


def get_db(db_path=DB, isolation_level='IMMEDIATE'):
    """get sqlite db connection with autocommit

    :param db_path: path of the sqlite database
    :type db_path: str
    :param isolation_level: isolation level of db: DEFERRED, IMMEDIATE, EXCLUSIVE or None
    :type isolation_level: str or None

    :return: db_path connection.
    :rtype: sqlite3.Connection
    """
    db = sqlite3.connect(db_path, isolation_level=isolation_level)
    db.row_factory = _make_dicts
    return db


def _make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))

# -*- coding: utf-8 -*-

import sqlite3

from .sql import SCHEMA
from ..constants import DB


def init_db(db_path=DB):
    """init sqlite database and create feed table

    :param db_path: path of the sqlite database
    """
    db = get_db(db_path)
    db.executescript(SCHEMA)
    db.close()
    print('Init onefeed database in {}'.format(db_path))


def get_db(db_path=DB):
    """get sqlite db connection with autocommit

    :param db_path: path of the sqlite database
    :type db_path: str

    :return: db_path connection.
    :rtype: sqlite3.Connection
    """
    return sqlite3.connect(db_path, isolation_level=None)

# -*- coding: utf-8 -*-

import sqlite3

from .sql import CREATE_TABLE

DB = 'onefeed_data/onefeed.db'
'''str: default onefeed DB path'''


def init_database(database=DB):
    """init sqlite database and create feed table

    :param database: path of the sqlite database
    """
    with sqlite3.connect(database) as conn:
        conn.execute(CREATE_TABLE)


def get_conn(database=DB):
    """get sqlite db connection with autocommit

    :param database: path of the sqlite database
    :type database: str

    :return: db connection.
    :rtype: sqlite3.Connection
    """
    return sqlite3.connect(database, isolation_level=None)

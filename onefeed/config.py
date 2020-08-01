# -*- coding: utf-8 -*-

from pathlib import Path

ONEFEED_DATA_PATH = '{}/onefeed_data'.format(str(Path.home()))
CUSTOM_CONFIG_PATH = '{}/config'.format(ONEFEED_DATA_PATH)

DB = '{}/onefeed.db'.format(ONEFEED_DATA_PATH)
'''str: default store DB path'''
MAX_FEED_NUM = 50

# -*- coding: utf-8 -*-

import os
import shutil
from .retriever.db import init_database, DB
from .retriever import retriever_settings

ONEFEED_DATA_PATH = '{}/onefeed_data'.format(os.getcwd())
CUSTOM_CONFIG = '{}/config'.format(ONEFEED_DATA_PATH)


def init_config(config_path):
    print('Init custom config in {}'.format(config_path))
    if not os.path.exists(config_path):
        os.mkdir(config_path)
    for name, path in retriever_settings.items():
        shutil.copy(path, os.path.join(config_path, name))


if not os.path.exists(ONEFEED_DATA_PATH):
    os.mkdir(ONEFEED_DATA_PATH)
    init_config(CUSTOM_CONFIG)
    init_database(DB)

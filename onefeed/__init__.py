# -*- coding: utf-8 -*-

import os
import shutil
from .retriever.db import init_db, DB
from .retriever import retriever_settings
from .config import ONEFEED_DATA_PATH, CUSTOM_CONFIG_PATH


def init_config(config_path):
    try:
        os.mkdir(config_path)
        print('Init custom config in {}'.format(config_path))
    except FileExistsError:
        pass
    for name, path in retriever_settings.items():
        if not os.path.exists(os.path.join(config_path, name)):
            shutil.copy(path, os.path.join(config_path, name))
            print('Add {} custom settings'.format(name))


if not os.path.exists(ONEFEED_DATA_PATH):
    os.mkdir(ONEFEED_DATA_PATH)
init_config(CUSTOM_CONFIG_PATH)
if not os.path.exists(DB):
    init_db(DB)

# -*- coding: utf-8 -*-

import os
import shutil
from .retriever.db import init_db, DB
from .retriever import retriever_settings
from .config import ONEFEED_DATA_PATH, CUSTOM_CONFIG_PATH


def init_config(config_path):
    print('Init custom config in {}'.format(config_path))
    os.mkdir(config_path)
    for name, path in retriever_settings.items():
        shutil.copy(path, os.path.join(config_path, name))


if not os.path.exists(ONEFEED_DATA_PATH):
    os.mkdir(ONEFEED_DATA_PATH)
if not os.path.exists(CUSTOM_CONFIG_PATH):
    init_config(CUSTOM_CONFIG_PATH)
if not os.path.exists(DB):
    init_db(DB)

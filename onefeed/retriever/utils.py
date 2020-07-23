# -*- coding: utf-8 -*-

import os
import sys

from importlib import import_module
import pkgutil

from onefeed.config import CUSTOM_CONFIG_PATH


def get_spiders():
    """get all spiders in the retriever and their custom settings

    :return: a dict whose key is spider module and value is custom setting dict
    :rtype: dict
    """
    spider_settings = {}
    for module in pkgutil.walk_packages([os.path.dirname(__file__)], prefix='onefeed.retriever.'):
        if module.name.endswith('spiders'):
            setting_file = os.path.join(CUSTOM_CONFIG_PATH, module.name.replace('spiders', 'settings'))
            setting = {}
            with open(setting_file, 'r') as f:
                exec(f.read(), setting)
            import_module(module.name)
            for spider in pkgutil.iter_modules(sys.modules[module.name].__path__, module.name + '.'):
                spider_class = spider.name.split('.')[-1].capitalize() + 'Spider'
                spider_module = import_module(spider.name)
                spider_settings[getattr(spider_module, spider_class)] = setting
    return spider_settings


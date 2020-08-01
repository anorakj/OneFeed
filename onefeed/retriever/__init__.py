# -*- coding: utf-8 -*-

from importlib import import_module
import pkgutil

from .retriever import fetch_once

retriever_settings = {}
for module in pkgutil.walk_packages(__path__, prefix='onefeed.retriever.'):
    if module.name.endswith('settings'):
        imported_module = import_module(module.name)
        retriever_settings[module.name] = imported_module.__file__

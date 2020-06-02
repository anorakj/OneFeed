# -*- coding: utf-8 -*-

import os
from .db import init_database

if not os.path.exists('./onefeed_data'):
    os.mkdir('./onefeed_data')
    init_database()

# -*- coding: utf-8 -*-

import csv
import os

from flask import Flask
from flask import jsonify
from flask import render_template

from onefeed import config


def create_app():
    basedir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__, template_folder="{}/templates".format(basedir), static_folder="{}/static".format(basedir), static_url_path='')
    app.config.from_object(config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/items/github', methods=['GET', 'POST'])
    def get_github_items():
        github_items = []
        with open('{}/github_items.csv'.format(app.config['DATA_PATH'])) as f:
            r = csv.reader(f)
            for row in r:
                github_items.append({
                    'repository': row[0],
                    'description': row[1],
                    'star': row[2],
                    'language': row[3],
                })
        return jsonify(github_items[1:])

    return app

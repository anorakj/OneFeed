# -*- coding: utf-8 -*-

import os

from flask import Flask, g

from .blueprints import blueprints
from onefeed import config


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def create_app():
    basedir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__, template_folder="{}/templates".format(basedir), static_folder="{}/static".format(basedir),
                static_url_path='')
    app.config.from_object(config)
    register_blueprints(app)
    return app


app = create_app()


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.commit()
        db.close()

# -*- coding: utf-8 -*-

import json

from flask import Blueprint, current_app, jsonify

from ..db import get_db
from ...retriever import fetch_once
from ..sql import GET_MESSAGE, DELETE_MESSAGE, DELETE_DUPLICATE

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/items/github', methods=['GET', 'POST'])
def get_github_items():
    items = []
    db = get_db()
    db.execute(DELETE_DUPLICATE, ('github_trending', ))
    db.execute(DELETE_MESSAGE, ('github_trending', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('github_trending',)).fetchall()
    for result in results:
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'repository': message['repository'],
            'description': message['description'],
            'star': message['star'],
            'language': message['language'],
        })
    return jsonify(items)


@api.route('/items/hackernews', methods=['GET', 'POST'])
def get_hackernews_items():
    items = []
    db = get_db()
    db.execute(DELETE_DUPLICATE, ('hackernews_homepage', ))
    db.execute(DELETE_MESSAGE, ('hackernews_homepage', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('hackernews_homepage',)).fetchall()
    for result in results:
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'title': message['title'],
            'points': message['points'],
            'comments': message['comments'],
            'link': message['link'],
        })
    return jsonify(items)


@api.route('/items/infoq', methods=['GET', 'POST'])
def get_infoq_items():
    items = []
    db = get_db()
    db.execute(DELETE_DUPLICATE, ('infoq_articles', ))
    db.execute(DELETE_MESSAGE, ('infoq_articles', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('infoq_articles',)).fetchall()
    for result in results:
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'title': message['title'],
            'description': message['description'],
            'link': message['link'],
        })
    return jsonify(items)


@api.route('/crawler/fetch', methods=['POST'])
def fetch():
    fetch_once()
    return jsonify({})

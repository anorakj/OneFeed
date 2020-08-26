# -*- coding: utf-8 -*-
import time
import json

from flask import Blueprint, current_app, jsonify, request

from ..db import get_db
from ...retriever import fetch_once
from ..sql import GET_MESSAGE, DELETE_MESSAGE, DELETE_DUPLICATE, INSERT_FAVORITES, GET_FAVORITES

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/favorites/item/id', methods=['POST'])
def add_to_favorites():
    id = request.json['id']
    ts = int(time.time())
    db = get_db()
    db.execute(INSERT_FAVORITES, (ts, ts, id,))
    return jsonify({})


@api.route('/favorites/items', methods=['GET'])
def get_favorites():
    db = get_db()
    results = db.execute(GET_FAVORITES)
    items = []
    for result in results:
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'title': message['title'],
            'link': message.get('link', ''),
        })
    return jsonify(items)


@api.route('/items/github', methods=['GET', 'POST'])
def get_github_items():
    items = []
    db = get_db()
    db.execute(DELETE_DUPLICATE, ('github_trending',))
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
            'link': message.get('link', ''),
        })
    return jsonify(items)


@api.route('/items/hackernews', methods=['GET', 'POST'])
def get_hackernews_items():
    items = []
    db = get_db()
    db.execute(DELETE_DUPLICATE, ('hackernews_homepage',))
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
    db.execute(DELETE_DUPLICATE, ('infoq_articles',))
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

# -*- coding: utf-8 -*-

import json

from flask import Blueprint, jsonify

from ..db import get_db
from ..sql import GET_MESSAGE, DELETE_MESSAGE

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/items/github', methods=['GET', 'POST'])
def get_github_items():
    items = []
    db = get_db()
    results = db.execute(GET_MESSAGE, ('github_trending',)).fetchall()
    for result in results:
        print(result)
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'repository': message['repository'],
            'description': message['description'],
            'star': message['star'],
            'language': message['language'],
        })
    ids = [str(v['id']) for v in items]
    db.execute(DELETE_MESSAGE.format(message_ids=','.join(ids)))
    return jsonify(items)


@api.route('/items/hackernews', methods=['GET', 'POST'])
def get_hackernews_items():
    items = []
    db = get_db()
    results = db.execute(GET_MESSAGE, ('hackernews_homepage',)).fetchall()
    for result in results:
        print(result)
        message, id = json.loads(result['message_info']), result['id']
        items.append({
            'id': id,
            'title': message['title'],
            'points': message['points'],
            'comments': message['comments'],
            'source_website': message['source_website'],
        })
    ids = [str(v['id']) for v in items]
    db.execute(DELETE_MESSAGE.format(message_ids=','.join(ids)))
    return jsonify(items)

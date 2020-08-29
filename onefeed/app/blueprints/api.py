# -*- coding: utf-8 -*-
import time
import json

from flask import Blueprint, current_app, jsonify, request

from ..db import get_db
from ...retriever import fetch_once
from ..sql import GET_MESSAGE, DELETE_MESSAGE, INSERT_FAVORITES, GET_FAVORITES, UPDATE_FAVORITES, DELETE_FAVORITES

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/favorites/item/id', methods=['POST'])
def add_to_favorites():
    message_id = request.json['message_id']
    ts = int(time.time())
    db = get_db()
    db.execute(INSERT_FAVORITES, {'create_time': ts, 'update_time': ts, 'id': message_id})
    db.execute(UPDATE_FAVORITES, {'message_id': message_id, 'is_favorite': 1})
    return jsonify({})


@api.route('/favorites/item/delete', methods=['POST'])
def delete_favorites():
    message_id = request.json['message_id']
    db = get_db()
    db.execute(DELETE_FAVORITES, {'message_id': message_id})
    db.execute(UPDATE_FAVORITES, {'message_id': message_id, 'is_favorite': 0})
    return jsonify({})


@api.route('/favorites/items', methods=['GET'])
def get_favorites():
    db = get_db()
    results = db.execute(GET_FAVORITES)
    items = []
    for result in results:
        id, message, message_id = result['id'], json.loads(result['message_info']), result['message_id']
        items.append({
            'message_id': message_id,
            'title': message['title'],
            'link': message.get('link', ''),
            'source': message.get('source', ''),
        })
    return jsonify(items)


@api.route('/items/github', methods=['GET', 'POST'])
def get_github_items():
    items = []
    db = get_db()
    db.execute(DELETE_MESSAGE, ('github_trending', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('github_trending',)).fetchall()
    for result in results:
        message, id, is_favorite = json.loads(result['message_info']), result['id'], result['is_favorite']
        items.append({
            'message_id': id,
            'repository': message['repository'],
            'description': message['description'],
            'star': message['star'],
            'language': message['language'],
            'link': message.get('link', ''),
            'is_favorite': is_favorite,
        })
    return jsonify(items)


@api.route('/items/hackernews', methods=['GET', 'POST'])
def get_hackernews_items():
    items = []
    db = get_db()
    db.execute(DELETE_MESSAGE, ('hackernews_homepage', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('hackernews_homepage',)).fetchall()
    for result in results:
        message, id, is_favorite = json.loads(result['message_info']), result['id'], result['is_favorite']
        items.append({
            'message_id': id,
            'title': message['title'],
            'points': message['points'],
            'comments': message['comments'],
            'link': message['link'],
            'is_favorite': is_favorite,
        })
    return jsonify(items)


@api.route('/items/infoq', methods=['GET', 'POST'])
def get_infoq_items():
    items = []
    db = get_db()
    db.execute(DELETE_MESSAGE, ('infoq_articles', current_app.config['MAX_FEED_NUM'],))
    results = db.execute(GET_MESSAGE, ('infoq_articles',)).fetchall()
    for result in results:
        message, id, is_favorite = json.loads(result['message_info']), result['id'], result['is_favorite']
        items.append({
            'message_id': id,
            'title': message['title'],
            'description': message['description'],
            'link': message['link'],
            'is_favorite': is_favorite,
        })
    return jsonify(items)


@api.route('/crawler/fetch', methods=['POST'])
def fetch():
    fetch_once()
    return jsonify({})

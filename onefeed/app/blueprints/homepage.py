# -*- coding: utf-8 -*-


from flask import Blueprint, render_template

homepage = Blueprint('index', __name__)


@homepage.route('/', defaults={'subpath': ''})
@homepage.route('/tech-news/<path:subpath>')
def index(subpath):
    return render_template('index.html')

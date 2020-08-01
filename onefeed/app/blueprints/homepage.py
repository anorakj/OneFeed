# -*- coding: utf-8 -*-


from flask import Blueprint, render_template

homepage = Blueprint('index', __name__)


@homepage.route('/', defaults={'path': '', 'subpath': ''})
@homepage.route('/<path:path>/<path:subpath>')
def index(path, subpath):
    return render_template('index.html')

# -*- coding: utf-8 -*-


from flask import Blueprint, render_template

homepage = Blueprint('index', __name__)


@homepage.route('/')
def index():
    return render_template('index.html')

# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def home():
    return render_template('index.html', **locals())

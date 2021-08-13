# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('audit', __name__, url_prefix='/audit', static_folder='static')


@bp.route('/', methods=['GET'])
def list_audits():
    if request.method == 'GET':
        return render_template('audit.html', **locals())
    else:
        data = request.json
        return jsonify({'hello': 1}), 200

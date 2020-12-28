# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('reqs', __name__, url_prefix='/reqs')


@bp.route('/', methods=['GET', 'POST'])
def deal_reqs():
    if request.method == 'GET':
        return render_template('reqs/req.html', **locals())
    else:
        data = request.json
        print(data)
        return jsonify({'hello': 1}), 200

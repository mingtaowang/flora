# -*- coding: utf-8 -*-
import json

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('audit', __name__, url_prefix='/', static_folder='static')


@bp.route('/audit/', methods=['GET', 'POST'])
def list_audits():
    if request.method == 'GET':
        return render_template('audit/audit.html', img_src='static/images/strawberry.jpeg')
    else:
        data = request.json
        print(data)
        return jsonify({'msg': 'success'}), 200


@bp.route('/audit_via/', methods=['GET', 'POST'])
def list_via_audits():
    if request.method == 'GET':
        return render_template('via/via.html')
    else:
        data = request.json
        print(data)
        return jsonify({'msg': 'success'}), 200


@bp.route('/audit/back/', methods=['GET'])
def list_audited():
    data = {'notes': 'not beauty', 'defect': 'Green', 'x': 538, 'y': 106, 'w': 290, 'h': 393}
    return render_template('audit/back.html', img_src='http://127.0.0.1:8000/strawberry.jpeg', **data)


@bp.route('/audit/backs/', methods=['GET'])
def list_audited_photos():
    data = {
        "info": [
            {'notes': 'not beauty', 'defect': 'Size', 'x': 153, 'y': 77, 'w': 81, 'h': 93},
            {'notes': 'd', 'defect': 'Shape', 'x': 309, 'y': 49, 'w': 87, 'h': 120}
        ]
    }
    return render_template('audit/photo_back.html', img_src='http://127.0.0.1:8000/strawberry.jpeg', **data)

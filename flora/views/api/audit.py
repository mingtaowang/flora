# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('audit', __name__, url_prefix='/', static_folder='static')


@bp.route('/audit', methods=['GET', 'POST'])
def list_audits():
    if request.method == 'GET':
        return render_template('audit/audit.html', img_src='static/images/strawberry.jpeg')
    else:
        data = request.json
        print(data)
        return jsonify({'msg': 'success'}), 200


@bp.route('/audit_via', methods=['GET', 'POST'])
def list_via_audits():
    if request.method == 'GET':
        return render_template('via/via.html')
    else:
        data = request.json
        print(data)
        return jsonify({'msg': 'success'}), 200


@bp.route('/audit/back', methods=['GET'])
def list_audited():
    data = {'notes': 'not beauty', 'defect': 'Shape', 'x': 167, 'y': 80, 'w': 234, 'h': 133}
    return render_template('audit/back.html', img_src='http://127.0.0.1:8000/strawberry.jpeg', **data)

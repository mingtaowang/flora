# -*- coding: utf-8 -*-

from celery import Celery
from flask import Blueprint, render_template, request, jsonify

from flora.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_ACCEPT_CONTENT, CELERY_TASK_SERIALIZER, \
    CELERY_RESULT_SERIALIZER

bp = Blueprint('reqs', __name__, url_prefix='/reqs')


celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
celery.conf.update(CELERY_ACCEPT_CONTENT=CELERY_ACCEPT_CONTENT, CELERY_TASK_SERIALIZER=CELERY_TASK_SERIALIZER,
                   CELERY_RESULT_SERIALIZER=CELERY_RESULT_SERIALIZER)


@bp.route('/', methods=['GET', 'POST'])
def deal_reqs():
    if request.method == 'GET':
        return render_template('reqs/req.html', **locals())
    else:
        data = request.json
        # 模拟遠程調用
        celery.send_task('tasks.add', kwargs={'name': 'wmt1', 'password': 123456})
        return jsonify({'hello': 1}), 200

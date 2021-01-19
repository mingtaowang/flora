# -*- coding: utf-8 -*-

from flask import Flask
from celery import Celery

from flora import config
from flora.libs.db.store import init_mysql
from flora.service.insert_user import insert_one


def create_celery_app(config=None):
    app = Flask(__name__)
    app.config.from_object('flora.config')
    app.config.from_object(config)
    init_mysql(app)
    return app


def make_celery(app):
    celery = Celery(
        "task",
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"]
    )
    celery.conf.update(CELERY_ACCEPT_CONTENT=app.config['CELERY_ACCEPT_CONTENT'],
                       CELERY_TASK_SERIALIZER="json",
                       CELERY_RESULT_SERIALIZER="json")

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = create_celery_app()
celery = make_celery(app)


@celery.task(name='tasks.add')
def add(*args, **kwargs):
    name = kwargs.get('name')
    password = kwargs.get('password')
    insert_one(name, password)

# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import import_string

blueprints = [
    'flora.views.home:bp',
    'flora.views.reqs.reqs:bp',
    'flora.views.api.audit:bp',
]


def create_app(config=None):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object('flora.config')
    app.config.from_object(config)

    for blueprint in blueprints:
        blueprint = import_string(blueprint)
        app.register_blueprint(blueprint)
    return app

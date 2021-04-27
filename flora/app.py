# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

from flora.views.home import bp as bp_home
from flora.views.reqs.reqs import bp as bp_reqs


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_reqs)
    return app

# -*- coding: utf-8 -*-

from settings import CONFIG
from flora.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host=CONFIG.http_host, port=CONFIG.http_port, debug=CONFIG.debug)

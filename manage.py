# -*- coding: utf-8 -*-
import os

from flask import send_from_directory

from flora.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run()

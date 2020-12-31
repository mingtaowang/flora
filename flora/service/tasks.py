# -*- coding: utf-8 -*-

import time

from celery import Celery

celery = Celery("tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")


@celery.task
def send_main():
    print('邮件开始发送...')
    time.sleep(2)
    print('邮件发送结束...')

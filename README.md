celery启动命令

1、目录切换到flora/service/
2、celery -A tasks.celery --pool=eventlet worker --loglevel INFO
3、运行同级别目录下的main.py

## 1、master分支
    实现了flask基础功能，接口调通，get和post请求调通，连接了一个基础的redis本地数据库
    
## 2、celery分支
    2.1 celery -A tasks.celery --pool=eventlet worker --concurrency=6 --loglevel=INFO
    2.2 实现了celery启动的远程调用

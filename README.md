## master分支
    实现了flask基础功能，接口调通，get和post请求调通，连接了一个基础的redis本地数据库
## 实现的功能
    flask封装成win32服务，windows下可执行的exe文件
## base
    python3.6.3
## 注意事项
    -p命令指定虚拟环境目录
## 测试
    python service.py install
    python service.py debug
## 打包
    pyinstaller -F -p D:/env_f/Lib/site-packages --hidden-import=win32timezone service.py --version-file file_version_info.txt
    cd dist
    将config.conf文件拷贝到service.exe同级目录下
    service.exe install
    service.exe debug
## python直接flask接口测试功能
    python manage.py
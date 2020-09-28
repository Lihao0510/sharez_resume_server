## 中后台搭建系统服务端

### 1. 项目开发

使用python3配合虚拟环境进行开发
```shell script
python3 -m venv venv

source venv/bin/activate

pip3 install flask_script flask_migrate flask flask_sqlalchemy pymysql flask-jwt-extended flask_cors

# 如果已经导出requirements.txt

pip install -r requirements.txt
```

运行服务
gunicorn -w 2 -b 127.0.0.1:4003 server:app

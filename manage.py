from flask_script import Manager
from server import app
from flask_migrate import Migrate, MigrateCommand
from app.model import db

manage = Manager(app)
migrate = Migrate(app, db)

# 增加数据库升降级命令
manage.add_command('db', MigrateCommand)


@manage.command
def start(*args, **kwargs):
    print('开发模式即将启动 ==>', args, kwargs)
    app.run()


@manage.command
def debug(*args, **kwargs):
    print('调试模式即将启动 ==>', args, kwargs)
    app.run(debug=True)


if __name__ == '__main__':
    manage.run()

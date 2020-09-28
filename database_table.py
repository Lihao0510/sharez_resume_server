# 记录程序中用到的所有表, 使用Migrate进行更新
from app.model.user import User


def get_tables():
    print('表加载完成 ==>', User)

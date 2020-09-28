from ..model.user import User
from ..model import db
from flask import jsonify
from flask_jwt_extended import create_access_token


# 获取Token
def get_token_by_password(query_data):
    if query_data['username'] == 'yiautos' and query_data['password'] == '123456':
        token = create_access_token(identity='yiautos_service')
        return jsonify({
            'token': token
        })
    else:
        return jsonify({
            'msg': '用户名或密码错误!'
        }), 401


# def create_user():
#     new_user = User(name='Lihao', mobile='17786123214', password='123456', level=1)
#     db.session.add(new_user)
#     db.session.commit()
#     return


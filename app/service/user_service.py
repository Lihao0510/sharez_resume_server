from ..model.user import User
from ..model import db
from flask_jwt_extended import create_access_token
import traceback
import datetime
from ..utils.response_body import build_success_body, build_error_body


# 根据openid获取token
def get_token_by_open_id(open_id):
    try:
        '''
        通过openid登录, 如果此openid没有登录过, 那么会创建一条记录
        '''
        user_record = User.query.filter(User.open_id == open_id).first()
        print('查询到的用户信息 ==>', user_record)
        if user_record is None:
            # 如果数据库中没有此用户, 则先执行创建逻辑
            wait_create_user = User()
            wait_create_user.open_id = open_id
            db.session.add(wait_create_user)
            db.session.flush()
            print('新增用户的Id ==>', wait_create_user.id)
            db.session.commit()
            user_record = wait_create_user
        user_record_dict = {
            'id': user_record.id,
            'open_id': user_record.open_id,
        }
        token = create_access_token(identity=user_record_dict)
        response_body = {
            'token': token,
            'open_id': user_record.open_id,
            'user_id': user_record.id,
        }
        return build_success_body(response_body)
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return build_error_body(e)


# 根据当前登录的用户获取用户详细信息
def get_user_detail(request_user):
    try:
        print('当前请求的用户 ==>', request_user)
        user_info = User.query.get(request_user['id'])
        if user_info is None:
            raise KeyError('没有找到用户信息!')
        return build_success_body(user_info.to_json())
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return build_error_body(e)


# 根据当前登录的用户获取用户详细信息
def complete_user_info(request_user, complete_info):
    try:
        user_info = User.query.get(request_user['id'])
        print('当前即将补充的用户资料 ==>', user_info)
        if user_info is None:
            raise KeyError('没有找到用户信息!')
        '''
        'gender': {'type': 'string'},
        'nick_name': {'type': 'string'},
        'avatar_url': {'type': 'string'},
        'mobile': {'type': 'string'},
        'real_name': {'type': 'string'},
        'level': {'type': 'string'},
        'device_message': {'type': 'string'},
        '''
        if 'gender' in complete_info.keys():
            user_info.gender = complete_info['gender']
        if 'nick_name' in complete_info.keys():
            user_info.nick_name = complete_info['nick_name']
        if 'avatar_url' in complete_info.keys():
            user_info.avatar_url = complete_info['avatar_url']
        if 'mobile' in complete_info.keys():
            user_info.mobile = complete_info['mobile']
        if 'real_name' in complete_info.keys():
            user_info.real_name = complete_info['real_name']
        if 'level' in complete_info.keys():
            user_info.level = complete_info['level']
        if 'device_message' in complete_info.keys():
            user_info.device_message = complete_info['device_message']
        user_info.update_time = datetime.datetime.now()
        db.session.flush()
        db.session.commit()
        return build_success_body(user_info.id)
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return build_error_body(e)

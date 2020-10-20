from ..wechat import wx_api
from ..utils.response_body import build_success_body, build_error_body
from flask_jwt_extended import create_access_token
from sqlalchemy import exc
import traceback
import datetime
from . import user_service


# 小程序快速登录接口, 传入code, 返回openId与access_token
def login_by_openid(query_params):
    try:
        temp_code = query_params['code']
        user_openid = wx_api.exchange_code_for_session_key(code=temp_code)
        '''
        登录步骤:
        根据用户的openId查询用户表, 取出用户信息并创建token返回
        如果是第一次登陆的openId, 则在用户表中新建一条记录, 再创建token
        后续可以使用补充用户信息的接口获取到用户的头像/昵称/电话号码等信息完善
        '''
        user_result = user_service.get_token_by_open_id(user_openid['openid'])
        print('用户服务返回信息 ==>', user_result)
        return user_result
    except Exception as e:
        traceback.print_exc()
        return build_error_body(e)


# 完善用户信息
def accomplish_user_info(query_params):
    try:
        user_open_id = query_params['open_id']
        user_message = query_params['user_message']
        '''
        完善用户信息可以分为完善手机号/完善用户信息
        手机号和用户信息在微信中是不同的权限获取的, 所以不可能一次性完善
        通过传入的参数不同完善不同的参数实现用户信息的完善
        '''
        return build_success_body('')
    except Exception as e:
        traceback.print_exc()
        return build_error_body(e)


# 获取用户tab信息, 包含用户的简历数等基础信息
def get_user_basic_info():
    try:
        return build_success_body('')
    except Exception as e:
        traceback.print_exc()
        return build_error_body(e)

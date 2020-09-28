from flask import Blueprint, request
import json
from ..service import wechat_service
from . import schema
from ..schema.normal import openid_schema


controller = Blueprint('wechat', __name__)


# 使用临时授权码获取当前用户的openId
@controller.route('/login', methods=['POST'])
@schema.validate(openid_schema)
def wechat_login():
    request_data = request.get_data()
    query_data = json.loads(request_data.decode('utf-8'))
    return wechat_service.login_by_openid(query_data)


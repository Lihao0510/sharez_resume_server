from ..wechat import api as wx_api
from ..utils.response_body import build_success_body, build_error_body
from sqlalchemy import exc
import traceback
import datetime


def login_by_openid(query_params):
    try:
        temp_code = query_params['code']
        user_openid = wx_api.exchange_code_for_session_key(code=temp_code)
        return build_success_body(user_openid)
    except Exception as e:
        traceback.print_exc()
        return build_error_body(e)

from flask import Blueprint, request
import json
from ..service import user_service
from . import schema
from ..schema.normal import user_pwd_schema


controller = Blueprint('user', __name__)


@controller.route('/login', methods=['POST'])
@schema.validate(user_pwd_schema)
def user_login():
    request_data = request.get_data()
    query_data = json.loads(request_data.decode('utf-8'))
    return user_service.get_token_by_password(query_data)


@controller.route('/<user_id>', methods=['GET'])
@schema.validate(user_pwd_schema)
def user_init(user_id):
    return {
        'code': 200,
        'data': user_id
    }


@controller.route('/open_id/<temp_code>', methods=['GET'])
def get_open_id(temp_code):
    return

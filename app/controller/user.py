from flask import Blueprint, request
import json
from ..service import user_service
from . import schema
from ..schema.normal import user_complete_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

controller = Blueprint('user', __name__)


@controller.route('/info', methods=['GET'])
@jwt_required
def get_user_detail():
    request_user = get_jwt_identity()
    return user_service.get_user_detail(request_user)


@controller.route('/complete', methods=['POST'])
@jwt_required
@schema.validate(user_complete_schema)
def complete_user_message():
    request_user = get_jwt_identity()
    request_data = request.get_data()
    complete_info = json.loads(request_data.decode('utf-8'))
    return user_service.complete_user_info(request_user, complete_info)

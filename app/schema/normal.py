user_complete_schema = {
    'required': [],
    'properties': {
        'gender': {'type': 'number'},
        'nick_name': {'type': 'string'},
        'avatar_url': {'type': 'string'},
        'mobile': {'type': 'string'},
        'real_name': {'type': 'string'},
        'level': {'type': 'string'},
        'device_message': {'type': 'string'},
    }
}

openid_schema = {
    'required': ['code'],
    'properties': {
        'code': {'type': 'string'},
        'platform': {'type': 'string'}
    }
}

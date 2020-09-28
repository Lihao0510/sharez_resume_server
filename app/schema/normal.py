# 新建模块的参数格式
ocr_screenshot_schema = {
    'required': ['anchor_time', 'image', 'auth', 'icon', 'is_enable', 'module_type'],
    'properties': {
        'anchor_time': {'type': 'string'},
        'name': {'type': 'string'},
        'prop': {'type': 'string'},
        'route': {'type': 'string'},
        'auth': {'type': 'string'},
        'icon': {'type': 'string'},
        'module_type': {'type': 'integer'},
        'is_enable': {'type': 'integer'}
    }
}

user_pwd_schema = {
    'required': ['username', 'password'],
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'}
    }
}

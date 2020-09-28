import json
from datetime import date, datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def build_success_body(response):
    body = {
        'code': 200,
        'data': response,
        'message': 'success'
    }
    return json.dumps(body, cls=DateEncoder, ensure_ascii=False)


def build_error_body(error, description="Server Error: "):
    body = {
        'code': 1002,
        'message': description + "{0}".format(error)
    }
    return json.dumps(body)


def build_manual_error_body(text):
    body = {
        'code': 1003,
        'message': text
    }
    return json.dumps(body)

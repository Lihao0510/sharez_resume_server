from gevent import monkey;monkey.patch_all()
from flask import Flask, jsonify
from app.controller import user, schema
from config import config, env
from app.model import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_json_schema import JsonValidationError
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(user.controller, url_prefix='/user')

# 开发时临时使用开发环境参数
app.config.from_object(config[env])

app.url_map.strict_slashes = False

db.init_app(app)

jwt = JWTManager(app)

schema.init_app(app)

# sentry_sdk.init(
#     dsn="http://78d7bb41f74d40f48fc5a12d97f0818c@sentry.admin.liritian.top/3",
#     integrations=[FlaskIntegration()],
#     traces_sample_rate=1.0
# )


@app.route('/')
def app_init():
    return app.config['APP_NAME'] + '服务启动成功!'


@app.errorhandler(JsonValidationError)
def on_validate_error(e):
    return jsonify(
        {'code': 1001, 'message': '参数校验失败!', 'data': [validation_error.message for validation_error in e.errors]})

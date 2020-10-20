# 当前程序环境 production / development
env = 'development'

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'lihao'
PASSWORD = '55637179q'
HOST = '106.12.81.74'
PORT = '3306'
DATABASE = 'sharez_resume_db'
DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                            PORT,
                                                            DATABASE)


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_RECYCLE = 20
    JWT_SECRET_KEY = 'sharez_user_token_secret'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_REFRESH_TOKEN_EXPIRES = False
    APP_ID = 'wx87808bebcc300a00'
    APP_SECRET = 'f52c85bb05eb63ec65a0c2e36156c1e9'
    WP_APP_ID = 'wx26c94e694ad3bbf8'
    WP_APP_SECRET = 'ef85a0cec21f4cf844332590dedf725d'
    WP_TOKEN = 'sharez_resume_server_token'
    WP_REDIRECT_URI = 'https://sharez.liritian.top'


class DevConfig(BaseConfig):
    APP_NAME = 'SHAREZ_RESUME_SERVER_DEV'


class ProdConfig(DevConfig):
    APP_NAME = 'SHAREZ_RESUME_SERVER'


config = {
    'development': DevConfig,
    'production': ProdConfig
}

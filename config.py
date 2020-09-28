# 当前程序环境 production / development
env = 'development'

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'yiautos_front'
PASSWORD = 'yiautos123456'
HOST = '121.37.11.149'
PORT = '3306'
DATABASE = 'information_procast'
DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                            PORT,
                                                            DATABASE)


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_RECYCLE = 20
    JWT_SECRET_KEY = 'genz_user_token_secret'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_REFRESH_TOKEN_EXPIRES = False


class DevConfig(BaseConfig):
    APP_NAME = 'GENZ_SERVER'


class ProdConfig(DevConfig):
    APP_NAME = 'GENZ_SERVER_PROD'


config = {
    'development': DevConfig,
    'production': ProdConfig
}

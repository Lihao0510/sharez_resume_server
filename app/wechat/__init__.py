from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
from config import config, env

APP_ID = config[env].APP_ID
APP_SECRET = config[env].APP_SECRET

api = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)


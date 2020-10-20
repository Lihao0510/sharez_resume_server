from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
from weixin.client import WeixinMpAPI
from config import config, env

APP_ID = config[env].APP_ID
APP_SECRET = config[env].APP_SECRET
WP_APP_ID = config[env].WP_APP_ID
WP_APP_SECRET = config[env].WP_APP_SECRET
WP_REDIRECT_URI = config[env].WP_REDIRECT_URI

wx_api = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)

# scope = ("snsapi_base",)
# api = WeixinMpAPI(appid=WP_APP_ID,
#                   app_secret=WP_APP_SECRET,
#                   redirect_uri=WP_REDIRECT_URI)
# authorize_url = api.get_authorize_url(scope=scope)
#
# access_token = api.exchange_code_for_access_token(code=code)
#
# api = WeixinMpAPI(access_token=access_token)
#
# user = api.user(openid="openid")

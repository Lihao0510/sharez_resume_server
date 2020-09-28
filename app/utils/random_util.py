import random
import string


# 获取指定位数的随机字符串
def random_str(num):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt

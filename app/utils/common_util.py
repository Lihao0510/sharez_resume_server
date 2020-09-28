import time
import os
from . import random_util


# 获取目标的Id
def get_form_id(item):
    return item['relation_form']


# 过滤可用的项
def filter_enable_item(item):
    if 'enable' in item:
        return item['enable'] != 0
    return True


def generate_rule(field):
    prop = field['prop']
    name = field['name']
    rules_list = []
    for rule in field['rules']:
        # {code: 'required', name: '必填'},
        # {code: 'mobile', name: '手机号'},
        # {code: 'number', name: '数字'},
        # {code: 'price', name: '金额'},
        # {code: 'idcard', name: '身份证号'},
        # {code: 'min_10', name: '大于10个字符'},
        # {code: 'max_50', name: '小于50个字符'}
        if rule == 'required':
            rules_list.append({
                'required': True,
                'message': name + '为必填项!',
                'trigger': 'blur'
            })
        elif rule == 'min_10':
            rules_list.append({
                'min': 10,
                'message': name + '不能少于10个字符!',
                'trigger': 'blur'
            })
        elif rule == 'max_50':
            rules_list.append({
                'max': 50,
                'message': name + '不能多于50个字符!',
                'trigger': 'blur'
            })
    return {
        'prop': prop,
        'rules': rules_list
    }


# 生成代码目录
def generate_dirs():
    time_line = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    dir_name = time_line + '_' + random_util.random_str(8)
    # 生成代码文件夹
    path = os.getcwd() + '/dist/' + dir_name
    if not os.path.exists(path):
        os.makedirs(path)
    tab_path = path + '/Tabs'
    if not os.path.exists(tab_path):
        os.makedirs(tab_path)
    form_path = path + '/Forms'
    if not os.path.exists(form_path):
        os.makedirs(form_path)
    return {
        'path': path,
        'tab_path': tab_path,
        'form_path': form_path,
        'time_line': time_line
    }



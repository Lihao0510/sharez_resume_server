from jinja2 import Environment, PackageLoader

# jinja配置, 为了防止{{}}与Vue中的绑定相冲突, 将关键字符改为{{{}}}
jinja_env = Environment(loader=PackageLoader('templates', 'vue'), variable_start_string='{{{',
                        variable_end_string='}}}')

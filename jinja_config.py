from jinja2 import Environment, PackageLoader

jinja_env = Environment(loader=PackageLoader('templates', 'vue'), variable_start_string='{{{',
                        variable_end_string='}}}')

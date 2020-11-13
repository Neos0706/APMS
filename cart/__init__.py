# 设置App(cart)的中文名
from django.apps import AppConfig
import os
# 修改App在admin后台显示的名称
# default_app_config的值来自app.py的类名
default_app_config = 'cart.IndexConfig'

# 获取当前App的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


#重写类IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = "购物车管理"
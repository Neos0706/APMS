from django.contrib import admin
from .models import *

# Register your models here.
# 自定义ProductAdmin类继承ModelAdmin
# 使用python装饰器将ProductAdmin和模型Product绑定并注册到后台

# 修改title和header
admin.site.site_title = '农产品后台管理系统'
admin.site.site_header = '农产品后台管理系统'



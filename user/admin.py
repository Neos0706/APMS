from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    # 设置显示的字段
    list_display = ['username', 'email', 'mobile', 'qq', 'weChat', 'user_address']
    # 将源码的UserAdmin.fieldsets转换为列表格式
    fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin的fieldsets,添加'mobile','qq','weChat'的信息录入
    fieldsets[1] = (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile', 'qq', 'weChat',
                                                    'user_address')})



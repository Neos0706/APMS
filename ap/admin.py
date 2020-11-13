from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['type_name']     # admin中显示那些属性


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['ap_name', 'ap_number', 'ap_price', 'ap_area', 'ap_mark', ]
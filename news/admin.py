from django.contrib import admin
from .models import News
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = [ 'news_title', 'news_send', 'news_context', 'news_mark', ]
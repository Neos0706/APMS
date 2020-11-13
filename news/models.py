from django.db import models
from user.models import MyUser
# Create your models here.


class News(models.Model):
    news_title = models.CharField('新闻标题', max_length=20)
    news_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='新闻发布人')
    news_context = models.CharField('新闻内容', max_length=200)
    news_mark = models.CharField('新闻备注', max_length=20)

    # 设置返回值
    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = '新闻信息'
        verbose_name_plural = '新闻信息'

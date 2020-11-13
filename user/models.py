from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    qq = models.CharField('qq号码', max_length=16)
    weChat = models.CharField('微信账号', max_length=100)
    mobile = models.CharField('手机账号', max_length=11)
    user_level = models.CharField('用户权限', max_length=20)
    user_mark = models.CharField('用户备注', max_length=20)
    user_book_id = models.CharField('用户订单', max_length=20)
    user_address = models.CharField('地址', max_length=100, default='')
    user_pc = models.CharField('邮编', max_length=6, default='')

    # 设置返回值

    def __str__(self):
        return self.username


class Order(models.Model):
    order_id = models.AutoField('订单序号', primary_key=True)
    order_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='订单用户')
    order_number = models.CharField('订单数量', max_length=20)
    order_price = models.FloatField('订单总价',max_length=20)



from django.db import models

# Create your models here.


class TypeInfo(models.Model):       # index首页商品分类信息
    type_name = models.CharField('类型名称', max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)   # 是否删除,默认不删

    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'


class Product(models.Model):
    ap_name = models.CharField('农产品名称', max_length=50)
    ap_pic = models.ImageField('农产品图片', upload_to='goods', null=True, blank=True)  # 商品图片
    ap_number = models.FloatField('农产品数量', max_length=20)
    ap_price = models.DecimalField('商品价格', max_digits=7, decimal_places=2)  # 总共最多有7位,小数占2位
    ap_unit = models.CharField('商品单位', max_length=20, default='500g')  # 商品的单位
    ap_area = models.CharField('农产品产地', max_length=20)
    ap_mark = models.CharField('农产品备注', max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)
    ap_click = models.IntegerField('点击量')  # 商品点击量,便于排人气
    ap_type = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)  # 商品所属类型

    # 设置返回值
    def __str__(self):
        return self.ap_name

    class Meta:
        # 如只设置verbose_name,在Admin会显示为'农产品信息s'
        verbose_name = '农产品信息'
        verbose_name_plural = '农产品信息'

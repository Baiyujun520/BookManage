from django.db import models

from django.db import models
from tinymce.models import HTMLField


# 富文本编辑器
class GoodInfo(models.Model):
    gcontent = HTMLField(verbose_name='商品详情')

    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


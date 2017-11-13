from django.contrib import admin

# 后台站点注册富文本编辑器
from Book import models


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gcontent']

admin.site.register(models.GoodInfo, GoodsInfoAdmin)

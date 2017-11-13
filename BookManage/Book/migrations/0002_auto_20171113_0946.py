# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookInfo',
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
        migrations.AlterModelTable(
            name='goodinfo',
            table='df_goods',
        ),
    ]

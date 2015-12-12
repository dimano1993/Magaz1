# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0013_auto_20151205_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='user',
        ),
        migrations.AddField(
            model_name='notebook',
            name='description',
            field=models.TextField(verbose_name=
                                   'Описание ноутбука', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notebook',
            name='amount',
            field=models.IntegerField(verbose_name=
                                      'Количество ноутбуков в наличии'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='cost',
            field=models.IntegerField(verbose_name=
                                      'Стоимость ноутбука'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='model',
            field=models.CharField(max_length=100,
                                   verbose_name='Модель ноутбука'),
        ),
        migrations.AlterField(
            model_name='otlojit',
            name='user',
            field=models.TextField(verbose_name=
                                   'Пользователь, заказавший ноутбук'),
        ),
    ]

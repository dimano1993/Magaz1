# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0008_otlojit_konkruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='otlojit',
            name='user',
            field=models.TextField(verbose_name=
                                   django.contrib.auth.models.User,
                                   default=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otlojit',
            name='konkrnote',
            field=models.ForeignKey(verbose_name=
                                    'Заказаная модель ноутбука',
                                    to='basket.notebook'),
        ),
        migrations.AlterField(
            model_name='otlojit',
            name='konkruser',
            field=models.ForeignKey(verbose_name=
                                    'Пользователь, сделавший заказ',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]

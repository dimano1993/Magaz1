# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('basket', '0010_auto_20151203_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otlojit',
            name='zakaz',
            field=
            models.PositiveIntegerField(default=0,
                                        verbose_name='Заказать ноутбуков'),
        ),
    ]

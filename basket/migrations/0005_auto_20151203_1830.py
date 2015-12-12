# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20151202_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otlojit',
            name='zakaz',
            field=models.IntegerField(verbose_name=
                                      'Заказать ноутбуков', default=0),
        ),
    ]

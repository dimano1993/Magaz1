# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0012_otlojit_sostoyanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otlojit',
            name='sostoyanie',
            field=models.CharField(max_length=100, default='В обработке'),
        ),
    ]

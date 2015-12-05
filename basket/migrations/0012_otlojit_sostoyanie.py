# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0011_auto_20151204_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='otlojit',
            name='sostoyanie',
            field=models.CharField(default=7, max_length=100),
            preserve_default=False,
        ),
    ]

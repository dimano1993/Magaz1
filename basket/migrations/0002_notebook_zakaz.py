# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='zakaz',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]

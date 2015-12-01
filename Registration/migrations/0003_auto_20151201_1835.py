# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20151129_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='user',
        ),
        migrations.DeleteModel(
            name='notebook',
        ),
    ]

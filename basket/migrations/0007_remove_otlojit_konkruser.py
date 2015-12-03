# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_otlojit_konkruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otlojit',
            name='konkruser',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20151202_0012'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='otlojit',
            table='otloj',
        ),
    ]

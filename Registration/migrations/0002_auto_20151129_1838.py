# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]

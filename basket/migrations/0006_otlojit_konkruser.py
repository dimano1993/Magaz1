# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0005_auto_20151203_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='otlojit',
            name='konkruser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=7),
            preserve_default=False,
        ),
    ]

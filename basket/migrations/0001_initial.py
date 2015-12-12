# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID',
                                        primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_notebook_zakaz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otlojit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        verbose_name='ID', auto_created=True)),
                ('zakaz', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='zakaz',
        ),
        migrations.AddField(
            model_name='otlojit',
            name='konkrnote',
            field=models.ForeignKey(to='basket.notebook'),
        ),
    ]

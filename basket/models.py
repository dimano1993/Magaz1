# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class notebook(models.Model):
    model = models.CharField(max_length=100)
    cost = models.IntegerField()
    amount = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.model


class Otlojit(models.Model):
    class Meta():
        db_table = 'otloj'
    konkrnote = models.ForeignKey(notebook, verbose_name="Заказаная модель ноутбука")
    konkruser = models.ForeignKey(User, verbose_name="Пользователь, сделавший заказ")
    zakaz = models.PositiveIntegerField(default=0, verbose_name="Заказать ноутбуков")
    user = models.TextField()
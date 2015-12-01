from django.contrib.auth.models import User
from django.db import models


class notebook(models.Model):
    model = models.CharField(max_length=100)
    cost = models.IntegerField()
    amount = models.IntegerField()
    zakaz = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.model
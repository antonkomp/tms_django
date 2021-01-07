from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, default=None)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=1000, default=None)


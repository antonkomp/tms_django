from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    profession = models.CharField(max_length=80)

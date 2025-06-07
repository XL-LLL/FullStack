from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=100)


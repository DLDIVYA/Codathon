from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Thinkis(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    persona = models.CharField(max_length=200, null=True)
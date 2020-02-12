from django.conf import settings
from django.db import models
from django.utils import timezone


class fooddetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(null=True)
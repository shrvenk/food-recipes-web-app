from django.conf import settings
from django.db import models
from django.utils import timezone


class fooddetail(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.FileField(blank=True,null=True)
    
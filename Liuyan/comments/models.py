from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    user = models.CharField(max_length=32)
    comment = models.CharField(max_length=800)
    likes = models.IntegerField()
# Create your models here.

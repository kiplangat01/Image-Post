from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100),
    content = models.ImageField()
    dateposted = models.DateTimeField(default=timezone)

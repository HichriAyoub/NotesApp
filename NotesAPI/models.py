from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    Name = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)

    
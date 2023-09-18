from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
import datetime

class Post(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    image = ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)

class Post2(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    image = ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
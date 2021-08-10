from django.db import models
from datetime import datetime


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateField(blank=True)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    display = models.BooleanField(default=True)
    def __str__(self):
        return self.title
from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=200, blank=True)
    is_alum = models.BooleanField(default=True)
    in_office = models.BooleanField(default=False)
    post = models.CharField(max_length=200, blank=True)
    pass_year = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

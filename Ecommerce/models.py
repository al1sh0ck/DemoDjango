from textwrap import shorten

from django.db import models

# Create your models here.
class ContactPage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

class ShortProd(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')


class ProductsFullDesc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    short_desc = models.CharField(max_length=500)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    depth = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    quality_checking = models.CharField(max_length=100)
    freshness_duration=models.CharField(max_length=100)
    when_packeting=models.CharField(max_length=100)
    each_box_contains=models.CharField(max_length=100)
    long_desc=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='products/')



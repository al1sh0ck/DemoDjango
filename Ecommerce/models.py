from textwrap import shorten

from django.db import models

# Create your models here.
class ContactPage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
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


#class DemoProduct(models.Model):
 #   id = models.AutoField(primary_key=True)
  #  name = models.CharField(max_length=100)
   # price = models.FloatField()
    #category = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='images/')
    #brand = models.CharField(max_length=100)
    #color = models.CharField(max_length=100)
    #short_desc = models.CharField(max_length=250)
    #full_desc = models.CharField(max_length=1000)




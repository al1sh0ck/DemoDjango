from textwrap import shorten

from django.db import models

# Create your models here.
class ContactPage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


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




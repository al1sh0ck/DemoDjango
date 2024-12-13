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
    image = models.ImageField(upload_to='static/img/')


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
    image=models.ImageField(upload_to='static/img/')

class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()
    views = models.IntegerField()
    commentsAmount = models.IntegerField()
    image = models.ImageField(upload_to='static/img/blog/')
class SingleBlogs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()
    views = models.IntegerField()
    commentsAmount = models.IntegerField()
    image = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)
    part1 = models.TextField(null=True, blank=True)
    part2 = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)
    image2 = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)
    image3 = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)
    image4 = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)
    image5 = models.ImageField(upload_to='static/img/blog/', null=True, blank=True)

    def split_tags(self):
        return self.tags.split(',') if self.tags else []

    def __str__(self):
        return self.name


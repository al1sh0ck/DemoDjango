from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactPage, ShortProd, ProductsFullDesc, Blogs, SingleBlogs


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'id')
    search_fields = ('name', 'email', 'subject')
@admin.register(ShortProd)
class ShortProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','id', 'brand','color')
@admin.register(ProductsFullDesc)
class ProductFullDeskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image','brand','color','short_desc', 'width','height','depth','weight','quality_checking','freshness_duration','when_packeting','each_box_contains','long_desc')
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','tags','author','date','views','commentsAmount','image')
@admin.register(SingleBlogs)
class SingleBlogsAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','tags','author','date','views','commentsAmount','image','part1','part2','image1','image2','image3','image4','image5')
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactPage, ShortProd, ProductsFullDesc, Blogs


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'id')
    search_fields = ('name', 'email', 'subject')
@admin.register(ShortProd)
class ShortProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','id')
@admin.register(ProductsFullDesc)
class ProductFullDeskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image','short_desc', 'width','height','depth','weight','quality_checking','freshness_duration','when_packeting','each_box_contains','long_desc')
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','tags','author','date','views','commentsAmount','image')
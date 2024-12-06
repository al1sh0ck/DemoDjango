from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactPage, ShortProd, ProductsFullDesc


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'id')
    search_fields = ('name', 'email', 'subject')
@admin.register(ShortProd)
class ShortProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','id')
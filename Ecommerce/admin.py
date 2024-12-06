from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactPage

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'id')
    search_fields = ('name', 'email', 'subject')
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand_name')
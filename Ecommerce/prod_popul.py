import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DemoDjango.settings')
django.setup()

from Ecommerce.models import ShortProd

products = [
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p1.jpg",
    },
    {
        "id": '2',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p2.jpg",
    },
    {
        "id": '3',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p3.jpg",
    },
    {
        "id": '4',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p4.jpg",
    },
    {
        "id": '5',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p5.jpg",
    },
    {
        "id": '6',
        "name": "addidas New Hammer sole for Sports person",
        "price": 150.00,
        "image": "static/img/product/p6.jpg",
    }
]

for product in products:
    ShortProd.objects.create(**product)
print("Products added successfully!")
from Ecommerce.models import ShortProd

products = [
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p1.jpg",
    },
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p2.jpg",
    },
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p3.jpg",
    },
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p4.jpg",
    },
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p5.jpg",
    },
    {
        "id": '1',
        "name": "addidas New Hammer sole for Sports person",
        "price": '150.00',
        "image": "Ecommerce\static\img\product\p6.jpg",
    }
]

for product in products:
    ShortProd.objects.create(**product)
print("Products added successfully!")
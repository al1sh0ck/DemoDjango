# Generated by Django 5.1.3 on 2024-12-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0006_alter_blogs_image_alter_productsfulldesc_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='static/img/blog/'),
        ),
    ]
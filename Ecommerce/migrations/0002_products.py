# Generated by Django 5.1.3 on 2024-12-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('brand_name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=500)),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('depth', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('quality_checking', models.CharField(max_length=100)),
                ('freshness_duration', models.CharField(max_length=100)),
                ('when_packeting', models.CharField(max_length=100)),
                ('each_box_contains', models.CharField(max_length=100)),
                ('long_desc', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]

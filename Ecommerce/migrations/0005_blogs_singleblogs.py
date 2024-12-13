# Generated by Django 5.1.3 on 2024-12-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0004_remove_productsfulldesc_brand_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tags', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('views', models.IntegerField()),
                ('commentsAmount', models.IntegerField()),
                ('image', models.ImageField(upload_to='blogs/')),
            ],
        ),
        migrations.CreateModel(
            name='SingleBlogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tags', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('views', models.IntegerField()),
                ('commentsAmount', models.IntegerField()),
                ('image', models.ImageField(upload_to='blogs/')),
                ('part1', models.TextField()),
                ('part2', models.TextField()),
                ('image1', models.ImageField(upload_to='blogs/')),
                ('image2', models.ImageField(upload_to='blogs/')),
                ('image3', models.ImageField(upload_to='blogs/')),
                ('image4', models.ImageField(upload_to='blogs/')),
                ('image5', models.ImageField(upload_to='blogs/')),
            ],
        ),
    ]

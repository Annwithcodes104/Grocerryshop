# Generated by Django 5.0.4 on 2024-04-22 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/product')),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=100)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groapp.category')),
            ],
        ),
    ]

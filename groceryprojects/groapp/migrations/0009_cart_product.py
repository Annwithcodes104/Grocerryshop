# Generated by Django 5.0.4 on 2024-05-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groapp', '0008_cart_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.TextField(blank=True, default={'objects': []}, null=True),
        ),
    ]

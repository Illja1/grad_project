# Generated by Django 4.1.7 on 2023-03-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

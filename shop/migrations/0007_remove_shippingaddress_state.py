# Generated by Django 4.1.7 on 2023-03-05 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_furniture_digital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-25 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_customer_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer',
        ),
    ]

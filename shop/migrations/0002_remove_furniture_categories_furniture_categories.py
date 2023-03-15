# Generated by Django 4.1.7 on 2023-03-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='categories',
        ),
        migrations.AddField(
            model_name='furniture',
            name='categories',
            field=models.ManyToManyField(to='shop.category'),
        ),
    ]
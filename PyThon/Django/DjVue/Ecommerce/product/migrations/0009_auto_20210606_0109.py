# Generated by Django 3.1.3 on 2021-06-05 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210606_0108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='toppings',
            new_name='photos',
        ),
    ]
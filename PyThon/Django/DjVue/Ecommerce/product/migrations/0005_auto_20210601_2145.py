# Generated by Django 3.1.3 on 2021-06-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210601_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(null=True, upload_to='products'),
        ),
    ]

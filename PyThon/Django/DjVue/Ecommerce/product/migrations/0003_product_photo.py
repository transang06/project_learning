# Generated by Django 3.1.3 on 2021-06-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210601_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]

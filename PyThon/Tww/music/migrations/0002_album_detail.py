# Generated by Django 3.1.3 on 2020-11-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='detail',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(default='Please Enter a Description'),
        ),
    ]

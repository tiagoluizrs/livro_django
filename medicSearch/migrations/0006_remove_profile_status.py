# Generated by Django 3.0.3 on 2020-05-09 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0005_auto_20200508_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
    ]
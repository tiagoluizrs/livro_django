# Generated by Django 3.0 on 2019-12-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0006_auto_20191226_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='opinion',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-22 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160522_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=1.0),
        ),
    ]

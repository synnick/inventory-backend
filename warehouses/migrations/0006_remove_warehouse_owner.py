# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-24 01:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0005_auto_20160524_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='owner',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-06 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='voucher',
        ),
    ]

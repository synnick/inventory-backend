# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-19 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0003_auto_20160524_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(blank=True, max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uoms', to='companies.Company')),
            ],
            options={
                'verbose_name': 'uom',
                'verbose_name_plural': 'uoms',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-09 05:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('price_per_uom', models.FloatField(default=1.0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.UOM'),
        ),
    ]

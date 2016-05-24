# coding: utf-8
from __future__ import unicode_literals

# DJANGO
from django.db import models

# INVENTORY
from commons.models import Dated
from warehouses.models import Warehouse, WarehouseStock


class Product(Dated):

    created_by = models.ForeignKey(
        'users.User',
        related_name='products')
    description = models.TextField(
        blank=True,
        null=True)
    name = models.CharField(
        blank=False,
        max_length=100,
        null=False)
    price = models.FloatField(
        blank=False,
        default=1.0,
        null=False)
    sales_price = models.FloatField(
        blank=False,
        null=True)

    REQUIRED_FIELDS = [
        'name',
        'price'
    ]

    class Meta:
        permissions = ()
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def init(self):
        for warehouse in Warehouse.objects.filter(
                created_by__company=self.created_by.company):

            WarehouseStock.objects.create(
                warehouse=warehouse,
                product=self,
                quantity=0.0
            )
        self.save()

    def save(self, *args, **kwargs):
        first_time = not self.pk
        product = super(Product, self).save(*args, **kwargs)
        if first_time:
            self.init()
        return product

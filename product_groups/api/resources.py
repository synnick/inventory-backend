# coding: utf-8
from __future__ import unicode_literals

# PYTHON
import math
import time

# TASTYPIE
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest, NotFound
from tastypie import fields

# INVENTORY
from commons.resources import DatedResource
from products.api.resources import ProductResource
from product_groups.models import GroupProduct, ProductGroup
from users.api.resources import UserResource


class GroupProductResource(DatedResource):

    class Meta:
        allowed_methods = ['get']
        authentication = SessionAuthentication()
        excludes = ['deleted_at']
        queryset = GroupProduct.objects.all().order_by('-id')
        resource_name = 'group_products'


class ProductGroupResource(DatedResource):

    products = fields.ListField(readonly=True)
    owner_id = fields.IntegerField()
    total = fields.FloatField(readonly=True)

    class Meta:
        allowed_methods = ['get', 'patch', 'post', 'delete']
        authorization = Authorization()
        authentication = SessionAuthentication()
        excludes = ['deleted_at']
        queryset = ProductGroup.objects.all().order_by('id')
        resource_name = 'product_groups'

    def dehydrate_created_at(self, bundle):
        if bundle.obj.created_at:
            return time.mktime(bundle.obj.created_at.timetuple())

    def full_dehydrate(self, bundle, for_list=False):
        bundle = super(ProductGroupResource, self).full_dehydrate(bundle, for_list=for_list)
        group_products = GroupProduct.objects.filter(group=bundle.obj)
        bundle.data['total'] = round(sum([gp.product.price_per_unit * gp.quantity for gp in group_products]), 6)
        bundle.data['products'] = []
        for gp in group_products:
            bundle.data['products'].append({
                'name': gp.product.name,
                'price': gp.product.price_per_unit,
                'quantity': gp.quantity,
                'resource_uri': '{}/{}/'.format(
                    GroupProductResource().get_resource_uri(),
                    gp.id)
            })
        return bundle

    def dehydrate_updated_at(self, bundle):
        if bundle.obj.updated_at:
            return time.mktime(bundle.obj.updated_at.timetuple())

    def hydrate_owner_id(self, bundle):
        bundle.obj.owner_id = bundle.request.user.company_id
        return bundle

    def obj_create(self, bundle, **kwargs):
        products = bundle.data.get('products', [])
        bundle = super(ProductGroupResource, self).obj_create(bundle, **kwargs)
        for product in products:
            product_uri, product_quantity = product.get('resource_uri'), product.get('quantity')
            product_obj = ProductResource().get_via_uri(product_uri, bundle.request)
            GroupProduct.objects.create(
                group=bundle.obj,
                product=product_obj,
                quantity=int(product_quantity))
        return bundle

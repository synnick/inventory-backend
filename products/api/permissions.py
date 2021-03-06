# coding: utf-8
from __future__ import unicode_literals

# TASTYPIE
from tastypie.authorization import Authorization


class ProductAuthorization(Authorization):

    def delete_detail(self, object_list, bundle):
      return bundle.obj.owner == bundle.request.user.company

    def update_list(self, object_list, bundle):
        return False

    def delete_list(self, object_list, bundle):
        return False

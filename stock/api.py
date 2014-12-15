from tastypie.resources import ModelResource, ALL
from stock.models import Product


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.filter(in_stock=False)
        excludes = ['id',]
        filtering = {
            'retail_code': ALL,
            'material_code': ALL,
        }

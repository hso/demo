from tastypie.resources import ModelResource
from stock.models import Product


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.filter(in_stock=False)

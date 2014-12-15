from django.db import models


class Product(models.Model):
    retail_code = models.CharField(max_length=4)
    material_code = models.CharField(max_length=9)
    description = models.CharField(max_length=21)
    in_stock = models.BooleanField(default=False)
    internal_code = models.CharField(max_length=5)

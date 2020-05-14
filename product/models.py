from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def stock_balance(self, name):
        return super().get_queryset().filter(name=name, is_not_sold=True).count()


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True, blank=False, null=False)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='products')
    is_allowed = models.BooleanField(default=True)
    is_not_sold = models.BooleanField(default=True)
    objects = ProductManager()

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

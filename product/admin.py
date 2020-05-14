from django.contrib import admin

from .models import Product, ProductGroup


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'product_group')
    list_filter = ('name',)
    search_fields = ('sku', 'name')


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

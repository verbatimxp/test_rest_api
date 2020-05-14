from rest_framework import serializers

from .models import Product, ProductGroup


class ProductSerializer(serializers.ModelSerializer):
    same_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'sku',
            'product_group',
            'same_count',
            'is_allowed',
            'is_not_sold',
        ]

    def get_same_count(self, obj):
        """
        Counts the number of products by name
        """
        return Product.objects.stock_balance(name=obj.name)


class ProductGroupBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = [
            'id',
            'name',
        ]


class ProductGroupSerializer(ProductGroupBaseSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta(ProductGroupBaseSerializer.Meta):
        fields = ProductGroupBaseSerializer.Meta.fields + [
            'products'
        ]

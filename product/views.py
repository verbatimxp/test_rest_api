from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, ProductGroup
from .serializers import ProductSerializer, ProductGroupSerializer, ProductGroupBaseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_group', 'name', ]

    def get_queryset(self):
        """
        Filters products by flags is_not_sold and is_allowed.
        """
        queryset = self.queryset
        if not self.request.query_params.get('all') == 'True' and self.action == 'list':
            return queryset.filter(is_not_sold=True, is_allowed=True)
        return queryset

    @action(methods=['PATCH'], detail=False)
    def buy_product(self, request):
        """
        Change the amount of residues of a particular product or random
        """
        product_ids = request.data.get('product_ids')
        if product_ids:
            product = Product.objects.filter(id__in=product_ids)
            product.update(is_not_sold=False)
        else:
            product = Product.objects.filter(is_not_sold=True).first()
            product.is_not_sold = False
            product.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['PATCH'], detail=True, url_path='reserve')
    def reservation(self, request, *args, **kwargs):
        """
        Possibility of reservation of goods and cancellation of reservation
        """
        product = self.get_object()
        product.is_allowed = not product.is_allowed
        product.save()
        product_serializer = ProductSerializer(product)
        return Response(data=product_serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def mass_changes(self, request):
        """
        Change multiple product
        """
        model_fields = Product._meta.get_fields()
        fields = list(map(lambda x: str(x).split('.')[-1], model_fields))
        for product_obj in request.data.get('products'):
            product_id = product_obj.get('id')
            product = Product.objects.filter(id__in=[product_id])
            data = product_obj.get('data')
            if product and data:
                product_data = {field: value for field, value in product_obj.get('data').items() if field in fields}
                product.update(**product_data)
        return Response(status=status.HTTP_200_OK)


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return ProductGroupBaseSerializer
        return self.serializer_class

    @action(methods=['GET'], detail=True)
    def products_count(self, request, *args, **kwargs):
        """
        Calculates the number of products in a specific group
        """
        group = self.get_object()
        products_count = group.products.count()
        return Response(data={'count': products_count}, status=status.HTTP_200_OK)

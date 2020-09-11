from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import Product, Kit, KitRelation
from product.serializers import ProductSerializer, KitRetrieveSerializer, KitPostSerializer
from django.db.models import Min, Sum, F

class ProductViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('id', 'name', 'sku', 'price', 'cost', 'stock')


class KitRetrieveViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Kit.objects.all()
    serializer_class = KitRetrieveSerializer
    filterset_fields = ('id', 'name', 'sku')

    @action(detail=True, methods=['get'])
    def get_calc(self, request, pk=None):
        kit = self.get_object()

        return Response(
            {
                'name': kit.name,
                'sku': kit.sku,
                'price': KitRelation.objects.filter(kit=kit).aggregate(
                    price=Sum(F('product__cost') * (1 - F('discount')))
                ).get('price'),
                'cost': kit.products.aggregate(sum=Sum('cost')).get('sum'),
                'stock': KitRelation.objects.filter(kit=kit).aggregate(
                    stock=Min(F('product__stock')/F('amount'))
                ).get('stock'),
            }
        )


class KitPostViewset(viewsets.ViewSet):

    serializer_class = KitPostSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers={})

    def update(self, request, pk=None):
        instance = Kit.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        instance = Kit.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)





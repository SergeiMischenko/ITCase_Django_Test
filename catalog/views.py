from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductListView(ListAPIView):
    queryset = Product.objects.select_related().prefetch_related('images', 'parameters')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.select_related().prefetch_related('images', 'parameters')
    serializer_class = ProductSerializer

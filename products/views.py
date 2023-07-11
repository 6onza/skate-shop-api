from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BaseAuthentication
from django.conf import settings

class CustomPagination(PageNumberPagination):
    page_size = 8


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter]
    sort_by_fields = ['price', 'created_at']
    sort_by = '-created_at'  # Default ordering
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = Product.objects.all()

        categories = self.request.query_params.get('categories')
        sort_by = self.request.query_params.get('sort_by')

        if categories == 'all':
            return queryset

        if categories:
            category_list = categories.split(',')  # Obtener una lista de categorías separadas por coma
            queryset = queryset.filter(Q(category__in=category_list))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset

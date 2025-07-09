# products/filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category_name = django_filters.CharFilter(field_name="category__name", lookup_expr='iexact') # Case-insensitive exact match

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'stock_quantity'] # 'category' filter uses ForeignKey ID
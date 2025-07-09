# products/views.py
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsAdminUser, IsSellerUserOrAdmin
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend # Import this
from rest_framework import filters # For SearchFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    # Only Admin users can create, update, delete categories.
    # Anyone authenticated can view, and unauthenticated can also view (due to IsAuthenticatedOrReadOnly).
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser] # Admin for write, all for read


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerUserOrAdmin]
    # --- Ensure these lines are correct ---
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # <--- Make sure OrderingFilter is here!
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'stock_quantity', 'created_at'] # Added 'created_at' for completeness
    ordering = ['name'] # Default ordering, e.g., by name ascending
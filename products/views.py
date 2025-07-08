# products/views.py
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsAdminUser, IsSellerUserOrAdmin, IsCustomerUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly # We set this as default in settings, but good to be explicit
from rest_framework.authentication import TokenAuthentication # Example if you wanted basic token auth, but we're using JWT

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    # Only Admin users can create, update, delete categories.
    # Anyone authenticated can view, and unauthenticated can also view (due to IsAuthenticatedOrReadOnly).
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser] # Admin for write, all for read


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Seller/Admin users can create, update, delete products.
    # Anyone authenticated can view, and unauthenticated can also view.
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerUserOrAdmin] # Seller/Admin for write, all for read
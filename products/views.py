# products/views.py
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly # We set this as default in settings, but good to be explicit
from rest_framework.authentication import TokenAuthentication # Example if you wanted basic token auth, but we're using JWT

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name') # Order categories alphabetically
    serializer_class = CategorySerializer
    # We'll refine permissions in Phase 3, for now allow read/write
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow anyone to read, but only authenticated users to write

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # We'll refine permissions in Phase 3
    permission_classes = [IsAuthenticatedOrReadOnly]
    # For now, let's keep it simple without filtering/searching. We'll add them in Phase 4.
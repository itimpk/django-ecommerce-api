# products/serializers.py
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # Include all fields from the Category model

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    # You can add a custom field for category ID if you want to also allow
    # sending category ID for creation/update
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)


    class Meta:
        model = Product
        fields = '__all__' # Include all fields from the Product model
        # Or explicitly list them:
        # fields = ('id', 'name', 'description', 'price', 'stock_quantity',
        #           'image_urls', 'category', 'category_name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at') # These fields are set automatically

    # You might add validation here if needed
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value
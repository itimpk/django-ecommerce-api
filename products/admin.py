from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    raw_id_fields = ('category',) # Makes category selection easier if you have many

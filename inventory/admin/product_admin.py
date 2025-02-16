from ..models.product_models import Category, Product, ProductImage
from django.contrib.admin import ModelAdmin

class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'created_at']

class ProductAdmin(ModelAdmin):
    list_display = ['sku_code', 'name', 'description', 'price', 'category', 'warehouse', 'created_at', 'updated_at']

    def formatted_category(self, obj):
        return obj.category.name
    formatted_category.short_description = 'Category'

    def formatted_warehouse(self, obj):
        return obj.warehouse.name
    formatted_warehouse.short_description = 'Warehouse'

class ProductImageAdmin(ModelAdmin):
    list_display = ['image', 'product', 'created_at']

    def formatted_product(self, obj):
        return obj.product.name
    formatted_product.short_description = 'Product'
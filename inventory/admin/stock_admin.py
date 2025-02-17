from ..models.stock_models import Stock, StockMovement
from django.contrib.admin import ModelAdmin

class StockAdmin(ModelAdmin):
    list_display = ['product', 'quantity', 'updated_at']
    list_per_page = 20

    def formatted_product(self, obj):
        return obj.product.name
    formatted_product.short_description = 'Product'

class StockMovementAdmin(ModelAdmin):
    list_display = ['stock', 'quantity', 'warehouse', 'movement_type', 'user', 'created_at', 'updated_at']
    list_per_page = 20

    def formatted_stock(self, obj):
        return obj.stock.product.name
    formatted_stock.short_description = 'Product'

    def formatted_movement_type(self, obj):
        return obj.movement_type
    formatted_movement_type.short_description = 'Movement Type'

    def formatted_user(self, obj):
        return obj.user.username
    formatted_user.short_description = 'User'

    def formatted_warehouse(self, obj):
        return obj.warehouse.name
    formatted_warehouse.short_description = 'Warehouse'
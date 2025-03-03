from django.contrib.admin import ModelAdmin

class StockProductAdmin(ModelAdmin):
    list_display = ['product','stock__warehouse','stock__warehouse__warehouse_type', 'batch_no', 'manufacture_date', 'expiry_date', 'quantity']
    ordering_fields = ['product','stock__warehouse','stock__warehouse__warehouse_type','batch_no', 'manufacture_date', 'expiry_date', 'quantity']
    search_fields = ['product__name','stock__slug','stock__warehouse__name','stock__warehouse__warehouse_type__name', 'batch_no', 'manufacture_date', 'expiry_date', 'quantity']
    list_per_page = 100

    def formatted_product(self, obj):
        return obj.product.name
    formatted_product.short_description = 'Product'

    def formatted_stock(self, obj):
        return obj.stock.slug
    formatted_stock.short_description = 'Stock'

# class StockMovementAdmin(ModelAdmin):
#     list_display = ['stock', 'quantity', 'warehouse', 'movement_type', 'user', 'created_at', 'updated_at']
#     ordering = ['stock','quantity','warehouse','movement_type','user', 'created_at', 'updated_at']
#     search_fields = ['stock__slug','quantity','warehouse__name','movement_type','user']
#     list_per_page = 20

#     def formatted_stock(self, obj):
#         return obj.stock.product.name
#     formatted_stock.short_description = 'Product'

#     def formatted_movement_type(self, obj):
#         return obj.movement_type
#     formatted_movement_type.short_description = 'Movement Type'

#     def formatted_user(self, obj):
#         return obj.user.username
#     formatted_user.short_description = 'User'

    # def formatted_warehouse(self, obj):
    #     return obj.warehouse.name
    # formatted_warehouse.short_description = 'Warehouse'
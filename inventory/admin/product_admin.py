from django.contrib.admin import ModelAdmin

class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'created_at']
    ordering = ['name']
    search_fields = ['name']
    list_per_page = 20

class ProductAdmin(ModelAdmin):
    list_display = ['sku_code', 'name', 'description', 'price', 'category', 'warehouse', 'created_at', 'updated_at']
    ordering = ['sku_code','name','price','category','warehouse','created_at','updated_at']
    search_fields = ['sku_code','name','price','category','warehouse__name']
    list_per_page = 20

    def formatted_category(self, obj):
        return obj.category.name
    formatted_category.short_description = 'Category'

    def formatted_warehouse(self, obj):
        return obj.warehouse.name
    formatted_warehouse.short_description = 'Warehouse'

from django.contrib import admin
from .product_admin import CategoryAdmin, ProductAdmin, ProductImageAdmin
from .stock_admin import StockAdmin, StockMovementAdmin
from .warehouse_admin import WarehouseAdmin, WarehouseEmployeeAdmin, WarehouseTypeAdmin
from ..models.product_models import Category, Product, ProductImage
from ..models.stock_models import Stock, StockMovement
from ..models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockMovement, StockMovementAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(WarehouseEmployee, WarehouseEmployeeAdmin)
admin.site.register(WarehouseType, WarehouseTypeAdmin)

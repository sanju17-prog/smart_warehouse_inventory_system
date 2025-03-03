from django.contrib import admin
from .product_admin import CategoryAdmin, ProductAdmin
from .stock_admin import StockProductAdmin
from .warehouse_admin import WarehouseAdmin, WarehouseEmployeeAdmin, WarehouseTypeAdmin
from inventory.models.product_models import Category, Product
from inventory.models.stock_models import Stock, StockProductQty, StockMovement
from inventory.models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from inventory.models.fleet_models import Fleet, FleetMovement
from .fleet_admin import FleetAdmin, FleetMovementAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(StockProductQty, StockProductAdmin)
# admin.site.register(StockMovement, StockMovementAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(WarehouseEmployee, WarehouseEmployeeAdmin)
admin.site.register(WarehouseType, WarehouseTypeAdmin)
admin.site.register(Fleet, FleetAdmin)
admin.site.register(FleetMovement, FleetMovementAdmin)
from django.urls import path, include

urlpatterns = [
    path("fleet/", include("inventory.urls.fleet_urls")),
    path("product/", include("inventory.urls.product_urls")),
    path("stock/", include("inventory.urls.stock_urls")),
    path("warehouse/", include("inventory.urls.warehouse_urls")),
]

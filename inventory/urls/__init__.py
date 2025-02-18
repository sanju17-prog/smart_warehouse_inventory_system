from django.urls import path, include
from .fleet_urls import urlpatterns as fleet_urls
from .product_urls import urlpatterns as product_urls
from .stock_urls import urlpatterns as stock_urls
from .warehouse_urls import urlpatterns as warehouse_urls

# List to collect all URL patterns
urlpatterns = fleet_urls + warehouse_urls + stock_urls + product_urls


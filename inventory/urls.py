from django.urls import path, include
from inventory.urls import urlpatterns as inventory_urls

urlpatterns = [
    path("",include(inventory_urls,'subsets', namespace = 'subsets')),
]

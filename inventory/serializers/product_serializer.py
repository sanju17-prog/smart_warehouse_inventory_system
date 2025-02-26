from inventory.models.fleet_models import Fleet, FleetMovement
from rest_framework import serializers
from inventory.models.product_models import Product

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name = 'products-detail',
        lookup_field = 'slug'
    )




'''
first create stock details fully, 
included - stock viewsets and serializers
then here, link stocks, of all the stocks having this product as fk

'''
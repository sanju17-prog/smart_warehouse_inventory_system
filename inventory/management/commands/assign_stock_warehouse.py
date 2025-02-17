from django.core.management.base import BaseCommand
from inventory.models.warehouse_models import Warehouse
from inventory.models.stock_models import Stock
import random

class Command(BaseCommand):
    help = 'Assigning random warehouses to existing stocks'

    def handle(self, *args, **options):
        stocks = Stock.objects.all()
        warehouses = Warehouse.objects.all()

        for stock in stocks:
            if stock.warehouse is None:
                stock.warehouse = random.choice(warehouses)
                stock.save()
        self.stdout.write("All stocks are assigned with warehouses")
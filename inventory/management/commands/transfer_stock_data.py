from django.core.management.base import BaseCommand
from inventory.models.stock_models import Stock, StockProductQty

class Command(BaseCommand):
    help = 'Transfers stock data to StockProductQty'

    def handle(self, *args, **options):
        for stock in Stock.objects.all():
            StockProductQty.objects.create(
                stock = stock,
                product = stock.product,
                quantity = stock.quantity,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully transferred stock: {stock}'))
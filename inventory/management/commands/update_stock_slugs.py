from django.core.management.base import BaseCommand
from inventory.models.stock_models import Stock

class Command(BaseCommand):
    help = 'Updates the slugs for all existing stock records.'

    def handle(self, *args, **options):
        stocks = Stock.objects.all()
        for stock in stocks:
            stock.slug = stock.generate_unique_slug()
            stock.save()
        self.stdout.write("Successfully updated all stocks slugs!!")
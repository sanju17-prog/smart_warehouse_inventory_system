# Generated by Django 5.1.6 on 2025-02-20 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_remove_stock_product_remove_stock_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockmovement',
            old_name='vehicle',
            new_name='fleet',
        ),
    ]

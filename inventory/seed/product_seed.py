from inventory.models.product_models import Category, Product
from inventory.models.warehouse_models import Warehouse
from faker import Faker
import random
faker = Faker()

CATEGORY_CHOICES = {
    "Industrial Goods & Equipment": {
        "items": ["Compressor", "Drill", "Motor", "Valve", "Gear"],
        "descriptions": [
            "High-performance {} used in heavy industries.",
            "Durable {} for industrial applications.",
            "Advanced {} ensuring efficient operations.",
            "Reliable {} with long service life.",
        ],
    },
    "Perishables & Cold Chain Logistics": {
        "items": ["Fruits", "Vegetables", "Dairy", "Meat", "Seafood"],
        "descriptions": [
            "Fresh {} stored under optimal conditions.",
            "High-quality {} sourced from trusted suppliers.",
            "Temperature-controlled {} for maximum freshness.",
            "Premium-grade {} delivered with safety standards.",
        ],
    },
    "Fuel & Energy Logistics": {
        "items": ["Diesel", "Petrol", "Lubricant", "Battery", "Coal"],
        "descriptions": [
            "Top-grade {} ensuring reliable energy supply.",
            "High-efficiency {} meeting industrial standards.",
            "Premium-quality {} for enhanced performance.",
            "Eco-friendly {} with optimized efficiency.",
        ],
    },
    "Bulk & Containerized Cargo": {
        "items": ["Timber", "Steel", "Cement", "Grain", "Textiles"],
        "descriptions": [
            "High-strength {} used in construction and manufacturing.",
            "Bulk-packed {} ensuring secure transportation.",
            "Superior quality {} for industrial applications.",
            "Well-packaged {} to prevent damage during transit.",
        ],
    },
}

# faker.add_pro

def seed_categories():
    for category_choice in CATEGORY_CHOICES.keys():
        Category.objects.create(
            name = category_choice
        )

def get_unique_sku_code(category, warehouse):
    while True:
        sku_code = f"SKU-{category.name[:3].upper()}-{warehouse.name[:3].upper()}-{random.randint(2000, 2025)}-{faker.random_int(min=100,max=10000)}"
        if not Product.objects.filter(sku_code=sku_code).exists():
            return sku_code
        else:
            print(f"Duplicate SKU code generated: {sku_code}")

def seed_products(n = 1000):
    categories = list(Category.objects.all())
    warehouses = list(Warehouse.objects.all())
    for _ in range(n):
        category = random.choice(categories) # select a random category
        warehouse = random.choice(warehouses) # select a random warehouse

        # select relevant product type and description
        product_name = random.choice(CATEGORY_CHOICES[category.name]["items"]) 
        description_template = random.choice(CATEGORY_CHOICES[category.name]["descriptions"]) 

        # format description with product type
        description = description_template.format(product_name.lower())
        sku_code = get_unique_sku_code(category, warehouse)

        product = Product.objects.create(
            sku_code = sku_code,
            name = product_name,
            description = description,
            price = round(random.uniform(50.0, 5000.0), 2),
            category = category,
            warehouse = warehouse
        )

        product.save()
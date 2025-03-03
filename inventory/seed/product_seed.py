from inventory.models.product_models import Category, Product
from inventory.models.warehouse_models import Warehouse
from django.db import transaction
from faker import Faker
import random
faker = Faker()

CATEGORY_CHOICES = {
    "Industrial Goods & Equipment": {
        "items": [
            {"name": "Compressor", "brands": ["Ingersoll Rand", "Atlas Copco", "Sullair", "Kaeser", "Gardner Denver", "Kirloskar", "Fusheng", "Mitsubishi", "Caterpillar", "Siemens"]},
            {"name": "Drill", "brands": ["Bosch", "Makita", "DeWalt", "Hilti", "Black & Decker", "Milwaukee", "Kobalt", "Ryobi", "Hitachi", "Festool"]},
            {"name": "Motor", "brands": ["Siemens", "ABB", "GE", "Schneider", "Emerson", "Baldor", "Toshiba", "Crompton Greaves", "Weg", "Leroy Somer"]},
            {"name": "Valve", "brands": ["Parker", "Swagelok", "Emerson", "Fisher", "GE", "Cameron", "Schneider", "Metso", "Velan", "Crane"]},
            {"name": "Gear", "brands": ["Nidec", "Bonfiglioli", "Siemens", "Sumitomo", "Brevini", "Leroy Somer", "Nord Drivesystems", "ABB", "Falk", "SPX Flow"]},
        ],
        "descriptions": [
            "High-performance {} used in heavy industries.",
            "Durable {} for industrial applications.",
            "Advanced {} ensuring efficient operations.",
            "Reliable {} with long service life.",
        ],
    },
    "Perishables & Cold Chain Logistics": {
        "items": [
            {"name": "Fruits", "brands": ["Mango", "Apple", "Papaya", "Banana", "Peach", "Pineapple", "Grapes", "Cherries", "Watermelon", "Strawberries"]},
            {"name": "Vegetables", "brands": ["Carrot", "Cucumber", "Tomato", "Spinach", "Onion", "Potato", "Lettuce", "Cabbage", "Broccoli", "Peas"]},
            {"name": "Dairy", "brands": ["Amul", "Mother Dairy", "Nestle", "Parag Milk Foods", "Britannia", "Danone", "Vita", "Kwality", "Havmor", "Gowardhan"]},
            {"name": "Meat", "brands": ["Tyson", "JBS", "Hormel", "Smithfield", "Perdue Farms", "Sanderson Farms", "Dole", "Cargill", "Marfrig", "Mountaire"]},
            {"name": "Seafood", "brands": ["Marine Harvest", "SeaPak", "Thai Union", "Highliner", "Stavis", "Pacific Seafood", "Blue Star", "Clearwater", "Ocean Beauty", "AquaBounty"]},
        ],
        "descriptions": [
            "Fresh {} stored under optimal conditions.",
            "High-quality {} sourced from trusted suppliers.",
            "Temperature-controlled {} for maximum freshness.",
            "Premium-grade {} delivered with safety standards.",
        ],
    },
    "Fuel & Energy Logistics": {
        "items": [
            {"name": "Diesel", "brands": ["Aldo", "ExxonMobil", "Shell", "BP", "Chevron", "Total", "Repsol", "Marathon Petroleum", "Valero", "Phillips 66"]},
            {"name": "Petrol", "brands": ["Aldo", "Shell", "BP", "ExxonMobil", "Chevron", "Total", "Repsol", "Marathon", "Mobil", "Valero"]},
            {"name": "Lubricant", "brands": ["Castrol", "Shell", "Mobil 1", "Valvoline", "Chevron", "Royal Purple", "Liquimoly", "Liqui Moly", "Fuchs", "Kendall"]},
            {"name": "Battery", "brands": ["Duracell", "Energizer", "Panasonic", "Exide", "Amaron", "Bosch", "Varta", "Eveready", "Yuasa", "NorthStar"]},
            {"name": "Coal", "brands": ["Peabody Energy", "Arch Coal", "China Shenhua", "Glencore", "Shaanxi Coal and Chemical", "Adani", "BHP", "Anglo American", "Xstrata", "Teck Resources"]},
        ],
        "descriptions": [
            "Top-grade {} ensuring reliable energy supply.",
            "High-efficiency {} meeting industrial standards.",
            "Premium-quality {} for enhanced performance.",
            "Eco-friendly {} with optimized efficiency.",
        ],
    },
    "Chemicals & Hazardous Materials": {
        "items": [
            {"name": "Acid", "brands": ["Sulfuric Acid", "Hydrochloric Acid", "Nitric Acid", "Phosphoric Acid", "Peracetic Acid", "Acetic Acid", "Citric Acid", "Formic Acid", "Oxalic Acid", "Lactic Acid"]},
            {"name": "Solvent", "brands": ["Acetone", "Toluene", "Xylene", "Methanol", "Isopropyl Alcohol", "Ethanol", "Butanol", "Ethyl Acetate", "Hexane", "Chloroform"]},
            {"name": "Pesticide", "brands": ["BASF", "Syngenta", "Dow AgroSciences", "Monsanto", "DuPont", "FMC Corporation", "Adama", "Bayer CropScience", "Valent", "Sumitomo Chemical"]},
            {"name": "Industrial Gas", "brands": ["Linde", "Air Products", "Praxair", "Air Liquide", "Messer", "The BOC Group", "Matheson", "Gulf Cryo", "Taiyo Nippon Sanso", "SIAD"]},
            {"name": "Resin", "brands": ["DOW", "BASF", "SABIC", "LG Chem", "Mitsui Chemicals", "Covestro", "Eastman", "Huntsman", "INEOS", "Celanese"]},
        ],
        "descriptions": [
            "Highly pure {} for industrial applications.",
            "Specialized {} ensuring safety and compliance.",
            "Premium {} meeting international standards.",
            "Carefully handled {} for safe transportation.",
        ],
    },
    "Bulk & Containerized Cargo": {
        "items": [
            {"name": "Cement", "brands": ["Ambuja Cement", "Ultratech Cement", "ACC Cement", "JK Cement", "Dalmia Cement", "Shree Cement", "Ramco Cement", "Birla White", "Anjani Portland", "Madhav Cement"]},
            {"name": "Grain", "brands": ["Wheat", "Rice", "Corn", "Barley", "Oats", "Soybean", "Millet", "Sorghum", "Rye", "Pulses"]},
            {"name": "Steel", "brands": ["Tata Steel", "JSW Steel", "ArcelorMittal", "POSCO", "Nippon Steel", "U.S. Steel", "Steel Authority of India", "BaoSteel", "China Steel", "ThyssenKrupp"]},
            {"name": "Timber", "brands": ["Pine Wood", "Oak Wood", "Maple Wood", "Cedar Wood", "Birch Wood", "Douglas Fir", "Teak Wood", "Redwood", "Mahogany", "Eucalyptus"]},
            {"name": "Textiles", "brands": ["Cotton Fabric", "Polyester", "Nylon", "Wool", "Silk", "Denim", "Linen", "Tencel", "Spandex", "Rayon"]},
        ],
        "descriptions": [
            "High-strength {} used in construction and manufacturing.",
            "Bulk-packed {} ensuring secure transportation.",
            "Superior quality {} for industrial applications.",
            "Well-packaged {} to prevent damage during transit.",
        ],
    },
}

def seed_categories():
    for category_choice in CATEGORY_CHOICES.keys():
        Category.objects.create(
            name = category_choice
        )

def get_unique_sku_code(category, existing_skus):
    """Generate a unique SKU and ensure it's not already used."""
    attempts = 5

    for _ in range(attempts):
        sku_code = f"SKU-{category.name[:3].upper()}-{random.randint(2000, 2099)}-{random.randint(10000, 99999)}"

        if sku_code not in existing_skus and not Product.objects.filter(sku_code=sku_code).exists():
            existing_skus.add(sku_code)
            return sku_code

    raise ValueError("❌ Failed to generate a unique SKU after multiple attempts!")

def seed_products(n=1000):
    """Efficiently seed products using bulk_create."""
    categories = list(Category.objects.all())

    if not categories:
        print("⚠️ No categories found. Cannot seed products.")
        return

    existing_skus = set(Product.objects.values_list("sku_code", flat=True))  # Track existing SKUs
    products_to_create = []

    for _ in range(n):
        category = random.choice(categories)

        category_data = CATEGORY_CHOICES.get(category.name, {})
        product_list = category_data.get("items", [])
        description_templates = category_data.get("descriptions", [])

        if not product_list or not description_templates:
            print(f"⚠️ Skipping category '{category.name}' due to missing data.")
            continue

        product_name = random.choice(product_list)
        product_name = product_name["name"] if isinstance(product_name, dict) else product_name
        description_template = random.choice(description_templates)
        description = description_template.format(product_name.lower())

        try:
            sku_code = get_unique_sku_code(category, existing_skus)
            supplier = faker.company()

            product = Product(
                sku_code=sku_code,
                name=product_name,
                description=description,
                price=round(random.uniform(50.0, 5000.0), 2),
                category=category,
                supplier_company=supplier
            )
            products_to_create.append(product)

        except ValueError:
            print("❌ Could not generate unique SKU, skipping product.")

    # 🚀 **Bulk insert products in one query**
    if products_to_create:
        Product.objects.bulk_create(products_to_create)
        print(f"✅ {len(products_to_create)} products created successfully!")

    else:
        print("⚠️ No products were created.")

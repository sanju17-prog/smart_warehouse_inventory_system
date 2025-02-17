# Smart Warehouse Management System

This project is a comprehensive warehouse management system designed to handle product and inventory management, stock movement tracking, warehouse organization, user roles, and notifications.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
    - [Windows](#windows)
    - [macOS](#macos)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- **Product & Inventory Management**: Add, update, delete, and view products with unique SKUs, track stock levels, and assign products to specific warehouse locations.
- **Stock Movement Tracking**: Log stock in/out transactions, track quantity changes, and maintain a history of stock movements for audits.
- **Warehouse Organization**: Divide the warehouse into zones, aisles, shelves, and bins, and track storage capacity.
- **User Roles & Permissions**: Define roles like Admin, Manager, and Staff with specific permissions.
- **Search, Filtering & Reports**: Search and filter inventory, generate reports on stock levels, and export reports as CSV/PDF.
- **Notifications & Alerts**: Send alerts for low stock, new stock arrivals, and stock discrepancies.

## Project Structure

The project is organized into several modules:

```bash
smart_warehouse_management/
│
├── viewsets/                          # Viewsets for handling API views
│   ├── __init__.py
│   ├── fleet_viewset.py               # Viewset for fleet management
│   ├── product_viewset.py             # Viewset for product management
│   ├── stock_viewset.py               # Viewset for stock management
│   └── warehouse_viewset.py           # Viewset for warehouse management
│
├── apps.py                            # Application configuration
├── tests.py                           # Test cases
├── urls.py                            # URL routing
│
├── notifications/                     # Notifications module (planned with Celery)
│
├── orders/                            # Orders management module
│
├── reports/                           # Reports generation module
│
├── smart_warehouse_management/         # Core application settings
│   ├── __pycache__/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── asgi.py                        # ASGI configuration
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # URL routing for the app
│   └── wsgi.py                        # WSGI configuration
│
├── users/                             # User management module
│   ├── __pycache__/
│   │   └── __init__.py
│   ├── migrations/                    # Database migrations
│   │   └── __init__.py
│   ├── admin.py                       # Admin configurations
│   ├── apps.py                        # Application configurations
│   ├── models.py                      # User models
│   ├── permissions.py                  # Permissions configurations
│   ├── seed.py                        # Seed data for testing
│   ├── signals.py                     # Signal handlers
│   ├── tests.py                       # Test cases
│   ├── urls.py                        # URL routing
│   ├── views.py                        # Views for user-related operations
│   ├── .gitignore                     # Git ignore file
│   ├── db.sqlite3                     # SQLite database file
│   ├── manage.py                      # Django management script
│   └── README.md                      # Project README
│
├── inventory/                          # Inventory management module
│   ├── admin/                         # Admin configurations for inventory
│   │   ├── __pycache__/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── fleet_admin.py             # Admin for fleet management
│   │   ├── product_admin.py           # Admin for product management
│   │   ├── stock_admin.py             # Admin for stock management
│   │   └── warehouse_admin.py         # Admin for warehouse management
│   │
│   ├── models/                        # Models for inventory management
│   │   ├── __pycache__/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── fleet_models.py            # Models for fleet
│   │   ├── product_models.py          # Models for products
│   │   ├── stock_models.py            # Models for stock
│   │   └── warehouse_models.py        # Models for warehouse
│   │
│   ├── seed/                          # Seed data for inventory
│   │   ├── __pycache__/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── fleet_seed.py              # Seed data for fleet
│   │   ├── product_seed.py            # Seed data for products
│   │   ├── stock_seed.py              # Seed data for stock
│   │   └── warehouse_seed.py          # Seed data for warehouse
│   │
│   └── viewsets/                     # Viewsets for inventory management
│       ├── __init__.py
│       ├── product_viewset.py          # Viewset for product management
│       ├── stock_viewset.py            # Viewset for stock management
│       ├── warehouse_viewset.py        # Viewset for warehouse management
│       └── fleet_viewset.py            # Viewset for fleet management
│
├── requirements.txt                    # Project dependencies
```

## Technologies Used

- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **Authentication:** JWT
- **Data Generation:** Faker
- **Notifications:** Celery, Signals (Planned)

## SetUp Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/smart_warehouse_management.git
cd smart_warehouse_management
```

2. **Set up a virtual environment:**
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Apply migrations:**
```bash
python manage.py migrate
```

5. **Run the development server:**
```bash
python manage.py runserver
```

## Usage
- **Admin:** Manage all products, employees, and settings.
- **Manager:** Update inventory and approve stock movements.
- **Staff:** View inventory and report stock issues.

## Dependencies
- The project dependencies are listed in the requirements.txt file.
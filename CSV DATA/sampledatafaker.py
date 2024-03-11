import random
import string
import uuid
import csv
from datetime import datetime, timedelta

# Generate Supplier Data
def generate_supplier_data(num_records):
    suppliers = []
    for _ in range(num_records):
        supplier = {
            'supplier_id': str(uuid.uuid4()),
            'supplier_name': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'supplier_location': random.choice(['USA', 'Canada', 'UK', 'Germany', 'China']),
            'supplier_lead_time': random.randint(1, 60),
            'supplier_capacity': random.randint(1000, 10000),
            'supplier_reliability': random.randint(0, 100),
            'supplier_cost_per_unit': round(random.uniform(10, 100), 2)
        }
        suppliers.append(supplier)
    return suppliers

# Generate Product Data
def generate_product_data(num_records):
    products = []
    for _ in range(num_records):
        product = {
            'product_id': str(uuid.uuid4()),
            'product_name': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'product_category': random.choice(['Category A', 'Category B', 'Category C']),
            'product_length': round(random.uniform(10, 100), 2),
            'product_width': round(random.uniform(10, 100), 2),
            'product_height': round(random.uniform(10, 100), 2),
            'product_weight': round(random.uniform(1, 20), 2),
            'product_unit_cost': round(random.uniform(10, 1000), 2),
            'product_demand_forecast': random.randint(100, 1000)
        }
        products.append(product)
    return products

# Generate Inventory Data
def generate_inventory_data(num_records, products):
    inventory = []
    for _ in range(num_records):
        product_id = random.choice(products)['product_id']
        inventory_item = {
            'warehouse_id': str(uuid.uuid4()),
            'warehouse_location': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'London']),
            'warehouse_capacity': random.randint(10000, 100000),
            'product_id': product_id,
            'quantity_on_hand': random.randint(100, 1000),
            'reorder_point': random.randint(50, 500),
            'safety_stock_level': random.randint(20, 200)
        }
        inventory.append(inventory_item)
    return inventory

# Generate Transportation Data
def generate_transportation_data(num_records):
    transportation = []
    for _ in range(num_records):
        transportation_item = {
            'transportation_mode': random.choice(['Air', 'Sea', 'Land']),
            'origin': str(uuid.uuid4()),
            'destination': str(uuid.uuid4()),
            'distance': random.randint(100, 5000),
            'transit_time': random.randint(1, 30),
            'transportation_cost_per_unit': round(random.uniform(1, 20), 2),
            'carbon_emissions_per_unit': round(random.uniform(0.1, 1), 2)
        }
        transportation.append(transportation_item)
    return transportation

# Generate Order Data
def generate_order_data(num_records, products, customers):
    orders = []
    for _ in range(num_records):
        product_id = random.choice(products)['product_id']
        customer_id = random.choice(customers)['customer_id']
        order_date = datetime.now() - timedelta(days=random.randint(1, 365))
        order = {
            'order_id': str(uuid.uuid4()),
            'customer_id': customer_id,
            'product_id': product_id,
            'order_quantity': random.randint(1, 100),
            'order_date': order_date.strftime('%Y-%m-%d'),
            'requested_delivery_date': (order_date + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
            'actual_delivery_date': None,
            'order_status': random.choice(['Pending', 'Shipped', 'Delivered'])
        }
        orders.append(order)
    return orders

# Generate External Data
def generate_external_data(num_records):
    external = []
    for _ in range(num_records):
        external_item = {
            'date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
            'temperature': round(random.uniform(-10, 40), 2),
            'precipitation': round(random.uniform(0, 100), 2),
            'natural_disaster': random.choice([None, 'Earthquake', 'Hurricane', 'Flood', 'Wildfire']),
            'geopolitical_event': random.choice([None, 'Trade War', 'Tariffs', 'Sanctions']),
            'market_demand_trend': round(random.uniform(-5, 5), 2),
            'competitor_activity': random.choice([None, 'New Product', 'Price Change', 'Marketing Campaign']),
            'currency_exchange_rate': round(random.uniform(0.5, 2), 2),
            'commodity_price': round(random.uniform(20, 200), 2)
        }
        external.append(external_item)
    return external

# Generate Customer Data
def generate_customer_data(num_records):
    customers = []
    for _ in range(num_records):
        customer = {
            'customer_id': str(uuid.uuid4()),
            'customer_name': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'customer_location': random.choice(['USA', 'Canada', 'UK', 'Germany', 'China'])
        }
        customers.append(customer)
    return customers

# Generate Sample Data
num_suppliers = 50
num_products = 100
num_inventory_items = 200
num_transportation_items = 300
num_customers = 75
num_orders = 1000
num_external_items = 365

suppliers_data = generate_supplier_data(num_suppliers)
products_data = generate_product_data(num_products)
customers_data = generate_customer_data(num_customers)
inventory_data = generate_inventory_data(num_inventory_items, products_data)
transportation_data = generate_transportation_data(num_transportation_items)
orders_data = generate_order_data(num_orders, products_data, customers_data)
external_data = generate_external_data(num_external_items)

# Save the generated data to CSV files
def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

save_to_csv(suppliers_data, 'suppliers.csv')
save_to_csv(products_data, 'products.csv')
save_to_csv(customers_data, 'customers.csv')
save_to_csv(inventory_data, 'inventory.csv')
save_to_csv(transportation_data, 'transportation.csv')
save_to_csv(orders_data, 'orders.csv')
save_to_csv(external_data, 'external.csv')
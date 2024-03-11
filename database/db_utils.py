from .db_config import db
from models import Product, Inventory, Supplier, Transportation, Order, OrderItem, Forecast, Anomaly, OptimizationResult

def create_tables():
    db.create_all()
    print("Database tables created successfully.")

def drop_tables():
    db.drop_all()
    print("Database tables dropped successfully.")

def commit_changes():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def add_product(name, description, price):
    product = Product(name=name, description=description, price=price)
    db.session.add(product)
    commit_changes()
    return product.id

def get_product(product_id):
    return Product.query.get(product_id)

def update_inventory(product_id, quantity):
    inventory = Inventory.query.filter_by(product_id=product_id).first()
    if inventory:
        inventory.quantity = quantity
    else:
        inventory = Inventory(product_id=product_id, quantity=quantity)
        db.session.add(inventory)
    commit_changes()

def get_inventory(product_id):
    inventory = Inventory.query.filter_by(product_id=product_id).first()
    return inventory.quantity if inventory else None

def create_order(customer_id, items):
    order = Order(customer_id=customer_id, status='Pending')
    for item in items:
        order_item = OrderItem(product_id=item['product_id'], quantity=item['quantity'])
        order.items.append(order_item)
    db.session.add(order)
    commit_changes()
    return order.id

def get_order(order_id):
    order = Order.query.get(order_id)
    return order

def create_transportation(order_id, source, destination, shipping_method):
    transportation = Transportation(order_id=order_id, source=source, destination=destination, shipping_method=shipping_method, status='Pending')
    db.session.add(transportation)
    commit_changes()
    return transportation.id

def get_transportation(transportation_id):
    return Transportation.query.get(transportation_id)

def save_forecast(product_id, forecast_date, forecasted_quantity):
    forecast = Forecast(product_id=product_id, forecast_date=forecast_date, forecasted_quantity=forecasted_quantity)
    db.session.add(forecast)
    commit_changes()

def save_anomaly(anomaly_type, description):
    anomaly = Anomaly(anomaly_type=anomaly_type, description=description)
    db.session.add(anomaly)
    commit_changes()

def save_optimization_result(optimization_type, parameters, result):
    optimization_result = OptimizationResult(optimization_type=optimization_type, parameters=parameters, result=result)
    db.session.add(optimization_result)
    commit_changes()
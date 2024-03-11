from flask import Blueprint, jsonify, request
from services import ProductService, InventoryService, OrderService, SupplierService, TransportationService
from utils.validate_request_data import validate_request_data

api_routes = Blueprint('api', __name__)

# Product routes
@api_routes.route('/products', methods=['GET'])
def get_products():
    product_service = ProductService()
    products = product_service.get_all_products()
    return jsonify(products), 200

@api_routes.route('/products', methods=['POST'])
@validate_request_data(['name', 'description', 'price'])
def create_product():
    data = request.get_json()
    product_service = ProductService()
    product_id = product_service.add_product(data['name'], data['description'], data['price'])
    return jsonify({'message': 'Product created successfully', 'product_id': product_id}), 201

# Inventory routes
@api_routes.route('/inventory/<product_id>', methods=['GET'])
def get_inventory(product_id):
    inventory_service = InventoryService()
    quantity = inventory_service.get_inventory(product_id)
    if quantity is None:
        return jsonify({'message': 'Inventory not found'}), 404
    return jsonify({'product_id': product_id, 'quantity': quantity}), 200

@api_routes.route('/inventory', methods=['POST'])
@validate_request_data(['product_id', 'quantity'])
def add_inventory():
    data = request.get_json()
    inventory_service = InventoryService()
    inventory_service.add_inventory(data['product_id'], data['quantity'])
    return jsonify({'message': 'Inventory added successfully'}), 201

# Order routes
@api_routes.route('/orders', methods=['POST'])
@validate_request_data(['customer_id', 'products'])
def create_order():
    data = request.get_json()
    order_service = OrderService()
    order_id = order_service.create_order(data['customer_id'], data['products'])
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 201

@api_routes.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order_service = OrderService()
    order = order_service.get_order(order_id)
    if order is None:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify(order), 200

# Supplier routes
@api_routes.route('/suppliers', methods=['GET'])
def get_suppliers():
    supplier_service = SupplierService()
    suppliers = supplier_service.get_all_suppliers()
    return jsonify(suppliers), 200

# Transportation routes
@api_routes.route('/shipments', methods=['POST'])
@validate_request_data(['order_id', 'source', 'destination', 'shipping_method'])
def create_shipment():
    data = request.get_json()
    transportation_service = TransportationService()
    shipment_id = transportation_service.create_shipment(data['order_id'], data['source'], data['destination'], data['shipping_method'])
    return jsonify({'message': 'Shipment created successfully', 'shipment_id': shipment_id}), 201

@api_routes.route('/shipments/<shipment_id>/track', methods=['GET'])
def track_shipment(shipment_id):
    transportation_service = TransportationService()
    tracking_info = transportation_service.track_shipment(shipment_id)
    return jsonify(tracking_info), 200
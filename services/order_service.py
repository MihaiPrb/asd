from utils.database import Database
from utils.logger import logger
from .inventory_service import InventoryService

class OrderService:
    def __init__(self, config):
        self.db = Database(config['database'])
        self.inventory_service = InventoryService(config)

    def create_order(self, customer_id, products):
        try:
            # Create order in the database
            query = "INSERT INTO orders (customer_id, status) VALUES (%s, 'pending')"
            order_id = self.db.execute_query(query, (customer_id,), return_id=True)

            # Create order items and update inventory
            for product_id, quantity in products.items():
                # Check if sufficient inventory is available
                current_quantity = self.inventory_service.get_inventory(product_id)
                if current_quantity is None or current_quantity < quantity:
                    raise Exception(f"Insufficient inventory for product {product_id}")

                # Create order item
                query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
                self.db.execute_query(query, (order_id, product_id, quantity))

                # Update inventory
                new_quantity = current_quantity - quantity
                self.inventory_service.update_inventory(product_id, new_quantity)

            logger.info(f"Order created: id = {order_id}, customer_id = {customer_id}")
            return order_id
        except Exception as e:
            logger.error(f"Error occurred while creating order for customer {customer_id}: {str(e)}")
            raise e

    def get_order(self, order_id):
        try:
            # Get order details
            query = "SELECT * FROM orders WHERE id = %s"
            order = self.db.execute_query(query, (order_id,))
            if not order:
                return None

            # Get order items
            query = "SELECT * FROM order_items WHERE order_id = %s"
            order_items = self.db.execute_query(query, (order_id,))

            order[0]['items'] = order_items
            return order[0]
        except Exception as e:
            logger.error(f"Error occurred while getting order {order_id}: {str(e)}")
            raise e

    def update_order_status(self, order_id, status):
        try:
            query = "UPDATE orders SET status = %s WHERE id = %s"
            self.db.execute_query(query, (status, order_id))
            logger.info(f"Order status updated: id = {order_id}, status = {status}")
        except Exception as e:
            logger.error(f"Error occurred while updating status for order {order_id}: {str(e)}")
            raise e
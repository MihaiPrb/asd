from utils.database import Database
from utils.logger import logger

class InventoryService:
    def __init__(self, config):
        self.db = Database(config['database'])

    def get_inventory(self, product_id):
        try:
            query = "SELECT quantity FROM inventory WHERE product_id = %s"
            result = self.db.execute_query(query, (product_id,))
            if result:
                return result[0]['quantity']
            else:
                return None
        except Exception as e:
            logger.error(f"Error occurred while getting inventory for product {product_id}: {str(e)}")
            raise e

    def update_inventory(self, product_id, quantity):
        try:
            query = "UPDATE inventory SET quantity = %s WHERE product_id = %s"
            self.db.execute_query(query, (quantity, product_id))
            logger.info(f"Inventory updated for product {product_id}: quantity = {quantity}")
        except Exception as e:
            logger.error(f"Error occurred while updating inventory for product {product_id}: {str(e)}")
            raise e

    def add_inventory(self, product_id, quantity):
        try:
            query = "INSERT INTO inventory (product_id, quantity) VALUES (%s, %s)"
            self.db.execute_query(query, (product_id, quantity))
            logger.info(f"Inventory added for product {product_id}: quantity = {quantity}")
        except Exception as e:
            logger.error(f"Error occurred while adding inventory for product {product_id}: {str(e)}")
            raise e

    def remove_inventory(self, product_id):
        try:
            query = "DELETE FROM inventory WHERE product_id = %s"
            self.db.execute_query(query, (product_id,))
            logger.info(f"Inventory removed for product {product_id}")
        except Exception as e:
            logger.error(f"Error occurred while removing inventory for product {product_id}: {str(e)}")
            raise e
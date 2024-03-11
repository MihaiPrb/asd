from utils.database import Database
from utils.logger import logger

class ProductService:
    def __init__(self, config):
        self.db = Database(config['database'])

    def get_product(self, product_id):
        try:
            query = "SELECT * FROM products WHERE id = %s"
            result = self.db.execute_query(query, (product_id,))
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            logger.error(f"Error occurred while getting product {product_id}: {str(e)}")
            raise e

    def get_all_products(self):
        try:
            query = "SELECT * FROM products"
            result = self.db.execute_query(query)
            return result
        except Exception as e:
            logger.error(f"Error occurred while getting all products: {str(e)}")
            raise e

    def add_product(self, name, description, price):
        try:
            query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
            product_id = self.db.execute_query(query, (name, description, price), return_id=True)
            logger.info(f"Product added: id = {product_id}, name = {name}")
            return product_id
        except Exception as e:
            logger.error(f"Error occurred while adding product: {str(e)}")
            raise e

    def update_product(self, product_id, name, description, price):
        try:
            query = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
            self.db.execute_query(query, (name, description, price, product_id))
            logger.info(f"Product updated: id = {product_id}, name = {name}")
        except Exception as e:
            logger.error(f"Error occurred while updating product {product_id}: {str(e)}")
            raise e

    def delete_product(self, product_id):
        try:
            query = "DELETE FROM products WHERE id = %s"
            self.db.execute_query(query, (product_id,))
            logger.info(f"Product deleted: id = {product_id}")
        except Exception as e:
            logger.error(f"Error occurred while deleting product {product_id}: {str(e)}")
            raise e
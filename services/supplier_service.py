from utils.database import Database
from utils.logger import logger

class SupplierService:
    def __init__(self, config):
        self.db = Database(config['database'])

    def get_supplier(self, supplier_id):
        try:
            query = "SELECT * FROM suppliers WHERE id = %s"
            result = self.db.execute_query(query, (supplier_id,))
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            logger.error(f"Error occurred while getting supplier {supplier_id}: {str(e)}")
            raise e

    def get_all_suppliers(self):
        try:
            query = "SELECT * FROM suppliers"
            result = self.db.execute_query(query)
            return result
        except Exception as e:
            logger.error(f"Error occurred while getting all suppliers: {str(e)}")
            raise e

    def add_supplier(self, name, contact_info):
        try:
            query = "INSERT INTO suppliers (name, contact_info) VALUES (%s, %s)"
            supplier_id = self.db.execute_query(query, (name, contact_info), return_id=True)
            logger.info(f"Supplier added: id = {supplier_id}, name = {name}")
            return supplier_id
        except Exception as e:
            logger.error(f"Error occurred while adding supplier: {str(e)}")
            raise e

    def update_supplier(self, supplier_id, name, contact_info):
        try:
            query = "UPDATE suppliers SET name = %s, contact_info = %s WHERE id = %s"
            self.db.execute_query(query, (name, contact_info, supplier_id))
            logger.info(f"Supplier updated: id = {supplier_id}, name = {name}")
        except Exception as e:
            logger.error(f"Error occurred while updating supplier {supplier_id}: {str(e)}")
            raise e

    def delete_supplier(self, supplier_id):
        try:
            query = "DELETE FROM suppliers WHERE id = %s"
            self.db.execute_query(query, (supplier_id,))
            logger.info(f"Supplier deleted: id = {supplier_id}")
        except Exception as e:
            logger.error(f"Error occurred while deleting supplier {supplier_id}: {str(e)}")
            raise e
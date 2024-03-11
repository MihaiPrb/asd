from utils.database import Database
from utils.logger import logger
from utils.external_api import ExternalAPI

class TransportationService:
    def __init__(self, config):
        self.db = Database(config['database'])
        self.external_api = ExternalAPI(config['external_api'])

    def create_shipment(self, order_id, source, destination, shipping_method):
        try:
            # Create shipment in the database
            query = "INSERT INTO shipments (order_id, source, destination, shipping_method) VALUES (%s, %s, %s, %s)"
            shipment_id = self.db.execute_query(query, (order_id, source, destination, shipping_method), return_id=True)
            
            # Call external API to schedule the shipment
            response = self.external_api.schedule_shipment(shipment_id, source, destination, shipping_method)
            
            if response['status'] == 'success':
                logger.info(f"Shipment created: id = {shipment_id}, order_id = {order_id}")
                return shipment_id
            else:
                logger.error(f"Failed to create shipment for order {order_id}")
                raise Exception("Shipment creation failed")
        except Exception as e:
            logger.error(f"Error occurred while creating shipment for order {order_id}: {str(e)}")
            raise e

    def track_shipment(self, shipment_id):
        try:
            # Call external API to get shipment tracking information
            response = self.external_api.track_shipment(shipment_id)
            
            if response['status'] == 'success':
                tracking_info = response['data']
                logger.info(f"Shipment tracking information retrieved: id = {shipment_id}")
                return tracking_info
            else:
                logger.error(f"Failed to retrieve tracking information for shipment {shipment_id}")
                raise Exception("Shipment tracking failed")
        except Exception as e:
            logger.error(f"Error occurred while tracking shipment {shipment_id}: {str(e)}")
            raise e
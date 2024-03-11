import unittest
from app import create_app

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_products(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, 200)
        # Assert the response data

    def test_create_order(self):
        data = {
            'customer_id': 1,
            'items': [
                {'product_id': 1, 'quantity': 2},
                {'product_id': 2, 'quantity': 1}
            ]
        }
        response = self.client.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 201)
        # Assert the response data

    # Add more test methods for other API routes

if __name__ == '__main__':
    unittest.main()
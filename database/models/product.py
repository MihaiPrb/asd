from database.db_config import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<Product {self.id}>'
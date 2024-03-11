from database.db_config import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref=db.backref('inventory', lazy=True))

    def __repr__(self):
        return f'<Inventory {self.id}>'
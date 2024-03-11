from dataclasses import dataclass

@dataclass
class Inventory:
    product_id: int
    quantity: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data.get('product_id'),
            quantity=data.get('quantity')
        )

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'quantity': self.quantity
        }
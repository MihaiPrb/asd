from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: Decimal

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            price=Decimal(data.get('price'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price)
        }
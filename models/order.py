from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class OrderItem:
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

@dataclass
class Order:
    id: int
    customer_id: int
    status: str
    items: List[OrderItem]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        items = [OrderItem.from_dict(item) for item in data.get('items', [])]
        return cls(
            id=data.get('id'),
            customer_id=data.get('customer_id'),
            status=data.get('status'),
            items=items,
            created_at=datetime.fromisoformat(data.get('created_at')),
            updated_at=datetime.fromisoformat(data.get('updated_at'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'status': self.status,
            'items': [item.to_dict() for item in self.items],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
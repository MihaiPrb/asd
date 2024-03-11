from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transportation:
    id: int
    order_id: int
    source: str
    destination: str
    shipping_method: str
    status: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            order_id=data.get('order_id'),
            source=data.get('source'),
            destination=data.get('destination'),
            shipping_method=data.get('shipping_method'),
            status=data.get('status'),
            created_at=datetime.fromisoformat(data.get('created_at')),
            updated_at=datetime.fromisoformat(data.get('updated_at'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'source': self.source,
            'destination': self.destination,
            'shipping_method': self.shipping_method,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
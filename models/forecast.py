from dataclasses import dataclass
from datetime import datetime

@dataclass
class Forecast:
    id: int
    product_id: int
    forecast_date: datetime
    forecasted_quantity: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            product_id=data.get('product_id'),
            forecast_date=datetime.fromisoformat(data.get('forecast_date')),
            forecasted_quantity=data.get('forecasted_quantity')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'forecast_date': self.forecast_date.isoformat(),
            'forecasted_quantity': self.forecasted_quantity
        }
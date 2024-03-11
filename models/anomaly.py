from dataclasses import dataclass
from datetime import datetime

@dataclass
class Anomaly:
    id: int
    anomaly_type: str
    description: str
    detected_at: datetime

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            anomaly_type=data.get('anomaly_type'),
            description=data.get('description'),
            detected_at=datetime.fromisoformat(data.get('detected_at'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'anomaly_type': self.anomaly_type,
            'description': self.description,
            'detected_at': self.detected_at.isoformat()
        }
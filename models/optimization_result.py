from dataclasses import dataclass
from datetime import datetime

@dataclass
class OptimizationResult:
    id: int
    optimization_type: str
    parameters: dict
    result: dict
    created_at: datetime

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            optimization_type=data.get('optimization_type'),
            parameters=data.get('parameters'),
            result=data.get('result'),
            created_at=datetime.fromisoformat(data.get('created_at'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'optimization_type': self.optimization_type,
            'parameters': self.parameters,
            'result': self.result,
            'created_at': self.created_at.isoformat()
        }
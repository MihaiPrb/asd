from dataclasses import dataclass

@dataclass
class Supplier:
    id: int
    name: str
    contact_info: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            contact_info=data.get('contact_info')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info
        }
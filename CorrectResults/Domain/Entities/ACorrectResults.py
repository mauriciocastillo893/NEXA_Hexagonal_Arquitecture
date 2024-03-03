from dataclasses import dataclass, field
from CorrectResults.Domain.Entities.Type_status import Type_status
import uuid

@dataclass
class ACorrectResults:
    correctResults_uuid: str = field(default_factory=uuid.uuid4, init=False)
    valorUno: str
    valorDos: str
    valueUno: Type_status
    valueDos: Type_status
    ask_uuid: str = None  # Agregar el campo ask_uuid como un parámetro opcional

    def to_dict(self):
        return {
            'correctResults_uuid': self.correctResults_uuid,
            'valorUno': self.valorUno,
            'valorDos': self.valorDos,
            'valueUno': self.valueUno,
            'valueDos': self.valueDos,
            'ask_uuid': self.ask_uuid
        }

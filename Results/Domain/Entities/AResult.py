from dataclasses import dataclass, field
from Results.Domain.Entities.Result import Result
import uuid

@dataclass
class AResult:
    result_uuid  : str = field(default_factory=uuid.uuid4, init=False)
    valorUno: Result
    valorDos: Result
    ask_uuid: str

    def to_dict(self):
        return {
            'result_uuid': self.result_uuid,
            'valorUno': self.valorUno,
            'valorDos': self.valorDos,
            'ask_uuid': self.ask_uuid
        }
    
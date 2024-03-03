from dataclasses import dataclass, field
import uuid
from typing import List

@dataclass
class ASurvey:
    title: str 
    survey_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    asks: List['Ask'] = field(default_factory=list)  # Lista de preguntas asociadas a la encuesta

    def to_dict(self):
        return {
            'title': self.title,
            'survey_uuid': self.survey_uuid,
            'asks': [ask.to_dict() for ask in self.asks]
        }

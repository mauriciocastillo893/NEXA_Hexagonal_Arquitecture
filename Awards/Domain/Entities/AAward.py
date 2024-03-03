from dataclasses import dataclass, field
import uuid

@dataclass
class AAward:
    award_uuid  : str = field(default_factory=uuid.uuid4, init=False)
    name : str
    description : str
    
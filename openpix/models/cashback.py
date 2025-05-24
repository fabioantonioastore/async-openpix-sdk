from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Cashback(BaseModel):
    value: int

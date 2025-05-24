from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Refund(BaseModel):
    value: int
    status: str
    correlationID: str
    refundId: str
    time: str
    comment: str

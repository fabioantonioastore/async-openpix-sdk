from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Dispute(BaseModel):
    status: str
    name: str
    email: str
    phoneNumber: str
    value: str
    disputeReason: str
    endToEndId: str

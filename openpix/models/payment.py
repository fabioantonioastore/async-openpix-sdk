from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Payment(BaseModel):
    value: int
    destinationAlias: str
    destinationAliasType: str
    qrCode: str
    correlationID: str
    comment: str
    status: str


@dataclass
class PaymentDestination(BaseModel):
    name: str
    taxID: str
    pixKey: str
    bank: str
    branch: str
    account: str

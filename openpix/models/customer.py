from pydantic.dataclasses import dataclass

from openpix.models import BaseModel, TaxID


class Address(BaseModel):
    zipcode: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    complement: str
    country: str


@dataclass
class Customer(BaseModel):
    name: str
    email: str
    phone: str
    taxID: TaxID
    correlationID: str
    address: Address

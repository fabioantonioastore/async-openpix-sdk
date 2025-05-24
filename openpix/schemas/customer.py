from pydantic import model_validator
from typing import Optional, Any, Dict

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class Address(BaseSchema):
    zipcode: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    complement: str
    country: str


class Customer(BaseSchema):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    taxID: Optional[str] = None
    correlationID: Optional[str] = None
    address: Optional[Address] = None

    @model_validator(mode="after")
    async def model_validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return await Validators.customer_model_validator(data)


class CustomerUpdate(BaseSchema):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    taxID: Optional[str] = None
    address: Optional[Address] = None
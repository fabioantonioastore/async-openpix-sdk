from typing import Optional, Any, Dict

from pydantic import model_validator, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic_extra_types.country import CountryAlpha2
from pydantic_br import CPF, CEP, SiglaEstado

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class Address(BaseSchema):
    zipcode: CEP
    street: str
    number: str
    neighborhood: str
    city: str
    state: SiglaEstado
    complement: str
    country: CountryAlpha2


class Customer(BaseSchema):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[PhoneNumber] = None
    taxID: Optional[CPF] = None
    correlationID: Optional[str] = None
    address: Optional[Address] = None

    @model_validator(mode="after")
    async def model_validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return await Validators.customer_model_validator(data)


class CustomerUpdate(BaseSchema):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[PhoneNumber] = None
    taxID: Optional[CPF] = None
    address: Optional[Address] = None

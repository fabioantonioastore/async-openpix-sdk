from typing import Optional

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from openpix.schemas import BaseSchema, Application
from openpix.schemas import TaxID


class User(BaseSchema):
    firstName: str
    lastName: str
    email: EmailStr
    phone: PhoneNumber
    taxID: TaxID


class PreRegistration(BaseSchema):
    name: str
    website: Optional[str]
    taxID: TaxID


class PartnerPreRegistrationCompanyApplicationCreate(BaseSchema):
    application: Application
    taxID: TaxID


class PartnerPreRegistrationCompanyCreate(BaseSchema):
    preRegistration: PreRegistration
    user: User

from typing import Optional

from openpix.schemas import BaseSchema, Application
from openpix.schemas import TaxID


class User(BaseSchema):
    firstName: str
    lastName: str
    email: str
    phone: str
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
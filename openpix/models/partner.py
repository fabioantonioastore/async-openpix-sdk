from dataclasses import dataclass

from openpix.models import BaseModel, TaxIDObjectPayload


@dataclass
class PartnerApplicationPayload(BaseModel):
    name: str
    isActive: bool
    type: str
    clientId: str
    clientSecret: str


@dataclass
class PreRegistrationObjectPayload(BaseModel):
    name: str
    taxID: TaxIDObjectPayload


@dataclass
class PreRegistrationUserObject(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    taxID: TaxIDObjectPayload


@dataclass
class CompanyObjectPayload(BaseModel):
    id: str
    name: str
    taxID: TaxIDObjectPayload


@dataclass
class AccountObjectPayload(BaseModel):
    clientId: str


@dataclass
class PreRegistration(BaseModel):
    preRegistration: PreRegistrationObjectPayload
    user: PreRegistrationUserObject
    company: CompanyObjectPayload
    account: AccountObjectPayload

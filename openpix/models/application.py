from dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Application(BaseModel):
    name: str
    isActive: bool
    type: str
    clientId: str
    clientSecret: str
    appID: str
    companyBankAccount: str

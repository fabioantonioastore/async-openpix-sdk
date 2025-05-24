from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Balance(BaseModel):
    total: int
    blocked: int
    available: int


@dataclass
class CompanyBankAccount(BaseModel):
    accountId: str
    isDefault: bool
    balance: Balance

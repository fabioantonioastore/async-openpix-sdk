from pydantic.dataclasses import dataclass

from openpix.models.base_model import BaseModel
from openpix.models.balance import Balance


@dataclass
class CompanyBankAccount(BaseModel):
    accountId: str
    isDefault: bool
    balance: Balance

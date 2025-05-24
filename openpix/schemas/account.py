from pydantic import Field

from decimal import Decimal

from openpix.schemas import BaseSchema


class AccountRegister(BaseSchema):
    officialName: str
    tradeName: str
    taxID: str
    annualRevenue: int


class WithdrawFromAccount(BaseSchema):
    value: Decimal = Field(decimal_places=2)
from pydantic import Field, field_serializer
from pydantic_br import CNPJ

from decimal import Decimal

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class AccountRegister(BaseSchema):
    officialName: str
    tradeName: str
    taxID: CNPJ
    annualRevenue: int


class WithdrawFromAccount(BaseSchema):
    value: Decimal = Field(decimal_places=2)

    @field_serializer("value")
    def value_serialize(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)

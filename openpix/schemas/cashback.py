from decimal import Decimal

from pydantic import Field, field_serializer
from pydantic_br import CNPJ, CPF

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class CashbackCreate(BaseSchema):
    taxID: CPF | CNPJ
    value: Decimal = Field(decimal_places=2)

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)

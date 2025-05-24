from decimal import Decimal

from pydantic import Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class TransferCreate(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    fromPixKey: str
    toPixKey: str

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)

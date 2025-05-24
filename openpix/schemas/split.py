from decimal import Decimal

from pydantic import Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class Split(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    pixKey: str
    splitType: str

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)

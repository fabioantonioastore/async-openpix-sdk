from decimal import Decimal
from typing import List

from pydantic import Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class DiscountFixedDate(BaseSchema):
    daysActive: int
    value: Decimal = Field(decimal_places=2)

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)


class DiscountSettings(BaseSchema):
    modality: str
    discountFixedDate: List[DiscountFixedDate]

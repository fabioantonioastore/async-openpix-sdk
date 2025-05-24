from decimal import Decimal
from typing import Optional

from pydantic import Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Serializer


class PixQRCodeStaticCreate(BaseSchema):
    name: str
    correlationID: Optional[str] = None
    value: Optional[Decimal] = Field(None, decimal_places=2)
    comment: Optional[str] = None

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> Optional[int] | Decimal:
        if value:
            return Serializer.decimal_to_int(value)
        return value

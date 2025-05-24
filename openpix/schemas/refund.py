from decimal import Decimal

from pydantic import field_validator, Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Validators, Serializer


class RefundCreate(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    transactionEndToEndId: str
    correlationID: str
    comment: str

    @field_validator("comment")
    @classmethod
    async def comment_validator(cls, value: str) -> str:
        return await Validators.comment_validator(value)

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)

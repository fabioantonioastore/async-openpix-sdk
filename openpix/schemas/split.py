from decimal import Decimal

from pydantic import Field, field_serializer, field_validator

from openpix.schemas import BaseSchema
from openpix.utils import Serializer, Validators


class Split(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    pixKey: str
    splitType: str

    @field_validator("splitType")
    @classmethod
    async def split_type_validator(cls, value: str) -> str:
        return await Validators.split_type_validator(value)

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)

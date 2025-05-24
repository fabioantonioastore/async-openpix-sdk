from decimal import Decimal
from typing import Optional

from pydantic import Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils.serializer import Serializer


class SubAccountCreate(BaseSchema):
    pixKey: str
    name: str


class TransferSubAccountToMainAccount(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    description: Optional[str] = None

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)


class SubAccountWithdraw(BaseSchema):
    value: Decimal = Field(decimal_places=2)

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)


class SubAccountTransferToSubAccount(BaseSchema):
    value: Decimal = Field(decimal_places=2)
    fromPixKey: str
    fromPixKeyType: str
    toPixKey: str
    toPixKeyType: str
    correlationID: Optional[str] = None

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)

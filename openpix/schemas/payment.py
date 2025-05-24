from decimal import Decimal
from typing import Optional

from pydantic import field_validator, Field, field_serializer

from openpix.schemas import BaseSchema
from openpix.utils import Validators, Serializer


class PaymentRequest(BaseSchema):
    correlationID: str


class PaymentRequestApprove(PaymentRequest):
    pass


class PaymentRequestPixKeyCreate(PaymentRequest):
    value: Decimal = Field(decimal_places=2)
    destinationAlias: str
    destinationAliasType: str
    comment: Optional[str] = None

    @field_validator("destinationAliasType")
    @classmethod
    async def destination_alias_type_validator(cls, value: str) -> str:
        return await Validators.pix_key_type_validator(value)

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> Optional[int] | Decimal:
        if value:
            return await Serializer.decimal_to_int(value)
        return value


class PaymentRequestQRCodeCreate(PaymentRequest):
    qr_code: str
    comment: Optional[str] = None

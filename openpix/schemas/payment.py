from typing import Optional

from pydantic import field_validator, Field

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class PaymentRequest(BaseSchema):
    correlationID: str


class PaymentRequestApprove(PaymentRequest):
    pass


class PaymentRequestPixKeyCreate(PaymentRequest):
    value: int = Field(description="Value in cents")
    destinationAlias: str
    destinationAliasType: str
    comment: Optional[str] = None

    @field_validator("destinationAliasType")
    async def destination_alias_type_validator(self, value: str) -> str:
        return await Validators.pix_key_type_validator(value)


class PaymentRequestQRCodeCreate(PaymentRequest):
    qr_code: str
    comment: Optional[str] = None
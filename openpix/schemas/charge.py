from decimal import Decimal
from typing import Optional, List, Dict, Any

from pydantic import field_validator, Field, field_serializer

from openpix.schemas import BaseSchema, Split, Customer, Fines, Interests
from openpix.utils import Validators, Serializer


class ChargeExpirationDateUpdate(BaseSchema):
    expiresDate: str

    @field_validator("expiresDate")
    @classmethod
    async def expires_date_validator(cls, value: str) -> str:
        pass


class ChargeCreate(BaseSchema):
    correlationID: str
    value: Decimal = Field(decimal_places=2)
    type: Optional[str] = None
    comment: Optional[str] = None
    expiresIn: Optional[int] = None
    expiresDate: Optional[str] = None
    customer: Optional[Customer] = None
    daysForDueDate: Optional[int] = None
    daysAfterDueDate: Optional[int] = None
    interests: Optional[Interests] = None
    fines: Optional[Fines] = None
    discountSettings: Optional[None] = None
    additionalInfo: Optional[List[Dict[str, Any]]] = []
    enableCashbackExclusivePercentage: Optional[bool] = None
    subaccount: Optional[str] = None
    splits: Optional[List[Split]] = None

    @field_validator("expiresIn")
    @classmethod
    async def expires_in_validator(cls, value: int) -> int:
        return await Validators.expires_in_validator(value)

    @field_validator("type")
    @classmethod
    async def charge_type_validator(cls, value: str) -> str:
        if value:
            return await Validators.charge_type_validator(value)
        return value

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> int:
        return await Serializer.decimal_to_int(value)


class ChargeRefundCreate(BaseSchema):
    correlationID: str
    value: Optional[Decimal] = Field(None, decimal_places=2)
    comment: Optional[str] = None

    @field_validator("comment")
    @classmethod
    async def comment_validator(cls, value: str) -> str:
        return await Validators.comment_validator(value)

    @field_serializer("value")
    async def value_serializer(self, value: Decimal) -> Optional[int] | Decimal:
        if value:
            return await Serializer.decimal_to_int(value)
        return value

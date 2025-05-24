from typing import Optional, List, Dict, Any

from pydantic import field_validator, Field

from openpix.schemas import BaseSchema, Split, Customer, Fines, Interests
from openpix.utils import Validators


class ChargeExpirationDateUpdate(BaseSchema):
    expiresDate: str

    @field_validator("expiresDate")
    async def expires_date_validator(self, value: str) -> str:
        pass


class ChargeCreate(BaseSchema):
    correlationID: str
    value: int = Field(description="Value in cents")
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
    async def expires_in_validator(self, value: int) -> int:
        return await Validators.expires_in_validator(value)

    @field_validator("type")
    async def charge_type_validator(self, value: str) -> str:
        if value:
            return await Validators.charge_type_validator(value)
        return value


class ChargeRefundCreate(BaseSchema):
    correlationID: str
    value: Optional[int] = Field(None, description="value in cents")
    comment: Optional[str] = None

    @field_validator("comment")
    async def comment_validator(self, value: str) -> str:
        return await Validators.comment_validator(value)
from decimal import Decimal

from pydantic import field_validator, Field, field_serializer
from typing import Optional, Any, List, Dict

from openpix.schemas import BaseSchema, Customer
from openpix.utils import Validators, Serializer


class SubscriptionCreate(BaseSchema):
    customer: Customer
    value: Decimal = Field(decimal_places=2)
    comment: Optional[str] = None
    additionalInfo: Optional[List[Dict[str, Any]]] = None
    dayGenerateCharge: int = 5
    frequency: Optional[str] = None
    chargeType: str = "DYNAMIC"
    dayDue: int = 7
    correlationID: str

    @field_validator("dayGenerateCharge")
    @classmethod
    async def day_generate_charge_validator(cls, value: int) -> int:
        return await Validators.day_generate_charge_validator(value)

    @field_validator("dayDue")
    @classmethod
    async def day_due_validator(cls, value: int) -> int:
        return await Validators.day_due_validator(value)

    @field_validator("frequency")
    @classmethod
    async def frequency_validator(cls, value: str) -> str:
        if value:
            return await Validators.frequency_validator(value)
        return value

    @field_validator("chargeType")
    @classmethod
    async def charge_type_validator(cls, value: str) -> str:
        return await Validators.charge_type_validator(value)

    @field_serializer("value")
    def value_serializer(self, value: Decimal) -> int:
        return Serializer.decimal_to_int(value)

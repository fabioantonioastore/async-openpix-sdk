from pydantic import field_validator, Field
from typing import Optional, Any, List, Dict

from openpix.schemas import BaseSchema, Customer
from openpix.utils import Validators


class SubscriptionCreate(BaseSchema):
    customer: Customer
    value: int = Field(description="Value in cents")
    comment: Optional[str] = None
    additionalInfo: Optional[List[Dict[str, Any]]] = None
    dayGenerateCharge: int = 5
    frequency: Optional[str] = None
    chargeType: str = "DYNAMIC"
    dayDue: int = 7
    correlationID: str

    @field_validator("dayGenerateCharge")
    async def day_generate_charge_validator(self, value: int) -> int:
        return await Validators.day_generate_charge_validator(value)

    @field_validator("dayDue")
    async def day_due_validator(self, value: int) -> int:
        return await Validators.day_due_validator(value)

    @field_validator("frequency")
    async def frequency_validator(self, value: str) -> str:
        if value:
            return await Validators.frequency_validator(value)
        return value

    @field_validator("chargeType")
    async def charge_type_validator(self, value: str) -> str:
        return await Validators.charge_type_validator(value)
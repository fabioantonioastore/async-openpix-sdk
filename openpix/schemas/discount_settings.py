from typing import List

from pydantic import Field

from openpix.schemas import BaseSchema


class DiscountFixedDate(BaseSchema):
    daysActive: int
    value: int = Field(description="Value in cents")


class DiscountSettings(BaseSchema):
    modality: str
    discountFixedDate: List[DiscountFixedDate]

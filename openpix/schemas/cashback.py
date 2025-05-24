from pydantic import Field

from openpix.schemas import BaseSchema


class CashbackCreate(BaseSchema):
    taxID: str
    value: int = Field(description="Value in cents")

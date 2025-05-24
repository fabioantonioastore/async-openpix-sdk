from pydantic import Field

from openpix.schemas import BaseSchema


class TransferCreate(BaseSchema):
    value: int = Field(description="Value in cents")
    fromPixKey: str
    toPixKey: str
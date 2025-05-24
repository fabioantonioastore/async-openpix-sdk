from pydantic import field_validator, Field

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class RefundCreate(BaseSchema):
    value: int = Field(description="Value in cents")
    transactionEndToEndId: str
    correlationID: str
    comment: str

    @field_validator("comment")
    async def comment_validator(self, value: str) -> str:
        return await Validators.comment_validator(value)
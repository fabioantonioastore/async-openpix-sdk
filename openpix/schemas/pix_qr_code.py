from typing import Optional

from pydantic import Field

from openpix.schemas import BaseSchema


class PixQRCodeStaticCreate(BaseSchema):
    name: str
    correlationID: Optional[str] = None
    value: Optional[int] = Field(None, description="Value in cents")
    comment: Optional[str] = None
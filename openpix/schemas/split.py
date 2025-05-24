from pydantic import Field

from openpix.schemas import BaseSchema


class Split(BaseSchema):
    value: int = Field(description="Value in cents")
    pixKey: str
    splitType: str
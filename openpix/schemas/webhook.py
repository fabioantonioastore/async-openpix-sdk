from pydantic import field_validator

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class WebhookCreate(BaseSchema):
    name: str
    event: str
    url: str
    authorization: str
    isActive: bool

    @field_validator("event")
    @classmethod
    async def event_validator(cls, value: str) -> str:
        return await Validators.webhook_event_validator(value)

from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class Webhook(BaseModel):
    id: str
    name: str
    event: str
    url: str
    authorization: str
    isActive: bool
    createdAt: str
    updatedAt: str

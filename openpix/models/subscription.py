from pydantic.dataclasses import dataclass

from openpix.models import BaseModel, Customer


@dataclass
class Subscription(BaseModel):
    globalID: str
    value: int
    customer: Customer
    dayGenerateCharge: int
    frequency: str
    status: str
    correlationID: str

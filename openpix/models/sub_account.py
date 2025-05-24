from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class SubAccount(BaseModel):
    name: str
    pixKey: str
    balance: int


@dataclass
class DestinationSubAccount(SubAccount):
    pass


@dataclass
class OriginSubAccount(SubAccount):
    pass

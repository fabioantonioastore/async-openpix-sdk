from pydantic.dataclasses import dataclass

from openpix.models import BaseModel


@dataclass
class TaxID(BaseModel):
    taxID: str
    type: str


@dataclass
class TaxIDObjectPayload(BaseModel):
    taxID: str
    type: str

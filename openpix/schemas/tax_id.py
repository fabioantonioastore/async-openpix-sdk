from pydantic import field_validator

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class TaxID(BaseSchema):
    taxID: str
    type: str

    @field_validator("type")
    async def tax_type_validator(self, value: str) -> str:
        return await Validators.tax_type_validator(value)
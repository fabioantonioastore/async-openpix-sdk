from typing import Dict, Any

from pydantic import model_validator
from pydantic_br import CPF, CNPJ

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class TaxID(BaseSchema):
    taxID: CPF | CNPJ
    type: str

    @model_validator(mode="after")
    async def tax_type_validator(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return await Validators.model_tax_id_validator(data)

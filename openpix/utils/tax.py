from enum import Enum


class TaxType(str, Enum):
    CPF = "BR:CPF"
    CNPJ = "BR:CNPJ"

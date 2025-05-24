from enum import Enum


class PixKeyType(str, Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    RANDOM = "RANDOM"

from dataclasses import dataclass
from typing import Any, Dict, List

from openpix.models import BaseModel


@dataclass
class Pix(BaseModel):
    method: str
    transactionID: str
    identifier: str
    additionalInfo: List[Dict[str, Any]]
    fee: int
    value: int
    status: str
    txId: str
    brCode: str
    qrCodeImage: str


@dataclass
class PaymentMethods(BaseModel):
    pix: Pix | None

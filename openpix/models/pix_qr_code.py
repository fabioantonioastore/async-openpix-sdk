from pydantic.dataclasses import dataclass
from typing import Any

from openpix.models import BaseModel


@dataclass
class PixQRCode(BaseModel):
    name: str
    value: str
    comment: str
    brCode: str
    correlationID: str
    paymentLinkID: str
    paymentLinkUrl: Any
    qrCodeImage: Any
    createdAt: str
    updatedAt: str

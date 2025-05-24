from dataclasses import dataclass
from typing import Any, Dict, List

from openpix.models import BaseModel, Customer, Subscription, PaymentMethods


@dataclass
class Charge(BaseModel):
    value: int
    customer: Customer
    type: str
    comment: str
    brCode: str
    status: str
    correlationID: str
    paymentLinkID: Any
    paymentLinkUrl: Any
    globalID: Any
    transactionID: Any
    identifier: str
    qrCodeImage: Any
    additionalInfo: List[Dict[str, Any]]
    pixKey: str
    createdAt: str
    updatedAt: str
    expiresIn: str
    subscription: Subscription
    paymentMethods: PaymentMethods


@dataclass
class ChargeRefund(BaseModel):
    value: int
    status: str
    correlationID: str
    endToEndId: str
    time: str
    comment: str

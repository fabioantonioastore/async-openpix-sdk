from dataclasses import dataclass
from typing import Any

from openpix.models import BaseModel, CompanyBankAccount, PixQRCode, Charge, Customer


@dataclass
class WithdrawTransaction(BaseModel):
    endToEndId: str
    value: str


@dataclass
class Withdraw:
    account: CompanyBankAccount
    transaction: WithdrawTransaction


@dataclass
class PaymentTransaction(BaseModel):
    value: int
    endToEndId: str
    time: str


@dataclass
class PixWithdrawTransaction(BaseModel):
    value: int
    time: str
    endToEndID: str
    transactionID: str
    infoPagador: str
    endToEndId: str
    payer: Customer
    type: str


@dataclass
class Transaction(BaseModel):
    charge: Charge
    value: int
    time: str
    endToEndID: str
    transactionID: str
    infoPagador: str
    endToEndId: str
    customer: Customer
    withdraw: PixWithdrawTransaction
    payer: Customer
    type: str
    globalID: Any
    pixQrCode: PixQRCode


@dataclass
class TransferTransaction(BaseModel):
    value: int
    time: str
    correlationID: str


@dataclass
class AccountTransaction(BaseModel):
    status: str
    value: int
    correlationID: str
    destinationAlias: str
    comment: str


@dataclass
class SubAccountWithdraw(BaseModel):
    account: AccountTransaction

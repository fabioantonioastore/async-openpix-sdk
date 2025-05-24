from typing import Optional

from pydantic import Field

from openpix.schemas import BaseSchema


class SubAccountCreate(BaseSchema):
    pixKey: str
    name: str


class TransferSubAccountToMainAccount(BaseSchema):
    value: int = Field(description="Value in cents")
    description: Optional[str] = None


class SubAccountWithdraw(BaseSchema):
    value: int = Field(description="Value in cents")


class SubAccountTransferToSubAccount(BaseSchema):
    value: int = Field(description="Value in cents")
    fromPixKey: str
    fromPixKeyType: str
    toPixKey: str
    toPixKeyType: str
    correlationID: Optional[str] = None
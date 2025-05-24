from openpix.sdk import BaseSDK
from openpix.api import api_classes


class OpenPix(BaseSDK):
    def __init__(self, app_id: str, sandbox: bool = False) -> None:
        super().__init__(app_id, sandbox)
        self.__instantiate_api_classes()

    def __instantiate_api_classes(self) -> None:
        for cls in api_classes:
            instance = cls(self.http_client)
            setattr(
                self, f"_{self.__class__.__name__}__{cls.__name__.lower()}", instance
            )

    @property
    def account(self):
        return self.__account

    @property
    def application(self):
        return self.__application

    @property
    def charge(self):
        return self.__charge

    @property
    def customer(self):
        return self.__customer

    @property
    def dispute(self):
        return self.__dispute

    @property
    def partner(self):
        return self.__partner

    @property
    def payment(self):
        return self.__payment

    @property
    def pix_qr_code(self):
        return self.__pix_qr_code

    @property
    def transactions(self):
        return self.__transactions

    @property
    def refund(self):
        return self.__refund

    @property
    def receipt(self):
        return self.__receipt

    @property
    def sub_account(self):
        return self.__sub_account

    @property
    def subscription(self):
        return self.__subscription

    @property
    def transfer(self):
        return self.__transfer

    @property
    def webhook(self):
        return self.__webhook

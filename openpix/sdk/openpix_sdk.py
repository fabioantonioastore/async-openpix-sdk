from openpix.api import api_classes


class BaseSDK:
    def __init__(self, app_id: str, sandbox: bool = False) -> None:
        self.__app_id = app_id
        self.__sandbox = sandbox
        self.__headers = {"Authorization": self.app_id}
        self.__base_url = "https://api.openpix.com.br/api/v1/"
        if self.sandbox:
            self.__base_url = "https://api.woovi-sandbox.com.br/api/v1/"

    @property
    def sandbox(self) -> bool:
        return self.__sandbox

    @property
    def app_id(self) -> str:
        return self.__app_id

    @property
    def headers(self) -> dict[str, str]:
        return self.__headers

    @property
    def base_url(self) -> str:
        return self.__base_url


class OpenPix(BaseSDK):
    def __init__(self, app_id: str, sandbox: bool = False) -> None:
        super().__init__(app_id, sandbox)
        self.__instantiate_api_classes()

    def __instantiate_api_classes(self) -> None:
        for cls in api_classes:
            instance = cls(self.base_url, self.headers)
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

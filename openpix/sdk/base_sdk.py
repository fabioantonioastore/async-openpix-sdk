from openpix.http import AsyncHTTPClient


class BaseSDK:
    def __init__(self, app_id: str, sandbox: bool = False) -> None:
        self.__app_id = app_id
        self.__sandbox = sandbox
        self.__headers = {
            "Authorization": self.app_id,
            "Content-Type": "application/json",
        }
        self.__base_url = "https://api.openpix.com.br/api/v1/"
        if self.sandbox:
            self.__base_url = "https://api.woovi-sandbox.com.br/api/v1/"
        self.__http_client = AsyncHTTPClient(base_url=self.__base_url)

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

    @property
    def http_client(self) -> AsyncHTTPClient:
        return self.__http_client

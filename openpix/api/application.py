from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient


@api_class_register
class Application(API):
    def __init__(self, http_client: AsyncHTTPClient) -> None:
        super().__init__(http_client)

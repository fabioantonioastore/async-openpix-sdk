from typing import Type, Dict

from openpix.http import AsyncHTTPClient


class API:
    def __init__(self, http_client: AsyncHTTPClient, headers: Dict[str, str]) -> None:
        self.__http_client = http_client
        self.__headers = headers

    @property
    def http_client(self) -> AsyncHTTPClient:
        return self.__http_client

    @property
    def headers(self) -> Dict[str, str]:
        return self.__headers


api_classes = set()


def api_class_register(cls: Type[API]) -> Type[API]:
    api_classes.add(cls)
    return cls

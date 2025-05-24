from typing import Type

from openpix.http import AsyncHTTPClient


class API:
    def __init__(self, http_client: AsyncHTTPClient) -> None:
        self.__http_client = http_client

    @property
    def http_client(self) -> AsyncHTTPClient:
        return self.__http_client


api_classes = set()


def api_class_register(cls: Type[API]) -> Type[API]:
    api_classes.add(cls)
    return cls

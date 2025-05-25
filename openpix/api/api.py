from typing import Type, Dict

from openpix.http import AsyncHTTPClient


class API:
    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        self.__headers = headers
        self.__base_url = base_url

    @property
    def headers(self) -> Dict[str, str]:
        return self.__headers

    @property
    def base_url(self) -> str:
        return self.__base_url


api_classes = set()


def api_class_register(cls: Type[API]) -> Type[API]:
    api_classes.add(cls)
    return cls

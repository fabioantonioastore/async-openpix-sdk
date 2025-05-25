from typing import Dict

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient


@api_class_register
class TransactionsAPI(API):
    def __init__(self, http_client: AsyncHTTPClient, headers: Dict[str, str]) -> None:
        super().__init__(http_client, headers)

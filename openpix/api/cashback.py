from typing import Dict, Any, AsyncGenerator, List

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient
from openpix.schemas import CashbackCreate
from openpix.models import Cashback


@api_class_register
class CashbackAPI(API):
    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        super().__init__(base_url, headers)
        self.endpoint = "/cashback-fidelity"

    async def get_user_cashback_amount(
        self, tax_id: str, timeout: float = 5
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/balance/{tax_id}"
            response = await http_client.get(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            )
            return response.json()

    async def get_many_user_cashback_amount(
        self, tax_ids: List[str] | AsyncGenerator[str], timeout: float = 5
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/balance"
            if isinstance(tax_ids, list):
                for tax_id in tax_ids:
                    endpoint = f"{new_endpoint}/{tax_id}"
                    response = await http_client.get(
                        endpoint=endpoint, headers=self.headers, timeout=timeout
                    )
                    yield response.json()
                return
            async for tax_id in tax_ids:
                endpoint = f"{new_endpoint}/{tax_id}"
                response = await http_client.get(
                    endpoint=endpoint, headers=self.headers, timeout=timeout
                )
                yield response.json()

    async def create_cashback(
        self,
        payload: CashbackCreate | Dict[str, Any],
        timeout: float = 5,
        as_dict: bool = False,
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payload, CashbackCreate):
                payload = payload.to_dict()
            response = await http_client.post(
                endpoint=self.endpoint,
                payload=payload,
                headers=self.headers,
                timeout=timeout,
            )
            if as_dict:
                return response.json()
            data = response.json()
            return {
                "message": data["message"],
                "cashback": Cashback(**data["cashback"]),
            }

    async def create_many_cashback(
        self,
        payloads: (
            List[CashbackCreate | Dict[str, Any]]
            | AsyncGenerator[CashbackCreate | Dict[str, Any]]
        ),
        timeout: float = 5,
        as_dict: bool = False,
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, CashbackCreate):
                        payload = payload.to_dict()
                    response = await http_client.post(
                        endpoint=self.endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    if as_dict:
                        yield response.json()
                        continue
                    data = response.json()
                    yield {
                        "message": data["message"],
                        "cashback": Cashback(**data["cashback"]),
                    }
                return
            async for payload in payloads:
                if isinstance(payload, CashbackCreate):
                    payload = payload.to_dict()
                response = await http_client.post(
                    endpoint=self.endpoint,
                    payload=payload,
                    headers=self.headers,
                    timeout=timeout,
                )
                if as_dict:
                    yield response.json()
                    continue
                data = response.json()
                yield {
                    "message": data["message"],
                    "cashback": Cashback(**data["cashback"]),
                }

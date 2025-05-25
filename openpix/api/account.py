from typing import Dict, List, AsyncGenerator, Any

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient
from openpix.models import CompanyBankAccount, Withdraw
from openpix.schemas import WithdrawFromAccount, AccountRegister


@api_class_register
class AccountAPI(API):
    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        super().__init__(base_url, headers)
        self.endpoint = "account"

    async def get_account(
        self, account_id: str, timeout: float = 5, as_dict: bool = False
    ) -> CompanyBankAccount | Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{account_id}"
            response = await http_client.get(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            )
            if as_dict:
                return response.json()
            return CompanyBankAccount(**response.json())

    async def get_list_of_accounts(
        self, timeout: float = 5, as_dict: bool = False
    ) -> List[CompanyBankAccount | Dict[str, Any]]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            response = await http_client.get(
                endpoint=self.endpoint, headers=self.headers, timeout=timeout
            )
            if as_dict:
                return [item for item in response.json()]
            return [CompanyBankAccount(**item) for item in response.json()]

    async def stream_get_list_of_accounts(
        self, timeout: float = 5, as_dict: bool = False
    ) -> AsyncGenerator[CompanyBankAccount | Dict[str, Any]]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/"
            async for item in http_client.get_stream(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            ):
                if as_dict:
                    yield item
                    continue
                yield CompanyBankAccount(**item)

    async def withdraw_from_an_account(
        self,
        payload: WithdrawFromAccount | Dict[str, Any],
        timeout: float = 5,
        as_dict: bool = False,
    ) -> Withdraw | Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, WithdrawFromAccount):
                payload = await payload.to_dict()
            new_endpoint = f"{self.endpoint}/{payload["accountId"]}/withdraw"
            response = await http_client.post(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout,
            )
            if as_dict:
                return response.json()
            return Withdraw(**response.json())

    async def many_withdraw_from_an_account(
        self,
        payloads: (
            List[WithdrawFromAccount | Dict[str, Any]]
            | AsyncGenerator[WithdrawFromAccount | Dict[str, Any]]
        ),
        timeout: float = 5,
        as_dict: bool = False,
    ) -> AsyncGenerator[Withdraw | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, WithdrawFromAccount):
                        payload = payload.to_dict()
                    new_endpoint = f"{self.endpoint}/{payload["accountId"]}/withdraw"
                    response = await http_client.post(
                        endpoint=new_endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    if as_dict:
                        yield response.json()
                        continue
                    yield Withdraw(**response.json())
                return
            async for payload in payloads:
                if isinstance(payload, WithdrawFromAccount):
                    payload = payload.to_dict()
                new_endpoint = f"{self.endpoint}/{payload["accountId"]}/withdraw"
                response = await http_client.post(
                    endpoint=new_endpoint,
                    headers=self.headers,
                    payload=payload,
                    timeout=timeout,
                )
                if as_dict:
                    yield response.json()
                    continue
                yield Withdraw(**response.json())

    async def register_account(
        self, payload: AccountRegister | Dict[str, Any], timeout: float = 5
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, AccountRegister):
                payload = payload.to_dict()
            new_endpoint = f"{self.endpoint}-register"
            response = await http_client.post(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout,
            )
            return response.json()

    async def register_many_account(
        self,
        payloads: (
            List[AccountRegister | Dict[str, Any]]
            | AsyncGenerator[AccountRegister | Dict[str, Any]]
        ),
        timeout: float = 5,
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, AccountRegister):
                        payload = payload.to_dict()
                    new_endpoint = f"{self.endpoint}-register"
                    response = await http_client.post(
                        endpoint=new_endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    yield response.json()

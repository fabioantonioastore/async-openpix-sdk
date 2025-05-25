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

    async def get_an_account(self, account_id: str, timeout: float = 5) -> CompanyBankAccount:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{account_id}"
            response = await http_client.get(
                endpoint=new_endpoint,
                headers=self.headers,
                timeout=timeout
            )
            data = response.json()
            return CompanyBankAccount(**data)

    async def get_a_list_of_accounts(self, timeout: float = 5) -> List[CompanyBankAccount]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            response = await http_client.get(
                endpoint=self.endpoint,
                headers=self.headers,
                timeout=timeout
            )
            data = response.json()
            return [CompanyBankAccount(**item) for item in data]

    async def stream_get_a_list_of_accounts(self, timeout: float = 5) -> AsyncGenerator:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/"
            async for item in http_client.get_stream(
                endpoint=new_endpoint,
                headers=self.headers,
                timeout=timeout
            ):
                yield CompanyBankAccount(**item)

    async def withdraw_from_an_account(self, account_id: str, payload: WithdrawFromAccount | Dict[str, Any], timeout: float = 5) -> Withdraw:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, WithdrawFromAccount):
                payload = await payload.to_dict()
            new_endpoint = f"{self.endpoint}/{account_id}/withdraw"
            response = await http_client.post(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout
            )
            data = response.json()
            return Withdraw(**data)

    async def register_account(self, payload: AccountRegister | Dict[str, Any], timeout: float = 5) -> Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, AccountRegister):
                payload = payload.to_dict()
            new_endpoint = f"{self.endpoint}-register"
            response = await http_client.post(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout
            )
            return response.json()

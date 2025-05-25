from typing import Dict, List, AsyncGenerator, Any

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient
from openpix.models import CompanyBankAccount, Withdraw
from openpix.schemas import WithdrawFromAccount, AccountRegister


@api_class_register
class AccountAPI(API):
    def __init__(self, http_client: AsyncHTTPClient, headers: Dict[str, str]) -> None:
        super().__init__(http_client, headers)
        self.endpoint = "account"

    async def get_an_account(self, account_id: str) -> CompanyBankAccount:
        new_endpoint = f"{self.endpoint}/{account_id}"
        response = await self.http_client.get(
            endpoint=new_endpoint,
            headers=self.headers
        )
        data = response.json()
        return CompanyBankAccount(**data)

    async def get_a_list_of_accounts(self) -> List[CompanyBankAccount]:
        response = await self.http_client.get(
            endpoint=self.endpoint,
            headers=self.headers
        )
        data = response.json()
        return [CompanyBankAccount(**item) for item in data]

    async def stream_get_a_list_of_accounts(self) -> AsyncGenerator:
        new_endpoint = f"{self.endpoint}/"
        async for item in self.http_client.get_stream(
            endpoint=new_endpoint,
            headers=self.headers
        ):
            yield CompanyBankAccount(**item)

    async def withdraw_from_an_account(self, account_id: str, payload: WithdrawFromAccount | Dict[str, Any]) -> Withdraw:
        if isinstance(payload, WithdrawFromAccount):
            payload = await payload.to_dict()
        new_endpoint = f"{self.endpoint}/{account_id}/withdraw"
        response = await self.http_client.post(
            endpoint=new_endpoint,
            headers=self.headers,
            payload=payload
        )
        data = response.json()
        return Withdraw(**data)

    async def register_account(self, payload: AccountRegister | Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(payload, AccountRegister):
            payload = payload.to_dict()
        new_endpoint = f"{self.endpoint}-register"
        response = await self.http_client.post(
            endpoint=new_endpoint,
            headers=self.headers,
            payload=payload
        )
        return response.json()

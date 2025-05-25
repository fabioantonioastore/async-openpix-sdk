from http.client import responses
from typing import Dict, Any, AsyncGenerator, List

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient
from openpix.schemas import ApplicationCreate, ApplicationDelete
from openpix.models import Application


@api_class_register
class ApplicationAPI(API):
    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        super().__init__(base_url, headers)
        self.endpoint = "/application"

    async def delete_application(
        self, payload: ApplicationDelete | Dict[str, Any], timeout: float = 5
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, ApplicationDelete):
                payload = payload.to_dict()
            response = await http_client.delete(
                endpoint=self.endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout,
            )
            return response.json()

    async def delete_many_application(
        self,
        payloads: (
            List[ApplicationDelete | Dict[str, Any]]
            | AsyncGenerator[ApplicationDelete | Dict[str, Any]]
        ),
        timeout: float = 5,
    ) -> AsyncGenerator[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, ApplicationDelete):
                        payload = payload.to_dict()
                    response = await http_client.delete(
                        endpoint=self.endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    yield response.json()
                return
            async for payload in payloads:
                if isinstance(payload, ApplicationDelete):
                    payload = payload.to_dict()
                response = await http_client.delete(
                    endpoint=self.endpoint,
                    headers=self.headers,
                    payload=payload,
                    timeout=timeout,
                )
                yield response.json()

    async def create_application(
        self,
        payload: ApplicationCreate | Dict[str, Any],
        as_dict: bool = False,
        timeout: float = 5,
    ) -> Application | Dict[str, Any]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payload, ApplicationCreate):
                payload = payload.to_dict()
            response = await http_client.post(
                endpoint=self.endpoint,
                payload=payload,
                headers=self.headers,
                timeout=timeout,
            )
            if as_dict:
                return response.json()
            return Application(**response.json())

    async def create_many_application(
        self,
        payloads: (
            List[ApplicationCreate | Dict[str, Any]]
            | AsyncGenerator[ApplicationCreate | Dict[str, Any]]
        ),
        as_dict: bool = False,
        timeout: float = 5,
    ) -> AsyncGenerator[Application | Dict[str, Any]]:
        async with AsyncHTTPClient(base_url=self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, ApplicationCreate):
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
                    yield Application(**response.json())
                return
            async for payload in payloads:
                if isinstance(payload, ApplicationCreate):
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
                yield Application(**response.json())

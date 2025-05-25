from typing import Dict, Any, List, AsyncGenerator

from openpix.api import API, api_class_register
from openpix.http import AsyncHTTPClient
from openpix.schemas import ChargeExpirationDateUpdate, ChargeCreate
from openpix.models import Charge, ChargeRefund


@api_class_register
class ChargeAPI(API):
    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        super().__init__(base_url, headers)
        self.endpoint = "/charge"

    async def get_charge_qr_code_image(
        self, id: str, size: int = 1024, timeout: float = 5
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient() as http_client:
            endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
            response = await http_client.get(
                endpoint=endpoint, headers=self.headers, timeout=timeout
            )
            return response.json()

    async def get_many_charge_qr_code_image(
        self, ids: List[str] | AsyncGenerator[str], size: int = 1024, timeout: float = 5
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient() as http_client:
            if isinstance(ids, List):
                for id in ids:
                    endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
                    response = await http_client.get(
                        endpoint=endpoint, headers=self.headers, timeout=timeout
                    )
                    yield response.json()
                return
            async for id in ids:
                endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
                response = await http_client.get(
                    endpoint=endpoint, headers=self.headers, timeout=timeout
                )
                yield response.json()

    async def stream_get_charge_qr_code_image(
        self, id: str, size: int = 1024, timeout: float = 5
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient() as http_client:
            endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
            async for item in http_client.get_stream(
                endpoint=endpoint, headers=self.headers, timeout=timeout
            ):
                yield item

    async def stream_get_many_charge_qr_code_image(
        self, ids: List[str] | AsyncGenerator[str], size: int = 1024, timeout: float = 5
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient() as http_client:
            if isinstance(ids, list):
                for id in ids:
                    endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
                    async for item in http_client.get_stream(
                        endpoint=endpoint, headers=self.headers, timeout=timeout
                    ):
                        yield item
                return
            async for id in ids:
                endpoint = f"https://api.openpix.com.br/openpix/charge/brcode/image/{id}.png?size={size}"
                async for item in http_client.get_stream(
                    endpoint=endpoint, headers=self.headers, timeout=timeout
                ):
                    yield item

    async def delete_charge(self, id: str, timeout: float = 5) -> Dict[str, Any]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{id}"
            response = await http_client.delete(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            )
            return response.json()

    async def delete_many_charge(
        self, ids: List[str] | AsyncGenerator[str], timeout: float = 5
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(ids, list):
                for id in ids:
                    new_endpoint = f"{self.endpoint}/{id}"
                    response = await http_client.delete(
                        endpoint=new_endpoint, headers=self.headers, timeout=timeout
                    )
                    yield response.json()
                return
            async for id in ids:
                new_endpoint = f"{self.endpoint}/{id}"
                response = await http_client.delete(
                    endpoint=new_endpoint, headers=self.headers, timeout=timeout
                )
                yield response.json()

    async def update_charge_expiration_date(
        self, payload: ChargeExpirationDateUpdate | Dict[str, Any], timeout: float = 5
    ) -> Dict[str, Any]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payload, ChargeExpirationDateUpdate):
                payload = payload.to_dict()
            new_endpoint = f"{self.endpoint}/{payload["id"]}"
            response = await http_client.patch(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout,
            )
            return response.json()

    async def update_many_charge_expiration_date(
        self,
        payloads: (
            List[ChargeExpirationDateUpdate | Dict[str, Any]]
            | AsyncGenerator[ChargeExpirationDateUpdate | Dict[str, Any]]
        ),
        timeout: float = 5,
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, ChargeExpirationDateUpdate):
                        payload = payload.to_dict()
                    new_endpoint = f"{self.endpoint}/{payload["id"]}"
                    response = await http_client.patch(
                        endpoint=new_endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    yield response.json()
                return
            async for payload in payloads:
                if isinstance(payload, ChargeExpirationDateUpdate):
                    payload = payload.to_dict()
                new_endpoint = f"{self.endpoint}/{payload["id"]}"
                response = await http_client.patch(
                    endpoint=new_endpoint,
                    headers=self.headers,
                    payload=payload,
                    timeout=timeout,
                )
                yield response.json()

    async def get_charge(
        self, id: str, as_dict: bool = False, timeout: float = 5
    ) -> Charge:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{id}"
            response = await http_client.get(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            )
            if as_dict:
                return response.json()
            return Charge(**response.json())

    async def get_list_of_charges(
        self,
        start_date: str = None,
        end_date: str = None,
        charge_status: str = None,
        customer_correlation_id: str = None,
        subscription_correlation_id: str = None,
        as_dict: bool = False,
        timeout: float = 5,
    ) -> List[Charge]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            params = {
                "start": start_date,
                "end": end_date,
                "status": charge_status,
                "customer": customer_correlation_id,
                "subscription": subscription_correlation_id,
            }
            response = await http_client.get(
                endpoint=self.endpoint,
                headers=self.headers,
                params=params,
                timeout=timeout,
            )
            if as_dict:
                return response.json()
            return [Charge(**item) for item in response.json()]

    async def get_many_charge(
        self,
        ids: List[str] | AsyncGenerator[str],
        as_dict: bool = False,
        timeout: float = 5,
    ) -> AsyncGenerator[Charge]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(ids, list):
                for id in ids:
                    new_endpoint = f"{self.endpoint}/{id}"
                    response = await http_client.get(
                        endpoint=new_endpoint, headers=self.headers, timeout=timeout
                    )
                    if as_dict:
                        yield response.json()
                        continue
                    yield Charge(**response.json())
                return
            async for id in ids:
                new_endpoint = f"{self.endpoint}/{id}"
                response = await http_client.get(
                    endpoint=new_endpoint, headers=self.headers, timeout=timeout
                )
                if as_dict:
                    yield response.json()
                    continue
                yield Charge(**response.json())

    async def stream_get_list_of_charge(
        self,
        start_date: str = None,
        end_date: str = None,
        charge_status: str = None,
        customer_correlation_id: str = None,
        subscription_correlation_id: str = None,
        as_dict: bool = False,
        timeout: float = 5,
    ) -> AsyncGenerator[Charge | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            params = {
                "start": start_date,
                "end": end_date,
                "status": charge_status,
                "subscription": subscription_correlation_id,
                "customer": customer_correlation_id,
            }
            async for item in http_client.get_stream(
                endpoint=self.endpoint,
                headers=self.headers,
                params=params,
                timeout=timeout,
            ):
                if as_dict:
                    yield item
                    continue
                yield Charge(**item)

    async def create_charge(
        self,
        payload: ChargeCreate | Dict[str, Any],
        return_existing: bool = True,
        as_dict: bool = False,
        timeout: float = 5,
    ) -> Charge | Dict[str, Any]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(payload, ChargeCreate):
                payload = payload.to_dict()
            new_endpoint = f"{self.endpoint}?return_existing={return_existing}"
            response = await http_client.post(
                endpoint=new_endpoint,
                headers=self.headers,
                payload=payload,
                timeout=timeout,
            )
            if as_dict:
                return response.json()
            return Charge(**response.json())

    async def create_many_charge(
        self,
        payloads: (
            List[ChargeCreate | Dict[str, Any]]
            | AsyncGenerator[ChargeCreate | Dict[str, Any]]
        ),
        return_existing: bool = True,
        as_dict: bool = False,
        timeout: float = 5,
    ) -> AsyncGenerator[Charge | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}?return_existing={return_existing}"
            if isinstance(payloads, list):
                for payload in payloads:
                    if isinstance(payload, ChargeCreate):
                        payload = payload.to_dict()
                    response = await http_client.post(
                        endpoint=new_endpoint,
                        headers=self.headers,
                        payload=payload,
                        timeout=timeout,
                    )
                    if as_dict:
                        yield response.json()
                        continue
                    yield Charge(**response.json())
                return
            async for payload in payloads:
                if isinstance(payload, ChargeCreate):
                    payload = payload.to_dict()
                response = await http_client.post(
                    endpoint=new_endpoint,
                    payload=payload,
                    headers=self.headers,
                    timeout=timeout,
                )
                if as_dict:
                    yield response.json()
                    continue
                yield Charge(**response.json())

    async def get_all_charge_refunds(
        self, id: str, as_dict: bool = False, timeout: float = 5
    ) -> List[ChargeRefund | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{id}/refund"
            response = await http_client.get(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            )
            if as_dict:
                return response.json()
            return [ChargeRefund(**item) for item in response.json()]

    async def stream_get_all_charge_refunds(
        self, id: str, as_dict: bool = False, timeout: float = 5
    ) -> AsyncGenerator[ChargeRefund | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            new_endpoint = f"{self.endpoint}/{id}/refund"
            async for item in http_client.get_stream(
                endpoint=new_endpoint, headers=self.headers, timeout=timeout
            ):
                if as_dict:
                    yield item
                    continue
                yield ChargeRefund(**item)

    async def stream_many_get_all_charge_refunds(
        self,
        ids: List[str] | AsyncGenerator[str],
        as_dict: bool = False,
        timeout: float = 5,
    ) -> AsyncGenerator[ChargeRefund | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(ids, list):
                for id in ids:
                    new_endpoint = f"{self.endpoint}/{id}/refund"
                    async for item in http_client.get_stream(
                        endpoint=new_endpoint, headers=self.headers, timeout=timeout
                    ):
                        if as_dict:
                            yield item
                            continue
                        yield ChargeRefund(**item)
                return
            async for id in ids:
                new_endpoint = f"{self.endpoint}/{id}/refund"
                async for item in http_client.get_stream(
                    endpoint=new_endpoint, headers=self.headers, timeout=timeout
                ):
                    if as_dict:
                        yield item
                        continue
                    yield ChargeRefund(**item)

    async def many_get_all_chage_refund(
        self,
        ids: List[str] | AsyncGenerator[str],
        timeout: float = 5,
        as_dict: bool = False,
    ) -> AsyncGenerator[ChargeRefund | Dict[str, Any]]:
        async with AsyncHTTPClient(self.base_url) as http_client:
            if isinstance(ids, list):
                for id in ids:
                    new_endpoint = f"{self.endpoint}/{id}/refund"
                    response = await http_client.get(
                        endpoint=new_endpoint, headers=self.headers, timeout=timeout
                    )
                    if as_dict:
                        yield response.json()
                        continue
                    yield ChargeRefund(**response.json())
            async for id in ids:
                new_endpoint = f"{self.endpoint}/{id}/refund"
                response = await http_client.get(
                    endpoint=new_endpoint, headers=self.headers, timeout=timeout
                )
                if as_dict:
                    yield response.json()
                    continue
                yield ChargeRefund(**response.json())

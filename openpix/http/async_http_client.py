from abc import abstractmethod
from typing import Optional, Dict, Any, AsyncGenerator
import json

from ijson.backends import yajl2_c as ijson
import httpx

from openpix.http import AbstractHTTPClient
from openpix.utils import AsyncBytesReader


class AsyncHTTPClientBase(AbstractHTTPClient):
    def __init__(self, base_url: str = "", timeout: Optional[float] = 5) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self.__client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    @property
    def client(self) -> httpx.AsyncClient:
        return self.__client

    @abstractmethod
    async def get(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def post(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def put(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def patch(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def delete(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def get_stream(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    @abstractmethod
    async def post_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    @abstractmethod
    async def put_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    @abstractmethod
    async def patch_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    @abstractmethod
    async def delete_stream(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    async def aclose(self) -> None:
        await self.client.aclose()

    @staticmethod
    async def stream(
        response: httpx.Response, prefix: str = "item", njson: bool = False
    ) -> AsyncGenerator[Dict[str, Any], None]:
        response.raise_for_status()
        if njson:
            buffer = ""
            async for chunk in response.aiter_text():
                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if not line:
                        continue
                    yield json.loads(line)
            if buffer.strip():
                yield json.loads(buffer)
        else:
            try:
                async_bytes_reader = AsyncBytesReader(response.aiter_bytes())
                async for item in ijson.items_async(async_bytes_reader, prefix):
                    yield item
            except ijson.common.IncompleteJSONError:
                pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()


class AsyncHTTPClient(AsyncHTTPClientBase):
    def __init__(self, base_url: str = "", timeout: Optional[float] = 5) -> None:
        super().__init__(base_url=base_url, timeout=timeout)

    async def get(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        response = await self.client.get(url=endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response

    async def post(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        response = await self.client.post(
            url=endpoint, json=payload, headers=headers, params=params
        )
        response.raise_for_status()
        return response

    async def put(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        response = await self.client.put(
            url=endpoint, json=payload, headers=headers, params=params
        )
        response.raise_for_status()
        return response

    async def patch(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        response = await self.client.patch(
            url=endpoint, json=payload, headers=headers, params=params
        )
        response.raise_for_status()
        return response

    async def delete(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        response = await self.client.delete(
            url=endpoint, headers=headers, params=params
        )
        response.raise_for_status()
        return response

    async def get_stream(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="GET", url=endpoint, headers=headers, params=params
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

    async def post_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="POST", url=endpoint, json=payload, headers=headers, params=params
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

    async def put_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="PUT", url=endpoint, json=payload, headers=headers, params=params
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

    async def patch_stream(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="PATCH", url=endpoint, json=payload, headers=headers, params=params
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

    async def delete_stream(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        njson: bool = False,
        prefix: str = "item",
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with self.client.stream(
            method="DELETE", url=endpoint, headers=headers, params=params
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

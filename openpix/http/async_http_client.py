from abc import abstractmethod
from typing import Optional, Dict, Any, AsyncGenerator
import json

from ijson.backends import yajl2_c as ijson
import httpx

from openpix.http import AbstractHTTPClient


class AsyncBytesReader:
    def __init__(self, aiter_bytes_gen) -> None:
        self.aiter_bytes_gen = aiter_bytes_gen
        self.__buffer = b""
        self.__eof = False

    async def read(self, n: int = -1) -> bytes:
        if self.__eof and not self.__buffer:
            return b""
        while len(self.__buffer) < n or n == -1:
            try:
                chunk = await self.aiter_bytes_gen.__anext__()
                self.__buffer += chunk
            except StopAsyncIteration:
                self.__eof = True
                break
            if n == -1 and self.__eof:
                break
        if n == -1:
            data = self.__buffer
            self.__buffer = b""
            return data
        else:
            data = self.__buffer[:n]
            self.__buffer = self.__buffer[n:]
            return data



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
        follow_redirects: bool = True,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def post(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def put(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def patch(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        pass

    @abstractmethod
    async def delete(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
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
        follow_redirects: bool = True,
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
        follow_redirects: bool = True,
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
        follow_redirects: bool = True,
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
        follow_redirects: bool = True,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        pass

    async def aclose(self) -> None:
        await self.client.aclose()

    @staticmethod
    async def stream(
        response: httpx.Response, prefix: str = "item", njson: bool = False
    ) -> Any:
        response.raise_for_status()
        if "application/pdf" in response.headers.get("content-type", ""):
            async for chunk in response.aiter_bytes():
                yield chunk
            return
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
            return
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
        follow_redirects: bool = True,
    ) -> httpx.Response:
        response = await self.client.get(
            url=endpoint,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
        )
        response.raise_for_status()
        return response

    async def post(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        response = await self.client.post(
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
        )
        response.raise_for_status()
        return response

    async def put(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        response = await self.client.put(
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
        )
        response.raise_for_status()
        return response

    async def patch(
        self,
        endpoint: str = "",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        response = await self.client.patch(
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
        )
        response.raise_for_status()
        return response

    async def delete(
        self,
        endpoint: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        follow_redirects: bool = True,
    ) -> httpx.Response:
        response = await self.client.delete(
            url=endpoint,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="GET",
            url=endpoint,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="POST",
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="PUT",
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        async with self.client.stream(
            method="PATCH",
            url=endpoint,
            json=payload,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
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
        follow_redirects: bool = True,
    ) -> AsyncGenerator[Dict[str, Any]]:
        async with self.client.stream(
            method="DELETE",
            url=endpoint,
            headers=headers,
            params=params,
            follow_redirects=follow_redirects,
        ) as response:
            async for item in self.stream(
                response=response, njson=njson, prefix=prefix
            ):
                yield item

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
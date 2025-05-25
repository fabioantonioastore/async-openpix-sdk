from asyncio import run

from openpix.http import AsyncHTTPClient


url = "https://run.mocky.io/v3/a4c6c63c-524c-4a54-9e92-b77d904bbd4e"
url2 = "https://run.mocky.io/v3/e1019553-7c38-46f9-abcb-8cd4767fdbf4"


async def main():
    async with AsyncHTTPClient() as http_client:
        response = await http_client.get(url)
        print(response.json())

        async for item in http_client.get_stream(url, njson=True):
            print(item)

        async for item in http_client.get_stream(url2):
            print(item)


run(main())

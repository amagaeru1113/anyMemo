import asyncio
import time

import aiohttp
import requests

# loopをとる
loop = asyncio.get_event_loop()

# 中身が非同期処理に対応していない
# async def hello(url):
#     print(requests.get(url).content)
#     print(time.time())


async def hello(url):
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         response = await response.read()
    #         print(response)
    #         print(time.time())
    await asyncio.sleep(10)


# loopでhelloを呼び出す
loop.run_until_complete(
    asyncio.wait(
        [hello("http://httpbin.org/headers"), hello("http://httpbin.org/headers")]
    )
)


import asyncio

loop = asyncio.get_event_loop()


async def worker1(lock):
    print("worker start")
    with await lock:
        await asyncio.sleep(3)
    print("worker end")


async def worker2(lock):
    print("worker start")
    with await lock:
        await asyncio.sleep(3)
    print("worker end")


lock = asyncio.Lock()

loop.run_until_complete(asyncio.wait([worker1(lock), worker2(lock)]))
loop.close()


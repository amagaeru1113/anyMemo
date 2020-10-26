import asyncio

loop = asyncio.get_event_loop()


async def worker1(event):
    print("worker start")
    await event.wait()
    print("worker got event")
    await asyncio.sleep(3)
    print("worker end")


async def worker2(event):
    print("worker start")
    await event.wait()
    print("worker got event")
    await asyncio.sleep(3)
    print("worker end")


async def worker3(event):
    print("worker start")
    await asyncio.sleep(3)
    print("worker end")
    event.set()


event = asyncio.Event()

loop.run_until_complete(asyncio.wait([worker1(event), worker2(event), worker3(event)]))
loop.close()


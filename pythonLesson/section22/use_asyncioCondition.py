import asyncio

loop = asyncio.get_event_loop()


async def worker1(condition):
    with await condition:
        condition.wait()
        print("worker1 start")
        print("worker got condition")
        await asyncio.sleep(3)
        print("worker1 end")


async def worker2(condition):
    with await condition:
        condition.wait()
        print("worker2 start")
        print("worker got condition")
        await asyncio.sleep(3)
        print("worker2 end")


async def worker3(condition):
    with await condition:
        print("worker3 start")
        print("worker got condition")
        await asyncio.sleep(3)
        print("worker3 end")
        condition.notify_all()


condition = asyncio.Condition()

loop.run_until_complete(
    asyncio.wait([worker1(condition), worker2(condition), worker3(condition)])
)
loop.close()

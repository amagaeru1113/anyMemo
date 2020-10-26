import asyncio

loop = asyncio.get_event_loop()


async def worker1(condition):
    async with condition:
        await condition.wait()
        print("asyncio native start1")
        await asyncio.sleep(3)
        print("asyncio native stop1")


async def worker2(condition):
    async with condition:
        await condition.wait()
        print("asyncio native start2")
        await asyncio.sleep(3)
        print("asyncio native stop2")


async def worker3(condition):
    await asyncio.sleep(1)
    async with condition:
        print("asyncio native start3")
        await asyncio.sleep(3)
        print("asyncio native stop3")
        condition.notify_all()


if __name__ == "__main__":
    condition = asyncio.Condition()
    loop.run_until_complete(
        asyncio.wait([worker1(condition), worker2(condition), worker3(condition)])
    )
    loop.close()

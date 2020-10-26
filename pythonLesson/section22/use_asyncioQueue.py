import asyncio

loop = asyncio.get_event_loop()


async def worker1(queue):

    print("worker1 start")
    await queue.put(100)  # awaitが無いとコルーチンに値が入らない
    print("worker1 end")


async def worker2(queue):
    print("worker2 start")
    x = await queue.get()
    print(x)
    print("worker2 end")


queue = asyncio.Queue()

loop.run_until_complete(asyncio.wait([worker1(queue), worker2(queue)]))
loop.close()

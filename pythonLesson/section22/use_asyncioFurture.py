import asyncio

loop = asyncio.get_event_loop()


async def f(future):
    await asyncio.sleep(1)
    future.set_result("Future is done")


def got_result(futures):
    print(future.result())
    loop.stop()


future = asyncio.Future()


asyncio.ensure_future(f(future))  # Task化しているから下のように書いてもいい
# # TaskはFutureを継承している
# task = asyncio.ensure_future(f(future))

# loop.run_until_complete(task)  # futureを回す
# print(future.result())
# loop.close()


future.add_done_callback(got_result)

loop.run_forever()
loop.close()


import asyncio

loop = asyncio.get_event_loop()

# 即座に実行する


def hello(name, loop):
    print("Hello, {}".format(name))
    loop.stop()


loop.call_soon(hello, "Nancy", loop)

loop.run_forever()
loop.close()

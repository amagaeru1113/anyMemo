import asyncio

loop = asyncio.get_event_loop()

# s秒後に実行する


def hello(name, loop):
    print("Hello, {}".format(name))
    loop.stop()


loop.call_later(3, hello, "Mike", loop)

loop.run_forever()
loop.close()

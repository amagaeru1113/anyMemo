# yield from文


def s_hello():
    yield "hello 1"
    yield "hello 2"
    yield "hello 3"
    return "done"


# 他のyiledを呼び出す
def g_hello():
    while True:
        r = yield from s_hello()
        yield r


g = g_hello()
# 一回目のwhike s_hello()
print(next(g))
print(next(g))
print(next(g))  # ここまでyield
print(next(g))  # return doneだが、Noneである

# 2回目のwhike s_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


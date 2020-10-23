# ジェネレータベースのこルーチン

# def g_hello():
#     yield "hello 1"
#     yield "hello 2"
#     yield "hello 3"


def g_hello():
    while True:
        r = yield "hello"
        yield r


g = g_hello()
print(next(g))  # helloが入っている
# print(next(g)) # 次のyieldがない
print(g.send("plus"))  # 他の値をいれる
print(next(g))

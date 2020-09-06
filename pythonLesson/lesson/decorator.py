# https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368
# デコレータ

# ---------------------------------------------------------------------------------
# step1
def foo1():
    return 1


# print(foo1())

# ---------------------------------------------------------------------------------
# step2
def foo2(arg):
    x = 10
    print(locals())


# foo2(20)
# print(globals())

# ---------------------------------------------------------------------------------
# step3
text = "I am global"


def foo3():
    text = "I am local"
    print(locals())


# foo3() -> {'text': 'I am local'}
# print(text) -> I am global

# ---------------------------------------------------------------------------------
# step4


def foo4():
    x = 1


# foo4()
# print(x) -> Traceback

# ---------------------------------------------------------------------------------
# step5
def foo5(x, y=0):
    return x - y


# print(foo5(3, 2))
# print(foo5(y=3, x=2))

# ---------------------------------------------------------------------------------
# step6
def outer():
    x = 1

    def inner():
        print(x)

    inner()


# outer()

# ----------------------------------------------------------------------------------------------------------
# step7


def foo():
    pass


# print(issubclass(int, object))  # Python内の全てのオブジェクトは同じ共通のクラスを継承して作られている
# print(issubclass(foo.__class__, object))


def add(x, y):
    return x + y


def apply(func, x, y):
    return func(x, y)


# print(apply(add, 2, 1))

# ----------------------------------------------------------------------------------------------------------
# step8


def outer():
    x = 1

    def inner():
        print(x)

    return inner


foo = outer()
# print(foo.func_closure)

# ----------------------------------------------------------------------------------------------------------
# step9
# デコレータとは「関数を引数に取り, 引き換えに新たな関数を返すcallable(*)」


def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()  # 1
        return ret + 1

    return inner


def foo():
    return 1


decorated = outer(foo)  # 2
# decorated()

foo = outer(foo)  # 常にデコレートされる


# とある座標のオブジェクトを保持するライブラリを使っているとします.
# そのオブジェクトはxとyの座標ペアを保持していますが, 残念ながら足し算や引き算など数字の処理機能を持っていません.
# しかし我々はこのライブラリを用いて大量の計算処理をする必要があり, ライブラリのソースを改編することも好ましくない状況だとします.
# どうすれば良いでしょうか？


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
# print(add(one, two))


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret

    return checker


sub = wrapper(sub)
print(sub(one, two))


# ----------------------------------------------------------------------------------------------------------
# step10


# sub = wrapper(sub)
# 以下でも表せる @は糖衣構文


@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

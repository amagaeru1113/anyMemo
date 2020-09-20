# --------------------------------------------------------------------------------------------------------------

# # 順序依存の引数
# def menu(entree, drink, desert):
#     print(entree)
#     print(drink)
#     print(desert)


# menu(entree="beef", drink="beer", desert="ice")


# --------------------------------------------------------------------------------------------------------------
# 51.デフォルト引数で気をつけること


def test_func(x, l=[]):
    l.append(x)
    return l


# r = test_func(100)  # 空のリストに追加される
# print(r)

# r = test_func(100)  # 追加されたリストに入る　デフォルト引数で空の配列を渡すのはバグの温床になる
# print(r)
# 理由：空の配列を読み込んだ際の先頭のアドレスと参照するので、一度100を追加した配列を呼び出して100を追加してしまう。 keyword：参照渡し


def test_func_better(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


# r = test_func_better(100)  # 空のリストに追加される
# print(r)

# r = test_func_better(100)  # 追加されたリストに入る
# print(r)


# --------------------------------------------------------------------------------------------------------------
# 52.位置引数のタプル化


def say_something(word, *args):  # *とつけると引数をタプルに入れてくれる
    print("word=", word)
    for arg in args:
        print(arg)


# say_something("Hi", "Mike", "Nancy")

# t = ("Mike", "Nancy")  # 予めタプルにしてアスタリスク月で渡すことも可能
# say_something("Hi", *t) #甘利使わない表現

# --------------------------------------------------------------------------------------------------------------
# 53.キーワード引数の辞書化


def menu(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# menu(entree="beef", drink="coffee")

d = {"entree": "beef", "drink": "beer", "dessert": "ice"}  # 辞書を作ってそれをいれるっていうのは割とある
# menu(**d)


def _menu_better(food, *args, **kwargs):  # *の数の準に引数に配置する
    print(food)
    print(args)
    print(kwargs)


# _menu_better("banana", "apple", "orange", entree="beef", drink="coffe")
#
# log
# banana
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'coffe'}

# --------------------------------------------------------------------------------------------------------------
# 54.Docstring


def example(param1, param2):  # 関数やクラスの説明をDocstringという
    """Example Docstring
    Args: 
        param1
        param2

    Retrun:
        bool  
    """

    print(param1)
    print(param2)
    return True


# print(example.__doc__)

# --------------------------------------------------------------------------------------------------------------
# 55.関数内関数


def outer(a, b):
    def plus(c, d):  # 他の箇所で使わない処理を関数ない関数にかく
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)

    print(r1 + r2)


# outer(1, 2)


# --------------------------------------------------------------------------------------------------------------
# 56.クロージャー

# 1,2をあとで実行したい。呼び出された時に初めて実行したい場合に使う


# def outer(a, b):  # functionを返す
#     def inner():
#         return a + b

#     return inner  # 実行するためのfunctionを返す


# f = outer(1, 2)
# r = f()  # ここでinnerが実行される
# # print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

# print(ca1(10))
# print(ca2(10))

# --------------------------------------------------------------------------------------------------------------
# 57.デコレータ
# 機能を付け加えたい時に使う


# これがデコレータ　メインの関数の前後に付随したい処理を付け加える
def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


def print_more(func):
    def wrapper(*args, **kwargs):
        print(f"func:{func.__name__}")
        print(f"args:{args}")
        print(f"kwargs:{kwargs}")
        result = func(*args, **kwargs)
        print(f"result:{result}")
        return result

    return wrapper


# 時間測定のデコレータ
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
        return result

    return wrapper


# デコレートする順序はだいじ。結果が変わる場合があるから
@measure_time
@print_more
def add_num(a, b):
    return a + b


# print("start")
# r = add_num(10,20)
# print("end")

# print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# r = add_num(10, 20)
# print(r)

# --------------------------------------------------------------------------------------------------------------
# 58.ラムダ

l = {"Mon", "tue", "Wed", "thu", "Fri", "sad", "Sun"}


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

sample_func = (
    lambda word: word.capitalize()
)  # ラムダ式　同じような処理をするが関数にするほど変更箇所はない時にラムダ織にしてしまう

# change_words(l, sample_func)

# --------------------------------------------------------------------------------------------------------------
# 59.ジェネレータ
# 反復処理をする際、要素を取り出して生成する

l = ["Good Morning", "Good afternoon", "Good night"]
# for i in l:
#     print(i)


# print("--------------")


def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"


# ジェネレータはnextを呼ばれた時にyieldを一度呼び出して抜ける
# for g in greeting():
#     print(g)
# print("--------------")

# forだと途中で別の処理を挟むことができないが、ジェネレータはできる
# g = greeting()
# print(next(g))
# print("@@@@@@@")
# print(next(g))
# print("@@@@@@@")
# print(next(g))


# 重たい処理を小分けにして実行する時に使う
def counter(num=10):
    for _ in range(num):
        yield "run"


g = greeting()
c = counter()
# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))

print(next(g))
# もう一度実行するとStopIterationとエラーが出る -> 例外処理


# --------------------------------------------------------------------------------------------------------------
# 60.リスト内包表記

t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

r = []
for i in t:
    r.append(i)

# print(r)

# リスト内包表記
g = [i for i in t]
# print(g)


r = [i for i in t if i % 2 == 0]
# print(r)

r = [i * j for i in t for j in t2]  # forが複数続くと他人が見た時に処理の抽象イメージが再現しづらくなる コードから知識への写像
# print(r)

# --------------------------------------------------------------------------------------------------------------
# 61.辞書内包表き

w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "tea"]

d = {}
for x, y in zip(w, f):
    d[x] = y
# print(d)

d = {x: y for x, y in zip(w, f)}
# print(d)

# --------------------------------------------------------------------------------------------------------------
# 62.集合内包表き

s = set()

for i in range(10):
    s.add(i)

# print(s)

s = {i for i in range(10) if i % 2 == 0}
# print(s)

# --------------------------------------------------------------------------------------------------------------
# 63.ジェネレータ内包表き


def g():
    for i in range(10):
        yield i


g = g()
g = (i for i in range(10) if i % 2 == 0)  # ジェネレータになる
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# --------------------------------------------------------------------------------------------------------------
# 64.名前空間

animal = "cat"


def f():
    print(animal)
    # ローカル変数としてanimalを宣言するならば使えるが、宣言前にanimalを使おうとすると下の理由で不可能
    # animal = 'dog' #グローバル変数に関数内で代入はできない


def f2():
    animal = "dog"
    # print(locals())  # ローカル変数を辞書で返す


# print(animal)
# f() #グローバル変数は表示できる
# f2()
# print(globals())# これまでグローバルで宣言した変数が表示
# __hoge__はpytonのシステムで使われているので置き換えない

# --------------------------------------------------------------------------------------------------------------
# 65.例外処理

l = [1, 2, 3]
i = 5

# try:
#     l[0]
# except IndexError as ex:
#     print(f"No idx: {ex}")
# except NameError as ex:
#     print(f"Name error:{ex}")
# except Exception as ex:  # ほとんどのプログラムの例外はException以下 訳のわからないexceptionを全てOtherにいれるのはやめた方がいい
#     print(f"other: {ex}")
# else:  # tryが実行された時にelseも実行される
#     print("done")
# finally:
#     print("clean up")


# --------------------------------------------------------------------------------------------------------------
# 66.独自例外の作成
# 自分の開発で使うエラー内容を作成して使える


class UppercaseError(Exception):
    pass
    # 継承した後にエラー内容を追加する


def check():
    words = ["APPLE", "orange", "banana"]
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as ex:
    print("This is my fault. Go next")


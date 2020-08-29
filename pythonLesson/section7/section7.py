# --------------------------------------------------------------------------------------------------------------
# 78.クラスの定義


# class Person(object):  # (object)と書かなくても可能だが、継承のベースクラスにできるから書いて方がいい
#     def say_something(self):
#         print("hello")


# person = Person()
# person.say_something()


# def person(name):
#     if name == 'A':
#         print('hello') 一々書くのは大変


# --------------------------------------------------------------------------------------------------------------
# 79.クラスの初期化とクラス変数


# class Person(object):
#     def __init__(self, name):  # 初めに実行される、作成時に変数にいれる
#         self.name = name
#         print(self.name)
#         self.run(2)  # メソッドも呼び出せる

#     def say_something(self):
#         print(f"hello, {self.name}")  # selfに格納された値が呼び出せる

#     def run(self, num):
#         print("run" * num)


# person = Person("Mike")
# person.say_something()


# --------------------------------------------------------------------------------------------------------------
# 80.コンストラクタとデストラクタ


# class Person(object):
#     def __init__(self, name):  # 初めに実行される <- コンストラクタ
#         self.name = name
#         print(self.name)
#         self.run(2)  # メソッドも呼び出せる

#     def say_something(self):
#         print(f"hello, {self.name}")  # selfに格納された値が呼び出せる

#     def run(self, num):
#         print("run" * num)

#     def __del__(self):
#         print("goodbye") # 最後に実行される <- デストラクタ


# person = Person("Mike")
# person.say_something()

# print("#####################")


# --------------------------------------------------------------------------------------------------------------
# 81.クラスの継承

# 似たようなクラスを作る場合に継承を行う


# class Car(object):
#     def run(self):
#         print("run")


# class ToyotaCar(Car):  # Carの機能を継承し、ToyotaCar特有の機能追加・拡張を行える
#     pass


# class TeslaCar(Car):
#     def auto_run(self):
#         print("auto run")


# car = Car()
# car.run()

# print("#####")

# toyota_car = ToyotaCar()  # Carの機能が使える
# toyota_car.run()

# print("#####")

# tesala_car = TeslaCar()
# tesala_car.run()
# tesala_car.auto_run()

# --------------------------------------------------------------------------------------------------------------
# 82.メソッドのオーバーライドとsuperによる親メソッドの呼び出し


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print("run")


# class ToyotaCar(Car):
#     def run(self):  # 同名のメソッドを作ると機能を上書きできる
#         print("fast")


# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False):
#         # self.model = model
#         super().__init__(model)  # 親クラスのメソッドを呼び出せる
#         self.enable_auto_run = enable_auto_run

#     def run(self):
#         print("super fast")

#     def auto_run(self):
#         print("auto run")


# car = Car()
# car.run()

# print("#####")

# toyota_car = ToyotaCar("Lexus")  # Carの機能が使える
# print(toyota_car.model)
# toyota_car.run()

# print("#####")

# tesala_car = TeslaCar("Model S")
# print(tesala_car.model)
# tesala_car.run()
# tesala_car.auto_run()


# --------------------------------------------------------------------------------------------------------------
# 83.プロパティーを使った属性の設定


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print("run")


# class ToyotaCar(Car):
#     def run(self):
#         print("fast")


# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False, password="123"):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run  # _を先頭につけることで外から見えづらくする
#         self.password = password

#     # プロパテぃはどういう時使うか、ある条件が合致したときに書き換え可能にする
#     @property  # 読み込みはできるけど、設定はできないようにできる
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter  # setできるようにする
#     def enable_auto_run(self, is_enable):
#         if self.password == "456":
#             self.enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")

#     def auto_run(self):
#         print("auto run")


# tesala_car = TeslaCar("Model S", password="456")
# print(tesala_car.enable_auto_run)  # -> False 読み込みはできる


# # tesala_car.enable_auto_run = True  # 買ってにオブジェクトを生成されて、enableを変更されたくないことがある
# # print(tesala_car.enable_auto_run)

# # Traceback (most recent call last):
# #   File "section7/section7.py", line 181, in <module>
# #     tesala_car.enable_auto_run = True  # 買ってにオブジェクトを生成されて、enableを変更されたくないことがある
# # AttributeError: can't set attribute


# --------------------------------------------------------------------------------------------------------------
# 84.クラスを構造体として扱う際の注意点


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print("run")


# class ToyotaCar(Car):
#     def run(self):
#         print("fast")


# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         self.enable_auto_run = is_enable

#     def run(self):
#         print("super fast")

#     def auto_run(self):
#         print("auto run")


# tesala_car = TeslaCar("Model S")
# # tesala_car.__enable_auto_run = "XXXXXX" #これを実行するとエラーにならないが、新たに値を入れる箱を作ってしまう

# print(tesala_car.__enable_auto_run)


# class T(object):
#     pass


# # データ構造体として扱う
# t = T()
# t.name = "Mike"
# t.age = 20
# print(t.name)


# --------------------------------------------------------------------------------------------------------------
# 85.ダックタイピング
# クラスが違くても、属性や関数は同じようなものを使うならそれを流用しよう？かな。
# https://molpako.hatenablog.com/entry/2018/03/19/112617

# class Person(object):  # 基本のクラス
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print("ok")
#         else:
#             raise Exception("No drives")


# class Baby(Person):  # Personクラスから子供クラスへ継承
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# baby = Baby()
# adult = Adult()


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print("run")

#     def ride(self, person):
#         person.drive()


# car = Car()
# # car.ride(baby)
# car.ride(adult)

# --------------------------------------------------------------------------------------------------------------
# 86.抽象クラス

# driveをBaby、Adultに書いても良かったのでは？
# 継承するクラスで毎回driveを定義しないといけない。これは忘れる。

# import abc  # 特に使う必要がなければ使わなくていい


# class Person(metaclass=abc.ABCMeta):  # 基本のクラス
#     def __init__(self, age=1):
#         self.age = age

#     @abc.abstractmethod  # 継承先で必ず実装するものとして指定
#     def drive(self):
#         pass


# class Baby(Person):  # Personクラスから子供クラスへ継承
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# baby = Baby()
# # TypeError: Can't instantiate abstract class Baby with abstract methods drive 実装してないぞ！
# adult = Adult()


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print("run")

#     def ride(self, person):
#         person.drive()


# car = Car()
# # car.ride(baby)
# car.ride(adult)

# --------------------------------------------------------------------------------------------------------------
# 87.多重継承

# なるべくない方がいい。 どっちにも同じ関数名があるときに整備が大変でバグにつながりやすい


# class Person(object):
#     def talk(self):
#         print("talk")

#     def run(self):
#         print("person run")


# class Car(object):
#     def run(self):
#         print("run")


# # 二つの機能を持たせたい -> 継承元を入れる
# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print("fly")


# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()  # 　左にあるものを呼び出す. (Person, Car) -> person run
# person_car_robot.fly()


# --------------------------------------------------------------------------------------------------------------
# 88.クラス変数


# class Person(object):
#     kind = "human"  # AもBも人間なのでクラス変数にする。オブジェクトで共有される。

#     def __init__(self, name):
#         self.name = name

#     def who_are_you(self):
#         print(self.name, self.kind)


# a = Person("A")
# a.who_are_you()
# b = Person("B")
# b.who_are_you()


# class T(object):
#     # words = [] # このままでおくとインスタンスでの操作によって期待しらリストにならなくなる.

#     def __init__(self):  # 避けるために毎度初期化する
#         self.words = []

#     def add_word(self, word):
#         self.words.append(word)


# c = T()
# c.add_word("add 1")
# c.add_word("add 2")
# print(c.words)

# d = T()
# d.add_word("add 3")
# d.add_word("add 4")
# print(c.words)  # リストが共有されてしまう。


# --------------------------------------------------------------------------------------------------------------
# 89.クラスメソッドとスタティックメソッド

# def about(year):
#     print(f"about human {year}") #クラスのデータにアクセスしない物は外に置いておいても良い。


# class Person(object):
#     kind = "human"

#     def __init__(self):
#         self.x = 100

#     @classmethod  # オブジェクトとして生成されていない時で使える -> クラスのメソッド
#     def what_is_your_kind(cls):
#         return cls.kind

#     @staticmethod
#     def about(year):
#         print(f"about human {year}")


# a = Person()
# # print(a) <__main__.Person object at 0x7f5ee6480bb0>
# # print(a.x) 100
# # print(a.kind) 'Human'
# print(a.what_is_your_kind())
# b = Person  # クラスのままだから初期化でxに100代入が行われない
# # print(b) <class '__main__.Person'>
# # print(b.x) AttributeError: type object 'Person' has no attribute 'x'
# # print(b.kind) 'human'
# print(b.what_is_your_kind())


# Person.about(1999)

# --------------------------------------------------------------------------------------------------------------
# 90.特殊メソッド
# https://docs.python.org/ja/3.6/reference/datamodel.html#special-method-names


class Word(object):
    def __init__(self, text):  # __で挟まれた物が特殊メソッド
        self.text = text

    def __str__(self):
        return "Word!!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word("test")
w2 = Word("########")
print(w)
print(len(w))
print(w + w2)
print(w == w2)

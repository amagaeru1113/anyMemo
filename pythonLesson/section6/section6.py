# --------------------------------------------------------------------------------------------------------------
# 67.コマンドライン引数


# $ ython section6.py option1 option2
import sys

# print(sys.argv)

# 出力 ['section6.py', 'option1', 'option2']

# --------------------------------------------------------------------------------------------------------------
# 68.import文とAS

"""
__init__.py パッケージの最初に読み込まれる。必須


"""
# import lessonPackage.utils # fullpathがどこから持ってきたのか分かりやすいという会社もある
from lessonPackage.tools import utils  # as u として、u.say_twiceでも使えるが多用しない方が良い

# from lessonPackage.utils import say_twice # あまり好まれていない。どこから呼び出したのかわからない

r = utils.say_twice("hello")
# print(r)


# --------------------------------------------------------------------------------------------------------------
# 69.絶対ぱすと相対パスのimport

from lessonPackage.talk import human

# print(human.sing())
# print(human.cry())

# --------------------------------------------------------------------------------------------------------------
# 70.アスタリスクのインポートと__init__.pyと__all__の意味
# from lessonPackage.talk import animal
from lessonPackage.talk import *  # NameError: name 'animal' is not defined

# -> lessonPackage.__init__に __all__を追加するとアスタリスクで呼び出せるものを絞れるが、何が呼び出せるか分かりづらいので避けること

# print(animal.sing())
# print(animal.cry())


# --------------------------------------------------------------------------------------------------------------
# 71.importErrorの使い所

try:  # パッケージのバージョン違いに対応する時に使う
    from lessonPackage import utils
except ImportError:
    from lessonPackage.tools import utils

# print(utils.say_twice("word"))

# --------------------------------------------------------------------------------------------------------------
# 72.setup.pyでパッケージを配布する

# --------------------------------------------------------------------------------------------------------------
# 73.組み込み関数 https://docs.python.org/ja/3/library/functions.html

ranking = {"A": 100, "B": 85, "C": 95}

# print(sorted(ranking))  # ['A', 'B', 'C']
# print(
#     sorted(ranking, key=ranking.get)
# )  # ['B', 'C', 'A'] ranking.getでkeyのvalueを基準にソートする この場合低い順
# print(
#     sorted(ranking, key=ranking.get, reverse=True)
# )  # ['A', 'C', 'B'] ranking.getでkeyのvalueを基準にソートする この場合高い順


# --------------------------------------------------------------------------------------------------------------
# 74.標準ライブラリ　https://docs.python.org/ja/3/library/index.html

s = "asdsavasvwrefnetntyiyturwetqwrehte"

# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)


# d = {}
# for c in s:
#     d.setdefault(c, 0) # cがなければ0をいれる
#     d[c] += 1
# print(d)

from collections import defaultdict

d = defaultdict(int)
for c in s:
    d[c] += 1
# print(d)
# print(d["f"])

# --------------------------------------------------------------------------------------------------------------
# 75.サードパーティのライブラリ https://pypi.org/ termcolor1.1.0をinstall

# $ pip install termcolor
from termcolor import colored

# print(colored("test", "red"))
# print(colored("test2", "blue"))
# print(colored("test3", "green"))
# print(help(colored))


# --------------------------------------------------------------------------------------------------------------
# 76.importする際の記述の仕方

# importの順番は標準ライブラリ -> サードパーティライブラリ -> 自作ライブラリ -> ローカルファイル
# import collections, sys, os 推奨されてない
# アルファベット順が好ましい
import collections
import os
import sys

# サーとバーティのライブラリと標準ライブラリは一行開ける
import termcolor

# 自作ライブラリとサードパーティは一行開ける
import lessonPackage

# ローカルのファイル
import config

# print(collections.__file__)
# print(termcolor.__file__)
# print(lessonPackage.__file__)
# print(config.__file__)

# print(sys.path)

# --------------------------------------------------------------------------------------------------------------
# 77.__name__と__main__

import lessonPackage.talk.animal

import config

# print("lesson:", __name__)
# import先も実行されてしまう


def main():
    lessonPackage.talk.animal.sing()


if __name__ == "__main__":  # 開発ではこれは重要　テスト目的ならそのまま書き始めても良い
    main()

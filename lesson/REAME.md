# 現役シリコンバレーエンジニアが教えるPython 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイル

udemyの講座を受けて、写経したコードやメモを残す。
個人的なメモになるため、多分他人には分かりづらくなる。
**ぜひ酒井さんの講座を受けて欲しい。 -> [リンク](https://www.udemy.com/course/python-beginner/)**

# section5 制御フローとコード構造

# section6 モジュールとパッケージ

# section7 オブジェクトとクラス
<details>
<summary>memo</summary>


基本的なクラスの形は以下
```
class Person(object):
    """ 三重クオートによるコメント """
    
    # コンストラクタ クラスのインスタンス作成時に最初に実行される
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print(f'{self.name} is running.') # selfに格納された値はメソッドでも使える
        
    def __del__(self):
        print('good bye')    
```

使う場合はインスタンスの生成を行い、メソッドの呼び出す
```
person = Person('Mike')
print(person.run()) # Mike is running.

# good bye # __del__で定義された処理が最後に実行される
```



--- 
似たようなクラスを作る場合は継承を行う。
例えば、車クラスを作ればトヨタの車クラス、テスラの車クラスなどに展開できる
```
"""
車    -> トヨタ
     |
     |-> テスラ
"""


class Car(object):
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print('run')
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
    def run(self): # 同名のメソッドを作れば、処理をオーバーライドできる
        print('Toyota run')

```

クラスではプロパティを設定できるが、これはある条件に合致した時だけ、変数の内容を変更できるシーンを作りたい時に使う

---

ダックタイピング

> アヒルと同じような動きをし、アヒルと同じように鳴くことがあるなら、それはアヒルだ

クラスが違くても属性や関数が同じような物ならそれは同じように動くクラスを継承して作るべき


---

抽象クラスや多重継承はあまり積極的に行わなくてもいい。分かりづらくなるし、使い方を熟知していないとバグを生みやすい。


---

クラス内で直接変数に値を渡すと、それはクラス変数になる。
これはインスタンスを2つ作成した時、片方がそのクラス変数の内容を変更するともう片方のインスタンスにもその変更が反映されるので注意が必要。


---

特殊メソッドは`__init__`のようにアンダースコア2つで挟まれた物のこと

</details>



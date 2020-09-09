# 現役シリコンバレーエンジニアが教えるPython 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイル

udemyの講座を受けて、写経したコードやメモを残す。
個人的なメモになるため、多分他人には分かりづらくなる。
**ぜひ酒井さんの講座を受けて欲しい。 -> [リンク](https://www.udemy.com/course/python-beginner/)**

# section5 制御フローとコード構造
途中からメモ撮り始めた。
<details>
<summary>memo</summary>

- デフォルト引数で注意すること
空のリストをデフォルト引数に設定して、二回実行すると二回目の実行時にはリスト要素は2こにな。
これは参照渡しで一度目のリストを呼び出してしまっているから。
そのため、空のリストを渡すのではなく、実行時にリストの指定がなければ生成するようにすること。



- 関数の引数にはタプルや辞書を渡せ、タプルなら*args、辞書なら**kwargsで指定する。
引数設定の順序はアスタリスクの少ない順。辞書を作って入れるというのはよくあるらしい。

- Docstringはチームに夜が、なるべく書く癖をつけよう。

- 関数ない関数の作るシーンは、他の箇所で使わないがその関数内では繰り返し使うとか、煩雑になりそうな時に作る

- クロージャーは、呼び出した時に初めて実行して欲しい。scalaの遅延評価っぽい。

- デコレータは関数の前後に処理を付随させたい時に付け加える。汎用的に使う処理はデコレータにしちゃうとかかな？例えば処理時間を測るとか。

```
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
```

- ラムダ式は同じような処理をするが関数にするほど変更箇所がない時に使う？

- ジェネレータは反復処理をするさ際に、要素を取り出して生成するもの。`next`で次の要素を取り出すが、実行するたびにジェネレータから抜けている。重たい処理を小分けにして実行したいがモチベ。

- リスト内包表記は楽だが、ネストが続くとすごくわかりづらくなる。多くて2重かな。ほかにも辞書、集合、ジェネレータで内包表記が可能。

- 名前空間は変数のスコープの話。グローバル変数やローカル変数とか。

- 例外処理。ほかのエラー全て検知するようなexceptをかくと辛い。
```
try:
    # 試行内容
except #例外型 as ex(#変数名):
    # エラーに応じた処理
else:
    # 正常にtryの内容が終了できた時の処理
finaly:
    # 正常終了、異常終了に関わらず実行する処理
```



</details>

# section6 モジュールとパッケージ

# section7 オブジェクトとクラス
<details>
<summary>memo</summary>

とほほのPython入門(http://www.tohoho-web.com/python/class.html)

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


# section8 ファイル操作とシステム
<details>
<summary>memo</summary>

 
 ファイルの作成
 
```
 with open('filenPath', 'w') as f:
     f.write('test')
 ```

ファイルの読み込み
```
 with open('filenPath', 'r') as f:
     print(f.read())

     # もしくは以下でchunkごとに文字を取り出せる
     while True:   
        chunk = 2
        line = f.readline(chunk)
        if not line:
            break
```

- モード指定
    - w -> w+にすることで書き込みと同時に読み込みもできる。しかし、この場合seek(0)で現在地を最初に戻す必要がある。

- テンプレート
    - string.Template()でテンプレート作ることで、変数への注入が行える

- csvの書き込みと読み込み
    - ファイルの書き込みと読み込みと大体同じ。
    - fieldNamesの指定をし、rowの挿入は辞書形式で行う

- ファイル操作
    - os(ファイル操作全般), pathlib(ファイル作成), glob(ファイル検索), shutil(高機能なファイル操作)を使えば大体できる


- tarfile、zipfile
    - ファイルの圧縮展開で使う

- tempfile
    - python上で一時的なファイルを作れる。処理終了時に削除される。

- datetime
    - pythonの時間取得とかのライブラリ

 
 
</details>


# section9 入門編の終了　応用編に行く前に簡単なアプリケーションの演習

<details>
<summary>memo</summary>
 

# **このセクションの動画は何回か見直そう**
- 自分で書いたのがmyCode、講師作成の物がexample
    - 関数ベースでとりあえず動くものとという意識で作成
    - templateはpyで書いたが、必ずしもpyである必要はないし、これだと一々スクロールがめんどいなと思った
    - exportCSVはぱっと見密集していて分かりづらい。細かくても切り分けをするべきだと思った
    - 講師のと比較して、どうして分かりにくいかを言語化した方が良い


- MVCで実装
    - Model：実際の処理、ロジックを記述-> ロボットの言動、ランキングの取得、保存
    - View：表示する部分について記述-> templateとtemplateの呼び出し、変数の代入
    - Controler：ModelとViewの接続部分を記述

- ベースクラスと継承をうまく使う
    - ロボットの言動ならコンストラクタでhelloを言わせる（最初に実行されるから）
    - レストランはロボットの使ったデータをまた使うから継承


</details>


# section10 コードスタイル


<details>
<summary>memo</summary>
 
 Pythonのコード規約 [PEP]
 
- 文章のようにPythonを書く
    - 一番綺麗で読みやすいコードはドキュメントが無くても、コードを読んで何をしているかが分かるコード

- シングルクオートとダブルクオートの使い分け
    - 併用する時、大体はダブルクオートを外側におく

- 便利なツール
    - flake8；コードチェック
    - autopep8：コード規約にしたがって自動整形

</details>

# section11 コンフィグとロギング


<details>
<summary>memo</summary>

参考URL
[Pythonでロギングを学ぼう](https://qiita.com/__init__/items/91e5841ed53d55a7895e)
[logging doc](https://docs.python.org/ja/3/library/logging.html)


- configの作成
    - configParserでconfig.iniの作成・読み込み
    - yamlでconfig.ymlの作成・読み込み
    - 個人的にはtoml使うことが多い。poetryもtoml。
    - circleciの設定とかはyamlで書いていた気がする。

- logging
    - loglevel：下に行くほど重要度が高い。基本はwarning以上がログ表示される
        - debug
        - info
        - warning
        - error
        - critical
    - `logger = getLogger(__name__)`を基本使う

- optparse
    - ファイル実行時に渡す引数やoptionを設定できる
    - config書くほどではないが、ハードコードしたくないこととかに使うのか？
    - あとはloglevelを渡すのにいいかもしれない

- 仮想環境
    - virtualenvが説明されていた
    - 個人的にはローカルで簡単に試す程度ならpyenv+poetryを使っている
        - pythonバージョン：pyenv
        - ライブラリ管理:poetry
    - 最近はdockerに慣れるために逐一Dockerfileを書いている
        - pythonバージョン:Docker
        - ライブラリ管理:poetyr

</details>


# section12 データベース

<details>
<summary>memo</summary>

pythonでDBに色々する

ライブラリ
- sqlalchemy：あとでDB切替ができる 
- mysql関連
    - mysql-connector-python
    - MySQLdb
    - pymysql
- mongoDB関連
    - pymongo

DBの種類
- RDB（リレーショナルデータベース）
    - MySQL
    - postgress
- NoSQL
    - キーバリュー型 (DBM、memcash)
    - ワイドカラム型 (Hbase)
    - ドキュメント型 (MongoDB)
    - グラフ型 (neo4j)


sqlalchemyで立ち上がりを書いて、mysqlに向き先を変えて書き込むようにするとやり直しが少なくて済みそう。
必要に応じてpostgressにできる。今でもRDB多いし、結局GCPのBigQuery使っている。



参考
【超入門】RDBとNoSQLの違いに着目！NoSQLに求めるものとは？
https://tech-blog.rakus.co.jp/entry/20180919/nosql/bigdata


</details>
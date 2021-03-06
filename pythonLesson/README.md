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

# section13 WEBとネットワーク


<details>
<summary>memo</summary>


restは大量のリクエストを捌ける
xml_rpcは記述が簡単なのでちょっとした作業で使う場合がある

networkx ：　ネットワークをグラフで図示するツール

</details>



</details>

# section14 ユニットテスト

<details>
<summary>memo</summary>



試した物は
doctest
unittest
pytest


python unittest
- https://qiita.com/aomidro/items/3e3449fde924893f18ca
- https://docs.python.org/ja/3/library/unittest.html

pytest-cov  pytest-xdist -> テストのカバレッジを表示
- --cov=calculation(<- test.pyでimportしているやつ)
- --cov-report term-missing でどの行をテストしていないかも教えてくれる

テストしなくてもいいようなメソッド
- 単にstringを返すだけのメソッドとか
- ifのネストはどこまでかくか -> ifの第一階層までは必ずやるのが一般的
- 失敗が許されない基幹系なら全部やる場合もある


pytest と同じようなライブラリ nose

tox virtualenvにパッケージをインストールしてその仮想環境上でテストを実行できる



どこまでmockするのか
- いれる値は全てmockする場合もある -> ユニットテストのバグを含む可能性があるから外部要因だけmockする場合が多い
- つまりはapiとかDBとかから持ってくる場合にmockする

</details>



# section15 並列化

<details>
<summary>memo</summary>


並列に処理を行う場合

- マルチスレッド：コアは共用、スレッドが複数、メモリは共用
- マルチプロセス：コアが複数、プロセスと対応、メモリもコアに追従

マルチスレッドで使うメソッド
- Thread：メソッドに処理を切り出して、それをworkerとして渡す。リストにして処理をまとめることができる。
- Timer：何秒後にスレッドを実行するか指定
- Lock：スレッドの処理が終わるまで他のスレッドの処理を凍結
- RLock：Lockでは一回の処理だけしか実行できなかったが、同じスレッド内部なら複数回処理実行可能
- Queue：スレッド間で値の受け渡しが可能
- Event：event.set()とevent.wait()でスレッド間の依存関係を記述可能
- Condition：EventとLockを組み合わせたような処理
- Barrier：指定の数のスレッドが立ち上がるまで次の処理を凍結

マルチプロセスで使うメソッド
- マルチスレッドで使ったもの（Lock、RLock、Queue、Event、Condition、Barrier）は基本使える
- Pipe：親プロセスから子プロセスに値を渡す際に使う
- Value、Array：プロセス間で値を共有する形でやり取りする際に使う
- Manager：サーバ間のデータのやり取りをValueやArrayより書きやすいもの。なお、二つに比べると遅い。


高水準のインターフェース concurrent.futures
- 簡単な並列化を行える
- マルチスレッドではじめは書いておいて、コードを動かすマシンのコア数が増えたりしたらマルチプロセスに書き換えることが可能



参考
python 並列処理
https://qiita.com/simonritchie/items/1ce3914eb5444d2157ac

</details>


# section16 暗号化

<details>
<summary>memo</summary>

個人情報や機密情報の取り扱いの際に使う暗号化<br>
-> 基本的に取り扱うものは文字列<br>
-> 文字コードが密接に絡む<br>
-> [新人さんに知って欲しい「文字コード」の話](https://qiita.com/yuji38kwmt/items/b3a7820b4d3b544da4ff)


pythonで扱う場合の例として次のライブラリを使用
- pycrypto（現在はメンテナンスされてないっぽい）
- hashlib

調べてみた他のライブラリ -> [AES対応のPython暗号化ライブラリを比較検証してみた](https://dev.classmethod.jp/articles/python-crypto-libraries/)
- PyCryptodome
- pyca/cryptography



</details>


# section17 インフラ自動化構築の環境に関して

<details>
<summary>memo</summary>

使用ツール
- vagrant
- virtualbox

vargantfileの中身でnetworkの部分はdockerのbridgeで実現するのか？


### Fablic デプロイツール
http://www.fabfile.org/

### Ansible 構成管理ツール
https://docs.ansible.com/




</details>


# section19 グラフィックス
docker上でのwindowの取り扱いは大分面倒なので、このセクションはコード実行を保証しない

<details>
<summary>memo</summary>


### 簡単な描画ツール：turtle
- 線を引いたり、塗り潰したりと行ったことが簡単に行える
- 幾何学模様の作成の際に、forループや再起処理などが学べる

### pythonのGUIツール:tkinter
- 計算機の作成



</details>


# section20 データ解析


<details>
<summary>memo</summary>

`jupyter lab --ip=0.0.0.0 --allow-root`


- jupyternotebook, numpy, pandasなどの基本操作
- データマイニング
- 株価予測

### pandas_datareader:経済データや金融商品の価格データの取得

- 株価ならAlpha Vantage
- 人口、GDPとかならWorld Bank

速報性には難があるが、金利データを長期的に見るとかなら有用らしい。
記事の多いブログは[こちら](https://www.mazarimono.net/entry/2018/07/20/pandas_datareader)


</details>


# section21 キューイングシステム


<details>
<summary>memo</summary>


## キューイングシステムとは

[MQとは](http://e-words.jp/w/%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0.html)
> メッセージキューイングとは、異なるソフトウェア間でデータを送受信する手法の一つで、直接データを渡すのではなく一旦第三者のソフトウェアに預けることで、送信側も受信側も好きなタイミングで送受信処理をおこなうことができるようにする方式。

- ブローカなし（ZeroMQ）：メモリ上にアクセスして情報を取得する
- ブローカあり（RabbitMQ、Kafka、Redis）：スケジューリングされたサーバにアクセスして情報を取得する

## ZeroMQ(https://zeromq.org/)

- push:pull　送られるデータが一対一対応になるため、複数のクライアントがあると順番通りのデータが取得できない
- pub:sub 送られるデータが一対多対応になるため、複数のクライアントで同じ情報が順番通りに取得できる（ただし、リアルタイムなので過去のデータは取得不可能）


## RabbitMQ(https://www.rabbitmq.com/)
オープンソースのメッセージブローカー

## Celery(https://docs.celeryproject.org/en/master/getting-started/first-steps-with-celery.html)
RabbitMQをPythonで使うための物

[Djangoで使ったりの例](http://taichino.com/programming/python-programming/2811)がある


</details>


# section22 非同期処理 asyncio


<details>
<summary>memo</summary>

- 並行（Concurrent）：Threading：交互に処理を取り合う
- 並列（Parallel）：Multiprocess

CPUバウンド：数値計算
I/Oバウンド：ネットワーク通信、ファイル読み書き

非同期I/O（Asyncio）、ノンブロッキングI/O

- マルチスレッド：PythonGILを取得したスレッドがコード実行する。スイッチングのイメージ
- マルチプロセス：コアが違うので独立にコードを実行する。
※[グローバルインタプリタロック](https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%97%E3%83%AA%E3%82%BF%E3%83%AD%E3%83%83%E3%82%AF)

CPUバウンドについてはマルチプロセスの方が早い。また関数呼び出しよりマルチスレッドの方が遅い場合がある。


### 非同期処理とは？

例：WebServer , DB , API　（データ受信、DB送信、DB処理、APIデータ送受信）を1タスクとする
    - 同期処理；タスクを受け付けた順番に実行していくイメージ。
    - マルチスレッド：タスクの一つ一つを順繰りにスレッドの数だけ実行していくイメージ
    - マルチプロセス：タスクの数だけプロセスが起動し、同時実行していくイメージ
    - 非同期処理：シングルスレッドで複数のタスクを嵌め込んで実行するイメージ




</details>
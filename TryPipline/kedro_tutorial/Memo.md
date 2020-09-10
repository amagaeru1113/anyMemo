# kedro docker作成のref
poetry でkedro installするときpython バージョンは指定する必要あり
https://github.com/python-poetry/poetry/issues/1413
python = "3.7.5"


まずはkedro get startした
https://kedro.readthedocs.io/en/stable/02_get_started/04_new_project.html
https://qiita.com/noko_qii/items/2395d3a3dbcd9410e5e7
https://qiita.com/mogom625/items/b1b673f530a05ec6b423
https://qiita.com/1000ch/items/93841f76ea52551b6a97
https://socinuit.hatenablog.com/entry/2020/02/08/210423
https://qiita.com/canonrock16/items/a7c57f4d29d0c88cc198


# GetStart
## 要素の説明
### Node
nodeはkedro特有の概念です。Pythonの関数のラッパーである、その関数の入力と出力を指定します。nodeはパイプラインの構成要素です。
前のnodeの出力を後のnodeの入力にすることで接続が行えます。

以下はnodeの例です。`return_greeting`という関数を作成した後、その関数名の後ろに`_node`とつけます。そしてnodeの引数として
func、inputs、outputsを指定します。今回は挨拶の関数なので入力は無く、出力の名前として`my_salutation`とおきます。
おそらくイメージとしては`my_salutation=return_greeting()`です。

```
from kedro.pipeline import node

def return_greeting():
    # Prepare first node
    return "Hello"


return_greeting_node = node(
    func=return_greeting, inputs=None, outputs="my_salutation"
)
```

次にもう一つnodeを作り、接続を例示します。
ここではgreetingで受け取った文字列に"Kedro"を追加する関数を作ります。入力は`greeting`ですが、これには`my_salutation`を期待しています。
この関数の出力もまたsingle outputで、`my_message`とします。
```
def join_statements(greeting):
    # Prepare second node
    return f"{greeting} Kedro!"


join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)
```

### Pipline
pipelineは、nodeの依存関係と実行順序を整理し、コードをモジュール化しながら入力と出力を接続します。pipelineは依存関係を解決することでnodeの実行順序を決定しますが、
必ずしもnodeが渡された順番で実行されるとは限りません。

以下の例では、pipelineはjoin_statements_nodeを実行する前にreturn_greeting_nodeを実行しています。
```
from kedro.pipeline import Pipeline

# Assemble nodes into a pipeline 左から順にnodeを渡す。ここでjoin_~が前にあると期待した入力が準備されない。
pipeline = Pipeline([return_greeting_node, join_statements_node])
```

### DataCatalog
DataCatalogもKedroで重要な概念です。これは、プロジェクトが使用できるすべてのデータソースのレジストリです。これは、nodeの入力と出力の名前をDataSetのキーとしてマッピングし、異なるタイプのデータ保存に特化できるKedroクラスです。Kedroは、単にメモリ内に保存されているデータにはMemoryDataSetを使用します。

```
from kedro.io import DataCatalog, MemoryDataSet

# Prepare a data catalog
data_catalog = DataCatalog({"example_data": MemoryDataSet()}) #コード内で宣言された変数など
```

Kedroがフォローしているデータソースのカタログについては[こちら](https://kedro.readthedocs.io/en/stable/kedro.extras.datasets.html#data-sets)を参照

### Runner
Runnerはpipelineの実行オブジェクトです。Kedroはノードが実行される順番を解決します。

1. Kedroは最初にreturn_greeting_nodeを実行します。
2. このノードはreturn_greetingを実行し、入力は受け取らないが "Hello "という文字列を出力する。
3. 出力された文字列は、example_dataという名前のMemoryDataSetにmy_salutationというキーで格納されます。
4. 次にKedroは2番目のノードであるjoin_statements_nodeを実行します。
5. このノードはexample_dataからmy_salutationをロードし、それをjoin_statements関数に注入します。
6. この関数は、入力されたsalutationを "Kedro!"と結合して、出力文字列 "Hello Kedro!"を形成します。
7. 出力文字列は、example_data内にmy_messageとして格納されます。

## Hello Kedro
これまで示した例を一つのファイルで実現した例が以下です。
今回、DataCatalogはありません。メモリ上にあるデータのみでrunできるためです。


```
"""Content of hello_kedro.py"""
from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner

# Prepare a data catalog
data_catalog = DataCatalog({"example_data": MemoryDataSet()})


def return_greeting():
    # Prepare first node
    return "Hello"


return_greeting_node = node(
    return_greeting, inputs=None, outputs="my_salutation"
)


def join_statements(greeting):
    # Prepare second node
    return f"{greeting} Kedro!"


join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([return_greeting_node, join_statements_node])

# Create a runner to run the pipeline
runner = SequentialRunner()

# Run the pipeline
print(runner.run(pipeline, data_catalog))
```

# Create New Project
新しくプロジェクトを作成する際は`kedro new`を実行します。

その際、以下のことが聞かれます。
```
project_name:  ex) Get_Started
repo_name: ex) get-started
python_package: ex) get_staretd
include_example: y/n -> yesの場合、irisデータセットの例が含まれる
```
Kedroは、--starterフラグを使ってプロジェクトを作成するために、カスタムスターターテンプレートを使用することをサポートしています。これによりユーザー独自のスタートレンプレートを使って、スムーズにプロジェクト作成が行えます。この機能の詳細については、[Kedro Startersを使った新規プロジェクトの作成ガイド](https://kedro.readthedocs.io/en/stable/02_get_started/06_starters.html)をお読みください。


# Iris dataset example project
## Background

この例では、シンプルで親しみやすい[アイリスのデータセット](https://www.kaggle.com/uciml/iris)を使用します。

アイリスのデータセットは、1936年にイギリスの統計学者で生物学者のRonald Fisherによって作成されました。このデータセットには、3つの異なる種のアイリス植物（Iris Setosa、Iris Versicolour、Iris Virginica）の50個のサンプルからなる合計150個のサンプルが含まれています。各サンプルについて、以下の図に示すように、セパルの長さ、セパルの幅、花弁の長さ、花弁の幅についての花の測定値が記録されています。

アイリスのデータセットは、機械学習モデルによって分類（以前に分類された類似した物体と比較することで、物体の種類を決定するために使用される方法）を説明するために使用することができます。一度既知のデータで訓練されると、機械学習モデルは、テストオブジェクトをその訓練データの出力と比較することで、予測的な分類を行うことができます。

## Create the example project
ここでは`getting-started`という名前でリポジトリが作成されていると仮定します。

## Project directory structure
このサンプルプロジェクトは、便利な出発点とベストプラクティスを示しています。これは、デフォルトのKedroプロジェクトテンプレートに沿っており、データセット、ノートブック、設定、ソースコードを格納するためのフォルダを使用します。独自のプロジェクトを作成する際には、必要に応じてフォルダ構造を変更することができます。

サンプルプロジェクトのディレクトリは以下のように設定されています。
```
    getting-started     # Parent directory of the template
    ├── conf            # Project configuration files
    ├── data            # Local project data (not committed to version control)
    ├── docs            # Project documentation
    ├── kedro_cli.py    # A collection of Kedro command line interface (CLI) commands
    ├── logs            # Project output logs (not committed to version control)
    ├── notebooks       # Project related Jupyter notebooks (can be used for experimental code before moving the code to src)
    ├── README.md       # Project README
    ├── setup.cfg       # Configuration options for `pytest` when doing `kedro test`
    └── src             # Project source code
```

同様に隠しファイルや隠しフォルダは以下のように設定されています。
```
    getting-started
    ├── .coveragerc     # Configuration file for the coverage reporting when doing `kedro test`
    ├── .gitignore      # Prevent staging of unnecessary files to `git`
    ├── .ipython        # IPython startup scripts
    ├── .isort.cfg      # Configuration file for the `isort` utility when doing `kedro lint`
    └── .kedro.yml      # Identifies the project root and [contains configuration information](https://kedro.readthedocs.io/en/latest/06_resources/02_architecture_overview.html?#kedro-yml)
```

### `conf/`
`conf`には`base`と`local`のサブフォルダがあり、強い設定の情報を記載します。
- `conf/base`：プロジェクト固有の設定を異なるインストレーション間で共有する場合(例えば、異なるユーザーで共有する場合)に使用してください。
    - `catalog.yml`：使用するデータセットのload/saveのパスが設定します。
    - `logging.yml`：loggingのセットアップ情報を記載します。
    - `parameters.yml`：機械学習実験のパラメータを定義することができます。
- `conf/local`：共有すべきではない設定の情報を記載します。
    - 例えば、アクセス資格情報、カスタムエディタの設定、個人的なIDEの設定、その他のセンシティブな内容や個人的な内容など
    - これは、ユーザーやインストールに固有のものです。
    - conf/local/の内容はgitによって無視されます（.gitignoreに含めることで）。

デフォルトでは、Kedro が conf/local フォルダを作成するとき、それは空です。しかし、Kedro は例として使用するために conf/base/ に credentials.yml を作成します。このファイルを生成して使用する前に、まず conf/local/ に移動させます。

### `data`
データフォルダには、プロジェクトデータを格納するためのいくつかのサブフォルダがあります。生データを`raw`に入れ、データエンジニアリングの慣習に従って処理済みデータを他のサブフォルダに移動することをお勧めします。

サンプルプロジェクトには iris.csv という単一のファイルがあり、そこには Iris データセットが含まれています。データのサブフォルダは .gitignore に含めることで git に無視されます。.gitignore に慣れていて、データをgitで管理する必要があると確信しているのであれば、それに応じて編集できます。

### `src`
このサブフォルダには、プロジェクトのソースコードが含まれています。2つのサブフォルダが含まれています。

- `get_started/`：プロジェクトの Python パッケージです。
- `tests/`：プロジェクトのユニットテスト用のサブフォルダ。プロジェクトのルートディレクトリから kedro test を呼び出すと、プロジェクトは pytest を使ってテストを実行するようにあらかじめ設定されています。

## What best practice should I follow to avoid leaking confidential data?
機密データの漏洩を防ぐためには、どのようなベストプラクティスに従えばよいのでしょうか。

- バージョン管理にデータをコミットしないようにする。
- ノートブックの出力セルにデータをコミットしないようにする（出力セルを削除しないと、データがノートブックにこっそり入ってしまうことがあります）。
- 機密性の高い結果やプロットをバージョン管理にコミットしないようにしてください (ノートブック内やその他の場所で)。
- conf/に資格情報をコミットしないでください。アクセス資格情報のような機密情報には、conf/local/フォルダのみを使用してください。認証情報を追加するには、プロジェクトテンプレートの conf/base/credentials.yml ファイルを参照してください。
- デフォルトでは、conf/ フォルダ (およびそのサブフォルダ) 内のファイル名に認証情報を含むファイルは .gitignore で無視され、git リポジトリにコミットされません。
- 同僚がその資格情報にアクセスできる場所を記述するには、README.md を編集して指示を出すことができます。

## Run the example project
exampleを実行してみましょう。

```
cd getting-started
kedro run
```

<details>
<summary>実行すると以下のようなログがみれます。</summary>

```
root@bb4010f480f9:/app/get-started# kedro run
2020-09-08 09:20:16,132 - root - INFO - ** Kedro project get-started
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
2020-09-08 09:20:16,161 - kedro.versioning.journal - WARNING - Unable to git describe /app/get-started
/usr/local/lib/python3.8/site-packages/fsspec/implementations/local.py:29: FutureWarning: The default value of auto_mkdir=True has been deprecated and will be changed to auto_mkdir=False by default in a future release.
  warnings.warn(
2020-09-08 09:20:16,248 - kedro.io.data_catalog - INFO - Loading data from `example_iris_data` (CSVDataSet)...
2020-09-08 09:20:16,262 - kedro.io.data_catalog - INFO - Loading data from `params:example_test_data_ratio` (MemoryDataSet)...
2020-09-08 09:20:16,263 - kedro.pipeline.node - INFO - Running node: split_data([example_iris_data,params:example_test_data_ratio]) -> [example_test_x,example_test_y,example_train_x,example_train_y]
2020-09-08 09:20:16,278 - kedro.io.data_catalog - INFO - Saving data to `example_train_x` (MemoryDataSet)...
2020-09-08 09:20:16,280 - kedro.io.data_catalog - INFO - Saving data to `example_train_y` (MemoryDataSet)...
2020-09-08 09:20:16,282 - kedro.io.data_catalog - INFO - Saving data to `example_test_x` (MemoryDataSet)...
2020-09-08 09:20:16,283 - kedro.io.data_catalog - INFO - Saving data to `example_test_y` (MemoryDataSet)...
2020-09-08 09:20:16,284 - kedro.runner.sequential_runner - INFO - Completed 1 out of 4 tasks
2020-09-08 09:20:16,286 - kedro.io.data_catalog - INFO - Loading data from `example_train_x` (MemoryDataSet)...
2020-09-08 09:20:16,287 - kedro.io.data_catalog - INFO - Loading data from `example_train_y` (MemoryDataSet)...
2020-09-08 09:20:16,288 - kedro.io.data_catalog - INFO - Loading data from `parameters` (MemoryDataSet)...
2020-09-08 09:20:16,289 - kedro.pipeline.node - INFO - Running node: train_model([example_train_x,example_train_y,parameters]) -> [example_model]
2020-09-08 09:20:16,746 - kedro.io.data_catalog - INFO - Saving data to `example_model` (MemoryDataSet)...
2020-09-08 09:20:16,748 - kedro.runner.sequential_runner - INFO - Completed 2 out of 4 tasks
2020-09-08 09:20:16,749 - kedro.io.data_catalog - INFO - Loading data from `example_model` (MemoryDataSet)...
2020-09-08 09:20:16,750 - kedro.io.data_catalog - INFO - Loading data from `example_test_x` (MemoryDataSet)...
2020-09-08 09:20:16,751 - kedro.pipeline.node - INFO - Running node: predict([example_model,example_test_x]) -> [example_predictions]
2020-09-08 09:20:16,753 - kedro.io.data_catalog - INFO - Saving data to `example_predictions` (MemoryDataSet)...
2020-09-08 09:20:16,754 - kedro.runner.sequential_runner - INFO - Completed 3 out of 4 tasks
2020-09-08 09:20:16,755 - kedro.io.data_catalog - INFO - Loading data from `example_predictions` (MemoryDataSet)...
2020-09-08 09:20:16,756 - kedro.io.data_catalog - INFO - Loading data from `example_test_y` (MemoryDataSet)...
2020-09-08 09:20:16,758 - kedro.pipeline.node - INFO - Running node: report_accuracy([example_predictions,example_test_y]) -> None
2020-09-08 09:20:16,759 - get_started.pipelines.data_science.nodes - INFO - Model accuracy on test set: 100.00%
2020-09-08 09:20:16,761 - kedro.runner.sequential_runner - INFO - Completed 4 out of 4 tasks
2020-09-08 09:20:16,762 - kedro.runner.sequential_runner - INFO - Pipeline execution completed successfully.
root@bb4010f480f9:/app/get-started# 
```

</details>

## Under the hood: Pipelines and nodes
exampleでは二つのパイプラインを含んでいます。

- data_engineeringパイプライン（`src/getting_started/pipelines/data_engineering/pipeline.py`）は，データを学習サンプルとテストサンプルに分割します．
- data_scienceパイプライン（`src/getting_started/pipelines/data_science/pipeline.py`）は，モデルの学習，予測，精度報告を行います．

#### Data Engineering Node
`pipelines/data_engineering/nodes.py`には次のnodeが含まれています。

Node | Description | Node Function Name
--- | --- | ---
Split data | アイリスデータセットを学習とテストに分割する | `split_data`



#### Data Science Node
`pipelines/data_science/nodes.py`には次のnodeが含まれています。

Node | Description | Node Function Name
--- | --- | ---
Train model | ロジスティック回帰による分類器の学習を行う | `train_model`
Predict | 事前学習モデルとテストセットからクラス分類を行う | `predict`
Report accuracy | 一つ前のノードの予測器の正答率をレポートする | `report_accuracy`

`src/pipeline.py`は、プロジェクトのモジュール式パイプラインを作成して1つのパイプラインにまとめ、ノード間の入力データと出力データの依存関係からノードの実行順序を解決します。

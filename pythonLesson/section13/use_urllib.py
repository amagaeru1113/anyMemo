"""
REST

参考　https://qiita.com/fukulingo/items/a9e8d18467fe3e04068e
HTTPメソッド　クライアントが行いたい処理をサーバに伝える

GET	    リソースの取得
POST	子リソースの作成、リソースへのデータ追加、その他処理
PUT	    リソースの更新、リソースの作成
DELETE	リソースの削除
HEAD	リソースのヘッダ (メタデータの取得)
OPTIONS	リソースがサポートしているメソッドの取得
TRACE	プロキシ動作の確認
CONNECT	プロキシ動作のトンネル接続への変更

CRUDはCreate, Read, Update, Deleteのこと。
HTTPメソッドのうちGET、POST、PUT、DELETEは「CRUD」を満たし、また使用頻度が高い

CURD名	意味	メソッド
Create	作成	    POST/PUT
Read	読み込み	 GET
Update	更新	    PUT
Delete	削除	    DELETE


"""

import urllib.request
import json


# get 見られても問題ない引数は?でつなげても良い------------------------------------------------------------
# paylaod = {"key1": "value1", "key2": "value2"}

# url = "http://httpbin.org/get" + "?" + urllib.parse.urldecode(paylaod)
# print(url)

# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode("utf-8"))
#     print(r)

# post 他人に見られないような情報を渡す -----------------------------------------------------------

# payload = json.dumps({"key1": "value1", "key2": "value2"}).encode("utf-8")
# url = "http://httpbin.org/post"
# req = urllib.request.Request(url, data=payload, method="POST")


# with urllib.request.urlopen(req) as f:
#     r = json.loads(f.read().decode("utf-8"))
#     print(r)

# put  -----------------------------------------------------------

payload = json.dumps({"key1": "value1", "key2": "value2"}).encode("utf-8")
url = "http://httpbin.org/put"
req = urllib.request.Request(url, data=payload, method="PUT")


with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode("utf-8"))
    print(r)

# delete  -----------------------------------------------------------

payload = json.dumps({"key1": "value1", "key2": "value2"}).encode("utf-8")
url = "http://httpbin.org/delete"
req = urllib.request.Request(url, data=payload, method="DELETE")


with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode("utf-8"))
    print(r)

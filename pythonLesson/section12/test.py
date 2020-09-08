# import pymysql.cursors #Raspberry Pi，Win用
import MySQLdb  # mac用

# 上の方をmacで使う場合は
# pip3 install pymysql
# でインストールする必要がある


# ---------
# 接続
# ---------
# cnct = pymysql.connect( #Raspberry Pi用
cnct = MySQLdb.connect(  # Win,mac用
    host="sample-mysql",  # ホスト名
    user="root",  # MySQLユーザ名
    password="",  # MySQLユーザパスワード
    db="test-db",  # データベース名
    charset="utf8",  # 文字コード
)
# TABLE = "test"  # テーブル名

cur = cnct.cursor()

# host="sample-mysql",
# port="3306", user="root", password="", database="test-db",
